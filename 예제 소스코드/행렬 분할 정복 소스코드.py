n, m = map(int, input().split())
mod = 100000007
mat_o = [list(map(int, input().split())) for _ in range(n)]
mat_a = [[0] * n for _ in range(n)]
for i in range(n):
    mat_a[i][i] = 1

def mul(a, b):
    return [[sum(a[i][k] * b[k][j] % mod for k in range(len(a))) % mod for j in range(len(a))] for i in range(len(a))]

while m > 0:
    if m % 2:
        mat_a = mul(mat_a, mat_o)
        m -= 1
    mat_o = mul(mat_o, mat_o)
    m //= 2

print(*mat_a, sep='\n')

'''

m번의 움직임으로 이동할 수 있는 경우의 수:

3 4
0 1 1
1 0 1
1 1 0


피보나치 m번째 수:

2 10
0 1
1 1

'''

