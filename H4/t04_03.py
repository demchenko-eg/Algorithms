def find_x():
    left, right = 0, 10
    eps = 1e-7
    while right - left > eps:
        mid = (left + right) / 2
        if mid**3 + mid + 1 > 5:
            right = mid
        else:
            left = mid
    return round(left, 6)

print(f"{find_x():.6f}")

# корінь 1.378797