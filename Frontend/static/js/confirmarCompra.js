document.addEventListener('DOMContentLoaded', function() {
    const camposAdicionalesContainer = document.getElementById('camposAdicionales');
    const agregarCamposButton = document.getElementById('agregarCampos');
    let contador = 1;

    agregarCamposButton.addEventListener('click', function(event) {
        event.preventDefault(); // Evita el comportamiento predeterminado del botón

        // Crea un nuevo conjunto de campos
        const nuevoCampos = document.createElement('div');
        nuevoCampos.innerHTML = `
            <div class="form-group">
            <label for="tipoDescripcion${contador}">Tipo de Descripción</label>
            <select class="form-control" id="tipoDescripcion${contador}" required>
                <option value="Sabor">Sabor</option>
                <option value="Relleno">Relleno</option>
            </select>
            </div>
            <div class="form-group">
                <label for="descripcion${contador}">Descripción</label>
                <textarea class="form-control" id="descripcion${contador}" rows="4" placeholder="Agrega notas adicionales"></textarea>
            </div>
        `;

        contador = contador + 1;

        camposAdicionalesContainer.appendChild(nuevoCampos);
    });
});

$(document).ready(function() {
    $('form').submit(function(e) {
        e.preventDefault();

        // Obtener los valores de los campos
        const nombre = $('#nombre').val();
        const sabor = $('#sabor').val();
        const relleno = $('#ingredientes').val();
        const tipoPastel = $('#tipoPastel').val();
        const precio = $('#precio').val();
        const tipoDescripcion = $('#tipoDescripcion').val();
        const descripcion = $('#descripcion').val();

        axios.post('/api/crearPasteles', { nombre, sabor, relleno, tipoPastel, precio, tipoDescripcion, descripcion })
        .then(response => {
          console.log("todo bien");
        })
        .catch(error => {
          console.error('Error:', error);
        });
    });
});
