from bisect import bisect_left as bl
n = int(input().strip())
arr = list(map(int, input().split()))
l_a, l_b = [], []
for i in arr:
    if not l_a or i > l_a[-1]:
        l_a.append(i)
        l_b.append((i, len(l_a)-1))
    else:
        t = bl(l_a, i)
        l_a[t] = i
        l_b.append((i, t))

ans = []
cur = len(l_a) - 1
for i in range(n-1, -1, -1):
    if l_b[i][1] == cur:
        ans.append(l_b[i][0])
        cur -= 1

for i in range(len(ans)-1, -1, -1):
    print(ans[i])

'''

10
10 20 1 10 30 20 2 3 4 50

'''
