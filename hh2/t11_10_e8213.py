def f1(i, left, right):
    if i == m:
        if left == right:
            res.add(left)
        return
    f1(i+1, left, right)
    f1(i+1, left + plates[i], right)
    f1(i+1, left, right + plates[i])

n, m = map(int, input().split())
barbells = list(map(int, input().split()))
plates = list(map(int, input().split()))
res = set()
f1(0, 0, 0)
ans = set()
for b in barbells:
    for s in res:
        ans.add(b + 2 * s)
for weight in sorted(ans):
    print(weight)