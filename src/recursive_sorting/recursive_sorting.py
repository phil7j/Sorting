# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    '''
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # compare smallest of arrA with smallest of arrB
    # Smaller Value gets put into the merged_arr at current iterable
    # Next smallest value gets put into the iterable + 1
    # iterate +2 and do it again
    for i, val in enumerate(merged_arr):
        print(i)
        print(merged_arr)
        if arrA[i] < arrB[i]:
            merged_arr[i] == arrA[i]
            merged_arr[i+1] == arrB[i]
        else:
            merged_arr[i] == arrB[i]
            merged_arr[i+1] == arrA[i]
    '''
    # initialize empty array
    # find which array is longest
    # iterate over longest array
    # compare the two arrays, append smallest value first, and the other value
    # if value of smaller array doesn't exist, just append the value from the longer array
    merged_arr = []
    long_arr = None
    short_arr = None
    # find which arrays and longer or shorter
    if len(arrA) > len(arrB):
        long_arr = arrA
        short_arr = arrB
    else:
        long_arr = arrB
        short_arr = arrA
    for i in range(0, len(long_arr)-1):
        if i > len(short_arr)-1:
            merged_arr.append(long_arr[i])
        elif long_arr[i] < short_arr[i]:
            merged_arr.append(long_arr[i])
            merged_arr.append(short_arr[i])
        else:
            merged_arr.append(short_arr[i])
            merged_arr.append(long_arr[i])
    return merged_arr


print(merge([1, 2, 3], [4, 5, 6]))

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
