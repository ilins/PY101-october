<<<<<<< HEAD
import numpy as np

# arr = np.array([i for i in range(10)])
# arr = np.array([])

def binary_iter(elem, arr):
    l = 0
    r = len(arr)
    mid = (l + r) // 2
    while arr[mid] != elem:
        if arr[mid] < elem:
            l = mid + 1
        else:
            r = mid - 1
        mid = (l + r) // 2
    return print(mid)

def binary_search(elem, arr, l=0, r=-1):
    if r == -1:
        r = len(arr)
    if l > r or elem < 0:return None
    # if elem not in arr: #decrease from O(logn) to O(nlogn), bad idea use it
    #     return None
    mid = (l + r) // 2
    if mid == elem: return mid
    if arr[mid] < elem:
        return binary_search(elem, arr, l=mid + 1, r=r)
    else:
        return binary_search(elem, arr, l=l, r=mid - 1)
=======
def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	return None
>>>>>>> 0a10cd6c85aa9486d3350e979e6bd177e77e78e6
