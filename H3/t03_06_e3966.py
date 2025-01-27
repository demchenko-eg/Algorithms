def butterflies():
    n = int(input())
    collection = list(map(int, input().split()))
    m = int(input())
    queries = list(map(int, input().split()))
    def s(array, target):
        left, right = 0, len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    result = []
    for query in queries:
        if s(collection, query):
            result.append("YES")
        else:
            result.append("NO")
    print("\n".join(result))

butterflies()
