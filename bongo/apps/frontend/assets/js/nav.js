// Set up listeners to trigger the following behavior:
// - hiding the large header on scroll
// - displaying the mini header on scroll
// - displaying the sidebar on scroll
// - displaying the sidebar on small viewports
// - displaying the basement menu

// Handles minimizing the header on scroll and viewport shrink
Zepto(function($){
    var $hw = $(".header-wrapper");
    var $header = $("header");

    var checkWidth = function(){
        if (window.innerWidth <= 645) {
            $hw.addClass("min-by-width");
        } else {
            $hw.removeClass("min-by-width");
        }
    };

    checkWidth();

    $(window).on("resize", function() {
        window.requestAnimationFrame(function(){
            checkWidth();
        });
    });

    $(window).on("scroll", function() {
        window.requestAnimationFrame(function(){
            if (window.pageYOffset >= 145) {
                $header.addClass("fall-in");
                $hw.addClass("min-by-scroll");
            } else {
                $header.removeClass("fall-in");
                $hw.removeClass("min-by-scroll");
            }
        });
    });
});

// Handles the basement menu
Zepto(function($){
    var $burger = $("nav");
    var $burgerlines = $(".burger-lines");
    var $menu = $(".basement-menu");
    var $content = $(".main-content");

    $burger.on("click", function(){
        if(window.innerWidth <= 645 || window.pageYOffset >= 145){
            $menu.toggleClass("active");
            $burgerlines.toggleClass("active");
            $content.toggleClass("shift-menu");
        }
    });
});

