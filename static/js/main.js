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