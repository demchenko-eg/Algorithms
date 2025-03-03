def perm(lst):
    if len(lst) == 0:
        yield []
    else:
        for i in range(len(lst)):
            rest = lst[:i] + lst[i+1:]
            for p in perm(rest):
                yield [lst[i]] + p

def operators(n):
    ops = ['+', '-', '*']
    if n == 0:
        yield []
    else:
        for op in ops:
            for rest in operators(n - 1):
                yield [op] + rest

def func(numbers):
    for p in perm(numbers):
        for ops in operators(4):
            result = p[0]
            for i in range(4):
                if ops[i] == '+':
                    result += p[i+1]
                elif ops[i] == '-':
                    result -= p[i+1]
                elif ops[i] == '*':
                    result *= p[i+1]
            if result == 23:
                return True
    return False

while True:
    line = input().strip()
    if not line:
        continue
    numbers = list(map(int, line.split()))
    if sum(numbers) == 0:
        break
    print("Possible" if func(numbers) else "Impossible")