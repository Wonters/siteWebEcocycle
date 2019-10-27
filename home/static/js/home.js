function HiddenServices() {
    let classbloc = document.getElementsByClassName('service');
    for (let i in classbloc) {
        let bloci = classbloc[i];
        bloci.hidden = true;
    }
}

function showHidden(id){
    HiddenServices();
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







