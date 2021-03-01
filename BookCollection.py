from BookCollectionNode import BookCollectionNode
from Book import Book

class BookCollection: #DONE
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def getNumberOfBooks(self):
		temp = self.head
		count = 0
		while temp != None:
			count += 1
			temp = temp.getNext()
		return count
		
	def insertBook(self, Book):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:# find the correct place in the list to add
			if current.getData() > Book:
			    stop = True
			else:
				previous = current
				current = current.getNext()
		
		temp = BookCollectionNode(Book)

		if previous == None:# Case 1: insert at the front of the list
			temp.setNext(self.head)
			self.head = temp
		else: # Case 2: insert anywhere besides the front
			temp.setNext(current)
			previous.setNext(temp)

	
	def getBooksByAuthor(self, author):
		current = self.head
		output = ""
		while current != None:
			if str(author.lower()) in str(current.getData().getAuthor()).lower():
				output += str(current.getData().getBookDetails()) + "\n"
			current = current.getNext()
		return output
		
	def getAllBooksInCollection(self):
		current = self.head
		output = ""
		while current != None:
			output += str(current.getData().getBookDetails()) + "\n"
			current = current.getNext()
		return output
    
