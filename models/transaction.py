from dataclasses import dataclass
from datetime import date

@dataclass
class Transaction:
    date: date
    merchant: str
    amount: float
    category: str = "Uncategorized"

    def __str__(self):
        return f"{self.date} | {self.merchant} | {self.amount:.2f} | {self.category}"
