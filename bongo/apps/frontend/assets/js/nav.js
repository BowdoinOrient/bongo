// Set up listeners to trigger the following behavior:
// - hiding the large header on scroll
// - displaying the mini header on scroll
// - displaying the sidebar on scroll
// - displaying the sidebar on small viewports

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