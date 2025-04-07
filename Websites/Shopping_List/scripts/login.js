document.getElementById("managerButton").addEventListener("click", managerLogin);
document.getElementById("customerButton").addEventListener("click", function() {
    window.location.href = "pages/index.html";
});

let tries;

const correctPasscode = "sigmaMale";

function managerLogin() {
    let passcode = prompt("Please enter passcode.");

    if (passcode === correctPasscode) {
        window.location.href = "pages/manager.html";
    } else {
        alert("Incorrect passcode.");
    }
}