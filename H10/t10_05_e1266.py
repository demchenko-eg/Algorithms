def f1(line):
    tokens = line.split()
    if not tokens:
        return
    N = int(tokens[0])
    s = int(tokens[1])
    tracks = list(map(int, tokens[2:]))
    best = 0
    def f2(i, total):
        nonlocal best
        if total > N:
            return
        if i == s:
            if total > best:
                best = total
            return
        f2(i + 1, total)
        f2(i + 1, total + tracks[i])
    f2(0, 0)
    print("sum:" + str(best))

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    f1(line)