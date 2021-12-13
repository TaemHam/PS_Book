n = int(input())
a = 0
for i in range(0,n+1):
    if i not in [3, 13, 23]:
        a += 15*(60-15) + 15*60
    else:
        a += 60*60
    print(a)
