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

$('#assignment_due').min = date.getFullYear() + "-" +  parseInt(date.getMonth() + 1 ) + "-" + date.getDate();

$.fn.jQuerySimpleCounter = function( options ) {
   var settings = $.extend({
       start:  0,
       end:    100,
       easing: 'swing',
       duration: 400,
       complete: ''
   }, options );

   var thisElement = $(this);

   $({count: settings.start}).animate({count: settings.end}, {
     duration: settings.duration,
     easing: settings.easing,
     step: function() {
        var mathCount = Math.ceil(this.count);
        thisElement.text(mathCount);
     },
     complete: settings.complete
  });
};


$('#number1').jQuerySimpleCounter({end: 13,duration: 3000});
$('#number2').jQuerySimpleCounter({end: 65,duration: 3000});
$('#number3').jQuerySimpleCounter({end: 50405, duration: 10000});
$('#number4').jQuerySimpleCounter({end: 305,duration: 2500});


    document.getElementById("yes").addEventListener('change', function() {
       defineSetting(this.value)
    })
    document.getElementById("no").addEventListener('change', function() {
      defineSetting(this.value)
   })
    function defineSetting(setting) {
      if (setting == "True") {
        document.getElementById("stud_div").classList.remove('hidden');
        document.getElementById("prof_div").classList.add('hidden');
      } else {
         document.getElementById("stud_div").classList.add('hidden');
         document.getElementById("prof_div").classList.remove('hidden');
      }
    }

    window.onload=function(){defineSetting("True")}
