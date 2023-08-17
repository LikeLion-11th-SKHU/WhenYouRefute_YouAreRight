// nav

var menuBtn = document.querySelector('.menu-btn');
var nav = document.querySelector('.navbar_m');
var lineOne = document.querySelector('.navbar_m .menu-btn .line--1');
var lineTwo = document.querySelector('.navbar_m .menu-btn .line--2');
var lineThree = document.querySelector('.navbar_m .menu-btn .line--3');
var link = document.querySelector('.navbar_m .nav-links');
menuBtn.addEventListener('click', () => {
    nav.classList.toggle('nav-open');
    lineOne.classList.toggle('line-cross');
    lineTwo.classList.toggle('line-fade-out');
    lineThree.classList.toggle('line-cross');
    link.classList.toggle('fade-in');
})



// 슬라이드

const slides = document.querySelector('.slides-box');
const slideimg = document.querySelectorAll('.slide-li img');
let currentIdx = 0; 
const slideCount = slideimg.length;
const prev = document.querySelector('.prev');
const next = document.querySelector('.next');
const slideWidth = 90;
makeClone();
initfunction();
autoSlide();

function makeClone() {
    let cloneSlide_first = slideimg[0].cloneNode(true);
    let cloneSlide_last = slides.lastElementChild.cloneNode(true);
    slides.append(cloneSlide_first);
    slides.insertBefore(cloneSlide_last, slides.firstElementChild);

}

function initfunction() {
    slides.style.width = (slideWidth) * (slideCount+2) + 'vw';
    slides.style.left = -(slideWidth) + 'vw';
}

function autoSlide() {
    setInterval(function () {
        if (currentIdx <= slideCount -1){
            slides.style.left = -(currentIdx + 2) * (slideWidth) + 'vw';
            slides.style.transition = `${0.5}s ease-out`;
        }
        if (currentIdx === slideCount - 1) {
            setTimeout(function () {
                slides.style.left = -(slideWidth) + 'vw';
                slides.style.transition = `${0}s ease-out`;
            }, 500);
            currentIdx = -1;
        }
        currentIdx += 1;
    }, 4000);
}

next.addEventListener('click', function(){
    if (currentIdx <= slideCount -1){
        slides.style.left = -(currentIdx + 2) * (slideWidth) + 'vw';
        slides.style.transition = `${0.5}s ease-out`;
    }
    if (currentIdx === slideCount - 1) {
        setTimeout(function () {
            slides.style.left = -(slideWidth) + 'vw';
            slides.style.transition = `${0}s ease-out`;
        }, 500);
        currentIdx = -1;
    }
    currentIdx += 1;
});

prev.addEventListener('click', function(){
    if (currentIdx >=0) {
        slides.style.left = -currentIdx * (slideWidth)+'vw';
        slides.style.transition = `${0.5}s ease-out`;
    }
    if (currentIdx === 0){
        setTimeout(function() {
            slides.style.left = -slideCount * (slideWidth) +'vw';
            slides.style.transition = `${0}s ease-out`;
        }, 500);
        currentIdx = slideCount;
    }
    currentIdx -= 1;
});
