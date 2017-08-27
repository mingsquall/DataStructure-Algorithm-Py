"""
读入一个字符串str，输出字符串str中的连续最长的数字串 
输入描述:
个测试输入包含1个测试用例，一个字符串str，长度不超过255。


输出描述:
在一行内输出str中里连续最长的数字串。

输入例子1:
abcd12345ed125ss123456789

输出例子1:
123456789
"""
import re
def findStr(s):
	reObj = re.compile('\d+')
	nums = reObj.findall(s)
	num = sorted(nums, key = lambda x: len(x), reverse=True)
	return num[0]
print(findStr('abcd12345ed125ss123'))
