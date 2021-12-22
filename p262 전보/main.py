# CP template Version 1.006
import os
import sys
#import string
#from functools import cmp_to_key, reduce, partial
#import itertools
#from itertools import product
#import collections
#from collections import deque
#from collections import Counter, defaultdict as dd
#import math
#from math import log, log2, ceil, floor, gcd, sqrt
from heapq import heappush, heappop
#import bisect
#from bisect import bisect_left as bl, bisect_right as br
DEBUG = False


def main(f=None):
    init(f)
    # sys.setrecursionlimit(10**9)
    # ######## INPUT AREA BEGIN ##########

    n, m, c = map(int,input().split())
    inf = int(1e9)
    dist = [inf for _ in range(n+1)]
    d = dict()
    for i in range(1, n+1):
        d[i] = []
    for _ in range(m):
        x, y, z = map(int, input().split())
        d[x] = d[x] + [(z, y)]
        d[y] = d[y] + [(z, x)]
    
    q = [(0, c)]
    dist[c] = 0

    while q:
        cost, node = heappop(q)

        if dist[node] < cost:
            continue

        for i in d[node]:
            temp_cost = cost + i[0]
            if dist[i[1]] > temp_cost:
                dist[i[1]] = temp_cost
                heappush(q, (temp_cost, i[1]))
    
    ans = [-1, 0]
    for i in dist:
        if i != inf:
            ans[0] += 1
            ans[1] = max(ans[1], i)
    print(*ans)


    

    # ######## INPUT AREA END ############


# TEMPLATE ###############################


enu = enumerate


def For(*args):
    return itertools.product(*map(range, args))


def Mat(h, w, default=None):
    return [[default for _ in range(w)] for _ in range(h)]


def nDim(*args, default=None):
    if len(args) == 1:
        return [default for _ in range(args[0])]
    else:
        return [nDim(*args[1:], default=default) for _ in range(args[0])]


def setStdin(f):
    global DEBUG, input
    DEBUG = True
    sys.stdin = open(f)
    input = sys.stdin.readline


def init(f=None):
    global input
    input = sys.stdin.readline  # by default
    if os.path.exists("o"):
        sys.stdout = open("o", "w")
    if f is not None:
        setStdin(f)
    else:
        if len(sys.argv) == 1:
            if os.path.isfile("in/i"):
                setStdin("in/i")
            elif os.path.isfile("i"):
                setStdin("i")
        elif len(sys.argv) == 2:
            setStdin(sys.argv[1])
        else:
            assert False, "Too many sys.argv: %d" % len(sys.argv)


def pr(*args):
    if DEBUG:
        print(*args)


def pfast(*args, end="\n", sep=' '):
    sys.stdout.write(sep.join(map(str, args)) + end)


def parr(arr):
    for i in arr:
        print(i)


if __name__ == "__main__":
    main()