import csv
from datetime import datetime
from models.transaction import Transaction

def import_csvs(paths):
    txs = []
    for path in paths:
        try:
            with open(path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    try:
                        d = datetime.strptime(row["date"], "%Y-%m-%d").date()
                        m = row["merchant"]
                        a = float(row["amount"])
                        txs.append(Transaction(date=d, merchant=m, amount=a))
                    except Exception as e:
                        print("Skipping row:", e)
        except FileNotFoundError:
            print("File not found:", path)
    return txs
