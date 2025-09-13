from services.importer import import_csvs
from services.storage import Storage
from services.categorize import Categorizer
from models.ledger import TransactionLedger
from services.reports import Reports
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "outputs", "reports")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    print("Welcome to BudgetBuddy!")
    storage = Storage(DATA_DIR)
    rules = storage.load_rules()
    budgets = storage.load_budgets()
    categorizer = Categorizer(rules)
    ledger = TransactionLedger()

    while True:
        print("\nMenu:")
        print("1) Import CSV")
        print("2) Set/Update Budget")
        print("3) List Transactions")
        print("4) Reports")
        print("5) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            path = input("Enter CSV file path (or press Enter for sample): ").strip()
            if not path:
                path = os.path.join(DATA_DIR, "sample_transactions.csv")
            txs = import_csvs([path])
            for t in txs:
                categorizer.categorize(t)
                ledger.add_transaction(t)
            print(f"Imported {len(txs)} transactions.")
        elif choice == "2":
            ym = input("Enter month (YYYY-MM): ").strip()
            cat = input("Enter category: ").strip()
            amt = float(input("Enter budget amount: ").strip())
            if ym not in budgets:
                budgets[ym] = {}
            budgets[ym][cat] = amt
            storage.save_budgets(budgets)
            print("Budget saved.")
        elif choice == "3":
            for t in ledger:
                print(t)
        elif choice == "4":
            if not ledger.transactions:
                print("No transactions. Import first.")
                continue
            ym = input("Enter month (YYYY-MM): ").strip()
            if not ym and ledger.transactions:
                ym = ledger.transactions[0].date.strftime("%Y-%m")
            rep = Reports(ledger, budgets.get(ym, {}), ym)
            txt = rep.monthly_summary_text()
            txt_path = os.path.join(OUTPUT_DIR, f"monthly_summary_{ym}.txt")
            rep.save_text(txt_path, txt)
            rep.save_category_csv(os.path.join(OUTPUT_DIR, f"category_spend_{ym}.csv"))
            print("Reports generated in outputs/reports/")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
