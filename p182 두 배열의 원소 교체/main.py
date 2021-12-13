n,k = map(int, input().split())
l1 = sorted(list(map(int, input().split())))
l2 = sorted(list(map(int, input().split())))
for i in range(k):
    l1[i],l2[-1-i] = l2[-1-i],l1[i]
print(sum(l1))
