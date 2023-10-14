        // Precios y subtotal inicial
        const pricePerItem = localStorage.getItem("precioPastel"); // Precio por artículo en quetzales
        let quantity = 1;
        let subtotal = pricePerItem;

        // Funciones JavaScript para controlar la cantidad y eliminar productos
        function incrementQuantity(button) {
            const quantityElement = button.parentNode.querySelector('span');
            quantity += 1;
            quantityElement.textContent = quantity;
            updateSubtotal();
            updateTotalPrice();
        }

        function decrementQuantity(button) {
            const quantityElement = button.parentNode.querySelector('span');
            if (quantity > 1) {
                quantity -= 1;
                quantityElement.textContent = quantity;
                updateSubtotal();
                updateTotalPrice();
            }
        }

        function updateSubtotal() {
            const subtotalElement = document.getElementById('subtotalPrice');
            const newSubtotal = quantity * pricePerItem;
            subtotalElement.textContent = newSubtotal.toFixed(2);
            subtotal = newSubtotal;
        }

        function updateTotalPrice() {
            const totalPriceElement = document.getElementById('totalPrice');
            totalPriceElement.textContent = subtotal.toFixed(2);
        }

        function removeProduct(button) {
            const listItem = button.parentNode;
            listItem.parentNode.removeChild(listItem);
            updateSubtotal();
            updateTotalPrice();
        }

        function showPaymentMethod() {
            document.getElementById('paymentMethod').style.display = 'block';
            document.querySelector('.progress-bar').style.width = '50%';
            document.querySelector('.confirm-button').style.display = 'block';
        }

        function finishPurchase() {
            document.querySelector('.progress-bar').style.width = '100%';
            
            // Código para crear un pedido al hacer clic en "Agregar al carrito"
            // const agregarAlCarritoButton = document.getElementById('agregarAlCarrito');
            // agregarAlCarritoButton.addEventListener('click', function () {
            const usuario = localStorage.getItem("Usuario");
            const cliente = usuario; 
            const productos = ["Pastel de Chocolate"];

            // Realiza una solicitud AJAX para crear un pedido al contado
            $.ajax({
                type: 'POST',
                url: '/api/pedido',
                contentType: 'application/json',
                data: JSON.stringify({ cliente, productos }),
                success: function (response) {
                // Crea un enlace para descargar el PDF
                const blob = new Blob([response], { type: 'application/pdf' });
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'factura.pdf';
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                $('#comprarModal').modal('hide');
                },
                error: function (error) {
                // Maneja cualquier error que ocurra durante la solicitud
                alert('Error al crear el pedido: ' + error.responseJSON.message);
                }
            });
            // });
        }

        //   document.addEventListener("DOMContentLoaded", function () {
        //     // Obtener los parámetros de la URL
        //     const params = new URLSearchParams(window.location.search);
        //     const nombrePastel = params.get("nombrePastel");
        //     const precioPastel = params.get("precioPastel");
        
        //     // Crear un nuevo elemento de producto con los datos de compra
        //     const productList = document.getElementById("productList");
        
        //     const li = document.createElement("li");
        //     li.className = "product";
        //     li.innerHTML = `
        //         <div class="product-details">
        //             <h2>${nombrePastel}</h2>
        //             <p>Precio: <span>${precioPastel}</span></p>
        //         </div>
        //         <div class="quantity">
        //             <button onclick="decrementQuantity(this)">-</button>
        //             <span>1</span>
        //             <button onclick="incrementQuantity(this)">+</button>
        //         </div>
        //         <button class="delete-button" onclick="removeProduct(this)"><i class="fas fa-trash-alt"></i></button>
        //     `;
        
        //     // Agregar el nuevo producto a la lista
        //     productList.appendChild(li);
        // });
        


        // document.addEventListener("DOMContentLoaded", function () {
        //     // Obtener los datos del pastel del almacenamiento local
        //     const nombrePastel = localStorage.getItem("nombrePastel");
        //     const precioPastel = localStorage.getItem("precioPastel");
        
        //     // Actualizar los elementos HTML con los datos
        //     const nombrePastelElement = document.getElementById("nombrePastel");
        //     const precioPastelElement = document.getElementById("precioPastel");
        //     const totalPastelElement = document.getElementById("totalPrice");
        //     const subtotalPastelElement = document.getElementById("subtotalPrice");
        
        //     nombrePastelElement.textContent = nombrePastel;
        //     precioPastelElement.textContent = precioPastel;
        //     totalPastelElement.textContent = precioPastel;
        //     subtotalPastelElement.textContent = precioPastel;
        // });

        document.addEventListener("DOMContentLoaded", function () {
            // Obtener la lista de pasteles del almacenamiento local
            const pastelesEnCarrito = JSON.parse(localStorage.getItem("pastelesEnCarrito")) || [];
        
            // Obtén una referencia a la lista de productos en el carrito
            const productList = document.getElementById("productList");
        
            // Recorre la lista de pasteles en el carrito y agrega cada pastel a la lista
            pastelesEnCarrito.forEach(pastel => {
                const li = document.createElement("li");
                li.className = "product";
                li.innerHTML = `
                    <div class="product-details">
                        <h2>${pastel.nombre}</h2>
                        <p>Precio: Q${pastel.precio}</p>
                    </div>
                    <div class="quantity">
                        <button onclick="decrementQuantity(this)">-</button>
                        <span>1</span>
                        <button onclick="incrementQuantity(this)">+</button>
                    </div>
                    <button class="delete-button" onclick="removeProduct(this)"><i class="fas fa-trash-alt"></i></button>
                `;
                productList.appendChild(li);
            });
        
            // Calcula el subtotal y total, y actualiza los elementos HTML correspondientes
            const subtotalPrice = pastelesEnCarrito.reduce((total, pastel) => total + parseFloat(pastel.precio.replace(/[^0-9.]/g, '')), 0);
            const totalPriceElement = document.getElementById("totalPrice");
            const subtotalPriceElement = document.getElementById("subtotalPrice");
            totalPriceElement.textContent = subtotalPrice.toFixed(2);
            subtotalPriceElement.textContent = subtotalPrice.toFixed(2);
        });
        
        