document.addEventListener('DOMContentLoaded', function() {
  var cartItems = [];

  // Load cart items from session storage if available
  if (sessionStorage.getItem('cartItems')) {
    cartItems = JSON.parse(sessionStorage.getItem('cartItems'));
  }

  function addToCart(itemId) {
    var item = {
      id: itemId,
      name: "Item " + itemId
    };

    cartItems.push(item);
    saveCartItems();
    refreshCartItems();
  }

  function saveCartItems() {
    // Save cart items to session storage
    sessionStorage.setItem('cartItems', JSON.stringify(cartItems));
  }

  function refreshCartItems() {
    var cartItemsElement = document.getElementById('cartItems');
    cartItemsElement.innerHTML = '';

    cartItems.forEach(function(item) {
      var li = document.createElement('li');
      li.textContent = item.name;
      cartItemsElement.appendChild(li);
    });
  }

  var addToCartButtons = document.querySelectorAll('.add-to-cart');
  addToCartButtons.forEach(function(button) {
    button.addEventListener('click', function() {
      var itemId = button.getAttribute('data-item-id');
      addToCart(itemId);
    });
  });

  // Initialize cart items on page load
  refreshCartItems();
});
