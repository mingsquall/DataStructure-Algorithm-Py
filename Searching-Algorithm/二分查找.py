def searchDivHalf(data, find_data):
	mid = int((len(data))/2)
	if data[mid] > find_data:
		searchDivHalf(data[:mid],find_data)
	elif data[mid] < find_data:
		searchDivHalf(data[mid:],find_data)
	else:
		print('find %s' % data[mid])

if __name__ == '__main__':
	data = list(range(100))
	searchDivHalf(data, 35)
