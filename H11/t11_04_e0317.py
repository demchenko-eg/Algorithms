import sys
sys.set_int_max_str_digits(10**6)

def f34(x: str, y: str) -> str:
    x = x.lstrip("0") or "0"
    y = y.lstrip("0") or "0"
    if x == "0" or y == "0":
        return "0"
    if len(x) == 1 and len(y) == 1:
        return str(int(x) * int(y))
    n = max(len(x), len(y))
    if len(x) < n:
        x = x.zfill(n)
    if len(y) < n:
        y = y.zfill(n)
    if n <= 4:
        return str(int(x) * int(y))
    m = n // 2
    x_H, x_L = x[:-m], x[-m:]
    y_H, y_L = y[:-m], y[-m:]
    z0 = f34(x_L, y_L)
    z2 = f34(x_H, y_H)
    sum_x = str(int(x_H) + int(x_L))
    sum_y = str(int(y_H) + int(y_L))
    z1 = f34(sum_x, sum_y)
    mid = int(z1) - int(z2) - int(z0)
    result = int(z2) * 10 ** (2 * m) + mid * 10 ** m + int(z0)
    return str(result)

with open("input.txt", "r") as infile:
    A, B = infile.read().split()
with open("output.txt", "w") as outfile:
    outfile.write(f34(A, B))