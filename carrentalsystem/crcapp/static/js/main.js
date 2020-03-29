
$(document).ready(function(){
    $("#collapse").click(function(e){
        $("#subtopbar").toggle( "slide" );

        e.preventDefault();
      });
        $('.subtopbar nav-link.active').removeClass('active');
        $('a[href="' + location.pathname + '"]').closest('li').addClass('active'); 
});