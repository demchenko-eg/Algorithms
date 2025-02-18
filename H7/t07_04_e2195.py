class Set:
    def __init__(self, size=2003):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return sum(ord(c) for c in key) % self.size

    def add(self, key):
        key = key.lower()
        index = self._hash(key)
        if self.contains(key):
            return
        node = (key, self.table[index])
        self.table[index] = node

    def contains(self, key):
        key = key.lower()
        index = self._hash(key)
        current = self.table[index]
        while current:
            if current[0] == key:
                return True
            current = current[1]
        return False

    def extract_words(text):
        word = ""
        words = []
        for char in text.lower():
            if char.isalpha():
                word += char
            elif word:
                words.append(word)
                word = ""
        if word:
            words.append(word)
        return words

    def check(self, n, m, vocab_lines, text_lines):
        vocabulary = Set()
        for word in vocab_lines:
            vocabulary.add(word.strip())
        text_words = Set()
        used_words = Set()
        for line in text_lines:
            words = Set.extract_words(line.strip())
            for word in words:
                text_words.add(word)
                used_words.add(word.lower())
        all_words = True
        current = used_words.table
        for cont in current:
            while cont:
                if not vocabulary.contains(cont[0]):
                    all_words = False
                    break
                cont = cont[1]
        all_used = True
        for cont in vocabulary.table:
            while cont:
                if not text_words.contains(cont[0]):
                    all_used = False
                    break
                cont = cont[1]
        if all_words and all_used:
            return "Everything is going to be OK."
        elif not all_words:
            return "Some words from the text are unknown."
        else:
            return "The usage of the vocabulary is not perfect."


n, m = map(int, input().split())
vocab_lines = [input().strip() for _ in range(n)]
text_lines = [input().strip() for _ in range(m)]
print(Set().check(n, m, vocab_lines, text_lines))