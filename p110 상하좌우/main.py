n = int(input())
cmd = list(input().split())
x,y = 1, 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]
l = ['L','R','U','D']

for i in cmd:
    for j in range(4):
        if i == l[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if 0<nx<=n and 0<ny<=n:
        x,y = nx,ny
print(x,y)


#----------- 내가 짠 코드 ------------
####n = int(input())
####cmd = list(input().split())
####c = [1,1]
####for i in cmd:
    ####if i == 'U' and 0 < c[0]-1:
        ####c[0] -= 1
    ####if i == 'D' and c[0]+1 <= n:
        ####c[0] += 1
    ####if i == 'L' and 0 < c[1]-1:
        ####c[1] -= 1
    ####if i == 'R' and c[1]+1 <= n:
        ####c[1] += 1
####print(c) 
