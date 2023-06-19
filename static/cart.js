document.addEventListener('DOMContentLoaded', function() {
  var cartItems = [];

  function addToCart(itemId) {
    var item = {
      id: itemId,
      name: "Item " + itemId
    };

    cartItems.push(item);
    refreshCartItems();
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
});
