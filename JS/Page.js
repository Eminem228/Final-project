const prevButton = document.querySelector('.carousel-prev');
const nextButton = document.querySelector('.carousel-next');
const carousel = document.querySelector('.carousel');
const itemWidth = document.querySelector('.carousel-item').offsetWidth;
const gap = parseInt(window.getComputedStyle(document.querySelector('.carousel-item')).marginRight);
let currentIndex = 0;

function updateCarousel() {
    const offset = -(itemWidth + gap) * currentIndex;
    carousel.style.transform = `translateX(${offset}px)`;
}

nextButton.addEventListener('click', () => {
    if (currentIndex < carousel.children.length  -1) {
        currentIndex++;
    } else {
        currentIndex = 0;
    }
    updateCarousel();
});

prevButton.addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
    } else {
        currentIndex = carousel.children.length - 1;
    }
    updateCarousel();
});
