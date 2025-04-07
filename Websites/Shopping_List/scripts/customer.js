import {Store} from './store.js';
import {ShoppingCart} from './shoppingCart.js';
import {Product} from './product.js';


const store = new Store();
const cart = new ShoppingCart();

const products = {
    apple: new Product("apple", 1.65),
    banana: new Product("banana", 0.95),
    orange: new Product("orange", 1.25),
    mango: new Product("mango", 2.50),
    grapes: new Product("grapes", 3.15)
}