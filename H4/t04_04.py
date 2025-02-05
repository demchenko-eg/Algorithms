from math import sin

def find_x():
    left, right = 1.6, 3
    eps = 1e-7
    while right - left > eps:
        mid = (left + right) / 2
        if (sin(left) - left / 3) * (sin(mid) - mid / 3) <= 0:
            right = mid
        else:
            left = mid
    return round(left, 6)

print(f"{find_x():.6f}")

# корінь 2.278863