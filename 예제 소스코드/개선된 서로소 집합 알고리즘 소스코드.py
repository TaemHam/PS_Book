def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    a= find_parent(parent, a)
    b= find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
l = list(range(v+1))

for _ in range(e):
    a, b = map(int,input().split())
    union_find(l, a, b)                                     # 자식 노드들 업데이트 안되어있음 주의

for i in range(1, v+1):
    print(find_parent(l, i), end= ' ')