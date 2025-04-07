import {Store} from "./store"

export class Product {
    constructor(name, price) {
        this.name = name;
        this.price = price;
        Store.products.push(this);
    }
    changePrice(newPrice) {
        this.price = newPrice;
    }
    changeName(newName) {
        this.name = newName;
    }
    delete() {
        Store.products.splice(Store.products.indexOf(this), 1);
    }
}