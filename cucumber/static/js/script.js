$(document).ready(function(){
    $("#slide-one").owlCarousel({
        items: 3,
        margin: 50,
        nav: true,
        loop: true,
        dots: false,
        navText : ['<i class="fas fa-arrow-left"></i>','<i class="fas fa-arrow-right"></i>']
    });

    $("#slide-two").owlCarousel({
        items: 1,
        nav: true,
        loop: true,
        dots: false,
        navText : ['<i class="fas fa-arrow-left"></i>','<i class="fas fa-arrow-right"></i>']
    });

    $("#slide-three").owlCarousel({
        items: 2,
        margin: 50,
        nav: true,
        loop: true,
        dots: false,
        stagePadding: 20,
        navText : ['<i class="fas fa-arrow-left"></i>','<i class="fas fa-arrow-right"></i>']
    });
});