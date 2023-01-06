from random import shuffle, randint
import sys

def arrange(jars,lids):
    low,high=0,len(jars)-1

    pairing(jars,lids,low,high)


#The space complexity of arrange is O(logn) and time complexity is O(nlogn).
# Below is the partition function which places a number in its correct position
# in a list with all elements less than it and greater than it coming before and after the element respectively.
def partition(arr, low, high, pivot):
    i = low
    j = low
    while j < high:
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif (arr[j] == pivot):
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
        j += 1
    arr[i], arr[high] = arr[high], arr[i]

    return i

# The partition function is called with last element of lids acting as pivot for jars.
def pairing(jars, lids,low,high):

    if (low < high):

        pivot = partition(jars, low, high, lids[high])

        partition(lids, low, high, jars[pivot])


        pairing(jars, lids, low, pivot - 1)
        pairing(jars, lids, pivot + 1, high)
    """
    This method cannot compare any lid to any other lid and cannot 
    compare any jar to any other jar.
    The mehod can compare a jar to a lid an vice versa.
    For example, jar[i] < jar[j] is not allowed but jar[i] < lid[j] is allowed
    """
    pass

jars = list({randint(0, sys.maxsize) for i in range(15)})
lids = list(jars)

shuffle(jars)
shuffle(lids)

print(lids)
print(jars)

arrange(jars, lids)

print(jars == lids)
