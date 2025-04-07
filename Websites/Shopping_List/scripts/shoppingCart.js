export class ShoppingCart {
    constructor() {
        this.itemsInCart = [];
    }
    addItems(items) {
        // Will be a list of items
        this.itemsInCart.push(items);
    }
    removeItem(item) {
        this.itemsInCart.splice(this.itemsInCart.indexOf(item), 1);
    }
    checkOut() {
        let total = 0;
        for (let i = 0; i < this.itemsInCart.length; i++) {
            total = total + this.itemsInCart[i].price;
        }
        return total;
    }
}