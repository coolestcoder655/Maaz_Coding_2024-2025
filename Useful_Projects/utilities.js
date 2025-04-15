export function turnIntoINT(num) {
    if (num == parseInt(num)) {
        return parseInt(num)
    } else {
        return parseFloat(num)
    }
}