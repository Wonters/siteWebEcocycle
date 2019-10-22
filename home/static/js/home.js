function showHidden(id){
    let bloc = document.getElementById(id);
    if(bloc.hidden == false){
        bloc.hidden = true;
        $('#'+id).addClass('moove');
    }
    else {
        bloc.hidden = false;
        $('#'+id).removeClass('moove');

    }
}

$(window).scroll(
    function () {

    }
)



