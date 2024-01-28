from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_expense', methods=['POST'])
def add_expense():
    try:
        description = request.form['description']
        amount = float(request.form['amount'])
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect('expense_tracker.db')
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                amount REAL,
                date TEXT
            )
        ''')
        conn.commit()
        cursor.execute('INSERT INTO expenses (description, amount, date) VALUES (?, ?, ?)', (description, amount, date))
        conn.commit()
        conn.close()

        return jsonify({'status': 'success', 'message': 'Expense added successfully!'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})


@app.route('/view_expenses')
def view_expenses():
    conn = sqlite3.connect('expense_tracker.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM expenses')
    expenses = cursor.fetchall()
    conn.close()

    return render_template('expenses.html', expenses=expenses)


if __name__ == '__main__':
    app.run(debug=True)
