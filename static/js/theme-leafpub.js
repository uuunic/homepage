// Leafpub Theme
$(function() {
    // Toggle nav menu
    $('.nav-toggle').on('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
        $('html').toggleClass('nav-open');
    });

    // Close menu when clicking outside of it
    $(document).on('click touchstart', function(event) {
        if(
            $('html').is('.nav-open') &&
            !$(event.target).closest('.nav-items').length &&
            !$(event.target).parents().andSelf().is('.nav-toggle')
        ) {
            $('html').removeClass('nav-open');
        }
    });

    // Close menu on escape
    $(document).on('keydown', function(event) {
        if(event.keyCode === 27) {
            $('html').removeClass('nav-open');
        }
    });
});