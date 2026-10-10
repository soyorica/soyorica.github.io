const english = document.documentElement.lang === 'en';
for (const link of document.querySelectorAll('[data-language-switch]')) {
  link.addEventListener('click', () => {
    link.hash = window.location.hash;
  });
}
for (const button of document.querySelectorAll('[data-copy]')) {
  button.hidden = false;
  button.addEventListener('click', async () => {
    const status = button.parentElement.querySelector('.copy-status');
    try {
      await navigator.clipboard.writeText(button.dataset.copy);
      status.textContent = english ? 'Copied.' : 'コピーしました。';
    } catch {
      const range = document.createRange();
      range.selectNodeContents(button.parentElement.querySelector('code'));
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = english ? 'Press Ctrl+C to copy the selected path.' : '選択したパスを Ctrl+C でコピーしてください。';
    }
  });
}

// Highlight the section currently being read in the page contents.
const contentsLinks = [...document.querySelectorAll('.toc a[href^="#"]')];
const sections = contentsLinks.map(link => ({
  link,
  heading: document.getElementById(link.hash.slice(1))
})).filter(section => section.heading);
if (sections.length) {
  function highlightSection() {
    let current = sections[0];
    for (const section of sections) {
      if (section.heading.getBoundingClientRect().top <= 160) {
        current = section;
      }
    }
    if (window.scrollY > 0 && window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4) {
      current = sections[sections.length - 1];
    }
    for (const section of sections) {
      if (section === current) {
        section.link.setAttribute('aria-current', 'location');
      } else {
        section.link.removeAttribute('aria-current');
      }
    }
  }
  let scheduled = false;
  function scheduleHighlight() {
    if (scheduled) {
      return;
    }
    scheduled = true;
    requestAnimationFrame(() => {
      scheduled = false;
      highlightSection();
    });
  }
  window.addEventListener('scroll', scheduleHighlight, { passive: true });
  window.addEventListener('resize', scheduleHighlight);
  window.addEventListener('hashchange', scheduleHighlight);
  window.addEventListener('load', scheduleHighlight);
  highlightSection();
}
