def max_pr(s, m):
    n = len(s)
    def dp(i, parts):
        if parts == 1:
            return int(s[i:])
        best = 0
        for j in range(i + 1, n - (parts - 1) + 1):
            first = int(s[i:j])
            candidate = first * dp(j, parts - 1)
            if candidate > best:
                best = candidate
        return best
    return dp(0, m)

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    tokens = line.split()
    if len(tokens) != 2:
        continue
    s, m_str = tokens
    m = int(m_str)
    if s == "0" and m == 0:
        break
    print(max_pr(s, m))