document.addEventListener("DOMContentLoaded", function() {
  var userButton = document.querySelector(".user-button");
  var dropdownContent = document.getElementById("dropdown-content");

  function toggleDropdown(event) {
    dropdownContent.classList.toggle("show");
    if (event) {
      event.stopPropagation();
    }
  }

  userButton.addEventListener("click", toggleDropdown);
  document.addEventListener("click", function(event) {
    if (dropdownContent.classList.contains("show") && !event.target.matches(".user-button")) {
      dropdownContent.classList.remove("show");
    }
  });
});
