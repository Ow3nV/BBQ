var zIndexCounter = 0;
function displayAddedToCartBanner(identifier) {

    zIndexCounter++
    console.log(identifier)
      var popupBanner = document.querySelector(identifier);
      popupBanner.style.display = 'block';
      popupBanner.style.zIndex = ++zIndexCounter;

      // Fade out after 4 seconds
      setTimeout(function() {
        var opacity = 1;
        var fadeInterval = setInterval(function() {
          opacity -= 0.05; // Adjust the fading speed by changing the decrement value

          // Apply opacity to the banner
          popupBanner.style.opacity = opacity;

          // Check if the banner has fully faded out
          if (opacity <= 0) {
            clearInterval(fadeInterval);
            var zIndexCounter = 0;
            popupBanner.style.display = 'none';
            popupBanner.style.opacity = 1; // Reset opacity for future use
          }
        }, 50); // Adjust the fading interval (milliseconds) for a smoother effect
      }, 4000); // Adjust the duration (milliseconds) for the banner to be displayed before fading out
}
