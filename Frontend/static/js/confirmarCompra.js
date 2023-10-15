
        // Precios y subtotal inicial
        const pricePerItem = parseFloat(localStorage.getItem("precioPastel")); // Precio por artículo en quetzales
        let subtotal = 0;

        function incrementQuantity(buttonContainer) {
            console.log(buttonContainer);
            const quantityElement = buttonContainer.querySelector('span');
            const productName = buttonContainer.parentNode.querySelector(".product-details h2").textContent;
            const pastelesEnCarrito = JSON.parse(localStorage.getItem("pastelesEnCarrito")) || [];
            const product = pastelesEnCarrito.find(item => item.nombre === productName);
        
            if (product) {
                product.cantidad += 1;
                quantityElement.textContent = product.cantidad;
                updateSubtotal();
                updateTotalPrice();
                saveToLocalStorage(pastelesEnCarrito);
            }
        }
        
        function decrementQuantity(buttonContainer) {
            console.log(buttonContainer);

            if (buttonContainer instanceof Element) {
                const quantityElement = buttonContainer.querySelector('span');
                const productName = buttonContainer.parentNode.querySelector(".product-details h2").textContent;
                const pastelesEnCarrito = JSON.parse(localStorage.getItem("pastelesEnCarrito")) || [];
                const product = pastelesEnCarrito.find(item => item.nombre === productName);
            
                if (product && product.cantidad > 1) {
                    product.cantidad -= 1;
                    quantityElement.textContent = product.cantidad;
                    updateSubtotal();
                    updateTotalPrice();
                    saveToLocalStorage(pastelesEnCarrito);
                }
            } else {
                console.error('buttonContainer no es un elemento del DOM válido.');
            }
        }
        

        function updateCartUI() {
            // Actualiza la lista de productos en la interfaz de usuario
            const productList = document.getElementById("productList");
            productList.innerHTML = "";

            let subtotalPrice = 0;
            let totalPrice = 0;

            const pastelesEnCarrito = JSON.parse(localStorage.getItem("pastelesEnCarrito")) || [];
            const usuario = localStorage.getItem("Usuario");
            pastelesEnCarrito.forEach(pastel => {
                const cantidad = pastel.cantidad / pastel.cantidad;
                const li = document.createElement("li");
                li.className = "product";
                li.innerHTML = `
                    <div class="product-details">
                        <h2>${pastel.nombre}</h2>
                        <p>Precio: Q${pastel.precio}</p>
                    </div>
                    <div class="quantity">
                        <button onclick="decrementQuantity('${pastel.nombre}')">-</button>
                        <span>${cantidad}</span>
                        <button onclick="incrementQuantity('${pastel.nombre}')">+</button>
                    </div>
                    <button class="delete-button" onclick="removeProduct('${pastel.nombre}')"><i class="fas fa-trash-alt"></i></button>
                `;

                productList.appendChild(li);

                // Calcula el subtotal y total para este pastel y añádelo a los totales generales
                const precioNumerico = parseFloat(pastel.precio.replace(/[^0-9.]/g, ''));
                subtotalPrice += cantidad * precioNumerico;
                totalPrice += cantidad * precioNumerico;
            });

            // Actualiza el subtotal y total en la interfaz
            const subtotalPriceElement = document.getElementById("subtotalPrice");
            const totalPriceElement = document.getElementById("totalPrice");
            subtotalPriceElement.textContent = subtotalPrice.toFixed(2);
            totalPriceElement.textContent = totalPrice.toFixed(2);
            subtotal = subtotalPrice; // Actualiza el subtotal global
        }

        function removeProduct(productName) {
            const pastelesEnCarrito = JSON.parse(localStorage.getItem("pastelesEnCarrito")) || [];
            const updatedPastelesEnCarrito = pastelesEnCarrito.filter(pastel => pastel.nombre !== productName);
            localStorage.setItem("pastelesEnCarrito", JSON.stringify(updatedPastelesEnCarrito));
            
            // Verifica si se han eliminado todos los pasteles
            if (updatedPastelesEnCarrito.length === 0) {
                // Restablece la cantidad a 0 si no hay pasteles en el carrito
                const quantityElements = document.querySelectorAll(".quantity span");
                quantityElements.forEach(element => {
                    element.textContent = "0";
                    // product.cantidad = 0;
                    document.querySelector('.progress-bar').style.width = '0%';
                });
            }
            
            updateCartUI();
        }

        document.addEventListener("DOMContentLoaded", function () {
            // Obtener la lista de pasteles del carrito desde el almacenamiento local
            const pastelesEnCarrito = JSON.parse(localStorage.getItem("pastelesEnCarrito")) || [];

            // Obtén una referencia a la lista de productos en el carrito
            const productList = document.getElementById("productList");

            // Limpia la lista de productos en la interfaz
            productList.innerHTML = "";

            // Variables para calcular el subtotal y total
            let subtotalPrice = 0;
            let totalPrice = 0;

            pastelesEnCarrito.forEach(pastel => {
                const cantidad = pastel.cantidad / pastel.cantidad;
                const li = document.createElement("li");
                li.className = "product";
                li.innerHTML = `
                    <div class="product-details">
                        <h2>${pastel.nombre}</h2>
                        <p>Precio: Q${pastel.precio}</p>
                    </div>
                    <div class="quantity">
                        <button onclick="decrementQuantity('${pastel.nombre}')">-</button>
                        <span>${cantidad}</span>
                        <button onclick="incrementQuantity('${pastel.nombre}')">+</button>
                    </div>
                    <button class="delete-button" onclick="removeProduct('${pastel.nombre}')"><i class="fas fa-trash-alt"></i></button>
                `;

                productList.appendChild(li);

                // Calcula el subtotal y total para este pastel y añádelo a los totales generales
                const precioNumerico = parseFloat(pastel.precio.replace(/[^0-9.]/g, ''));
                subtotalPrice += cantidad * precioNumerico;
                totalPrice += cantidad * precioNumerico;
            });

            // Actualiza el subtotal y total en la interfaz
            const subtotalPriceElement = document.getElementById("subtotalPrice");
            const totalPriceElement = document.getElementById("totalPrice");
            subtotalPriceElement.textContent = subtotalPrice.toFixed(2);
            totalPriceElement.textContent = totalPrice.toFixed(2);
            subtotal = subtotalPrice; // Actualiza el subtotal global
        });

        
        function showPaymentMethod() {
            document.getElementById('paymentMethod').style.display = 'block';
            document.querySelector('.progress-bar').style.width = '50%';
            document.querySelector('.confirm-button').style.display = 'block';
        }

        function finishPurchase() {
            document.querySelector('.progress-bar').style.width = '100%';
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

        function saveToLocalStorage(pastelesEnCarrito) {
            localStorage.setItem("pastelesEnCarrito", JSON.stringify(pastelesEnCarrito));
        }