"""Reference solution: Lesson 34 - Item Class (Base)."""


class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value


if __name__ == "__main__":
    ring = Item("Ring", "A shiny ring", 25)
    print(f"{ring.name} - {ring.description} ({ring.value} gold)")
