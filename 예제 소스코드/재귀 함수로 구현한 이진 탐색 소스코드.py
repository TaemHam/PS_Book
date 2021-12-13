n, targ = 10, 7
l = [1,3,5,7,9,11,13,15,17,19]

def bin_search(arr, targ, s, e):

    if s > e:
        return None

    mid = (s + e) // 2
    if arr[mid] == targ:
        return mid

    elif arr[mid] > targ:
        return bin_search(arr,targ,s,mid-1)
    else:
        return bin_search(arr,targ,mid+1,e)

ans = bin_search(l,targ,0,n-1)
if ans == None:
    print('None')
else:
    print(ans + 1)