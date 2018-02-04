# coding:utf-8

def merge_sort(lis):
	n = len(lis)
	if n <= 1:
		return lis
	# 拆分过程
	mid = n // 2
	l_lis = merge_sort(lis[:mid])
	r_lis = merge_sort(lis[mid:])
	lp, rp = 0, 0
	res = []
	# 合并过程
	while lp < len(l_lis) and rp < len(r_lis):
		if l_lis[lp] < r_lis[rp]:
			res.append(l_lis[lp])
			lp += 1
		else:
			res.append(r_lis[rp])
			rp += 1
	# 拼接过程
	res += l_lis[lp:]
	res += r_lis[rp:]

	return res

if __name__ == '__main__':
	lis = [23,12,3,4,1,2,56,77,11,2,3]
	print(lis)
	lis = merge_sort(lis)
	print(lis)
