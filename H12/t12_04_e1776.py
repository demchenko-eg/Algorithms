def st(n, tg):
    stack = []
    curr = 1
    for target in tg:
        while curr <= n and (not stack or stack[-1] != target):
            stack.append(curr)
            curr += 1
        if stack and stack[-1] == target:
            stack.pop()
        else:
            return "No"
    return "Yes"


if __name__ == "__main__":
    r = []
    while True:
        n = int(input().strip())
        if n == 0:
            break
        t = []
        while True:
            line = input().strip()
            if line == "0":
                break
            tg = list(map(int, line.split()))
            t.append(st(n, tg))
        r.append("\n".join(t) + "\n")
    print("\n".join(r))