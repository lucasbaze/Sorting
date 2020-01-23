# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    i = j = 0
    for k in range(elements):
        if(i >= len(arrA)):
            merged_arr[k] = arrB[j]
            j += 1
        elif(j >= len(arrB)):
            merged_arr[k] = arrA[i]
            i += 1
        elif(arrA[i] < arrB[j]):
            merged_arr[k] = arrA[i]
            i += 1
        elif(arrA[i] > arrB[j]):
            merged_arr[k] = arrB[j]
            j += 1

    return merged_arr

# Conceptually
# Step one... check if the array is length 1, return 
# Then recursively split the array into 1/2s
# We'll do this by splitting the indexes 
# Then at the point in which the array is "sorted" we'll merge them together

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if(len(arr) <= 1):
        return arr
    
    left = arr[:len(arr) // 2]
    right = arr[len(arr) //2:]
        
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    left = arr[start : mid]
    right = arr[mid + 1 : end]

    i = j = 0
    for k in range(start, end + 1):
        if(i >= len(left)):
            arr[k] = right[j]
            j += 1
        elif(j >= len(right)):
            arr[k] = left[i]
            i += 1
        elif(left[i] < right[j]):
            arr[k] = left[i]
            i += 1
        elif(left[i] > right[j]):
            arr[k] = right[j]
            j += 1 

    return arr

# Doesn't pass test... I'm mad... stupid merge sort
def merge_sort_in_place(arr, left, right): 
    # TO-DO
    if(left < right):
        middle = len(arr) // 2
        merge_sort_in_place(arr, left, middle)
        merge_sort_in_place(arr, middle + 1, right)
        merge_in_place(arr, left, middle, last)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
