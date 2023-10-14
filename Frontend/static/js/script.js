// Manejar la creación de pedido al contado
document.getElementById("crear-pedido-contado-form").addEventListener("submit", function (e) {
    e.preventDefault();
});

// Manejar la creación de pedido al crédito
document.getElementById("crear-pedido-credito-form").addEventListener("submit", function (e) {
    e.preventDefault();
});

// Manejar la búsqueda de pasteles
document.getElementById("buscar-pasteles-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const consulta = document.getElementById("consulta").value;
    
    // Realizar una solicitud AJAX para buscar pasteles basados en la consulta
    // Actualizar el contenido de resultados-busqueda con los resultados
    // Por ejemplo:
    // fetch(`/buscar_pasteles?consulta=${consulta}`)
    //     .then(response => response.text())
    //     .then(data => {
    //         document.getElementById("resultados-busqueda").innerHTML = data;
    //     })
    //     .catch(error => console.error(error));
});