const display = document.getElementById("display");

document.querySelectorAll("button").forEach(btn => {
    btn.addEventListener("click", () => {
        const v = btn.textContent;

        if (v === "C") {
            display.value = "";
        }
        else if (v === "=") {
            try {
                display.value = eval(display.value);
            } catch (error) {
                display.value = 'Error';
            }
        }
        else if (v === "x²") {
            display.value = Math.pow(display.value, 2);
        }
        else if (v === "√") {
            display.value = Math.sqrt(display.value);
        }
        else if (v === "π") {
            display.value = Math.PI.toFixed(2);
        }
        else if (v === "sin") {
            display.value = Math.sin(display.value * Math.PI/180).toFixed(2);
        }
        else if (v === "cos") {
            display.value = Math.cos(display.value * Math.PI/180).toFixed(2);
        }
        else if (v === "tan") {
            display.value = Math.tan(display.value * Math.PI/180).toFixed(2);
        }
        else if (v === "log") {
            display.value = Math.log10(display.value).toFixed(2);
        }
        else if (v === "ln") {
            display.value = Math.log(display.value).toFixed(2);
        }
        else {
            display.value += v;
        }
    });
});
