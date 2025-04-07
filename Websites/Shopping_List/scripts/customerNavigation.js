const shoppingListButton = document.getElementById("shoppingListButton");
const addItemButton = document.getElementById("addItemButton");
const removeItemButton = document.getElementById("removeItemsButton");
const editShoppingListButton = document.getElementById("editListButton");
const clearShoppingListButton = document.getElementById("clearListButton");
const checkoutButton = document.getElementById("checkOutButton");
const logoutButton = document.getElementById("logoutButton");

shoppingListButton.addEventListener("click", () => {
    window.location.href = "../pages/customerPages/viewShoppingList.html"
});

addItemButton.addEventListener("click", () => {
    window.location.href = "../pages/customerPages/removeItems.html";
});

removeItemButton.addEventListener("click", () => {
    window.location.href = "../pages/customerPages/removeItems.html";
});

editShoppingListButton.addEventListener("click", () => {
    window.location.href = "../pages/customerPages/editShoppingList.html";
});

clearShoppingListButton.addEventListener("click", () => {
    window.location.href = "../pages/customerPages/clearShoppingList.html";
});

checkoutButton.addEventListener("click", () => {
    window.location.href = "../pages/customerPages/checkOut.html";
});

logoutButton.addEventListener("click", () => {
    window.location.href = "../login.html";
});