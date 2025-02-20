def sort_books_by_length(n, books):
    books_with_length = []
    for index, book in enumerate(books):
        text = "\n".join(book)
        books_with_length.append((len(text.replace("\n", "")), index, text))
    books_with_length.sort(key=lambda x: (x[0], x[1]))
    for i, (_, _, text) in enumerate(books_with_length):
        if i > 0:
            print("***")
        print(text)

n = int(input())
books = []
for _ in range(n):
    m = int(input())
    book = [input().rstrip().strip() for _ in range(m)]
    # book = [input() for _ in range(m)]
    books.append(book)
sort_books_by_length(n, books)