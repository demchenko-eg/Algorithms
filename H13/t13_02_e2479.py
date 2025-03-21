def f2(s):
    stack = []
    br = {')': '(', ']': '['}
    for ch in s:
        if ch in br.values():
            stack.append(ch)
        elif ch in br.keys():
            if not stack or stack[-1] != br[ch]:
                return 'No'
            stack.pop()
    return 'Yes' if not stack else 'No'

n = int(input().strip())
for _ in range(n):
    exp = input().strip()
    print(f2(exp))