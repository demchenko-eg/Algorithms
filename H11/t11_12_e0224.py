def f3(city, cost, tax_acc):
    global max_profit
    if city == N:
        revenue = 0.0
        for i in range(3):
            margin = 1 - (tax_acc[i] / 100)
            if margin > 0:
                revenue += goods[i] * prices[i] * margin
        profit = revenue - cost
        if profit > max_profit:
            max_profit = profit
        return
    for u, v, road_cost in roads:
        if u == city:
            new_cost = cost + road_cost
            new_tax = tax_acc[:]
            if v != N:
                for i in range(3):
                    new_tax[i] += taxes[v]
            f3(v, new_cost, new_tax)

N, M = map(int, input().split())
goods = list(map(int, input().split()))
prices = list(map(int, input().split()))
taxes = [0] * (N + 1)
for city in range(2, N):
    taxes[city] = sum(map(int, input().split()))
roads = [tuple(map(int, input().split())) for _ in range(M)]
max_profit = -10**9
f3(1, 0, [0, 0, 0])
print(f"{max_profit:.2f}" if max_profit > 0 else "0.00")