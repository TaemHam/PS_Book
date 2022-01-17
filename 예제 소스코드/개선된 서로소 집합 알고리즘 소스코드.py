def find(x):
    if par[x] != x:
        par[x] = find(par[x])
    return par[x]

def union(a, b):
    a= find(a)
    b= find(b)
    if a < b:
        par[b] = a
    else:
        par[a] = b

v, e = map(int, input().split())
par = list(range(v+1))

for _ in range(e):
    a, b = map(int,input().split())
    union(a, b)                                     # 자식 노드들 업데이트 안되어있음 주의

for i in range(1, v+1):
    print(find(i), end= ' ')