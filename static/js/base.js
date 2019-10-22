function animateLike() {
    let pixel = 30;
    let icon = document.getElementById('iconlike');
    let interval = setInterval(dyn, 30);
    function dyn () {
        pixel ++;
        icon.style.fontSize = pixel ;
        if (pixel > 40) {
            icon.style.fontSize = 30;
            clearInterval(interval);
        }
    }

}
function like() {
    animateLike();
    $.ajax(
        {
            url: '/like',
            type: 'GET',
            dataType: 'json',
            data: {like: 1},
            success: function (data) {
                console.log('user liked the site')
                divNblike = document.getElementById('nblike');
                divNblike.innerHTML = data.nblike;
            },
            error: function () {
                console.log('error ajax, request failed')
            }
        }
    )
}

// let inputlike = document.getElementById('datalike');
// let divNblike = document.getElementById('nblike');
// divNblike.innerHTML = inputlike.value;

// listen for scroll
 var positionElementInPage = $('#menubar').offset().top;
 $(window).scroll(
 function() {
 if ($(window).scrollTop() >= positionElementInPage) {
 // fixed
 $('#menubar').addClass("floatable");
 } else {
 // relative
 $('#menubar').removeClass("floatable");
 }
 }
 );

