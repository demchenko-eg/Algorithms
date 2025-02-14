size = 10007
library = [[] for _ in range(size)]

def init():
    global library
    library = [[] for _ in range(size)]
def addBook(author, title):
    index = hash(author) % size
    for pair in library[index]:
        if pair[0] == author:
            pair[1].add(title)
            return
    library[index].append([author, {title}])

def find(author, title):
    index = hash(author) % size
    for pair in library[index]:
        if pair[0] == author:
            return title in pair[1]
    return False

def delete(author, title):
    index = hash(author) % size
    for pair in library[index]:
        if pair[0] == author:
            pair[1].discard(title)
            if not pair[1]:
                library[index].remove(pair)
            return

def findByAuthor(author):
    index = hash(author) % size
    for pair in library[index]:
        if pair[0] == author:
            books = list(pair[1])
            for i in range(1, len(books)):
                key = books[i]
                j = i - 1
                while j >= 0 and books[j] > key:
                    books[j + 1] = books[j]
                    j -= 1
                books[j + 1] = key
            return books
    return []
