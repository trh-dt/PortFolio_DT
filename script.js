// Анимация появления карточек при прокрутке
const observerOptions = {
  threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, observerOptions);

document.querySelectorAll('.card').forEach(card => {
  observer.observe(card);
});

// Интерактивный курсор
const cursor = document.createElement('div');
cursor.classList.add('custom-cursor');
document.body.appendChild(cursor);

document.addEventListener('mousemove', (e) => {
  cursor.style.left = e.clientX + 'px';
  cursor.style.top = e.clientY + 'px';
});

document.querySelectorAll('a, button, .card').forEach(element => {
  element.addEventListener('mouseenter', () => cursor.classList.add('active'));
  element.addEventListener('mouseleave', () => cursor.classList.remove('active'));
});

// Эффект частиц
const particlesContainer = document.createElement('div');
particlesContainer.classList.add('particles');
document.body.appendChild(particlesContainer);

for (let i = 0; i < 50; i++) {
  const particle = document.createElement('div');
  particle.classList.add('particle');
  particle.style.left = Math.random() * 100 + 'vw';
  particle.style.animationDelay = Math.random() * 20 + 's';
  particlesContainer.appendChild(particle);
}

// Кнопка прокрутки вверх
const scrollButton = document.createElement('div');
scrollButton.classList.add('scroll-to-top');
document.body.appendChild(scrollButton);

window.addEventListener('scroll', () => {
  if (window.pageYOffset > 300) {
    scrollButton.classList.add('visible');
  } else {
    scrollButton.classList.remove('visible');
  }
});

scrollButton.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth'
  });
}); 