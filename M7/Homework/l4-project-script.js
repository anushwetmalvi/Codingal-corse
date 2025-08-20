function calculateIncome() {
            var income = parseFloat(document.getElementById("income").value);
            var expenses = parseFloat(document.getElementById("expenses").value);
            var NetIncome = income - expenses;

            document.getElementById("result").innerText = "Your net income is: " + NetIncome;
}