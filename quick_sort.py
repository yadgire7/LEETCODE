'''
Given: a list of integers
Goal: To sort the list in ascending order

Algorithm: Merger Sort

Time Complexity: O(n log n)
Sapce Complexity: O(1)   // in place sorting

Approach: Divide and Conquer (Recursion and Backtracking)

Logic: 
1. Choose a pivot element
2. Place the pivot element at its position in the sorted list
3. Place elements smaller than the pivot to the left of the pivot and elements greater than the pivot to the righ of the pivot.

* Placing the pivot element at the right position in the sorted list
    a. after choosing the pivot, set i = low(starting index) and j = high(last index)
    b. check if a[i] > pivot, until then increment i
    c. similarly, check if a[j] < pivot, until then decrement j
    d. check if i < j: swap(a[i], a[j])
    e. swap a[low], a[j]
    f. return jth index(this is the index of pivot in sorted array)
4. Implement quickSort on the left and right side of pivot(jth index) recursively


'''

def partition(a, low, high):
    pivot = a[low]
    i = low
    j = high

    # while i does not cross j
    while i < j:
        while a[i] <= pivot and i <= high - 1:
            i += 1
        while a[j] >= pivot and j >= low + 1:
            j -= 1
        
        if i < j:
            a[i], a[j] = a[j], a[i]
    # final swap
    a[low], a[j] = a[j], a[low]
    return j


def quickSort(a, low, high):
    if low < high:
        p_index = partition(a, low, high)
        quickSort(a, low, p_index - 1)
        quickSort(a, p_index + 1, high)

if __name__ == '__main__':
    a = [2, 1, 4, 2, 7, 4, 5]
    print(f"Unsorted List: {a}")
    quickSort(a, 0, 6)
    print(f"Sorted List: {a}")
