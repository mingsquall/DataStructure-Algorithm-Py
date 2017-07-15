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

# 2 方法2：排序和比较。复杂度
# 步骤：
