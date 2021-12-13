n = int(input())
cnt = 0
c = [500, 100, 50, 10]
for i in c:
    cnt += n//i
    n %= i
print(cnt)