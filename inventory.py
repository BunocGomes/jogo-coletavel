# inventory.py

class Inventory:
    def __init__(self):
        # Usa um dicionário para armazenar a quantidade de cada tipo de item
        self.items = {
            'coin': 0,
            'key': 0,
            'diamond': 0
        }

    def add_item(self, item):
        # Adiciona o item ao inventário
        if item.type in self.items:
            self.items[item.type] += 1

    def display(self):
        # Exibe o inventário
        print("Inventário:")
        for item_type, quantity in self.items.items():
            print(f"{item_type.capitalize()}: {quantity}")