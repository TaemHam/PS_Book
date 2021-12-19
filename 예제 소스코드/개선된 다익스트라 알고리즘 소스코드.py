from heapq import heappush, heappop
n, m = 6, 11
stt = 1
grp = {1 : [(2, 2), (5, 3), (1, 4)], 2 : [(3, 3), (2, 4)], 3 : [(3, 2), (5, 6)], 4 : [(3, 3), (1, 5)], 5 : [(1, 3), (2, 6)], 6 : []}

INF = int(1e9)
dist = [INF for _ in range(n+1)]
route = ['' for _ in range(n+1)]
q = [(0, stt)]
dist[stt] = 0
route [stt] = '1'

while q:
    cost_accum, node = heappop(q)

    if dist[node] < cost_accum:
        continue

    for cost_dest, dest_node in grp[node]:
        cost_detour = cost_accum + cost_dest
        if  dist[dest_node] > cost_detour:
            dist[dest_node] = cost_detour
            route[dest_node] = route[node] + str(dest_node)
            heappush(q, (cost_detour, dest_node))

print([i if i != INF else -1 for i in dist])
print(route)


