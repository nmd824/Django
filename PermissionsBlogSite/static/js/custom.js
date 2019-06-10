/*
-------------------------------------------------------------------------
* Template Name    : Pofto - Responsive Minimal Template                * 
* Author           : ThemesBoss                                         *
* Version          : 1.0.0                                              *
* Created          : February 2019                                      * 
* File Description : Main JS file of the template                       *
*------------------------------------------------------------------------
*/

! function($) {
    "use strict";

    var Pofto = function() {};

        Pofto.prototype.initStickyAddMenu = function() {
            $(window).on('scroll', function() {
                var scroll = $(window).scrollTop();

                if (scroll >= 50) {
                    $(".sticky").addClass("stickyadd");
                } else {
                    $(".sticky").removeClass("stickyadd");
                }
            });
        },

        Pofto.prototype.initMenuSub = function() {
            $('a.first_sub_menu').on('click', function(e) {
                if (window.matchMedia('(max-width: 992px)').matches) {
                    e.preventDefault();
                    $(this).toggleClass("active_menu");
                    $(this).next($('.sec_sub_menu')).slideToggle();
                }
            });
            $('a.nav-link[href^="#"]').on('click', function(event) {
                var $anchor = $(this);
                $('html, body').stop().animate({
                    scrollTop: $($anchor.attr('href')).offset().top
                }, 1500, 'easeInOutExpo');
                event.preventDefault();
            });
        },

        Pofto.prototype.initMenuActive = function() {
            $(".main_menu a").each(function() {
                if (this.href == window.location.href) {
                    $(this).parent().addClass("active"); // add active to li of the current link
                    $(this).parent().parent().parent().addClass("active"); // add active class to an anchor
                    $(this).parent().parent().parent().parent().parent().addClass("active"); // add active class to an anchor
                }
            });
        },

        Pofto.prototype.initSmoothLink = function() {
            $('.scroll_down').on('click', function(event) {
                var $anchor = $(this);
                $('html, body').stop().animate({
                    scrollTop: $($anchor.attr('href')).offset().top - 50
                }, 1500, 'easeInOutExpo');
                event.preventDefault();
            });
        },

        Pofto.prototype.initSmoothLink = function() {
            $('.scroll_down').on('click', function(event) {
                var $anchor = $(this);
                $('html, body').stop().animate({
                    scrollTop: $($anchor.attr('href')).offset().top - 50
                }, 1500, 'easeInOutExpo');
                event.preventDefault();
            });
        },

        Pofto.prototype.initMFPImage = function() {
            $('.img-zoom').magnificPopup({
                type: 'image',
                closeOnContentClick: true,
                mainClass: 'mfp-fade',
                gallery: {
                    enabled: true,
                    navigateByImgClick: true,
                    preload: [0, 1]
                }
            });
        },

        Pofto.prototype.initWorkFilter = function() {
            $(window).on('load', function() {
                var $container = $('.work-filter');
                var $filter = $('#menu-filter');
                $container.isotope({
                    filter: '*',
                    layoutMode: 'masonry',
                    animationOptions: {
                        duration: 750,
                        easing: 'linear'
                    }
                });

                $filter.find('a').on("click", function() {
                    var selector = $(this).attr('data-filter');
                    $filter.find('a').removeClass('active');
                    $(this).addClass('active');
                    $container.isotope({
                        filter: selector,
                        animationOptions: {
                            animationDuration: 750,
                            easing: 'linear',
                            queue: false,
                        }
                    });
                    return false;
                });
            });

        },

        Pofto.prototype.initClientSlider = function() {
            $("#owl-demo").owlCarousel({
                autoPlay: 10000,
                items: 3,
                itemsDesktop: [1199, 3],
                itemsDesktopSmall: [979, 3]
            });
        },

        Pofto.prototype.initBTT = function() {
            $(window).on('scroll', function() {
                if ($(this).scrollTop() > 100) {
                    $('.back_top').fadeIn();
                } else {
                    $('.back_top').fadeOut();
                }
            });
            $('.back_top').on('click', function() {
                $("html, body").animate({
                    scrollTop: 0
                }, 1000);
                return false;
            });
        },

        Pofto.prototype.init = function() {
            this.initStickyAddMenu();
            this.initMenuSub();
            this.initMenuActive();
            this.initSmoothLink();
            this.initMFPImage();
            this.initWorkFilter();
            this.initClientSlider();
            this.initFunFacts();
            this.initBTT();
        },
        //init
        $.Pofto = new Pofto, $.Pofto.Constructor = Pofto
}(window.jQuery),

//initializing
function($) {
    "use strict";
    $.Pofto.init();
}(window.jQuery);