$(function () {
    // 恢复盒子大小
    $('.home').width(innerWidth)

    var topSwiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        slidesPerView: 1,
        paginationClickable: true,
        spaceBetween: 30,
        loop: true,
        autoplay: 3000,
        effect: 'coverflow',
    });


    var mustbuySwiper = new Swiper('#mustbuySwiper', {
        slidesPerView: 3,
        spaceBetween: 5,
        loop: true,
    });
})