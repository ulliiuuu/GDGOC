let number = 0;

const display = document.getElementById("counter");

document.getElementById("kurang1").addEventListener("click", () => {
    number -= 1;
    updateDisplay();
});

document.getElementById("kurang2").addEventListener("click", () => {
    number -= 2;
    updateDisplay();
});

document.getElementById("tambah1").addEventListener("click", () => {
    number += 1;
    updateDisplay();
});

document.getElementById("tambah2").addEventListener("click", () => {
    number += 2;
    updateDisplay();
});

document.getElementById("reset").addEventListener("click", () => {
    number = 0;
    updateDisplay();
});

function updateDisplay() {
    display.textContent = number;
}
