// Importing 'crypto' module
function hashear(string) {

    let hash = 0;

    if (string.length == 0) return hash;

    for (i = 0; i < string.length; i++) {
        char = string.charCodeAt(i);
        hash = ((hash << 5) - hash) + char;
        hash = hash & hash;
    }

    return hash;
}



users=['lucas']
passwds=[hashear('pass')]






document.querySelector('#enviar').addEventListener('click',(e)=>{
    e.preventDefault();
    let user=document.querySelector('#nombre');
    let pass=hashear(document.querySelector('#password').value);
    if (users.includes(user.value)&&passwds.includes(pass)){
        window.location.href="../Pages/MiTienda.html";
    }else{
        document.write('Contraseña incorrecta');
    }
})