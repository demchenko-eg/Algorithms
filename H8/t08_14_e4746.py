n = int(input())
if n == 0:
    print(0)
else:
    tips = list(map(int, input().split()))
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if tips[j] < tips[j + 1]:
                tips[j], tips[j + 1] = tips[j + 1], tips[j]
    profit = sum(max(tips[i] - i, 0) for i in range(n))
    print(profit)
