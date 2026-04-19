import sys
input = sys.stdin.readline

def solve():
    n, a, b = map(int, input().split())
    
    if n % 2 or a % 2 == b % 2:
        print("No")
        return
    
    print("Yes")
    res = []
    d = 1  # 1=r, 0=l
    
    if a == n:
        for i in range(1, n - 1):
            if d == 1:
                res.append('R' * (n - 1))
                d = 0
            else:
                res.append('L' * (n - 1))
                d = 1
            res.append('D')
        
        j = 1
        while j < b - 1:
            res.append("DRUR")
            j += 2
        res.append("RD")
        j = b + 1
        while j < n:
            res.append("RURD")
            j += 2
    else:
        i = 1
        while i <= n:
            if d == 1:
                if i == a:
                    j = 1
                    while j < b - 1:
                        res.append("DRUR")
                        j += 2
                    res.append("DR")
                    j = b + 1
                    while j < n:
                        res.append("RURD")
                        j += 2
                    i += 1
                else:
                    res.append('R' * (n - 1))
                d = 0
            else:
                if i == a:
                    j = n
                    while j > b + 1:
                        res.append("DLUL")
                        j -= 2
                    res.append("DL")
                    j = b - 1
                    while j > 1:
                        res.append("LULD")
                        j -= 2
                    i += 1
                else:
                    res.append('L' * (n - 1))
                d = 1
            
            if i != n:
                res.append('D')
            i += 1
    
    print(''.join(res))

def main():
    t = int(input())
    for _ in range(t):
        solve()

main()