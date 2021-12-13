import sys
input = sys.stdin.readline
n = int(input().strip())
l = [int(input().strip()) for _ in range(n)]

def q_sort(arr):
    if len(arr) <= 1:
        return arr
    piv = arr[0]
    tail = arr[1:]
    l_side = [i for i in tail if i > piv]
    r_side = [i for i in tail if i <= piv]
    return q_sort(l_side) + [piv] + q_sort(r_side)

for i in q_sort(l):
    print(i)