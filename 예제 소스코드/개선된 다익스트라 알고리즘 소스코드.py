from heapq import heappush, heappop
n, m = map(int, input().split())
stt = int(input().strip())
grp = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    grp[a].append((c, b))

INF = int(1e9)
dist = [INF for _ in range(n+1)]
route = ['' for _ in range(n+1)]
q = [(0, stt)]
dist[stt] = 0
route[stt] = str(stt)

while q:
    d, p = heappop(q)

    if dist[p] < d:
        continue

    for td, np in grp[p]:
        nd = d + td
        if  dist[np] > nd:
            dist[np] = nd
            route[np] = route[p] + str(np)
            heappush(q, (nd, np))

print([i if i != INF else -1 for i in dist])
print(route)

'''
입력 예시

6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

