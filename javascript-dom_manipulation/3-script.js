let headerTitle = document.querySelectorAll("header")[0];
let headerElement = document.getElementById("toggle_header");


headerElement.addEventListener("click", function(){
    headerTitle.classList.toggle("red");
    headerTitle.classList.toggle("green");
});