import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    l, r = 0, N - 1
    cl, cr = 0, 0  # carry on left side, right side
    ans = 0
    while l < r:
        a = (A[l] + cl) % M
        b = (A[r] + cr) % M
        d1 = (b - a) % M  # increment a by d1 to reach b → add d1 to cl
        d2 = (a - b) % M  # increment b by d2 to reach a → add d2 to cr
        if d1 <= d2:
            ans += d1
            cl = (cl + d1) % M
        else:
            ans += d2
            cr = (cr + d2) % M
        l += 1
        r -= 1
    print(ans)

T = int(input())
for _ in range(T):
    solve()