# BudgetBuddy

BudgetBuddy is a Python application to track personal finances, manage budgets, and generate insightful reports. It supports importing transactions, categorizing expenses automatically, analyzing monthly spending, and storing data persistently using JSON and CSV files.

This project is designed as a hands-on exercise to reinforce core Python skills including object-oriented programming, file I/O, modular design, and data analysis.


## Features

* Import transactions from CSV files
* Categorize expenses automatically based on rules
* View reports:

  * Monthly summaries
  * Category-wise spending
  * Budget tracking
* Persistent storage using files (`budgets.json`, `rules.json`, `transactions.csv`)
* Export reports in CSV and text formats
* Modular design for scalability


## Folder Structure

```
budgetbuddy-main/
├── main.py               # Entry point
├── data/                 # Stores budgets, rules, and sample transactions
│   ├── budgets.json
│   ├── rules.json
│   └── sample_transactions.csv
├── models/               # Core models
│   ├── transaction.py
│   └── ledger.py
├── services/             # Business logic
│   ├── importer.py
│   ├── categorize.py
│   ├── reports.py
│   └── storage.py
├── outputs/              # Generated reports
│   └── reports/
├── README.md             # Documentation
```


## Getting Started

### Installation

1. Clone or download the repository.
2. Navigate to the project root (`budgetbuddy-main/`).
3. Ensure required directories exist (they will be auto-created on first run):

   * `data/`
   * `outputs/`


## Running the Application

From the project root, run:

```bash
python main.py
```


## Sample Workflow

1. Import transactions from `sample_transactions.csv`.
2. Apply categorization rules from `rules.json`.
3. Generate a monthly summary report (saved in `outputs/reports/`).


## Data File Formats

### sample\_transactions.csv

CSV file storing transactions.

```csv
date,merchant,amount
2025-08-01,Amazon,1500
2025-08-02,Swiggy,450
```

### rules.json

JSON file storing categorization rules.

```json
{
  "Amazon": "Shopping",
  "Swiggy": "Food"
}
```

### budgets.json

JSON file storing budget limits.

```json
{
  "Food": 5000,
  "Shopping": 10000
}
```


## Outputs/Reports

BudgetBuddy generates reports in CSV and text formats:

* **Category Spend Report** → category-wise spending per month
* **Monthly Summary** → total income, expenses, and savings


## Team Members

* Gangadhar Madupu (gmadupu@cisco.com)
* Bhargava Sai Pasumarthy (bhpasuma@cisco.com)

