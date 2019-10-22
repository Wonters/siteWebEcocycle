function showHidden(id) {
    let bloc = document.getElementById(id);
    HiddenServices();
    if (bloc.hidden == false) {
        bloc.hidden = true;
    } else {
        bloc.hidden = false;

    }
}

function HiddenServices() {
    let classbloc = document.getElementsByClassName('service');
    for (let i in classbloc) {
        let bloci = classbloc[i];
        bloci.hidden = true;
    }
}


window.scrollTo(0, 500); // moove to the direct text in the page
// listen for scroll
let positionInPage = $('#fabdescription').offset().top;
$(window).scroll(
    function () {
        if ($(window).scrollTop() >= positionInPage - 400) {
            // fixed
            $('.btn-services').addClass("moove");
        } else {
            // relative
            $('.btn-services').removeClass("moove");
            HiddenServices();
        }
    }
);
