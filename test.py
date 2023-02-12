# 30. Write a Python program to print the following floating numbers upto 2 decimal places. 
def floating_nums(l):
	f_list = [str(each) for each in l]
	new_list = []
	for each in f_list:
		if each.find('.') == -1:
			new_list.append(each + '.00')
		elif len(each.split('.')[1]) > 2:
			new_list.append(each.split('.')[0] + '.' + each.split('.')[1][:2])
		elif len(each.split('.')[1]) == 2:
			new_list.append(each)
		elif len(each.split('.')[1]) == 1:
			new_list.append(each + '0')
	return new_list
# print(floating_nums([10,20.2,30.33,40.444]))

def add_string_before_after(l):
	l1 = []
	for each in l:
		if type(each) == type('s'):
			l1.append(each)
			l1.append(int(each))
		l1.append(each)
	return l1
# print(add_string_before_after([10,'2',1,'4',5]))

def list_comprehension(l):
	x = 10
	# z = [i for i in l if i%2 ==0]
	z = [{i:"even"} if i%2 == 0 else {i:"odd"} for i in l]
	return z
print(list_comprehension([1,4,3,7,8,6]))









