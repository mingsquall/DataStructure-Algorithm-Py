#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 问题：检查乱序字符串，我们假设两个字符串具有相等长度，且由26个小写字母集合组成。
# 例如：'heart'与'earth'、'python'与'typhon'，分别都是乱序字符串。
# 目标：写一个布尔函数，将两个字符串作为参数，并返回它们是不是乱序字符串。

# 1 方法1：检查。复杂度O(n^2)。
# 步骤：首先，将第二个字符串转换为列表。其次，检查第一个字符串中的每一个字符是否存在于第二个列表中。如果存在，替换为None。
def Solution1(s1, s2):
    alist = list(s2)

    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1

    return stillOK

print(Solution1('baco', 'ocab'))

# 2 方法2：排序和比较。复杂度与法1有同样的量级
# 步骤：首先，按照字母顺序从a->z排列每个字符串，如果两个字符串相同，则True。但是调用Python的【排序】也是需要成本。

def Solution2(s1, s2):
	alist1 = list(s1)
	alist2 = list(s2)

	alist1.sort()
	alist2.sort()

	pos = 0
	matches = True

	while pos < len(s1) and matches:
		if alist1[pos] == alist2[pos]:
			pos += 1
		else:
			matches = False

	return matches

print(Solution2('abcp', 'pbac'))

# 3 方法3：计数和比较。两个迭代都是n，第三个迭代比较两个计数列表，需要26步。一共T(n)=2n+26。复杂度O(n)。
# 步骤：计算每个字母出现的次数，由于有26个可能的字符，就用一个长度为26的列表，每个可能的字符占一个位置，
# 每次看到一个特定的字符，就增加该位置的计数器。最后，如果两个列表的计数器一样，则字符串为乱序字符串。

def Solution3(s1, s2):
	c1 = [0]*26
	c2 = [0]*26

	for i in range(len(s1)):
		pos = ord(s1[i]) - ord('a')
		c1[pos] = c1[pos] + 1
	for i in range(len(s2)):
		pos = ord(s2[i]) - ord('a')
		c2[pos] = c2[pos] + 1

	j = 0
	stillOK = True
	while j<26 and stillOK:
		if c1[j]==c2[j]:
			j = j + 1
		else:
			stillOK = False
	return stillOK

print(Solution3('apple','pleap'))