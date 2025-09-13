from collections import defaultdict, Counter
import csv, os

class Reports:
    def __init__(self, ledger, budgets: dict, month: str):
        self.ledger = ledger
        self.budgets = budgets or {}
        self.month = month

    def _month_txns(self):
        return [t for t in self.ledger.transactions if t.date.strftime("%Y-%m") == self.month]

    def monthly_summary_text(self):
        txs = self._month_txns()
        income = sum(t.amount for t in txs if t.amount > 0)
        expense = -sum(t.amount for t in txs if t.amount < 0)
        net = income - expense
        lines = []
        lines.append(f"Summary for {self.month}")
        lines.append(f"Income: {income:.2f}")
        lines.append(f"Expense: {expense:.2f}")
        lines.append(f"Net: {net:.2f}")
        lines.append("\nBy Category:")
        cat_totals = defaultdict(float)
        for t in txs:
            if t.amount < 0:
                cat_totals[t.category] += -t.amount
        for c, a in cat_totals.items():
            bud = self.budgets.get(c)
            if bud:
                lines.append(f"{c}: {a:.2f} (budget {bud:.2f})")
            else:
                lines.append(f"{c}: {a:.2f}")
        lines.append("\nTop Merchants:")
        top_mer = Counter()
        for t in txs:
            if t.amount < 0:
                top_mer[t.merchant] += -t.amount
        for m, a in top_mer.most_common(5):
            lines.append(f"{m}: {a:.2f}")
        return "\n".join(lines)

    def save_text(self, path, text):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

    def save_category_csv(self, path):
        txs = self._month_txns()
        cat_totals = defaultdict(float)
        for t in txs:
            if t.amount < 0:
                cat_totals[t.category] += -t.amount
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["category", "spend", "budget", "over_under"])
            for c, a in cat_totals.items():
                b = self.budgets.get(c, 0)
                writer.writerow([c, f"{a:.2f}", f"{b:.2f}", f"{(a-b):.2f}"])
