document.querySelector("#add_item").addEventListener("click", function() {
    document.querySelector(".my_list").innerHTML += "<li>Item</li>";
});

// document.addEventListener('DOMContentLoaded', function () {
//     let addItemButton = document.getElementById('add_item');
//     let myList = document.querySelector('.my_list');

//     addItemButton.addEventListener('click', function() {
//         let newItem = document.createElement('li');
//         newItem.textContent = 'Item';
//         myList.appendChild(newItem);
//     });
// });
