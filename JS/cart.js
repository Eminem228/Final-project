document.addEventListener('DOMContentLoaded', () => {
    const cartTableBody = document.querySelector('#cart-table tbody');
    const totalPriceElem = document.querySelector('#total-price');

    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    let totalPrice = 0;

    function renderCart() {
        cartTableBody.innerHTML = '';
        totalPrice = 0;

        cart.forEach(item => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${item.title}</td>
                <td>$${item.price.toFixed(2)}</td>
                <td>${item.quantity}</td>
                <td>$${(item.price * item.quantity).toFixed(2)}</td>
                <td><button class="remove-btn" data-id="${item.id}">Remove</button></td>
            `;
            cartTableBody.appendChild(row);
            totalPrice += item.price * item.quantity;
        });

        totalPriceElem.textContent = `$${totalPrice.toFixed(2)}`;
    }

    renderCart();

    cartTableBody.addEventListener('click', (event) => {
        if (event.target.classList.contains('remove-btn')) {
            const itemId = event.target.dataset.id;
            cart = cart.filter(item => item.id !== parseInt(itemId));
            localStorage.setItem('cart', JSON.stringify(cart));
            renderCart();
        }
    });

    document.querySelector('#checkout-btn').addEventListener('click', () => {
        alert('Proceeding to checkout...');
    });
});
