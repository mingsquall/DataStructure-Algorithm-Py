"""
Python解决按学生年龄排序问题
问题：定义一个`Class`：包含姓名`name`、性别`gender`、年龄`age`，需要按年龄给学生排序。
输入：包含学生对象的`List`。
输出：按照年龄`age`进行排序好的`List`。

思路1：使用冒泡排序，比较相邻的学生，如果第一个学生的`age`值比第二个学生的`age`值大，那么就整体交换这两个元素。持续每次对越来越少的元素重复上面的步骤。一直到没有任何一对学生需要比较。
思路2：使用Python內建方法`sorted()`。
"""

import time
import random
import string

class Student(object):
	def __init__(self, name, gender, age):
		self.__name = name
		self.__gender = gender
		self.__age = age

	# 取得age属性
	def getAge(self):
		return self.__age

	# 打印
	def printStudent(self):
		return self.__name, self.__gender, self.__age

# 生成包含随机学生对象的list
def generateStudent(num):
	# num为需要生成的测试对象数
	list = []
	for i in range(num):
		randName = ''.join(random.sample(string.ascii_letters, 4))
		randGender = random.choice(['Male', 'FeMale'])
		randAge = random.randint(10,30)
		s = Student(randName, randGender, randAge)
		list.append(s)
	return list

# 冒泡排序
def sortStudent(list):
	for i in range(len(list)):
		for j in range(1, len(list)-i):
			if list[j-1].getAge() > list[j].getAge():
				list[j-1], list[j] = list[j], list[j-1]
	return list

# def ageReturn(list):
# 	return list.age

if __name__ == '__main__':

	# list 形式是[('hZDw', 'FeMale', 17)...]
	list = generateStudent(10000)
	# for j in range(len(list)):
	# 	print(list[j].printStudent())

	# 方法1：使用冒泡排序
	start_Time1 = time.time()
	sortStudent(list)
	end_Time1 = time.time()
	# 方法1中，使用10000个测试数据的排序时间是22.243秒以上（非精确）
	print('%s cost time %s' % ('sortStudent' , end_Time1 - start_Time1))


	# 方法2：使用Python内建的sorted方法+lambda表达式
	# 由于sorted方法背后使用的timsort方法，当数据越接近Ordered data的时候，时间复杂度越接近O(N)。
	# 在这个例子里面，年龄属性是比较接近Ordered data的。
	start_Time2 = time.time()
	sorted(list, key=lambda student: student.getAge()) # 将对象的属性作为排序的Key
	end_Time2 = time.time()
	# 方法2中，使用使用1000000个测试数据的排序时间是0.575秒。虽然不是很精确，但差别显而易见了。
	print('%s cost time %s' % ('sorted' , end_Time2 - start_Time2))
