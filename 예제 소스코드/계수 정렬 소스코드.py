arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

l = [0] * 10

for i in arr:
    l[i] += 1

for i in range(len(l)):
    for j in range(l[i]):
        print(i)
