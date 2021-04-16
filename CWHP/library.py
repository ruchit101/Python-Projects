class Library:
    def __init__(self, Listofbooks, name):
        self.books = Listofbooks
        self.name = name
        self.lend_data = {}
        print(f"Welcome to {self.name}")

        for book in self.books:
            self.lend_data[book] = None

    def addbook(self, bookname):
        if bookname not in self.books:
            self.books.append(bookname)
            self.lend_data[bookname] = None
        else:
            print("Book already present")

    def lendbook(self, bookname, reader):
        if bookname in self.books:
            if self.lend_data[bookname] is None:
                self.lend_data[bookname] = reader
        else:
            print("Book not present in library.")

    def displaybooks(self):
        print(self.books)

    def returnbook(self, bookname, reader):
        if self.lend_data[bookname] is not None:
            self.lend_data[bookname] = None
            print(f"Book returned by {reader}")
        else:
            print("Book is already present in library.")


if __name__ == "__main__":
    cl = Library(["One Indian Girl", "Chetan", "Bhagat", "Demo", "Cracy", "Thinker", "APJ", "Gandhi"],
                 "Central Library")
    print(len(cl.books))
    print(cl.lend_data)
    cl.addbook("The Ruchit Bagdey")
    print(cl.lend_data)
    cl.lendbook("The Ruchit Bagdey", "Ruchit")
    print(cl.lend_data)
    cl.lendbook("Democracyy", "Rohan")
    cl.returnbook("The Ruchit Bagdey", "Rahul")
    cl.lendbook("The Ruchit Bagdey", "Dora")
    cl.returnbook("The Ruchit Bagdey", "Doraemon")
    print(cl.lend_data)
    print(f"Total Books: {len(cl.lend_data)}")
