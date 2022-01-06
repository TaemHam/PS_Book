from collections import deque
v, e = map(int, input().split())
ind = [0] * (v+1)
grp = [[] for _ in range(v+1)]
q = deque()

for _ in range(e):
    a, b = map(int, input().split())
    grp[a].append(b)
    ind[b] += 1

for i in range(1, v+1):
    if ind[i] == 0:
        q.append(i)

res = []
while q:
    t = q.popleft()
    res.append(t)
    for i in grp[t]:
        ind[i] -= 1
        if ind[i] == 0:
            q.append(i)

