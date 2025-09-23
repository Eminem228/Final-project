const cards = document.querySelector(".cards");
let descriptionText;
let data = [];
let favorites = [];

function getData() {
    fetch('https://dummyjson.com/products')
        .then(response => response.json())
        .then(res => {
            data = res.products;
            data.forEach((item) => {
                descriptionText = item?.description?.slice(0, 50);
                cards.innerHTML += `
                <div class="card">
                    <img src=${item.images[0]} alt="itemImg">
                    <h3>${item.title}</h3>
                    <p id=${item.id}>${descriptionText}...<button onclick="loadMore('${item.description.replace(/'/g, "\\'")}', '${item.id}')">More</button></p>
                    <span>${item.price}</span>
                    <button onclick='addToCart(${item.id})'><i class="fa-regular fa-cart-plus"></i> Add to Cart</button>
                    <button onclick='addToFav(${item.id})'><i class="fa-regular fa-heart"></i> Add to Favorites</button>
                </div>
                `;
            });
        });
}
getData();

function loadMore(text, id) {
    document.getElementById(id).innerHTML = text;
}

function addToCart(ID) {
    const item = data.find(product => product.id === ID);
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    
    const existingItemIndex = cart.findIndex(cartItem => cartItem.id === ID);
    if (existingItemIndex !== -1) {
        cart[existingItemIndex].quantity += 1;
    } else {
        cart.push({ ...item, quantity: 1 });
    }
    
    localStorage.setItem('cart', JSON.stringify(cart));
    alert('Item added to cart');
}

function addToFav(ID) {
    let searchElement = favorites.find(item => item.id == ID);
    
    if (!searchElement) {
        let clickedElement = data.find(item => item.id == ID);
        favorites.push(clickedElement);
        // Store favorites in localStorage or similar
        localStorage.setItem('favorites', JSON.stringify(favorites));
        alert('Item added to favorites');
    } else {
        alert('This item is already in your favorites');
    }
}
