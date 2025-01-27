def max_cyclic_value(n):
    binary = bin(n)[2:]
    max_value = n
    lenght = len(binary)
    current = binary
    for i in range(lenght - 1):
        current = current[1:] + current[0]
        max_value = max(max_value, int(current, 2))
    return max_value

print(max_cyclic_value(int(input())))