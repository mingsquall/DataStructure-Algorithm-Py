"""
快速排序
思想：冒泡+二分+递归分治

设置pivot作为枢纽，lp、rp两个指针指向左、右两端。
右指针找比pivot小的，左指针找比pivot大的，交换之。
两指针相遇，停止，然后交换pivot与指针对应的数。

tips:为什么先从rp开始扫描?
当pivot是左端点的时候，因为最后两个指针相遇的时候，要交换pivot到相遇的位置，那么这个相遇位置的数一定比pivot要小。
右指针先移动才能找到比pivot小的数。
"""
def quick_sort_basic(arr, left, right):
	if left >= right:
		return arr
	pivot = arr[left]
	lp = left
	rp = right
	while lp < rp:
		while arr[rp] >= pivot and lp < rp:
			rp -= 1
		while arr[lp] <= pivot and lp < rp:
			lp += 1
		arr[rp], arr[lp] = arr[lp], arr[rp]
	arr[left], arr[rp] = arr[rp], arr[left]
	quick_sort_basic(arr, left, lp-1)
	quick_sort_basic(arr, rp+1, right)
	return arr


# 利用Python的list conprehension实现快速排序的例子，短短几行代码，不仅展示出了快速排序的精髓，而且非常pythonic
def pythonic_quick_sort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[-1]
	pivots = [i for i in arr if i == pivot]
	left = pythonic_quick_sort([i for i in arr if i < pivot])
	right = pythonic_quick_sort([i for i in arr if i > pivot])
	return left + pivots + right

def quick_sort(arr):
	if arr:
		below = [i for i in arr[1:] if i < arr[0]]
		above = [i for i in arr[1:] if i >= arr[0]]
		return quick_sort(below) + [arr[0]] + quick_sort(above)
	else:
		return arr

if __name__ == '__main__':
	# Test
	arr = [5,3,1,4,10,7]
	# 方法1
	left = 0
	right = len(arr) - 1
	print(quick_sort_basic(arr, left, right))


	#方法2
	# print(pythonic_quick_sort(arr))
	# print(quick_sort(arr))
