import {products} from "./customer";

const container = document.getElementById("products-container");

function displayProducts(container) {
    Object.values(products).forEach(product => {
        const productDiv = document.createElement("div");
        productDiv.id = product.id;
        productDiv.className = "product-container"; // style with CSS
        productDiv.style.display = "grid";
        productDiv.style.placeItems = "center";

        productDiv.innerHTML = `
        <img class="product" src="${product.imageFilePath}" alt="product">
        <h3>${product.name}</h3>
        <h4>${product.price}</h4>
        `;

        container.appendChild(productDiv);
    });
}

displayProducts(container);