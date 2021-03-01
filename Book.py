class Book: #DONE
    def __init__(self, title = "", author = "", year = None):
        self.title = title
        self.author = author
        self.year = year

    def __gt__(self, other):
        if self.author > other.author:
            return True
        elif not(self.author > other.author) and not(other.author > self.author):
            if self.year > other.year:
                return True
            elif not(self.year > other.year) and not(other.year > self.year):
                if self.title > other.title:
                    return True
        return False
    
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year
    
    def getBookDetails(self):
        return "Title: {}, Author: {}, Year: {}".format(self.title, self.author, self.year)

    