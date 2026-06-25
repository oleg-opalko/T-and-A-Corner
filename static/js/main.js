(function () {
    'use strict';

    /* Mobile menu */
    const menuToggle = document.querySelector('.menu-toggle');
    const siteNav = document.querySelector('.site-nav');

    if (menuToggle && siteNav) {
        menuToggle.addEventListener('click', () => {
            const isOpen = siteNav.classList.toggle('is-open');
            menuToggle.classList.toggle('is-open', isOpen);
            menuToggle.setAttribute('aria-expanded', String(isOpen));
            menuToggle.setAttribute('aria-label', isOpen ? 'Close menu' : 'Open menu');
        });

        siteNav.querySelectorAll('a').forEach((link) => {
            link.addEventListener('click', () => {
                siteNav.classList.remove('is-open');
                menuToggle.classList.remove('is-open');
                menuToggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    /* Hero slider */
    const heroSlider = document.querySelector('[data-hero-slider]');
    if (!heroSlider) return;

    const slides = heroSlider.querySelectorAll('.hero-slide');
    const images = heroSlider.querySelectorAll('.hero-image');
    const indicators = heroSlider.querySelectorAll('.hero-indicators button');
    let current = 0;
    let timer;

    function goTo(index) {
        current = index;

        slides.forEach((slide, i) => slide.classList.toggle('is-active', i === index));
        images.forEach((img, i) => img.classList.toggle('is-active', i === index));
        indicators.forEach((btn, i) => btn.classList.toggle('is-active', i === index));
    }

    function next() {
        goTo((current + 1) % slides.length);
    }

    function startAutoplay() {
        timer = setInterval(next, 6000);
    }

    function resetAutoplay() {
        clearInterval(timer);
        startAutoplay();
    }

    indicators.forEach((btn) => {
        btn.addEventListener('click', () => {
            goTo(Number(btn.dataset.goTo));
            resetAutoplay();
        });
    });

    startAutoplay();
})();
