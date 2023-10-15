// Recupera los pasteles del almacenamiento local
const pasteles = JSON.parse(localStorage.getItem("Pasteles"));

function almacenarUsuarioEnLocalStorage() {
    const usuario = localStorage.getItem("Usuario");
    localStorage.setItem("nombreUsuario", usuario);
}

// Obtén la referencia al elemento donde se mostrarán los pasteles
const pastelesCatalog = document.getElementById("pastelesCatalog");

// Función para cargar los pasteles en el catálogo
function cargarPasteles(pastelesResponse) {
pastelesCatalog.innerHTML = '';

const pasteles = pastelesResponse.Pasteles;

if (pasteles && Array.isArray(pasteles)) {
  pasteles.forEach(pastel => {
    // Crea las tarjetas de los pastelesf
    const card = document.createElement("div");
    card.classList.add("col-md-4");

    card.innerHTML = `
      <div class="card mb-4 shadow-sm">
        <img src="${pastel.imagenSabor}" class="card-img-top" alt="Imagen del pastel">
        <div class="card-body">
          <h5 class="card-title">${pastel.Nombre}</h5>
          <p class="card-text">
            <strong>Tipo:</strong> ${pastel.Tipo}<br>
            <strong>Sabor:</strong> ${pastel.Sabor}<br>
            <strong>Relleno:</strong> ${pastel.Relleno}<br>
            <strong>Precio:</strong> Q${pastel.Precio}<br>
          </p>
          <button class="btn btn-primary">Comprar</button>
        </div>
      </div>
  `;
  pastelesCatalog.appendChild(card);

  // Obtener el botón "Comprar" dentro de esta tarjeta y agregar el evento de clic
  const comprarButton = card.querySelector('.btn.btn-primary');
  comprarButton.addEventListener('click', function () {
    // Aquí puedes usar 'pastel' para obtener la información correcta del pastel
    const nombreClienteInput = document.getElementById('nombreCliente');
    const nombrePastelInput = document.getElementById('nombrePastel');
    const tipoPastelInput = document.getElementById('tipoPastel');
    const saborPastelInput = document.getElementById('saborPastel');
    const precioPastelInput = document.getElementById('precioPastel');
    almacenarUsuarioEnLocalStorage();
    nombreClienteInput.value = usuario; // Nombre del cliente
    nombrePastelInput.value = pastel.Nombre;
    tipoPastelInput.value = pastel.Tipo; // Tipo del pastel
    saborPastelInput.value = pastel.Sabor; // Sabor del pastel
    precioPastelInput.value = `Q${pastel.Precio}`; // Precio del pastel

    $('#comprarModal').modal('show');
//     const agregarButton = document.getElementById("agregarAlCarrito");
//     agregarButton.addEventListener('click', function () {
//     // const nombrePastel = "Nada";
//     // const precioPastel = "15.25";
//     const nombrePastel = nombrePastelInput.value;
//     const precioPastel = precioPastelInput.value;
//     const precioNumerico = parseFloat(precioPastel.replace(/[^0-9.]/g, ''));
//     const precioFormateado = precioNumerico.toFixed(2);

//     // Almacena los datos en el almacenamiento local
//     localStorage.setItem("nombrePastel", nombrePastel);
//     localStorage.setItem("precioPastel", precioFormateado);
//     console.log(nombrePastel, precioFormateado);
//     $('#comprarModal').modal('hide');

//   });
const agregarButton = document.getElementById("agregarAlCarrito");
agregarButton.addEventListener('click', function () {
    const nombrePastel = nombrePastelInput.value;
    const precioPastel = precioPastelInput.value;
    const usuario = localStorage.getItem("nombreUsuario");
    const precioNumerico = parseFloat(precioPastel.replace(/[^0-9.]/g, ''));
    const precioFormateado = precioNumerico.toFixed(2);

    // Obtén la lista de productos en el carrito del almacenamiento local
    const pastelesEnCarrito = JSON.parse(localStorage.getItem("pastelesEnCarrito")) || [];

    // Verifica si el producto ya existe en el carrito
    const productoExistente = pastelesEnCarrito.find(pastel => pastel.nombre === nombrePastel);

    if (productoExistente) {
        // Si el producto ya existe, incrementa la cantidad
        productoExistente.cantidad += 1;
    } else {
        // Si el producto no existe, agrégalo al carrito
        pastelesEnCarrito.push({
            nombre: nombrePastel,
            precio: precioFormateado,
            cantidad: 1
        });
    }

    // Actualiza el carrito en el almacenamiento local
    localStorage.setItem("pastelesEnCarrito", JSON.stringify(pastelesEnCarrito));

    $('#comprarModal').modal('hide');
});

    });
});
} else {
// Maneja el caso en el que no haya pasteles en la respuesta
const noPastelesMessage = document.createElement("p");
noPastelesMessage.textContent = "No hay pasteles disponibles.";
pastelesCatalog.appendChild(noPastelesMessage);
}
}


// Manejar el clic en los enlaces
$("nav .nav-link").click(function (e) {
  e.preventDefault();

  const tipo = $(this).data("tipo");

  // Realizar una solicitud AJAX a la API basada en el tipo de pastel
  $.get(`http://localhost:5000/api/catalogo/${tipo}`, function (data) {
    cargarPasteles(data);
  });
});

// Mostrara todos los pasteles al cargar la página
cargarPasteles({ Pasteles: pasteles });


// Recupera los menús y submenús del almacenamiento local
const menus = JSON.parse(localStorage.getItem("Menus"));
const submenus = JSON.parse(localStorage.getItem("Submenus"));

localStorage.setItem("Menus", JSON.stringify(menus));
localStorage.setItem("Submenus", JSON.stringify(submenus));

// console.log(submenus)
// Recupera el nombre de usuario del almacenamiento local
const usuario = localStorage.getItem("Usuario");
// console.log(usuario)
// Verificar si el usuario es administrador y mostrar menús y submenús si es el caso
if (usuario === "Administrador" && menus && menus.length && submenus && submenus.length) {
  const adminMenu = document.getElementById("admin-menu");
  adminMenu.style.display = "block";

  // Agregar los elementos del menú y submenús aquí
  const adminMenuList = adminMenu.querySelector("ul.navbar-nav");
  submenus.forEach(submenu => {
    const submenuElement = document.createElement("li");
    submenuElement.classList.add("nav-item");
    const submenuLink = document.createElement("a");
    submenuLink.classList.add("nav-link");
    submenuLink.textContent = submenu;
    submenuElement.appendChild(submenuLink);
    adminMenuList.appendChild(submenuElement);
  });
}


function agregarAlCarrito() {

    const nombrePastel = "Nada";
    const precioPastel = "15.25";
    const usuario = localStorage.getItem("Usuario");

    // Almacena los datos en el almacenamiento local
    localStorage.setItem("nombrePastel", nombrePastel);
    localStorage.setItem("precioPastel", precioPastel);
    localStorage.setItem("Usuario", usuario);
    console.log(nombrePastel, precioPastel, usuario);
}

document.getElementById('searchButton').addEventListener('click', function () {
  const descripcion = document.getElementById('searchInput').value;

  axios.post('/api/buscar_pasteles', { descripcion })
  .then(response => {
      const resultados = response.data.resultados;
      const resultadosContainer = document.getElementById('pastelesCatalog');

      // Limpia el contenedor antes de agregar nuevos resultados
      resultadosContainer.innerHTML = '';

      if (resultados.length > 0) {
          resultados.forEach(pastel => {
              // Crea las tarjetas de los pasteles
              const card = document.createElement("div");
              card.classList.add("col-md-4");

              card.innerHTML = `
                <div class="card mb-4 shadow-sm">
                  <img src="${pastel.imagenSabor}" class="card-img-top" alt="Imagen del pastel">
                  <div class="card-body">
                    <h5 class="card-title">${pastel.nombre}</h5>
                    <p class="card-text">
                      <strong>Tipo:</strong> ${pastel.tipo}<br>
                      <strong>Sabor:</strong> ${pastel.sabor}<br>
                      <strong>Relleno:</strong> ${pastel.relleno}<br>
                      <strong>Precio:</strong> Q${pastel.precio}<br>
                    </p>
                    <button class="btn btn-primary">Comprar</button>
                  </div>
                </div>
              `;

              resultadosContainer.appendChild(card);
          });
      } else {
          resultadosContainer.innerHTML = 'No se encontraron pasteles que coincidan con la búsqueda.';
      }
  })
  .catch(error => {
      console.error('Error:', error);
  });
});

