#Helper function to call merge sort
def mergesort(arr,n):
    temp=[0]*n
    return _mergeSort(arr, temp,0, n-1)

#In this function, inv_count will store the total number of transpositions.
def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0

    if left<right:
        mid=(left+right)//2
        inv_count += _mergeSort(arr, temp_arr,left, mid)
        inv_count += _mergeSort(arr, temp_arr, mid+1, right)
        inv_count += merge(arr, temp_arr,left, mid, right)

    return inv_count

def merge(arr, temp_arr, left, mid, right):
    i=left
    j=mid+1
    k=left
    inv_count=0

    #Since an inversion only occurs when an element of left list is greater than element of right list,
    # so all the elements of left list after that element will also be greater than that element of right list
    # as both the lists are sorted.
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:

            # Inversion will occur.
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count

arr=[8,4,2,1]
n=len(arr)
result=mergesort(arr,n)
print("The total number of inversions are",result)