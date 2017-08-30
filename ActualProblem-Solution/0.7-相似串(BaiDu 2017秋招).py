"""
题目描述
									
S和T是两个字符串（它们只由小写字母构成），定义S与T相似当且仅当：
1、S和T长度相同。
2、对于任意两个位置i和j，如果Si和Sj相同，那么Ti和Tj相同；如果Si和Sj不同，那么Ti和Tj不同。
（Si的含义为字符串S在第i个位置的字符，Ti的含义为字符串T在第i个位置的字符）
与字符串”abca”相似的串有”abca”,”cdac”,”zetz”等，现在给出一个字符串S，输出与之相似的字典序最小的串。

输入:
输入只有一行，一个字符串，长度不超过100000，只由小写字母组成。
输出:
输出一行，与之相似的字典序最小的串（只由小写字母组成的串）。

样例输入
helloworld
样例输出
abccdedfcg

"""

def find_similarStr(input_str):
	count = 0
	strObj = 'abcdefghijklmnopqrstuvwxyz'
	mapStr = {}
	result = ''
	for single_str in input_str:
		if single_str not in mapStr:
			mapStr[single_str] = strObj[count]
			count += 1
		result += mapStr[single_str]
	return result
if __name__ == '__main__':
	print(find_similarStr('helloworld'))

