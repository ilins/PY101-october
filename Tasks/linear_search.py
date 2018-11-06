"""
This module implements some functions based on linear search algo
"""


def min_search(arr) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	min = arr[0]
	for i in range(1,len(arr)):
		if arr[i] < min:
			min = arr[i]
	return min


def min_weight_search(Graph) -> tuple:
	"""
	Function that find edge in graph with minimal weight of all

	:param Graph: NetworkX Graph (or digraph) with weighted edges
	:return: tuple of nodes (node, node) the weight of edge between which is minimal (any occurrence)
	"""


	return None, None