import sys
n,m = map(int,input().split())
x,y,d = map(int,input().split())
mat = [list(map(int,''.join(list(sys.stdin.readline().split())))) for _ in range(n)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
cnt = ans = 0
while True:
    d = (d+1)%4
    if mat[x][y] == 0:
        mat[x][y] = 2
        ans += 1
    nx = x + dx[d]
    ny = y + dy[d]
    if mat[nx][ny] != 0:
        cnt += 1
        if cnt == 4:
            cnt = 0
            hx = x + dx[(d+2)%4]
            hy = y + dy[(d+2)%4]
            if mat[hx][hy] == 1:
                break
            else:
                x,y = hx,hy
    else:
        x, y = nx, ny
        cnt = 0
print(ans)
