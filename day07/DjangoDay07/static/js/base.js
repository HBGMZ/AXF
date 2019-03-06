$(function () {

    var index = localStorage.getItem('index')
    console.log(index)
    if (index){
        var $current = $('.nav.navbar-nav:first>li').eq(index)
    } else {
        var $current = $('.nav.navbar-nav:first>li:first')
    }
    $current.addClass('active')

    $('.nav.navbar-nav:first>li').click(function () {
        $current.removeClass('active')
        $current = $(this)
        $current.addClass('active')

        // 记录下标
        localStorage.setItem("index", $(this).index());
    })
})