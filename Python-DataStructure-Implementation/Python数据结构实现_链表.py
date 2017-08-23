"""
链表的基本构造块是节点。
每个节点对象必须至少保存两个信息：
1.列表项本身（即节点的数据字段）
2.下一个节点的引用
"""
class Node(object):
	def __init__(self, initdata):
		self.data = initdata
		# 引用None代表没有下一节点
		self.next = None
	# 访问数据
	def getData(self):
		return self.data
	# 访问下一节点的引用
	def getNext(self):
		return self.next
	# 修改数据
	def setData(self, newdata):
		self.data = newdata
	# 修改下一节点的引用
	def setNext(self, newnext):
		self.next = newnext

# UnorderedList保持对第一个节点的引用，每个链表对象将维护对链表头部的单个引用
class UnorderedList():
	def __init__(self):
		# 链表头部指代列列表的第一项的第一个节点
		self.head = None

	# 只有在链表中没有节点的时候为真
	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item) # 创建一个新节点并将新项作为数据
		temp.setNext(self.head) # 更改新节点的下一个引用以引用旧链表的第一个节点
		self.head = temp # 重新设置链表的头以引用新节点

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count

	def search(self, item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if previous == None:
			self.head = current.getNext() # 要删除的项目恰好是链表中的第一个项，这时候prev是None，需要改变
		else:
			previous.setNext(current.getNext())



if __name__ == '__main__':
	# init
	myList = UnorderedList()

	myList.add(44)
	myList.add(11)
	myList.add(92)

	print(myList.size()) # 3

	print(myList.remove(44))
	print(myList.remove(11))

	print(myList.search(11)) # None
	print(myList.search(44)) # None

	print(myList.size()) # 1



