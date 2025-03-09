from math import factorial as f

def func1(letters, k):
    if not letters:
        return ""
    n = len(letters)
    fact = f(n - 1)
    index = (k - 1) // fact
    letter = letters.pop(index)
    return letter + func1(letters, k - index * fact)


data = input().split()
n = int(data[0])
k = int(data[1])
letters = [chr(ord('a') + i) for i in range(n)]
print(func1(letters, k))