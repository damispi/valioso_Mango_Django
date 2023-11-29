

const section = document.querySelector('.flex-container');
const wide = window.matchMedia("(min-width: 701px");


function wideSize(wide) {
    let nav = document.getElementsByTagName('nav');
    let menu = document.getElementById('opciones-nav');
    if (wide.matches) {
        menu.style.display = 'flex'
    } else {
        menu.style.display = 'none';

    }
}
wideSize(wide);
wide.addListener(wideSize);





const modales = ["modal-agregar", "modal-editar", "modal-eliminar"];
const botones = ["boton-agregar", "boton-editar", "boton-eliminar"];
const spans = document.getElementsByClassName("close");
for (let i = 0; i < spans.length; i++) {
    let modal = document.getElementById(modales[i]);
    let btn = document.getElementById(botones[i]);
    btn.addEventListener('click', () => {
        modal.style.display = "block";
    });
    window.addEventListener('click', (event) => {
        if (event.target == modal) {
            let inputs = document.getElementsByTagName('input')
            for (let i = 0; i < inputs.length; i++) {
                if (inputs[i].type != 'submit')
                    inputs[i].value = ''
            }
            let foto2=document.querySelector('#id_foto2').parentNode;
            foto2.style.display='none';
            foto2.nextElementSibling.style.display='none';
            cerrarModal();
        }
    })

    spans[i].addEventListener('click', () => {
        let inputs=document.getElementsByTagName('input')
        for (let i=0;i<inputs.length;i++){
            if (inputs[i].type!='submit')
                inputs[i].value=''
        }
        let foto2 = document.querySelector('#id_foto2').parentNode;
        foto2.style.display = 'none';
        
        foto2.nextElementSibling.style.display = 'none';
        cerrarModal();
    })

}

document.querySelector('#boton-eliminar').addEventListener('click', () => {
    let prods = document.querySelectorAll('.flex-item');
    let res = "";
    for (let i = 0; i < prods.length; i++) {
        res += `<option value="value${i}">${prods[i].firstChild.childNodes[3].childNodes[1].textContent}</option>`;
    }
    document.querySelector('#modal-eliminar').childNodes[1].innerHTML = `<span id="span-agregado" class="close">&times;</span>
                <p>Eliminar producto</p>
                Seleccione producto a eliminar: 
    <select name="select">
 ${res}
 </select>
 <button>Eliminar</button>`;
    document.querySelector('#span-agregado').addEventListener('click', () => {
        cerrarModal();
    })
})
document.querySelector('#boton-editar').addEventListener('click', () => {
    let prods = document.querySelectorAll('.flex-item');
    
    fetch('get_productos').then(response=>response.text()).then(result=>{
        let prods=JSON.parse(result);
        let res = "";
        for (let i = 0; i < prods.res.length; i++) {
            res += `<option value="${prods.res[i].titulo}">${prods.res[i].titulo}</option>`;
        }
        document.querySelector('#titulo-editar').innerHTML = `
 ${res}
 `
    })
  
})
document.querySelector('#boton-salir').addEventListener('click', () => {
    window.location.href = "../";
})


document.addEventListener('DOMContentLoaded',()=>{
    let fotos1 = document.querySelector('#id_foto1').parentNode
    let fotos2= fotos1.nextElementSibling;
    let fotos3 = fotos2.nextElementSibling;
    fotos2.style.display='none';
    fotos3.style.display='none';


    fotos1.addEventListener('change', () => {
        console.log("algo")
        fotos2.style.display = 'block'
        fotos2.addEventListener('change', () => {
            fotos3.style.display = 'block';
        })
    })
})

document.body.addEventListener('click', (e) => {
    if (!wide.matches) {
        let ids = [];
        let opciones = document.getElementById('opciones-nav')
        ids.push(e.target);
        ids.push(e.target.parentNode);
        ids.push(e.target.parentNode.parentNode);
        let esId = false;
        for (const id of ids) {
            if (id.id == 'menu-hamburguesa') {
                esId = true;
            }

        }
        if (esId && opciones.style.display != 'block') {
            opciones.style.display = 'block';
        } else if (esId && opciones.style.display == 'block') {
            opciones.style.display = 'none';
        } else {
            opciones.style.display = 'none';
        }
    }
})






function cerrarModal() {
    for (let i = 0; i < 3; i++) {
        document.getElementById(modales[i]).style.display = 'none';
    }
}