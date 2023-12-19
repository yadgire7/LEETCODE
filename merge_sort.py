'''
Given: a list of integers
Goal: To sort the list in ascending order

Algorithm: Merger Sort

Time Complexity: O(n log n)
Sapce Complexity: O(n)   // temporary list to store the sorted list

Approach: Divide and Conquer (Recursion and Backtracking)

Logic: 
1. Divide and Sort:
    a. set low = 0th index and high = last index
    b. divide the given list into two parts (mid = (low + high) / 2 )
    c. implement divide and sort on the new two halves (recursion)
2. Merge
    a. initialize an empty list arr
    b. set a variable left = low and right = right = mid + 1 (both point point to the first elements of the two partitions respectively)
    c. while left <= mid and right <= high:
        i. check if left <= right: arr.append(a[left]), left ++
        ii. else : arr.append(a[right]), right ++
    d. if any one partition is completed, add the other partition as it is to the temporary list
        while left <= mid:
            i. arrr.append(a[left]), left ++
        while right <= high:
            i. arr.append(a[right]), right ++

'''

def merge(a, low, mid, high):
    arr = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if a[left] <= a[right]:
            arr.append(a[left])
            left += 1
        else:
            arr.append(a[right])
            right += 1
    
    # if any one of the partition is appended completely

    while left <= mid:       #right has been appended completely
        arr.append(a[left])
        left += 1
    
    while right <= high:    # left has exhausted
        arr.append(a[right])
        right += 1
    for i in range(low, high + 1):
        a[i] = arr[i - low]


def mergeSort(a, low, high):
    if low == high:
        return
    mid = ( low + high ) // 2

    mergeSort(a, low, mid)
    mergeSort(a, mid + 1, high)
    merge(a, low, mid, high)

if __name__ == '__main__':
    a = [2, 1, 4, 2, 7, 4, 5]
    print(f"Unsorted List: {a}")
    mergeSort(a, 0, 6)
    print(f"Sorted List: {a}")

