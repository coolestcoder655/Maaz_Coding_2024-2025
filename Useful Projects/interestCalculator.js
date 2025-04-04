const utilites = require('./utilities.js')

class interestCalculator {
    constructor(principal, rate, time) {
        this.principal = principal;
        this.rate = rate;
        this.time = time;
    }
    calculateIntrest() {
        return utilites.turnIntoINT((this.principal * this.rate * this.time) / 100)
    }
    calculateInterestWithMoney() {
        return utilites.turnIntoINT(((this.principal * this.rate * this.time) / 100) + this.principal)
    }

}

const obj = new interestCalculator(1200, 5, 4)
console.log(obj.calculateInterestWithMoney())