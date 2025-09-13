from typing import List, Iterator
from models.transaction import Transaction

class LedgerIterator:
    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.transactions):
            t = self.transactions[self.index]
            self.index += 1
            return t
        else:
            raise StopIteration

class TransactionLedger:
    def __init__(self):
        self.transactions: List[Transaction] = []

    def add_transaction(self, txn: Transaction):
        self.transactions.append(txn)

    def __iter__(self) -> Iterator[Transaction]:
        return LedgerIterator(self.transactions)

    def filter_by_month(self, ym: str):
        ledger = TransactionLedger()
        for t in self.transactions:
            if t.date.strftime("%Y-%m") == ym:
                ledger.add_transaction(t)
        return ledger
