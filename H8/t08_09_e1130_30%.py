def bubble_sort(n, k):
    def digit_sum(x):
        return sum(int(d) for d in str(x))
    numbers = list(range(1, n + 1))
    length = len(numbers)
    for i in range(length - 1):
        for j in range(length - i - 1):
            a, b = numbers[j], numbers[j + 1]
            if (digit_sum(a) > digit_sum(b)) or (digit_sum(a) == digit_sum(b) and str(a) > str(b)):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    index = numbers.index(k) + 1
    print(index)
    print(numbers[k - 1])

n = int(input())
k = int(input())
bubble_sort(n, k)
