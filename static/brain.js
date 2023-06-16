document.addEventListener('DOMContentLoaded', function() {
  // Add an event listener to the support bubble
    document.querySelector('.support-bubble').addEventListener('click', function() {
  // Toggle the visibility of the popup
        var popup = document.querySelector('.popup');
        popup.style.display = popup.style.display === 'none' ? 'block' : 'none';
    });

});
