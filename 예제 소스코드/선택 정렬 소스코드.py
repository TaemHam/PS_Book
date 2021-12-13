arr = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(arr)):
    min_ind = i
    for j in range(i+1,len(arr)):
        if arr[min_ind] > arr[j]:
            min_ind = j
    arr[i],arr[min_ind] = arr[min_ind],arr[i]

print(arr)
    
    