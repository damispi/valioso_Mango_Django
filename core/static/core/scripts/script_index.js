var prevSize = window.innerWidth;
class Articulo {
    imgs=[];
    titulo;
    descripcion;
    precio;
    constructor(imgs, titulo, descripcion, precio) {
        this.imgs = imgs;
        this.descripcion = descripcion;
        this.titulo = titulo;
        this.precio = precio;
    }
}


// var art1 = new Articulo("Sources/Bici2.jpeg", "Bicicleta rodado 26", "Casi nueva", "126");
// var art2 = new Articulo("Sources/tv.jpg", "Tv 32 pulgadas", "Usada, en buen estado", "150");
// var art3 = new Articulo("Sources/YerbaSalus2.jpg", "Yerba Salus 1Kg", "Bulto por 10 paquetes", "30");
var articulos = [];

function dibujar(arts) {
    let box = document.getElementById('box');
    box.innerHTML = '';
    for (let i = 0; i < arts.length; i++) {
        box.innerHTML += `<article class="flex-item">
        <a href=${arts[i].imgs[0]}>
            <img src=${arts[i].imgs[0]} alt="Imagen de producto">
                <header class="image-header">
                    <h2 class="image-title1">${arts[i].titulo}</h2>
                </header>
                <footer class="image-info">
                    <h2 class="image-title2">${arts[i].descripcion}</h2>
                    <p class="image-description">ლ${arts[i].precio}</p>
                </footer>
        </a>
        </article>`
    }
}

const busqueda = document.getElementById('busqueda');
const busquedaYPrecio = document.getElementById('busqueda-y-precio');
busqueda.addEventListener('keydown', (e) => {
    if (e.keyCode == 13) {
        articulos=[]
        e.preventDefault();
        if (busqueda.value.length != 0) {
            let box = document.getElementById('box');
            box.classList.add('con-prods');
            fetch(`get_productos_${busqueda.value}`).then(response=>response.text()).then(result=>
            {
                let res=JSON.parse(result).res;
                for (let i=0;i<res.length;i++){
                    
                    let art = new Articulo([], res[i].titulo, res[i].descripcion, res[i].precio);
                    fetch(res[i].link1).then(result=>{
                        art.imgs.push(result.url)
                    }).then(x=>
                        fetch(res[i].link2).then(result => {
                            art.imgs.push(result.url)
                        }).then(x=>
                            fetch(res[i].link3).then(result => {
                                art.imgs.push(result.url)
                                console.log(result.url)
                                console.log[`${i}/${res.length}`]
                                articulos.push(art)
                            }).then(x=>
                                dibujar(articulos)
                            )
                        )
                    )
                }
            }).then(sleep(300).then(() => {
                dibujar(articulos);
                console.log(articulos)
            }));
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
let precioDolar = precioOro / 10000;
let precioArs = precioDolar * 1000;
if (apiFuncionando) {
    fetch("https://www.goldapi.io/api/XAU/USD", requestOptions)
        .then(response => response.text())
        .then(result => {
            let res = JSON.parse(result)
            precioOro = res.open_price;
            precioDolar = precioOro / 10000;
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
        precioArs = precioDolar * data.compra;
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


let main = document.querySelector('main');

// Función para cambiar la fuente del video
function changeVideoSource() {
    const screenWidth = window.innerWidth;
    let host = window.location.hostname;
    if (screenWidth < 768 && prevSize > 768) {
        window.location.href = "" + screenWidth;
    } else if ((screenWidth >= 768 && screenWidth < 1024) && (prevSize < 768 || prevSize >= 1024)) {
        // Tableta
        window.location.href = "" + screenWidth;
    } else if (screenWidth >= 1024 && prevSize < 1024) {
        // Pantalla grande (PC)
        window.location.href = "" + screenWidth;
    }
}
// Ejecutar la función al cargar la página y en cambios de tamaño de ventana
window.addEventListener('resize', changeVideoSource);

// Deshabilita los controles
video.controls = false;