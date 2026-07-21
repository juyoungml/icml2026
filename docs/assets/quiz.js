(() => {
  const QUESTIONS = [
    {
      category: 'Foundations',
      question: 'What is the main purpose of the 12-area taxonomy?',
      options: ['To rank every paper by quality', 'To provide a useful navigation map', 'To replace paper reading', 'To predict future citations'],
      answer: 1,
      explanation: 'The taxonomy helps people navigate 6,628 papers. It is not a final truth or quality ranking because some papers cross area boundaries.'
    },
    {
      category: 'Foundations',
      question: 'An oral enrichment value of 1.4 means:',
      options: ['Every paper is 40% better', 'The area has 40% more papers', 'The area appears among orals about 1.4 times as often as its share suggests', 'The area received 1.4 awards'],
      answer: 2,
      explanation: 'Enrichment compares an area’s oral representation with its overall paper share. It does not score every paper.'
    },
    {
      category: 'Foundations',
      question: 'What does AlphaXiv attention measure in this project?',
      options: ['Objective research quality', 'Votes and visits on AlphaXiv', 'Official reviewer scores', 'Independent reproduction'],
      answer: 1,
      explanation: 'AlphaXiv votes and visits show attention on that platform. Topic popularity, demos, project pages, and audience composition can affect it.'
    },
    {
      category: 'Foundations',
      question: 'Why use a nearby-venue baseline?',
      options: ['To prove why ICML selected papers', 'To see whether an area is unusually emphasized at ICML', 'To replace ICML counts', 'To measure paper correctness'],
      answer: 1,
      explanation: 'A venue baseline gives context. It helps separate “large everywhere” from “especially emphasized here,” but it does not prove the cause.'
    },
    {
      category: 'Foundations',
      question: 'Which statement best describes a directional pattern?',
      options: ['A settled causal law', 'A useful signal that still needs deeper checking', 'A direct official count', 'An unsupported guess'],
      answer: 1,
      explanation: 'Directional patterns are supported enough to guide reading, but still need paper-level validation before strong publication language.'
    },
    {
      category: 'Area Map',
      question: 'Which area is largest in the current project taxonomy?',
      options: ['Robotics and World Models', 'Generative Modeling', 'LLM Reasoning and Post-Training', 'Graphs and Geometry'],
      answer: 2,
      explanation: 'LLM Reasoning, Post-Training, and RLVR contains 1,099 mapped papers, or 16.6% of the corpus.'
    },
    {
      category: 'Area Map',
      question: 'A paper about training across separate devices without collecting all raw data most likely belongs to:',
      options: ['Federated and Data-Centric ML', 'Generative Modeling', 'Theory only', 'Video Generation'],
      answer: 0,
      explanation: 'Federated learning is part of the Data-Centric, Causal, and Federated ML area.'
    },
    {
      category: 'Area Map',
      question: 'Which pair meets most directly in a vision-language-action robot policy?',
      options: ['Theory and privacy', 'Multimodal perception and robotics', 'Causal inference and diffusion theory', 'Data valuation and bandits'],
      answer: 1,
      explanation: 'A VLA policy combines visual and language understanding with physical action, joining multimodal perception and robotics.'
    },
    {
      category: 'Area Map',
      question: 'Which area studies message passing, equivariance, and structured relationships?',
      options: ['Systems', 'Graphs, Geometry, and Representation Learning', 'Safety and Governance', 'Agents and Tools'],
      answer: 1,
      explanation: 'Graph and geometric methods use known structure, relationships, and symmetries in data and models.'
    },
    {
      category: 'Area Map',
      question: 'Which is a core Reinforcement Learning and Control topic outside LLM post-training?',
      options: ['Offline policy learning', 'Tokenization only', 'Image captioning only', 'Repository documentation'],
      answer: 0,
      explanation: 'The broader RL field includes offline RL, exploration, control, robust decision-making, and policy learning.'
    },
    {
      category: 'Area Map',
      question: 'Why can AI for Science require more than a general benchmark score?',
      options: ['Scientific data never has labels', 'It may require physical validity, uncertainty, or laboratory confirmation', 'Benchmarks are always wrong', 'Scientific models cannot be evaluated'],
      answer: 1,
      explanation: 'A proxy score may not establish physical validity, biological function, clinical usefulness, or a real scientific finding.'
    },
    {
      category: 'Area Map',
      question: 'Which is the best systems-level evaluation?',
      options: ['Only the speed of one kernel', 'End-to-end latency, memory, cost, and quality across realistic settings', 'Only parameter count', 'Only GitHub stars'],
      answer: 1,
      explanation: 'Systems claims should survive end-to-end measurement, realistic hardware and workload conditions, and capability-regression checks.'
    },
    {
      category: 'Evidence',
      question: 'Robotics has 2.9% paper share and 2.11× public-attention enrichment. What is supported?',
      options: ['Robotics is the best area', 'Robotics receives unusually high AlphaXiv attention for its size', 'Every robotics paper is popular', 'Robotics dominates oral selection'],
      answer: 1,
      explanation: 'The evidence supports a platform-attention contrast. It does not establish quality, importance, or program dominance.'
    },
    {
      category: 'Evidence',
      question: 'Theory has 1.45× oral enrichment and 0.46× public-attention enrichment. The strongest interpretation is:',
      options: ['Theory did not matter', 'Oral selection and public attention highlight different work', 'Every theory paper is excellent', 'The public dislikes mathematics'],
      answer: 1,
      explanation: 'The two signals answer different questions. The contrast is useful for selecting papers to inspect, not for judging every paper or audience motive.'
    },
    {
      category: 'Evidence',
      question: 'Multimodal and vision can be both large and underweight because:',
      options: ['The two claims use different years only', 'Large describes ICML size; underweight compares its share with nearby venues', 'One claim must be false', 'Underweight means low quality'],
      answer: 1,
      explanation: 'The area is large inside ICML while occupying a smaller share than in the project’s nearby-venue comparison.'
    },
    {
      category: 'Evidence',
      question: 'A repository has many stars. What does that prove?',
      options: ['The paper was reproduced', 'The code produces every result', 'The repository attracted attention', 'The taxonomy is correct'],
      answer: 2,
      explanation: 'Stars indicate attention. Reproducibility requires checking repository identity, contents, execution, and outputs.'
    },
    {
      category: 'Evidence',
      question: 'Which is the safest headline?',
      options: ['ICML proves reasoning is the future of all ML', 'LLM reasoning and post-training form the largest area in the current project taxonomy, with boundary review still needed', 'Reasoning papers are better than vision papers', 'All LLM papers are reasoning papers'],
      answer: 1,
      explanation: 'The safe headline names the current taxonomy, states the descriptive result, and keeps the known boundary limitation visible.'
    },
    {
      category: 'Evidence',
      question: 'Which check comes first when inspecting an artifact link?',
      options: ['Count stars', 'Confirm the artifact belongs to the paper', 'Assume the README is complete', 'Compare author popularity'],
      answer: 1,
      explanation: 'Identity comes first. This workspace already contains examples where collected repository metadata appears mismatched.'
    },
    {
      category: 'Paper Cases',
      question: 'What central question does “The Flexibility Trap” ask?',
      options: ['Whether larger images improve video', 'Whether arbitrary token order actually helps diffusion-language-model reasoning', 'Whether robots need memory', 'Whether graphs can represent molecules'],
      answer: 1,
      explanation: 'The paper tests whether flexible arbitrary-order generation can reduce exploration and reasoning coverage in mathematics and coding.'
    },
    {
      category: 'Paper Cases',
      question: 'Why is “To Grok Grokking” a useful theory example?',
      options: ['It gives quantitative delayed-generalization results in a controlled setting', 'It introduces a robot benchmark', 'It measures AlphaXiv votes', 'It releases a video generator'],
      answer: 0,
      explanation: 'It proves stages and timing of grokking in ridge regression, then checks whether the quantitative behavior appears in nonlinear networks.'
    },
    {
      category: 'Paper Cases',
      question: 'PaperBanana’s improvement is best described primarily as:',
      options: ['A new mathematical theorem', 'An agentic system and evaluation benchmark', 'A causal discovery method', 'An offline RL policy'],
      answer: 1,
      explanation: 'PaperBanana coordinates specialized agents and evaluates them using a 292-case academic-illustration benchmark.'
    },
    {
      category: 'Paper Cases',
      question: 'What safety failure does “The Obfuscation Atlas” study?',
      options: ['A model forgetting old images', 'A model learning to hide deception from a detector', 'A slow inference kernel', 'A graph losing edges'],
      answer: 1,
      explanation: 'Training against a deception monitor may create honest behavior, obfuscated activations, or detector-evading deceptive policies.'
    },
    {
      category: 'Paper Cases',
      question: 'RoboMME’s main technical focus is:',
      options: ['Memory in long-horizon robotic policies', 'Language-model tokenization', 'Federated privacy', 'Diffusion consistency'],
      answer: 0,
      explanation: 'RoboMME evaluates temporal, spatial, object, and procedural memory across history-dependent manipulation tasks.'
    },
    {
      category: 'Paper Cases',
      question: 'A protein generator has strong structure-validity scores. What remains unproven?',
      options: ['That it produced any output', 'Biological function and laboratory usefulness', 'That proteins have atoms', 'That benchmarks use numbers'],
      answer: 1,
      explanation: 'Structural metrics do not establish biological function, novelty beyond training data, safety, or laboratory performance.'
    }
  ];

  const QUICK_INDICES = [0, 2, 5, 7, 11, 12, 13, 15, 18, 21];
  const start = document.getElementById('quiz-start');
  const active = document.getElementById('quiz-active');
  const result = document.getElementById('quiz-result');
  const category = document.getElementById('quiz-category');
  const count = document.getElementById('quiz-count');
  const progress = document.getElementById('quiz-progress');
  const question = document.getElementById('quiz-question');
  const options = document.getElementById('quiz-options');
  const feedback = document.getElementById('quiz-feedback');
  const next = document.getElementById('quiz-next');
  let queue = [];
  let position = 0;
  let answers = [];
  let locked = false;

  function updateBestLabel() {
    const best = Number(localStorage.getItem('icml2026-quiz-best') || 0);
    document.getElementById('best-score').textContent = best ? `Best score on this browser: ${best}%` : 'Your best score will be saved in this browser.';
  }

  function startQuiz(mode, customQueue = null) {
    queue = customQueue || (mode === 'quick' ? QUICK_INDICES : QUESTIONS.map((_, i) => i));
    position = 0;
    answers = [];
    start.classList.add('hidden');
    result.classList.add('hidden');
    active.classList.remove('hidden');
    renderQuestion();
  }

  function renderQuestion() {
    locked = false;
    feedback.className = 'feedback';
    feedback.innerHTML = '';
    next.classList.add('hidden');
    const item = QUESTIONS[queue[position]];
    category.textContent = item.category;
    count.textContent = `${position + 1} of ${queue.length}`;
    progress.style.width = `${position / queue.length * 100}%`;
    question.textContent = item.question;
    options.innerHTML = '';
    item.options.forEach((text, index) => {
      const button = document.createElement('button');
      button.className = 'option';
      button.innerHTML = `<span class="option-key">${index + 1}</span><span>${text}</span>`;
      button.addEventListener('click', () => answerQuestion(index));
      options.appendChild(button);
    });
  }

  function answerQuestion(selected) {
    if (locked) return;
    locked = true;
    const item = QUESTIONS[queue[position]];
    const correct = selected === item.answer;
    [...options.children].forEach((button, index) => {
      button.disabled = true;
      if (index === item.answer) button.classList.add('correct');
      if (index === selected && !correct) button.classList.add('wrong');
    });
    answers.push({ questionIndex: queue[position], selected, correct });
    feedback.className = `feedback visible ${correct ? 'correct' : 'wrong'}`;
    feedback.innerHTML = `<strong>${correct ? 'Correct.' : 'Not quite.'}</strong> ${item.explanation}`;
    next.textContent = position === queue.length - 1 ? 'See results' : 'Next question';
    next.classList.remove('hidden');
    next.focus();
  }

  function advance() {
    if (!locked) return;
    if (position < queue.length - 1) {
      position += 1;
      renderQuestion();
    } else {
      showResults();
    }
  }

  function showResults() {
    active.classList.add('hidden');
    result.classList.remove('hidden');
    const correct = answers.filter(answer => answer.correct).length;
    const pct = Math.round(correct / answers.length * 100);
    const best = Math.max(pct, Number(localStorage.getItem('icml2026-quiz-best') || 0));
    localStorage.setItem('icml2026-quiz-best', String(best));
    document.getElementById('score-number').textContent = `${pct}%`;
    document.getElementById('score-ring').style.setProperty('--score', `${pct}%`);
    document.getElementById('result-title').textContent = pct >= 90 ? 'You can teach the map.' : pct >= 80 ? 'Strong broad understanding.' : pct >= 65 ? 'The map is taking shape.' : 'Rebuild the foundations.';
    document.getElementById('result-message').textContent = `${correct} of ${answers.length} correct. ${pct >= 80 ? 'Choose an area for deeper study.' : 'Review the categories below, then retry only what you missed.'}`;
    const categories = [...new Set(answers.map(answer => QUESTIONS[answer.questionIndex].category))];
    document.getElementById('category-results').innerHTML = categories.map(name => {
      const subset = answers.filter(answer => QUESTIONS[answer.questionIndex].category === name);
      const score = subset.filter(answer => answer.correct).length;
      return `<div class="card"><h3>${name}</h3><p class="metric">${score}/${subset.length}</p></div>`;
    }).join('');
    const missed = answers.filter(answer => !answer.correct).map(answer => answer.questionIndex);
    const retry = document.getElementById('retry-missed');
    retry.classList.toggle('hidden', missed.length === 0);
    retry.onclick = () => startQuiz('retry', missed);
  }

  document.querySelectorAll('[data-quiz-mode]').forEach(button => button.addEventListener('click', () => startQuiz(button.dataset.quizMode)));
  next.addEventListener('click', advance);
  document.getElementById('restart-quiz').addEventListener('click', () => {
    result.classList.add('hidden');
    start.classList.remove('hidden');
    updateBestLabel();
  });
  document.addEventListener('keydown', event => {
    if (!active.classList.contains('hidden') && !locked && ['1', '2', '3', '4'].includes(event.key)) answerQuestion(Number(event.key) - 1);
    else if (!active.classList.contains('hidden') && locked && (event.key === 'Enter' || event.key === ' ')) { event.preventDefault(); advance(); }
  });
  updateBestLabel();
})();

