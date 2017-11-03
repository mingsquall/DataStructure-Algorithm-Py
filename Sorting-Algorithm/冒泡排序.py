"""
冒泡排序的原理非常简单，它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

步骤：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""
def bubbleSort(list):
	for i in range(0, len(list)-1):
		for j in range(1, len(list)-i):
			if list[j-1] > list[j]:
				list[j-1], list[j] = list[j], list[j-1]
	return list

if __name__ == '__main__':
	print(bubbleSort([3,5,1,9,15,10,2,100,54,31]))
