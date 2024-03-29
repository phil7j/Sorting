# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    i = 0
    j = 0
    len1 = len(arrA)
    len2 = len(arrB)

    merged_arr = []

    while i < len1 and j < len2:
        if arrA[i] < arrB[j]:
            merged_arr.append(arrA[i])
            i = i + 1
        else:
            merged_arr.append(arrB[j])
            j = j + 1
    while i < len1:
        merged_arr.append(arrA[i])
        i = i + 1
    while j < len2:
        merged_arr.append(arrB[j])
        j = j + 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        arr = merge(left, right)

    return arr


print(merge_sort([2, 3, 5, 6, 7, 8, 9, 1]))

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
