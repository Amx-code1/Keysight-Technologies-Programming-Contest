from collections import defaultdict , deque

N, M = map(int , input().split())

G = defaultdict(list)
for _ in range(M):
    A, B = map(int , input().split())
    G[A].append(B)

owned = set([1])
queue = deque([1])

while queue:
    item = queue.popleft()
    for next_item in G[item]:
        if next_item not in owned:
            owned.add(next_item)
            queue.append(next_item)

print(len(owned))