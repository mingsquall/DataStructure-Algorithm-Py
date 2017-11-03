# coding:utf-8

class Node(object):
	"""结点"""
	def __init__(self, item):
		self.elem = item
		self.next = None
		self.prev = None

class DoubleLinkList(object):
	"""双向链表"""
	def __init__(self, node=None):
		self.__head = node

	def is_empty(self):
		"""链表是否为空"""
		return self.__head is None

	def length(self):
		"""链表长度"""
		# cur游标，遍历节点
		cur = self.__head
		count = 0
		while cur != None:
			count += 1
			cur = cur.next
		return count

	def travel(self):
		"""遍历整个链表"""
		cur = self.__head
		while cur != None:
			print(cur.elem, end=" ")
			cur = cur.next
		print("")

	def add(self, item):
		"""链表头部添加元素，头插法"""
		node = Node(item)
		node.next = self.__head
		self.__head = node
		node.next.prev = node

	def append(self, item):
		"""链表尾部添加元素，尾插法"""
		node = Node(item)
		if self.is_empty():
			self.__head = node
		else:
			cur = self.__head
			while cur.next != None:
				cur = cur.next
			cur.next = node
			node.prev = cur

	def insert(self, pos, item):
		"""指定位置添加元素
		:param pos 从0开始
		"""
		if pos <= 0:
			self.add(item)
		elif pos > (self.length()-1):
			self.append(item)
		else:
			node = Node(item)
			cur = self.__head
			count = 0
			while count != pos:
				count += 1
				cur = cur.next
			node.next = cur
			node.prev = cur.prev
			cur.prev.next = node
			cur.prev = node

	def remove(self, item):
		cur = self.__head
		while cur != None:
			if cur.elem is item:
				# 先判断此结点是否是头结点
				# 头结点
				if cur is self.__head:
					self.__head = cur.next
					if cur.next:
						# 判断链表是否只有一个结点，只有一个结点的话，它的next.prev是不存在的
						cur.next.prev = None
				else:
					cur.prev.next = cur.next
					if cur.next:
						cur.next.prev = cur.prev
				break
			else:
				cur = cur.next


	def search(self, item):
		"""查找节点是否存在"""
		cur = self.__head
		while cur != None:
			if cur.elem is item:
				return True
			else:
				cur = cur.next
		return False


if __name__ == '__main__':
	dll = DoubleLinkList()
	print(dll.is_empty())
	print(dll.length())

	dll.append(1)
	print(dll.is_empty())
	print(dll.length())

	dll.append(2)
	dll.add(8)
	dll.append(3)
	dll.append(4)
	dll.append(5)
	dll.append(6)
	dll.insert(-1, 9)
	dll.travel()
	dll.insert(3, 100)
	dll.travel()
	dll.insert(10, 200)
	dll.travel()
	dll.remove(100)
	dll.travel()
	dll.remove(9)
	dll.travel()
	dll.remove(200)
	dll.travel()
	dll.add(13)
	dll.travel()

