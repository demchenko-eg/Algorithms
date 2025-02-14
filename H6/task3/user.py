size = 10007
library = [None] * size

def init():
    global library
    library = [None] * size

def addBook(author, title):
    global library
    key = (author, title)
    index = hash(key) % size
    
    while library[index] is not None and library[index] != "DELETED":
        if library[index] == key:
            return
        index = (index + 1) % size
    library[index] = key

def find(author, title):
    key = (author, title)
    index = hash(key) % size
    while library[index] is not None:
        if library[index] == key:
            return True
        index = (index + 1) % size
    return False

def delete(author, title):
    global library
    key = (author, title)
    index = hash(key) % size
    while library[index] is not None:
        if library[index] == key:
            library[index] = "DELETED"
            return
        index = (index + 1) % size

def findByAuthor(author):
    books = [item[1] for item in library if item is not None and item != "DELETED" and item[0] == author]
    for i in range(1, len(books)):
        key = books[i]
        j = i - 1
        while j >= 0 and books[j] > key:
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = key
    return books
