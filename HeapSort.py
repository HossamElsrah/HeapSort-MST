# Unsorted list of numbers
list_ = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
listsort = []

def swap(arr, i, j):
    """
    Swap the values at positions i and j in the array arr.
    """
    arr[i], arr[j] = arr[j], arr[i]

def max_heapify(arr, n, index):
    """
    Rearrange the binary tree to satisfy the Max Heap property.
    """
    left = 2 * index + 1  # Left child index
    right = 2 * index + 2  # Right child index
    largest = index  # Assume the current index is the largest

    # Check if the left child is larger than the current largest
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if the right child is larger than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the current node is not the largest, swap and continue heapifying
    if largest != index:
        swap(arr, index, largest)
        # Recursively call max_heapify on the affected subtree
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    """
    Transform the list into a Max Heap.
    """
    n = len(arr)
    # Start from the last non-leaf node and work upwards
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    """
    Sort the list using Heap Sort.
    """
    # Build the Max Heap
    build_max_heap(arr)
    
    n = len(arr)
    for i in range(n - 1, 0, -1):
        # Move the largest element (root) to the end of the list
        listsort.append(arr[0])
        swap(arr, 0, i)
        # Reduce the heap size
        n -= 1
        # Restore the Max Heap property
        max_heapify(arr, n, 0)
    
    # Add the last element
    listsort.append(arr[0])

# Execute the algorithm
heap_sort(list_)

# Print the sorted elements
for num in listsort:
    print(num)
