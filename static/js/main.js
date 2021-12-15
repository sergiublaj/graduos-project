function dropdownMenu(){
   var dropDown = document.getElementById('dropdownClick');
   if(dropDown.className === 'topnav'){
      dropDown.className += ' responsive';
   } else{
      dropDown.className = 'topnav';
   }
}

const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(() => {
   $('#message').fadeOut('slow');
}, 3000);

// $('.toast').toast('show');

<<<<<<< HEAD
=======
$("#menu-toggle").click(function(e) {
   e.preventDefault();
   $("#wrapper").toggleClass("toggled");
});
$("#menu-toggle-2").click(function(e) {
   e.preventDefault();
   $("#wrapper").toggleClass("toggled-2");
   $('#menu ul').hide();
});

function initMenu() {
   $('#menu ul').hide();
   $('#menu ul').children('.current').parent().show();
   //$('#menu ul:first').show();
   $('#menu li a').click(
      function() {
         var checkElement = $(this).next();
         if ((checkElement.is('ul')) && (checkElement.is(':visible'))) {
            return false;
         }
         if ((checkElement.is('ul')) && (!checkElement.is(':visible'))) {
            $('#menu ul:visible').slideUp('normal');
            checkElement.slideDown('normal');
            return false;
         }
      }
   );
}
$(document).ready(function() {
   initMenu();
});
>>>>>>> 95f4f7d8b2dbfe38aff590b16199fc3ce68396e9
