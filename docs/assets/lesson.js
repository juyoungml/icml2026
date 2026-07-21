(() => {
  const STORAGE_KEY = 'icml2026-course-mastery-v2';
  const MODULES = [
    'foundations',
    'llm-reasoning-post-training-and-rlvr',
    'multimodal-vision-and-perception',
    'theory-optimization-and-algorithms',
    'ai-for-science-health-and-neuro',
    'data-centric-causal-and-federated-ml',
    'systems-and-efficient-foundation-models',
    'safety-governance-privacy-and-society',
    'agents-code-and-tool-use',
    'graphs-geometry-and-representation-learning',
    'generative-modeling',
    'reinforcement-learning-and-control',
    'robotics-embodiment-and-world-models',
    'synthesis'
  ];
  const MODULE_PATHS = Object.fromEntries(MODULES.map(module => [module, `learn/${module}.html`]));

  function readMastery() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}'); }
    catch (_) { return {}; }
  }

  function writeMastery(mastery) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(mastery));
    updateProgress();
  }

  function updateProgress() {
    const mastery = readMastery();
    const complete = MODULES.filter(module => mastery[module]?.mastered).length;
    const percent = Math.round(complete / MODULES.length * 100);
    document.querySelectorAll('[data-course-progress]').forEach(bar => { bar.style.width = `${percent}%`; });
    document.querySelectorAll('[role="progressbar"][aria-label="Course mastery"]').forEach(bar => { bar.setAttribute('aria-valuenow', String(percent)); });
    document.querySelectorAll('[data-course-progress-number]').forEach(label => { label.textContent = `${percent}%`; });
    document.querySelectorAll('[data-course-progress-label]').forEach(label => { label.textContent = `${complete} of ${MODULES.length} modules mastered`; });
    document.querySelectorAll('[data-module-label]').forEach(label => {
      const done = mastery[label.dataset.moduleLabel]?.mastered;
      label.textContent = done ? 'Mastered ✓' : 'Start';
      label.classList.toggle('complete', Boolean(done));
    });
    document.querySelectorAll('[data-module-state]').forEach(icon => {
      const result = mastery[icon.dataset.moduleState];
      icon.classList.toggle('complete', Boolean(result?.mastered));
      icon.setAttribute('aria-label', result?.mastered ? `Mastered with ${result.score}%` : 'Not yet mastered');
      icon.title = result?.mastered ? `Mastered · ${result.score}%` : 'Not yet mastered';
    });
    const nextModule = MODULES.find(module => !mastery[module]?.mastered);
    document.querySelectorAll('[data-course-resume]').forEach(link => {
      link.href = nextModule ? MODULE_PATHS[nextModule] : 'quiz.html';
      link.textContent = nextModule ? (complete ? 'Resume course' : 'Begin with foundations') : 'Take the final assessment';
    });
  }

  function initializeQuiz(root) {
    const module = root.dataset.module;
    const questions = JSON.parse(root.dataset.questions);
    const stage = root.querySelector('[data-quiz-stage]');
    let position = 0;
    let answers = [];
    let locked = false;

    function renderQuestion() {
      locked = false;
      const item = questions[position];
      stage.innerHTML = `
        <div class="lesson-quiz-top"><span>Question ${position + 1} of ${questions.length}</span><div class="mini-progress"><i style="width:${position / questions.length * 100}%"></i></div></div>
        <h3>${item.question}</h3>
        <div class="lesson-options"></div>
        <div class="lesson-feedback" aria-live="polite"></div>
        <button class="button lesson-next-question hidden" type="button">${position === questions.length - 1 ? 'See result' : 'Next question'}</button>`;
      const options = stage.querySelector('.lesson-options');
      item.options.forEach((option, index) => {
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'lesson-option';
        button.innerHTML = `<span>${index + 1}</span>${option}`;
        button.addEventListener('click', () => answer(index));
        options.appendChild(button);
      });
      stage.querySelector('.lesson-next-question').addEventListener('click', advance);
    }

    function answer(selected) {
      if (locked) return;
      locked = true;
      const item = questions[position];
      const correct = selected === item.answer;
      answers.push({ selected, correct });
      stage.querySelectorAll('.lesson-option').forEach((button, index) => {
        button.disabled = true;
        if (index === item.answer) button.classList.add('correct');
        if (index === selected && !correct) button.classList.add('wrong');
      });
      const feedback = stage.querySelector('.lesson-feedback');
      feedback.className = `lesson-feedback visible ${correct ? 'correct' : 'wrong'}`;
      feedback.innerHTML = `<strong>${correct ? 'Correct.' : 'Not quite.'}</strong> ${item.explanation}`;
      const next = stage.querySelector('.lesson-next-question');
      next.classList.remove('hidden');
      next.focus();
    }

    function advance() {
      if (!locked) return;
      if (position < questions.length - 1) {
        position += 1;
        renderQuestion();
      } else {
        renderResult();
      }
    }

    function renderResult() {
      const correct = answers.filter(answer => answer.correct).length;
      const score = Math.round(correct / questions.length * 100);
      const mastered = correct >= Math.ceil(questions.length * .75);
      const mastery = readMastery();
      if (!mastery[module] || score >= mastery[module].score) {
        mastery[module] = { score, mastered, completedAt: new Date().toISOString() };
        writeMastery(mastery);
      }
      stage.innerHTML = `
        <div class="mastery-result ${mastered ? 'passed' : 'retry'}">
          <span class="tag">${mastered ? 'Module mastered' : 'One more pass'}</span>
          <strong>${correct}/${questions.length}</strong>
          <h3>${mastered ? 'You can use this mental model.' : 'Review the lesson, then try again.'}</h3>
          <p>${mastered ? 'Your course progress has been updated in this browser.' : 'Mastery requires at least 3 correct answers. The retry uses the same core ideas.'}</p>
          <button class="button" type="button" data-retry-lesson>Retry checkpoint</button>
        </div>`;
      stage.querySelector('[data-retry-lesson]').addEventListener('click', () => {
        position = 0;
        answers = [];
        renderQuestion();
      });
    }

    renderQuestion();
  }

  document.querySelectorAll('[data-lesson-quiz]').forEach(initializeQuiz);
  document.querySelectorAll('[data-reset-course]').forEach(button => {
    button.addEventListener('click', () => {
      if (!window.confirm('Reset all 14 module scores stored in this browser?')) return;
      localStorage.removeItem(STORAGE_KEY);
      updateProgress();
    });
  });
  updateProgress();
})();
