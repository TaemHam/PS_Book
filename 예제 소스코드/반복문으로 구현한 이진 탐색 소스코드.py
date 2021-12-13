n,targ = 10,7
l = [1,3,5,7,9,11,13,15,17,19]

def bin_search(arr,targ,s,e):
    while s <= e:

        mid = (s+e) // 2
        if arr[mid] == targ:
            return mid

        elif arr[mid] > targ:
            e = mid - 1
        else:
            s = mid + 1

    return None

ans = bin_search(l,targ,0,n-1)
print(ans+1)