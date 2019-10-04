def task_1():
	result = ''
	for i in range(1, 10):
		result += str(i)*i
		result += '\n'
	print(result)
	return result


assert task_1() == '''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
