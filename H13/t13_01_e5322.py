def bin_hex(binv):
    stack = []
    dec = int(binv, 2)
    hex_sym = "0123456789ABCDEF"
    if dec == 0:
        return "0"
    while dec > 0:
        r = dec % 16
        stack.append(hex_sym[r])
        dec //= 16
    return "".join(reversed(stack))

n = input().strip()
print(bin_hex(n))