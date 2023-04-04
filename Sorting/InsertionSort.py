def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):  # i=0 already in sorted sub list
        key=arr[i]

        j=i-1   #compare index

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]  #j sub to j+1  right shift
            j-=1
        arr[j+1]=key

arr = [12, 11, 13, 5, 6]

print("Before sorting : {}".format(arr))
insertionSort(arr)
print("After sorting : {}".format(arr))