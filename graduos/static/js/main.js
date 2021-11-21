function dropdownMenu(){
   var dropDown = document.getElementById("dropdownClick");
   if(dropDown.className === "topnav"){
      dropDown.className += " responsive";
   } else{
      dropDown.className = "topnav";
   }
}

const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(() => {
    $('#message').fadeOut('slow');
 }, 3000);

$(document).ready(function(){
   $("#courses-slider").owlCarousel({
       items:3,
       itemsDesktop:[1000,3],
       itemsDesktopSmall:[979,2],
       itemsTablet:[768,2],
       itemsMobile:[650,1],
       pagination:true,
       autoPlay:true
   })
});