pos = input()
cnt = 0
x, y = ord(pos[0]) - 96, int(pos[1])
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0<nx<=8 and 0<ny<=8:
        cnt += 1
print (cnt)
