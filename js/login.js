document.getElementById('iniciar_sesion').addEventListener("click",pulse,false);

function pulse(){
    var usuario = document.getElementById('usuario').value 
    var password = document.getElementById('passowrd').value
    fetch('http://127.0.0.1:5000/login/users', {mode: 'no-cors'})
    .then(function(response){
        console.log(response);
    })
}