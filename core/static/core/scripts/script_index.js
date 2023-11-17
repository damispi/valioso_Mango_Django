class Articulo {
    img;
    textoHeader;
    textoFooter;
    textoPrecio;
    constructor(img, textoHeader, textoFooter, textoPrecio) {
        this.img = img;
        this.textoFooter = textoFooter;
        this.textoHeader = textoHeader;
        this.textoPrecio = textoPrecio;
    }
}


var art1 = new Articulo("Sources/Bici2.jpeg", "Bicicleta rodado 26", "Casi nueva", "126");
var art2 = new Articulo("Sources/tv.jpg", "Tv 32 pulgadas", "Usada, en buen estado", "150");
var art3 = new Articulo("Sources/YerbaSalus2.jpg", "Yerba Salus 1Kg", "Bulto por 10 paquetes", "30");
var articulos = [art1, art2, art3];

function dibujar(arts) {
    let box = document.getElementById('box');
    box.innerHTML = '';
    for (let i = 0; i < arts.length; i++) {
        box.innerHTML += `<article class="flex-item">
        <a href=${arts[i].img}>
            <img src=${arts[i].img} alt="Imagen de producto">
                <header class="image-header">
                    <h2 class="image-title1">${arts[i].textoHeader}</h2>
                </header>
                <footer class="image-info">
                    <h2 class="image-title2">${arts[i].textoFooter}</h2>
                    <p class="image-description">ლ${arts[i].textoPrecio}</p>
                </footer>
        </a>
        </article>`
    }
}

const busqueda = document.getElementById('busqueda');
const busquedaYPrecio = document.getElementById('busqueda-y-precio');
busqueda.addEventListener('keydown', (e) => {
    if (e.keyCode == 13) {
        e.preventDefault();
        if (busqueda.value.length != 0) {
            let box=document.getElementById('box');
            box.classList.add('con-prods');
            sleep(300).then(() => { dibujar(articulos); })
        }
    }
})
busqueda.addEventListener('input', () => {
    dibujar([]);
    document.getElementById('box').classList.remove('con-prods');
    let cuadro = document.getElementsByClassName('caja-busqueda');
    cuadro[0].classList.toggle('visible', busqueda.value.length != 0)
    cuadro[0].classList.toggle('para-caja', busqueda.value.length != 0)

})

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}



document.body.addEventListener('click', function (e) {
    if (!wide.matches) {
        let ids = [];
        ids.push(e.target);
        ids.push(e.target.parentNode);
        ids.push(e.target.parentNode.parentNode);
        let esId = false;
        let esClass = false;
        for (const id of ids) {
            if (id.id == 'menu-hamburguesa') {
                esId = true;
            }
            if (id.classList && id.classList.contains('boton-nav')) {
                esClass = true;
            }
        }
        let nav = document.getElementsByTagName('nav');
        let menu = document.getElementsByClassName('menu');
        if ((!esClass && menu[0].classList.contains('visible')) || (esId && menu[0].classList.contains('visible'))) {
            menu[0].classList.remove('visible');
            nav[0].classList.remove('para-hamburguesa');
            menu[0].style.position = 'absolute';
            menu[0].style.display = 'none';
        } else if (esId && !menu[0].classList.contains('visible')) {
            menu[0].style.display = 'flex';
            sleep(50).then(() => {
                nav[0].classList.toggle('para-hamburguesa');
                menu[0].classList.add('visible');
                menu[0].style.position = 'static';
            })
        }
    }

});

var myHeaders = new Headers();
myHeaders.append("x-access-token", "goldapi-dxjqzrlo8nrtiu-io");
myHeaders.append("Content-Type", "application/json");

var requestOptions = {
    method: 'GET',
    headers: myHeaders,
    redirect: 'follow'
};
let apiFuncionando = false;
let precioOro = 1651.651;
let precioDolar=precioOro/10000;
let precioArs=precioDolar*1000;
if (apiFuncionando) {
    fetch("https://www.goldapi.io/api/XAU/USD", requestOptions)
        .then(response => response.text())
        .then(result => {
            let res = JSON.parse(result)
            precioOro = res.open_price;
            precioDolar=precioOro/10000;
            document.querySelector('#precio-oro').textContent = `Precio por onza de oro en USD $${(precioOro).toFixed(2)}`;
            document.querySelector('#precio-dolar').textContent = `Valor del mango en USD: $${precioDolar.toFixed(2)}`;
        })
        .catch(error => console.log('error', error));
} else {
    document.querySelector('#precio-oro').textContent = `Precio por onza de oro en USD $${(precioOro).toFixed(2)}`
    document.querySelector('#precio-dolar').textContent = `Valor del mango en USD: $${precioDolar.toFixed(2)}`;
}

fetch("https://dolarapi.com/v1/dolares/blue")
    .then(response => response.json())
    .then(data => {
        precioArs=precioDolar*data.compra;
        document.querySelector('#precio-peso').textContent = `Valor del mango en ARS: $${precioArs.toFixed(2)}`
    });




let wide = window.matchMedia("(min-width: 550px");
function wideSize(wide) {
    let nav = document.getElementsByTagName('nav');
    let menu = document.getElementsByClassName('menu');
    if (wide.matches) {
        menu[0].style.display = 'flex';
        menu[0].classList.add('visible');
        menu[0].style.position = 'static';
    } else {
        menu[0].style.display = 'none';
        menu[0].classList.remove('visible');
        menu[0].style.position = 'absolute';
        nav[0].classList.remove('para-hamburguesa');
    }
}
wideSize(wide);
wide.addListener(wideSize);

// Obtener una referencia al video
const video = document.getElementById('responsive-video');

// Función para cambiar la fuente del video
function changeVideoSource() {
    const screenWidth = window.innerWidth;

    if (screenWidth < 768) {
        // Dispositivo móvil
        video.src = 'Sources/registrateVertical FULL (375 x 667 px).mp4';
    } else if (screenWidth >= 768 && screenWidth < 1024) {
        // Tableta
        video.src = 'Sources/registrateHorizontal FULL (1366 x 768 px).mp4';
    } else {
        // Pantalla grande (PC)
        video.src = 'Sources/registrateHorizontal FULL (1440 x 900 px).mp4';
    }
}

// Ejecutar la función al cargar la página y en cambios de tamaño de ventana
window.addEventListener('load', changeVideoSource);
window.addEventListener('resize', changeVideoSource);

// Deshabilita los controles
video.controls = false;
