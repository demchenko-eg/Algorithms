def height():
    results = []
    while True:
        try:
            n = int(input())
            heights = list(map(int, input().split()))
            lower, upper = map(int, input().split())
            count = 0
            for height in heights:
                if lower <= height <= upper:
                    count += 1
            results.append(count)
        except EOFError:
            break
    print("\n".join(map(str, results)))

height()