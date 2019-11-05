# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        # TO-DO: find next smallest element
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        # TO-DO: swap
        arr[j] = temp
    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    curr_swaps = 1
    # Loop when there was a swap
    while curr_swaps > 0:
        curr_swaps = 0
        for i in range(0, len(arr)-1):
            # Compare
            if arr[i] > arr[i+1]:
                # SWAP
                temp = arr[i+1]
                arr[i+1] = arr[i]
                arr[i] = temp
                curr_swaps += 1
        # Advance to next card
    return arr


print(bubble_sort([4, 3, 2, 12, 1]))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
