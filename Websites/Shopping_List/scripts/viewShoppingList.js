const viewContainer = document.getElementById("view-container")
import {products} from  "./customer.js"

function capitalizeFirstLetter(val) {
    return String(val).charAt(0).toUpperCase() + String(val).slice(1);
}

for (let product of products) {
    let child = document.createElement("div");
    child.id = product.name;
    child.style.display = "grid";
    child.style.placeItems = "center";
    child.innerHTML =
        `<img class='product' src='${product.imageFilePath}' alt='${product.name}/>` +
        `<h3>${capitalizeFirstLetter(product.name)}</h3>` +
        `<h4>${product.price}</h4>`;
    viewContainer.appendChild(child);
}