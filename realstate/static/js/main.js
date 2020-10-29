const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// i wanna fade out the alert after three secondes
setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000)