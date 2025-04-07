const shoppingListButton = document.getElementById("shoppingListButton");
const addItemButton = document.getElementById("addItemButton");
const removeItemButton = document.getElementById("removeItemButton");
const editShoppingListButton = document.getElementById("editListButton");
const clearShoppingListButton = document.getElementById("clearListButton");
const checkoutButton = document.getElementById("checkOutButton");
const logoutButton = document.getElementById("logoutButton");

shoppingListButton.addEventListener("click", () => {
    window.location.href = "customerPages/viewShoppingList.html"
});

addItemButton.addEventListener("click", () => {
    window.location.href = "customerPages/removeItems.html";
});

removeItemButton.addEventListener("click", () => {
    window.location.href = "customerPages/removeItems.html";
});

editShoppingListButton.addEventListener("click", () => {
    window.location.href = "customerPages/editShoppingList.html";
});

clearShoppingListButton.addEventListener("click", () => {
    window.location.href = "customerPages/clearShoppingList.html";
});

checkoutButton.addEventListener("click", () => {
    window.location.href = "customerPages/checkOut.html";
});

logoutButton.addEventListener("click", () => {
    window.location.href = "login.html";
});