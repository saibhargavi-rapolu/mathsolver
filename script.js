const display = document.getElementById("display");


function lastChar(str) {
    if (!str) return "";
    return str[str.length - 1];
}


function evalExpression(expr) {
    if (!expr) return "";

    expr = expr.replace(/π/g, `(${Math.PI})`);

  
    try {
        const res = eval(expr);
        return (res === undefined) ? "" : String(res);
    } catch (e) {
        throw e;
    }
}


document.querySelectorAll("button").forEach(btn => {
    btn.addEventListener("click", () => {
        const v = btn.textContent;
        const cur = display.value;

     
        if (v === "C") {
            display.value = "";
            return;
        }

        // BACKSPACE (delete last character)
        if (v === "x") {
            display.value = display.value.slice(0, -1);
            return;
        }

        // INSTANT SCIENTIFIC OPERATIONS (operate on current display numeric value)
        // If display is empty for these, do nothing.
        if (v === "x²") {
            if (cur !== "") {
                // parse float and square
                const n = parseFloat(cur);
                display.value = String(Math.pow(n, 2));
            }
            return;
        }

        if (v === "√") {
            if (cur !== "") {
                const n = parseFloat(cur);
                display.value = String(Math.sqrt(n));
            }
            return;
        }

        if (v === "sin") {
            if (cur !== "") {
                const n = parseFloat(cur);
                display.value = String(Math.sin(n * Math.PI / 180).toFixed(2));
            }
            return;
        }

        if (v === "cos") {
            if (cur !== "") {
                const n = parseFloat(cur);
                display.value = String(Math.cos(n * Math.PI / 180).toFixed(2));
            }
            return;
        }

        if (v === "tan") {
            if (cur !== "") {
                const n = parseFloat(cur);
                display.value = String(Math.tan(n * Math.PI / 180).toFixed(2));
            }
            return;
        }

        if (v === "log") {
            if (cur !== "") {
                const n = parseFloat(cur);
                display.value = String(Math.log10(n).toFixed(2));
            }
            return;
        }

        if (v === "ln") {
            if (cur !== "") {
                const n = parseFloat(cur);
                display.value = String(Math.log(n).toFixed(2));
            }
            return;
        }

        // PI: append the π token (so expressions like 3+π work)
        if (v === "π") {
            // If display currently ends with a number or ')', appending π is fine.
            display.value += "π";
            return;
        }

        // EQUALS: evaluate the whole expression (supports parentheses and π)
        if (v === "=") {
            try {
                const result = evalExpression(display.value);
                display.value = result;
            } catch (err) {
                display.value = "Error";
            }
            return;
        }

        // DEFAULT: append button label to display (digits, operators, parentheses)
        display.value += v;
    });
});
