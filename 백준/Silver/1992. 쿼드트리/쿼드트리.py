def quad(x, y, size, arr):
    if size == 1:
        return arr[x][y]

    first = arr[x][y]
    is_uniform = True
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != first:
                is_uniform = False
                break
        if not is_uniform:
            break

    if is_uniform:
        return str(first)

    mid = size // 2
    top_left = quad(x, y, mid, arr)
    top_right = quad(x, y + mid, mid, arr)
    bottom_left = quad(x + mid, y, mid, arr)
    bottom_right = quad(x + mid, y + mid, mid, arr)

    return f"({top_left}{top_right}{bottom_left}{bottom_right})"


n = int(input())
arr = [list(map(int, input().strip())) for i in range(n)]

print(quad(0, 0, n, arr))
