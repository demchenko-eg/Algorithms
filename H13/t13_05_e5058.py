def hgj(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack.pop() != pairs[ch]:
                return "no"
    return "yes" if not stack else "no"

s = input().strip()
print(hgj(s))