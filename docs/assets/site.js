(() => {
  const toggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
  }

  const checks = [...document.querySelectorAll('.lesson-check input')];
  const progress = document.querySelector('[data-learning-progress]');
  const progressLabel = document.querySelector('[data-learning-progress-label]');
  if (checks.length) {
    let saved = {};
    try { saved = JSON.parse(localStorage.getItem('icml2026-learning-progress') || '{}'); } catch (_) {}
    checks.forEach(check => {
      check.checked = Boolean(saved[check.id]);
      check.addEventListener('change', () => {
        saved[check.id] = check.checked;
        localStorage.setItem('icml2026-learning-progress', JSON.stringify(saved));
        updateProgress();
      });
    });
    function updateProgress() {
      const done = checks.filter(check => check.checked).length;
      const pct = Math.round(done / checks.length * 100);
      if (progress) progress.style.width = `${pct}%`;
      if (progressLabel) progressLabel.textContent = `${done} of ${checks.length} lessons marked complete`;
    }
    updateProgress();
  }
})();

