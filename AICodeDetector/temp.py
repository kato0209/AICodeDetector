import torch

code = """```python\nclass WorksheetManager:\n    def __init__(self):\n        self.worksheets = {}\n        self.worksheet_names = {}\n\n    def add_worksheet(self, id, name):\n        if id in self.worksheets:\n            raise ValueError(f\"Worksheet with id {id} already exists\")\n        if name in self.worksheet_names:\n            raise ValueError(f\"Worksheet with name {name} already exists\")\n        self.worksheets[id] = {'name': name, 'id': id}\n        self.worksheet_names[name] = id\n\n    def get_worksheet(self, id_or_name):\n        if isinstance(id_or_name,"""
print(code)
