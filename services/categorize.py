import re

class Categorizer:
    def __init__(self, rules: dict):
        self.rules = {cat: [kw.lower() for kw in kws] for cat, kws in rules.items()}

    def categorize(self, txn):
        merchant = txn.merchant.lower()
        for cat, kws in self.rules.items():
            for kw in kws:
                if kw in merchant:
                    txn.category = cat
                    return cat
        txn.category = "Uncategorized"
        return "Uncategorized"
