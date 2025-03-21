def ab(a, p):
    a = int(a)
    p = int(p)
    s = []
    if a == 0:
        s.append(0)
    while a:
        s.append(a % p)
        a //= p
    r = ""
    while s:
        d = s.pop()
        r += str(d) if d < 10 else "[" + str(d) + "]"
    return r

a = input().strip()
p = input().strip()
print(ab(a, p))