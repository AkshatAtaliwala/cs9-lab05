from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

def test_BookCollection1():
    
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc = BookCollection()
    assert bc.isEmpty() == True
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getNumberOfBooks() == 4
    assert bc.getBooksByAuthor("King, Stephen") == "Title: Rage, Author: King, Stephen, Year: 1977\n""Title: The Shining, Author: King, Stephen, Year: 1977\n""Title: Cujo, Author: King, Stephen, Year: 1981\n"
    assert bc.isEmpty() == False
    assert bc.getAllBooksInCollection() == "Title: Ready Player One, Author: Cline, Ernest, Year: 2011\n""Title: Rage, Author: King, Stephen, Year: 1977\n""Title: The Shining, Author: King, Stephen, Year: 1977\n""Title: Cujo, Author: King, Stephen, Year: 1981\n"

def test_BookCollection2():
    b0 = Book("The Cat in the Hat", "Dr. Seuss", 1957)
    b1 = Book("Green Eggs and Ham", "Dr. Seuss", 1960)
    b2 = Book("One fish, two fish, red fish, blue fish", "Dr. Seuss", 1960)
    bc = BookCollection()
    assert bc.isEmpty() == True
    assert bc.getNumberOfBooks() == 0
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    assert bc.isEmpty() == False
    assert bc.getNumberOfBooks() == 3
    assert bc.getBooksByAuthor("DR. SEUSS") == "Title: The Cat in the Hat, Author: Dr. Seuss, Year: 1957\n""Title: Green Eggs and Ham, Author: Dr. Seuss, Year: 1960\n""Title: One fish, two fish, red fish, blue fish, Author: Dr. Seuss, Year: 1960\n"
    assert bc.getBooksByAuthor("dr. seuss") == "Title: The Cat in the Hat, Author: Dr. Seuss, Year: 1957\n""Title: Green Eggs and Ham, Author: Dr. Seuss, Year: 1960\n""Title: One fish, two fish, red fish, blue fish, Author: Dr. Seuss, Year: 1960\n"
    assert bc.getBooksByAuthor("Dr. Seuss") == "Title: The Cat in the Hat, Author: Dr. Seuss, Year: 1957\n""Title: Green Eggs and Ham, Author: Dr. Seuss, Year: 1960\n""Title: One fish, two fish, red fish, blue fish, Author: Dr. Seuss, Year: 1960\n"
    assert bc.getAllBooksInCollection() == "Title: The Cat in the Hat, Author: Dr. Seuss, Year: 1957\n""Title: Green Eggs and Ham, Author: Dr. Seuss, Year: 1960\n""Title: One fish, two fish, red fish, blue fish, Author: Dr. Seuss, Year: 1960\n"

def test_Book():
    b0 = Book("The Cat in the Hat", "Dr. Seuss", 1957)
    assert b0.getAuthor() == "Dr. Seuss"
    assert b0.getTitle() == "The Cat in the Hat"
    assert b0.getYear() == 1957
    assert b0.getBookDetails() == "Title: The Cat in the Hat, Author: Dr. Seuss, Year: 1957"

    b1 = Book("Green Eggs and Ham", "Dr. Seuss", 1960)
    assert b1.getAuthor() == "Dr. Seuss"
    assert b1.getTitle() == "Green Eggs and Ham"
    assert b1.getYear() == 1960
    assert b1.getBookDetails() == "Title: Green Eggs and Ham, Author: Dr. Seuss, Year: 1960"

def test_BookCollectionNode():
    n = BookCollectionNode(20)
    assert n.getData() == 20
    assert n.getNext() == None
    n.setData("Book")
    assert n.getData() == "Book"
    n2 = BookCollectionNode("Test")
    n.setNext(n2)
    assert n.getNext() == n2
