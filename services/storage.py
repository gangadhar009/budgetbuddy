import json, os

class Storage:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def load_rules(self):
        path = os.path.join(self.data_dir, "rules.json")
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def load_budgets(self):
        path = os.path.join(self.data_dir, "budgets.json")
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_budgets(self, budgets):
        path = os.path.join(self.data_dir, "budgets.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(budgets, f, indent=2)
