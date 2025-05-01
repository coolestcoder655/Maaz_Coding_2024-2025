var conversion_form = document.getElementById("conversion-form");
var conversion_type = document.getElementById("conversion-type");
var inputArea = document.getElementById("input-value");
var resultArea = document.getElementById("resultArea");

conversion_form.addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form submission
    convert();
});

function convert() {
    var input = inputArea.value;
    var type = conversion_type.value;
    var result;

    if (type === "miles-to-kilometers") {
        result = parseFloat(input) * 1.60934;
        resultArea.value = result.toFixed(2) + " kilometers";
    } else if (type === "kilometers-to-miles") {
        result = parseFloat(input) / 1.60934;
        resultArea.value = result.toFixed(2) + " miles";
    } else {
        throw new Error("Incorrect Conversion Type");
    }
}
