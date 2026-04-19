import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))  # 1-indexed
    
    v = []
    for i in range(1, n // 2 + 1):
        v.append((a[i] - a[n - i + 1] + m) % m)
    
    v.append(0)
    v.reverse()
    v.append(0)
    
    b = []
    for i in range(1, len(v)):
        b.append((v[i] - v[i - 1] + m) % m)
    
    b.sort()
    
    ans = 0
    l, r = 0, len(b) - 1
    while l <= r:
        if b[l] < m - b[r]:
            ans += b[l]
            b[r] += b[l]
            b[l] = 0
            l += 1
        else:
            ans += m - b[r]
            b[l] -= m - b[r]
            b[r] = 0
            r -= 1
    
    print(ans)

def main():
    T = int(input())
    for _ in range(T):
        solve()

main()