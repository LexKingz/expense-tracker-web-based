function addExpense() {
    var form = document.getElementById('expenseForm');
    var formData = new FormData(form);

    fetch('/add_expense', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        var messageDiv = document.getElementById('message');
        messageDiv.innerHTML = data.message;
        messageDiv.className = data.status === 'success' ? 'success' : 'error';
        form.reset();
        if (data.status === 'success') {
            setTimeout(function() {
                messageDiv.innerHTML = '';
                messageDiv.className = '';
            }, 3000);
        }
    })
    .catch(error => console.error('Error:', error));
}


// Fetch and render child.html content using JavaScript
function viewExpenses(){
    expenseView = document.getElementById('expensesDiv')
        fetch('/view_expenses')
            .then(response => response.text())
            .then(data => {
                expenseView.innerHTML  = data;
            })
            .catch(error => console.error('Error:', error));

    setTimeout(function (){
         expenseView.innerHTML = '';
    }, 15000)
}
