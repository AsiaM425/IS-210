# assignment1_part2.py

class Book:
    def __init__(self, author="", title=""):
        self.author = author
        self.title = title

    def display(self):
        return f"{self.title}, written by {self.author}"

# Instantiate two Book objects
book1 = Book(author="J. K. Rowling", title="Harry Potter and the Goblet of Fire")
book2 = Book(author="Walter Scott", title="Ivanhoe: A Romance")

# Print the books using their display() method
print(book1.display())
print(book2.display())

