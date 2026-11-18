/* ========================================
   LANDING PAGE JAVASCRIPT
   ======================================== */

// Counter animation for stats
function animateCounter(element, target, duration = 1500) {
  const start = 0;
  const startTime = performance.now();
  const isDecimal = target % 1 !== 0;

  function update(currentTime) {
    const elapsed = currentTime - startTime;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3); // easeOutCubic
    const current = start + (target - start) * eased;
    element.textContent = isDecimal ? current.toFixed(1) : Math.floor(current);
    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}

// IntersectionObserver for scroll animations
const observerOptions = {
  root: null,
  rootMargin: '0px 0px -100px 0px',
  threshold: 0.1
};

const animateOnScroll = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      animateOnScroll.unobserve(entry.target);
    }
  });
}, observerOptions);

// Initialize all animations
document.addEventListener('DOMContentLoaded', () => {
  // 1. Counter animations for hero stats
  const heroStats = document.querySelectorAll('.hero-stat-number[data-count]');
  const heroStatsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseFloat(el.dataset.count);
        animateCounter(el, target, 1800);
        heroStatsObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });
  heroStats.forEach(el => heroStatsObserver.observe(el));

  // 2. Counter animations for footer stats
  const footerStats = document.querySelectorAll('.stat-number[data-count]');
  const footerStatsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseFloat(el.dataset.count);
        animateCounter(el, target, 1500);
        footerStatsObserver.unobserve(el);
      }
    });
  }, { threshold: 0.5 });
  footerStats.forEach(el => footerStatsObserver.observe(el));

  // 3. Feature cards staggered animation
  const featureCards = document.querySelectorAll('.feature-card');
  featureCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
  });

  const featuresObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        featuresObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });
  featureCards.forEach(el => featuresObserver.observe(el));

  // 4. Step cards animation
  const stepCards = document.querySelectorAll('.step-card');
  stepCards.forEach((card, index) => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = `opacity 0.6s ease ${index * 0.15}s, transform 0.6s ease ${index * 0.15}s`;
  });

  const stepsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        stepsObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });
  stepCards.forEach(el => stepsObserver.observe(el));

  // 5. Stat items animation
  const statItems = document.querySelectorAll('.stat-item');
  statItems.forEach((item, index) => {
    item.style.opacity = '0';
    item.style.transform = 'translateY(20px)';
    item.style.transition = `opacity 0.5s ease ${index * 0.1}s, transform 0.5s ease ${index * 0.1}s`;
  });

  const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        statsObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.2 });
  statItems.forEach(el => statsObserver.observe(el));

  // 6. Header scroll effect
  const header = document.querySelector('.landing-header');
  let lastScroll = 0;
  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    if (currentScroll > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
    lastScroll = currentScroll;
  }, { passive: true });

  // 7. Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        const headerOffset = 80;
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
        window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
      }
    });
  });

  // 8. Feature card hover effect enhancement
  document.querySelectorAll('.feature-card').forEach(card => {
    card.addEventListener('mouseenter', () => {
      card.style.transform = 'translateY(-8px) scale(1.01)';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'translateY(0) scale(1)';
    });
  });

  // 9. CTA button ripple effect
  document.querySelectorAll('.btn-primary, .btn-ghost').forEach(btn => {
    btn.addEventListener('click', function(e) {
      const ripple = document.createElement('span');
      ripple.classList.add('ripple');
      this.appendChild(ripple);
      const rect = this.getBoundingClientRect();
      ripple.style.left = `${e.clientX - rect.left}px`;
      ripple.style.top = `${e.clientY - rect.top}px`;
      setTimeout(() => ripple.remove(), 600);
    });
  });

  // 10. Illustration card subtle parallax
  const illustration = document.querySelector('.illustration-card');
  if (illustration) {
    document.addEventListener('mousemove', (e) => {
      const { clientX, clientY } = e;
      const { innerWidth, innerHeight } = window;
      const x = (clientX / innerWidth - 0.5) * 20;
      const y = (clientY / innerHeight - 0.5) * 20;
      illustration.style.transform = `perspective(1000px) rotateY(${x}deg) rotateX(${-y}deg)`;
    });
    document.addEventListener('mouseleave', () => {
      illustration.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg)';
    });
  }

  // 11. Floating shapes subtle parallax
  const shapes = document.querySelectorAll('.hero-shape');
  document.addEventListener('mousemove', (e) => {
    const { clientX, clientY } = e;
    const { innerWidth, innerHeight } = window;
    const x = (clientX / innerWidth - 0.5) * 2;
    const y = (clientY / innerHeight - 0.5) * 2;
    shapes.forEach((shape, i) => {
      const factor = (i + 1) * 0.5;
      shape.style.transform = `translate(${x * factor * 30}px, ${y * factor * 30}px)`;
    });
  });
});

// Add ripple CSS dynamically
const style = document.createElement('style');
style.textContent = `
  .btn-primary, .btn-ghost { position: relative; overflow: hidden; }
  .ripple {
    position: absolute; border-radius: 50%; background: rgba(255,255,255,0.4);
    transform: scale(0); animation: ripple 0.6s ease-out; pointer-events: none;
  }
  .btn-ghost .ripple { background: rgba(62, 98, 89, 0.3); }
  @keyframes ripple {
    to { transform: scale(4); opacity: 0; }
  }
`;
document.head.appendChild(style);