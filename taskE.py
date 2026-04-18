import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())

    # ❌ Impossible case
    if n % 2 == 0 and (a + b) % 2 == 0:
        print("No")
        continue

    print("Yes")

    path = []

    if n % 2 == 1:
        # Row-wise snake (safe for odd N)
        for i in range(1, n + 1):
            cols = range(1, n + 1) if i % 2 else range(n, 0, -1)
            for j in cols:
                if (i, j) == (a, b):
                    continue
                path.append((i, j))
    else:
        # Column-wise snake (important for even N)
        for j in range(1, n + 1):
            rows = range(1, n + 1) if j % 2 else range(n, 0, -1)
            for i in rows:
                if (i, j) == (a, b):
                    continue
                path.append((i, j))

    # Convert to moves
    moves = []
    for i in range(1, len(path)):
        x1, y1 = path[i - 1]
        x2, y2 = path[i]

        if x2 == x1 and y2 == y1 + 1:
            moves.append('R')
        elif x2 == x1 and y2 == y1 - 1:
            moves.append('L')
        elif x2 == x1 + 1 and y2 == y1:
            moves.append('D')
        elif x2 == x1 - 1 and y2 == y1:
            moves.append('U')

    print(''.join(moves))