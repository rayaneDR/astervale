'use strict';
// No analytics, remote requests or device access. This site is buildless.
document.querySelectorAll('a[href^="#"]').forEach(link => link.addEventListener('click', () => {
  const target = document.querySelector(link.getAttribute('href'));
  if (target) target.setAttribute('tabindex', '-1');
}));
