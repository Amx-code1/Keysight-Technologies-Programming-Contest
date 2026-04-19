N, M=map(int, input().split())
F = list(map(int, input().split()))

# question 1 Are all N people wearing different types of clothes ?
print("Yes" if len(set(F))==N else "No")

# question 2  For every one of the M types of clothes, is there at least one person wearing that type?
print("Yes" if len(set(F))==M else "No")