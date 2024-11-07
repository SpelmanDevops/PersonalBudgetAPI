const BASE_URL = 'http://127.0.0.1:8000/api';
let authToken = '';

// Login function
async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch(`${BASE_URL}/token/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password })
    });

    if (response.ok) {
        const data = await response.json();
        authToken = data.token;

        // Optionally store the token in localStorage for persistence
        localStorage.setItem('authToken', authToken);

        document.getElementById('login-section').style.display = 'none';
        document.getElementById('data-section').style.display = 'block';
        getTransactions();
    } else {
        const errorData = await response.json();
        alert(`Login failed: ${errorData.detail}`);
    }
}

// Retrieve stored token if it exists and use it in requests
function loadToken() {
    const storedToken = localStorage.getItem('authToken');
    if (storedToken) {
        authToken = storedToken;
        document.getElementById('login-section').style.display = 'none';
        document.getElementById('data-section').style.display = 'block';
        getTransactions();
    }
}

// Fetch transactions (incomes and expenses)
async function getTransactions() {
    const response = await fetch(`${BASE_URL}/transactions/`, {
        method: 'GET',
        headers: {
            'Authorization': `Token ${authToken}`
        }
    });

    if (response.ok) {
        const transactions = await response.json();
        const transactionsList = document.getElementById('transactions-list');
        transactionsList.innerHTML = '';
        transactions.forEach(transaction => {
            const transactionItem = document.createElement('div');
            transactionItem.textContent = `${transaction.transaction_type}: ${transaction.amount} on ${transaction.date}`;
            transactionsList.appendChild(transactionItem);
        });
    } else {
        alert('Failed to fetch transactions');
    }
}

// Add a new transaction
async function addTransaction() {
    const amount = document.getElementById('amount').value;
    const date = document.getElementById('date').value;
    const description = document.getElementById('description').value;
    const transactionType = document.querySelector('input[name="transaction_type"]:checked').value;

    const response = await fetch(`${BASE_URL}/transactions/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Token ${authToken}`
        },
        body: JSON.stringify({
            amount,
            date,
            description,
            transaction_type: transactionType
        })
    });

    if (response.ok) {
        alert('Transaction added successfully');
        getTransactions();  // Refresh the list
    } else {
        // Properly handle and log error data
        const errorData = await response.json();
        console.error('Error data:', errorData);
        alert(`Failed to add transaction: ${errorData.detail || 'Unknown error'}`);
    }
}

// Logout function
function logout() {
    authToken = ''; // Clear the token
    localStorage.removeItem('authToken');  // Clear from localStorage if stored
    document.getElementById('login-section').style.display = 'block';
    document.getElementById('data-section').style.display = 'none';
}

// Call loadToken on page load to persist login status
window.onload = loadToken;