import sys
input = sys.stdin.readline
n = int(input().strip())
l = []

for i in range(n):
    a = input().split()
    l.append((a[0],int(a[1])))

l = sorted(l, key = lambda x: x[1])
l = [i[0] for i in l]
print (' '.join(l))