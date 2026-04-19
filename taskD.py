import sys
input = sys.stdin.readline

def canonical(s):
    votqi = []
    for c in s:
        if c == ')':
            if len(votqi) >= 3 and votqi[-1] == 'x' and votqi[-2] == 'x' and votqi[-3] == '(':
                votqi.pop()
                votqi.pop()
                votqi.pop()
                votqi.append('x')
                votqi.append('x')
            else:
                votqi.append(c)
        else:
            votqi.append(c)
    return ''.join(votqi)

def solve():
    A = input().strip()
    B = input().strip()
    if canonical(A) == canonical(B):
        print("Yes")
    else:
        print("No")

T = int(input())
for _ in range(T):
    solve()