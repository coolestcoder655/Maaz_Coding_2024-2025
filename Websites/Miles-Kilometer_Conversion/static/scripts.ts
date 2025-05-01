const conversion_form: HTMLFormElement = document.getElementById("conversion-form") as HTMLFormElement;
const conversion_type: HTMLSelectElement = document.getElementById("conversion-type") as HTMLSelectElement;
const inputArea: HTMLInputElement = document.getElementById("input-value") as HTMLInputElement;
const resultArea: HTMLTextAreaElement = document.getElementById("resultArea") as HTMLTextAreaElement;

conversion_form.addEventListener("submit", convert);

function convert(): void {
    let input: string = inputArea.value;
    let type: string = conversion_type.value;
    let result: number;

    if (type === "miles-to-kilometers") {
        result = parseFloat(input) * 1.60934;

        resultArea.textContent = `${result} kilometers`

    } else if (type === "kilometers-to-miles") {
        result = parseFloat(input) / 1.60934;

        resultArea.textContent = `${result} miles`

    } else {
        throw new Error("Incorrect Conversion Type")
    }

    return;
}

/**
<p id="myValue"></p>

<script>
  let value = 42;
  document.getElementById("myValue").textContent = "The value is " + value;
</script>

 */