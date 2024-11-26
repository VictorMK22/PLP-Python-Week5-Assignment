class Book:

    def __init__ (self, name, author, price):
        self.name = name
        self.author = author
        self.price = price

    def display(self):
        print(f"\nThe book {self.name} was written by {self.author} and currently sells at {self.price}")

class NoteBook(Book):
    def __init__(self, name, price):
        super(). __init__(name, "N/A", price)

    def purpose(self):
        print(f"This book is used for jotting down short notes!\n")


nb1 = NoteBook("Bowen Notebook 661", 650)
nb1.display()
nb1.purpose()