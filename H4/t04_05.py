def find_x():
    left, right = 0, 2
    eps = 1e-7
    while right - left > eps:
        mid = (left + right) / 2
        if (left**3 + 4 * left**2 + left - 6) * (mid**3 + 4 * mid**2 + mid - 6) <= 0:
            right = mid
        else:
            left = mid
    return round(left, 6)

print(f"{find_x():.6f}")

# корінь 1.000000