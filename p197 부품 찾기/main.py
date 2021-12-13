import sys
input = sys.stdin.readline
n = int(input().strip())
n_l = sorted(list(map(int,input().split())))
m = int(input().strip())
m_l = list(map(int,input().split()))

def bin_srch(targ, s, e):

    if s > e:
        return 'no'

    mid = (s + e) // 2

    if n_l[mid] == targ:
        return 'yes'

    elif targ < mid:
        bin_srch(targ, s, mid - 1)

    else:
        bin_srch(targ, mid + 1, e)

ans = []
for i in m_l:
    print(bin_srch(i, 0, n-1))




