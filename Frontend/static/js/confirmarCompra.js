        // Precios y subtotal inicial
        const pricePerItem = 75.00; // Precio por artículo en quetzales
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