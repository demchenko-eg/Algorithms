max_value: int

def f1(index, curr, tracks, leng):
    global max_value
    if max_value == leng:
        return leng
    if index == len(tracks):
        if curr > max_value:
            max_value = curr
        return curr
    best = f1(index + 1, curr, tracks, leng)
    if curr + tracks[index] <= leng:
        best = max(best, f1(index + 1, curr + tracks[index], tracks, leng))
    return best

while True:
    try:
        line = input().strip()
    except EOFError:
        break
    if not line:
        continue
    data = list(map(int, line.split()))
    leng = data[0]
    count = data[1]
    tracks = data[2:]
    max_value = 0
    result = f1(0, 0, tracks, leng)
    print("sum:" + str(result))