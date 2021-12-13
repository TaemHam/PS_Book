import sys
from collections import deque
n,m = map(int,input().split())
grp = [list(sys.stdin.readline().strip()) for _ in range(n)]

def dfs(x,y):
    if 0 <= x < n and 0 <= y < m:
        if grp[x][y] == '0':
            grp[x][y] = '1'
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            return True
    return False

cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            cnt += 1

print(cnt)