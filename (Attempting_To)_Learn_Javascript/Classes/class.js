let items = [];

class Product {
    constructor(name, price, quantity) {
        if (typeof name !== "string" || name.trim() === "") {
            throw new Error("Name must be a non-empty string.");
        }
        if (typeof price !== "number" || price <= 0) {
            throw new Error("Price must be a positive number.");
        }
        if (typeof quantity !== "number" || quantity < 0) {
            throw new Error("Quantity must be a non-negative number.");
        }
        this.name = name;
        this.price = price;
        this.quantity = quantity;
        this.id = Product.generateId();
        items.push(this);
    }
    static generateId() {
        return Math.floor(Math.random() * 1000000);
    }
    static getProducts() {
        return items;
    }
    static getProductViaID(id) {
        const product = items.find(item => item.id === id);
        if (!product) {
            throw new Error("Product not found.");
        }
        return product;
    }
}