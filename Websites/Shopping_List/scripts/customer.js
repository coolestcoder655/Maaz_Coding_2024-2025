import {Store} from './store.js';
import {ShoppingCart} from './shoppingCart.js';
import {Product} from './product.js';

const store = new Store();
const cart = new ShoppingCart();

export const products = {
    apple: new Product("apple", 1.65, "../images/apple.jpg"),
    banana: new Product("banana", 0.95, "../images/banana.jpg"),
    orange: new Product("orange", 1.25, "../images/orange.jpg"),
    mango: new Product("mango", 2.50, "../images/mango.jpg"),
    grapes: new Product("grapes", 3.15, "../images/grapes.jpg")
}

export default {store, cart, products};