def f3(s):
    stack = []
    ts = s.split()
    for t in ts:
        if t.isdigit() or (t[0] == '-' and t[1:].isdigit()):
            stack.append(int(t))
        else:
            b = stack.pop()
            a = stack.pop()
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            elif t == "/":
                stack.append(a / b)
    return stack[0]

s = input().strip()
print(f3(s))