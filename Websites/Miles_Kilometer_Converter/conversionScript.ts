const convertButton: HTMLButtonElement = document.getElementById('convert-button') as HTMLButtonElement;
const inputArea: HTMLTextAreaElement = document.getElementById('input') as HTMLTextAreaElement;
const resultArea: HTMLTextAreaElement = document.getElementById('result') as HTMLTextAreaElement;
const optionSelect: HTMLSelectElement = document.getElementById('unit-select') as HTMLSelectElement;


function convert(): void {
    let inputValue: number = parseFloat(inputArea.value);
    let selectedOption: string = optionSelect.value;

    if (selectedOption === 'miles') {
        // m = k * 0.621371
        let result: number = inputValue * 0.621371;
        resultArea.value = `${result} miles`;
    } else {
        // m = k * 1.60934
        let result: number = inputValue * 1.60934;
        resultArea.value = `${result} kilometers`;
    }

    clearInput();
}

function clearInput(): void {
    inputArea.value = '';
    optionSelect.selectedIndex = 0;
}


convertButton.addEventListener('click', convert);