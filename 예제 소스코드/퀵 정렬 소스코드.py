arr = [7,5,9,1,3,0,6,2,4,8]

def q_sort(arr):

    if len(arr) <= 1:           # 리스트의 원소가 1개 이하면 끝
        return arr

    pivot = arr[0]
    tail = arr[1:]
    l_side = [i for i in tail if i <= pivot]
    r_side = [i for i in tail if i > pivot]

    return q_sort(l_side) + [pivot] + q_sort(r_side)

print(q_sort(arr))