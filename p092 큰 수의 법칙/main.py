n, m, k = map(int,input().split())
l = sorted(list(map(int,input().split())))
m1, m2 = l[-1], l[-2]
a = m1 * ((m//(k+1)*k)+(m%(k+1))) + m2 * (m//(k+1))
print(a)