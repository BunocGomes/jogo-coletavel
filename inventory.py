# inventory.py

class Inventory:
    def __init__(self):
        self.slots = [None] * 9

    def add_item(self, item):
        for i in range(len(self.slots)):
            if self.slots[i] is None:
                self.slots[i] = item
                break

    def organize(self):
        self.slots.sort(key=lambda x: x.type if x else '')

    def display(self):
        print("Inventário:")
        for i, item in enumerate(self.slots):
            print(f"Slot {i+1}: {item.type if item else 'Vazio'}")