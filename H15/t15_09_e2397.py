def subtract_rect(r, s):
    rx, ry, rw, rh = r
    sx, sy, sw, sh = s
    rx2, ry2 = rx + rw, ry + rh
    sx2, sy2 = sx + sw, sy + sh
    ix1 = max(rx, sx)
    iy1 = max(ry, sy)
    ix2 = min(rx2, sx2)
    iy2 = min(ry2, sy2)
    if ix1 >= ix2 or iy1 >= iy2:
        return [r]
    parts = []
    if ry < iy1:
        parts.append((rx, ry, rw, iy1 - ry))
    if iy2 < ry2:
        parts.append((rx, iy2, rw, ry2 - iy2))
    if rx < ix1:
        parts.append((rx, iy1, ix1 - rx, iy2 - iy1))
    if ix2 < rx2:
        parts.append((ix2, iy1, rx2 - ix2, iy2 - iy1))
    return parts

def is_visible(window, later_windows):
    fragments = [window]
    for later in later_windows:
        new_fragments = []
        for frag in fragments:
            new_fragments.extend(subtract_rect(frag, later))
        fragments = new_fragments
        if not fragments:
            return False
    return len(fragments) > 0

n = int(input().strip())
windows = []
for _ in range(n):
    x, y, w, h = map(int, input().split())
    windows.append((x, y, w, h))
visible_count = 0
for i in range(n):
    later_windows = windows[i+1:]
    if is_visible(windows[i], later_windows):
        visible_count += 1
print(visible_count)