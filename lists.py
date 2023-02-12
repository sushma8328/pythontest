ssssss
# 1. Write a Python program to sum all the items in a list. 
def addition(l):
	sum = 0
	for each in l:
		sum = sum + each
	return sum
print(addition([10,20,30]))

# 2. Write a Python program to multiply all the items in a list.
def multiply(l):
	sum = 1
	for each in l:
		sum = sum * each
	return sum
# print(multiply([2,3,4]))

# 3. Write a Python program to get the largest number from a list.
def largest_num(l):
	largest_number = l[0]
	for each_number in l[1:]:
		if(each_number > largest_number):
			largest_number = each_number
	return largest_number
# print(largest_num([10,30,20]))

# 4. Write a Python program to get the smallest number from a list.
def smallest_num(l):
	smallest_number = l[0]
	for each_number in l[1:]:
		if(each_number < smallest_number):
			smallest_number = each_number
	return smallest_number
# print(smallest_num([5,3,4,1,2]))

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
# Sample List : 'abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def count_strings(l):
	count = 0
	for each_string in l:
		if(len(each_string) >= 2 and each_string[0] == each_string[-1]):
			count = count + 1 
	return count
# print(count_strings(['abc', 'xyz', 'aba', '1221']))

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
def sort_last_element(l):
	final_list = []
	num_list = []
	for each_tuple in l:
		num_list.append(each_tuple[-1])
	num_list.sort()
	for i in num_list:
		for each in l:
			if each[-1] == i:
				final_list.append(each)
	return final_list
# print(sort_last_element([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# 7. Write a Python program to remove duplicates from a list.
def remove_duplicates(l):
	d = []
	for each in l:
		if each not in d:
			d.append(each)
	return d
# print(remove_duplicates([1,2,4,3,2,1]))

# 8. Write a Python program to check a list is empty or not. 


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.	
def one_comman_member(l1,l2):
	s = False
	for each in l1:
		if each in l2:
			s = True
			break
	return s
# print(one_comman_member([1,3,4],[2,3,5]))

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
def remove_specified_elements(l):
	d = []
	for i in range(len(l)):
		if(i != 0 and i != 4 and i != 5):
			d.append(l[i])
	return d
# print(remove_specified_elements(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']))

# 20. Write a Python program access the index of a list.
def access_index(l):
	s = []
	for  i in range(len(l)):
		s.append((l[i],i))
	return s
# print(access_index([10,20,30]))

# 21. Write a Python program to convert a list of characters into a string. 
def into_string(l):
	s = ''
	for each in l:
		s = s + each
	return s
# print(into_string(['a','b','c','d']))

# 22. Write a Python program to find the index of an item in a specified list. 
def item_index(l,s):
	for i in range(len(l)):
		if l[i] == s:
			return i
	return 'not found'
# print(item_index(['a','b','c','d'],'c'))

# 23. Write a Python program to flatten a shallow list. 
def flatten_list(l1,l2,l3):
	return l1 + l2 + l3
# print(flatten_list([1,10],[2,20],[3,30]))

# 24. Write a Python program to append a list to the second list.
def append_list(l1,l2):
	return l2 + l1
# print(append_list([10,20],['red','pink']))

# 25. Write a Python program to select an item randomly from a list.



# 26. Write a python program to check whether two lists are circularly identical.
def circularly_identical(l1,l2):
	for i in range(len(l1)):
		if l1 == l2[i:len(l2)] + l2[0:i]:
			return 'yes'
	return 'no'
# print(circularly_identical([0,0,10,10,30],[10, 30, 0,0,10]))

# 31. Write a Python program to count the number of elements in a list within a specified range. 
def count_elements(l,s,e):
	return len(l[s:e])
# print(count_elements([10,20,30,'a','b'],2,4))

# 32. Write a Python program to check whether a list contains a sublist.
def is_subslist(source, target):
	attempt_count = 0
	for attempt_count in range(len(target)-len(source)+1):
		found = True
		for i in range(len(source)):
			if source[i] == target[i+attempt_count]:
				continue
			found = False
			break
		if found == True:
			return 'yes'
	return 'no'
# print(is_subslist([4,1,3,6], [4,4,1,3,6,2,3]))

def find_sublist(l,s):
	# import pdb; pdb.set_trace()
	index = None
	sublist = False
	for i in s:
		if index and i == l[index]:
			sublist = True
		elif not index and i in l:
			index = l.index(i)
			sublist = True
		else:
			sublist = False
			break
		index += 1
	if sublist:
		print(True)
	else:
		print(False)
# find_sublist([1,2,3,3,4,5],[3,4])

# 34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
def primes(s):
	prime_numbers = []
	if s == 1:
		return prime_numbers
	if s == 2:
		prime_numbers.append(s)
		return prime_numbers
	prime_numbers.append(2)
	for i in range(3, s):
		is_prime = True
		for j in range(2, i):
			if i%j == 0:
				is_prime = False
				break
		if is_prime:
			prime_numbers.append(i)
	return prime_numbers
# print(primes(1000))	

# 37. Write a Python program to find common items from two lists. 
def common_items(l1,l2):
	l = []
	for each in l1:
		if each in l2:
			l.append(each)
	return l
# print(common_items([1,2,3,4,4],[2,4,5,3,4]))

# 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
def change_position(l):
	final_list = []
	for i in range(len(l)):
		if i % 2 ==0:
			final_list.append(l[i+1])
		else:
			final_list.append(l[i-1])
	return final_list
# print(change_position([0,1,2,3,4,5]))


def change_position2(l):
	for i in range(0, len(l), 2):
		l[i], l[i+1] = l[i+1], l[i]
	return l
# print(change_position2([0,1,2,3,4,5]))

# 39. Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50]
# Expected Output: 113350
def into_single_integer(l):
	s = ''
	for each in l:
		s = s + str(each)
	return int(s)
# print(into_single_integer([11,33,50]))

# 40. Write a Python program to split a list based on first character of word.
def split_based_on_first_char(l): 
	d = {'a':[],'b' : [],'c' : [], 'd' : []}
	for e in l:
		d[e[0]].append(e)
	return d
# print(split_based_on_first_char(['bat','appple','cat','ball','car']))

# 42. Write a Python program to find missing and additional values in two lists. Go to the editor
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h
def missing_and_additional_values(l1,l2):
	missing_values = []
	additional_values = []
	for each in l1:
		if each not in l2:
			missing_values.append(each)
	for each in l2:
		if each not in l1:
			additional_values.append(each)
	return missing_values, additional_values
# print(missing_and_additional_values(['a','b','c','d'],['c','a','e','f']))

# 44. Write a Python program to generate groups of five consecutive numbers in a list.
def list_of_five_numbers(l):
	f_list = []
	start = 0
	for each in range(0,len(l),4):
		f_list.append(l[start:each+4])
		start += 4
	return f_list
# print(list_of_five_numbers([1,2,3,4,5,6,7,8,9,10,11,12]))

# 45. Write a Python program to convert a pair of values into a sorted unique array.
def sorted_unique_array(l):
	s = []
	# import pdb;pdb.set_trace()	
	for each in l:
		for i in each:
			if i not in s:
				s.append(i)
	return s
# print(sorted_unique_array([(1,2),(2,3),(4,1)]))

# 48. Write a Python program to print a nested lists (each list on a new line) using the print() function
def each_list_on_new_line(l):
	for i in l:
		print(i)
# each_list_on_new_line([['red'],[10],['green']])	

# 49. Write a Python program to convert list to list of dictionaries. Go to the editor
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

def list_of_dictionaries(l1,l2):
	s = []
	for each in range(len(l1)):
		s.append({'color_name':l1[each], 'color_code':l2[each]})
	return s 
# print(list_of_dictionaries(['red','pink','green'],['#FF0000','#800000','#FFF000']))

def list_of_dictionaries2(l1,l2):
	s = []
	d = {'color_name':'','color_code':''}
	for each in range(len(l1)):
		d['color_name'] = l1[each]
		d['color_code'] = l2[each]
		s.append(d)
	return s
# print(list_of_dictionaries2(['red','pink','green'],['#FF0000','#800000','#FFF000']))

# 50. Write a Python program to sort a list of nested dictionaries.
def sort_dictionary(l):
	s = []
	for each in l:
		s.append(each['key'])
	s.sort()
	return s 
# print(sort_dictionary([{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]))


C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def list_slice(S, step):
	list1 =[]
	for i in range(step):
		list1.append(S[i::step])
	return list1
# print(list_slice(C,3))


# 52. Write a Python program to compute the difference between two lists. Go to the editor
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# Color1-Color2: ['white', 'orange', 'red']
# Color2-Color1: ['black', 'yellow']
def diff_between_lists(l1,l2):
	l = []
	for each in l1:
		if each not in l2:
			l.append(each)
	return l
# print(diff_between_lists(["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]))

# 54. Write a Python program to concatenate elements of a list. 
def concatenate(l):
	return '-'.join(l)
# print(concatenate(['red','green','orange']))

# 55. Write a Python program to remove key values pairs from a list of dictionaries.
def remove_key_value_pairs(l,key):
	for each in l:
		each.pop(key)
	return l
# print(remove_key_value_pairs([{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}],'key2'))

# 56. Write a Python program to convert a string to a list.
def string_into_list(s):
	l = []
	l.append(s)
	return l
# print(string_into_list('['sushma']'))

# 57. Write a Python program to check if all items of a given list of strings is equal to a given string.
def string_equal_to_list(l,s):
	x = True
	for each in l:
		if each not in s:
			x = False
	return x
# print(string_equal_to_list(['a','b','c'],'abc'))

# 58. Write a Python program to replace the last element in a list with another list. Go to the editor
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
def replace_last_with_list2(l1,l2):
	l1.remove(l1[-1])
	for each in l2:
		l1.append(each)
	return l1
# print(replace_last_with_list2([1,2,3,4,5],[2,3]))

# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
def small_second_index(l):
	d = []
	for each in l:
		d.append(each[1])
	d.sort()
	x = list(set(d))
	return x[1]
# print(small_second_index([(2,3),(1,2),(3,1),(4,2)]))

def sum_of_tuples(l):
	x = []
	for each in l:
		if(sum(each) <= 5):
			x.append(each)
	return x 
# print(sum_of_tuples([(6,1),(2,3),(4,1),(4,2),(3,0)]))

# 61. Write a Python program to create a list of empty dictionaries
def empty_dictionaries(n):
	l = []
	for i in range(n):
		l.append({})
	return l
# print(empty_dictionaries(5))m

# 62. Write a Python program to print a list of space-separated elements. 
def space_seperated_elements(l):
	s = ''
	for i in range(len(l)):
		if i < (len(l) - 1):
			s = s + str(l[i]) + ' '
		else:
			s = s + str(l[i])
	# return s
	return ' '.join(str(e) for e in l)
# print(space_seperated_elements([1,2,3,4,5]))

# 63. Write a Python program to insert a given string at the beginning of all items in a list. Go to the editor
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
def insert_string(l,s):
	x = []
	for each in l:
		x.append(s+str(each))
	return x
# print(insert_string([1,2,3,4,5],'emp'))

# 64. Write a Python program to iterate over two lists simultaneously. 
def iterate_over_lists(l1,l2):
	l = []
	for i in range(len(l1)):
		l.append((l1[i],l2[i]))
	return l
# print(iterate_over_lists(['1','2','3'],['red','green','pink']))

# 65. Write a Python program to move all zero digits to end of a given list of numbers. Go to the editor
# Expected output:
# Original list:
# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:
# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def move_all_zeroes_to_end(l):
	x = []
	each = 0
	for i in range(0,len(l)):
		if l[i] != 0:
			x.append(l[i])
			each+= 1
	for i in range(each,len(l)):
		x.append(0)
	return x
# print(move_all_zeroes_to_end([3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10]))

# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest. Go to the editor
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
def highest_sum_in_list(l):
	highest_sum_list = l[0]
	for each in l:
		if sum(each) > sum(highest_sum_list):
			highest_sum_list = each
	return highest_sum_list
# print(highest_sum_in_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))

# 67. Write a Python program to find all the values in a list are greater than a specified number.
def all_numbers_greaterthan_specified_num(l,specified_number):
	for each in l:
		if(each <= specified_number):
			return False
	return True
# print(all_numbers_greaterthan_specified_num([3,7,5,9,2,8,6,4],2))

# 68. Write a Python program to extend a list without append. Go to the editor
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]
def extend_list_without_append(l1,l2):
	l1[:0] = l2
	return l1
# print(extend_list_without_append([10,20,30],[40,50,60]))

# 69. Write a Python program to remove duplicates from a list of lists. Go to the editor
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]	
def remove_duplicates(l):
	s = []
	# for each_list in l:
	# 	if each_list not in s:
	# 		s.append(each_list)
	# return s
	# # import pdb;pdb.set_trace()
	for each in l[:]:
		for i in each[:]:
			if i not in s:
				s.append(i)
			else:
				each.remove(i)
		if each == []:
			l.remove(each)
	return l
# print(remove_duplicates([[10, 20], [40], [30, 56, 40, 25], [10, 20], [33], [40]]))

# 70. Write a Python program to find the items starts with specific character from a given list. Go to the editor
# Expected Output:
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']
# Items start with d from the said list:
# ['dagfa']
# Items start with w from the said list:
# [x
def starts_with_specific_char(l,s):
	x = []
	for each in l:
		if each[0] == s:
			x.append(each)
	return x
# print(starts_with_specific_char(['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd'],'a'))

# 71. Write a Python program to check whether all dictionaries in a list are empty or not. Go to the editor
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False
def empty_dictionary(l):
	x = {}
	for each in l:
		if each:
			return 'not empty'
	return 'empty'
# print(empty_dictionary([{},{},{}]))

# 72. Write a Python program to flatten a given nested list structure. Go to the editor
# Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
def flatten_list(l):
	x = []
	for each in l:
		if(type(each) == int):
			x.append(each)
		elif(type(each) == list):
			for e in each:
				x.append(e)
	return x 
# print(flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]))

# 73. Write a Python program to remove consecutive duplicates of a given list. Go to the editor
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
def remove_consecutive_duplicates(l):
	if l:
		x = l[0]
		d = [x]
		for i in range(1,len(l)):
			if l[i] != x:
				d.append(l[i])
				x = l[i]
		return d
# print(remove_consecutive_duplicates([2,4,4,5]))

# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists. Go to the editor
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After packing consecutive duplicates of the said list elements into sublists:
# [[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
def consecutive_lists(l):
	d = [[l[0]]]
	for i in range(1,len(l)):
		if l[i] in d[-1]:
		#if l[i] == d[-1][-1]:
			d[-1].append(l[i])
		else:
			d.append([l[i]])
	return d

# print(consecutive_lists([0,1,1,2,3,3,3]))

# 75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4.3, 5, 1]
# List reflecting the run-length encoding from the said list:
# [[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
# Original String:
# automatically
# List reflecting the run-length encoding from the said string:
# [[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]
def run_length_encoding(l):
	count = 1
	s = [[count,l[0]]]
	for i in range(1,len(l)):
		if l[i] == s[-1][-1]:
			count = count + 1
			s[-1][0] = count
		else:
			count = 1
			s.append([count,l[i]])
	return s
# print(run_length_encoding([1, 1, 2, 3, 4, 4.3, 5, 1]))

# 76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
# [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
def run_length_encoding2(l):
	d = [l[0]]
	count = 1
	for i in range(1,len(l)):
		if type(d[-1]) == int:
			if d[-1] == l[i]:
				d[-1] = [2, l[i]]
			else:
				d.append(l[i])
		else:
			if d[-1][-1] == l[i]:
				d[-1][0] = d[-1][0] + 1
			else:
				d.append(l[i])	
	return d 
# print(run_length_encoding2([1, 1, 2, 3, 4, 4, 5, 1]))

# 77. Write a Python program to decode a run-length encoded given list. Go to the editor
# Original encoded list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Decode a run-length encoded said list:
# [1, 1, 2, 3, 4, 4, 5, 1]
def decode_run_length_encoded(l):
	d = []
	for i in range(0,len(l)):
		if type(l[i]) == int:
			d.append(l[i])
		else:
			for e in range(l[i][0]):
				d.append(l[i][-1])
	return d
# print(decode_run_length_encoded([[2, 1], 2, 3, [2, 4], 5, 1]))

# 78. Write a Python program to split a given list into two parts where the length of the first part of the list is given. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Splited the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1])
def split_with_length(l,length):
	return (l[:length],l[length:])
# print(split_with_length([1, 1, 2, 3, 4, 4, 5, 1],4))

# 79. Write a Python program to remove the K'th element from a given list, print the new list. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After removing an element at the kth position of the said list:
# [1, 1, 3, 4, 4, 5, 1]
def k_element(l,num):
	l.remove(l[num-1])
	return l
# print(k_element([1, 1, 2, 3, 4, 4, 5, 1],3))

# 80. Write a Python program to insert an element at a specified position into a given list. Go to the editor
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at kth position in the said list:
# [1, 1, 12, 2, 3, 4, 4, 5, 1]
def insert_element(l,index,element):
	l.insert(index,element)
	return l 
# print(insert_element([1, 1, 2, 3, 4, 4, 5, 1],4,20))

# 89. Write a Python program to Zip two given lists of lists. Go to the editor
# Original lists:
# [[1, 3], [5, 7], [9, 11]]
# [[2, 4], [6, 8], [10, 12, 14]]
# Zipped list:
# [[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
def zip_two_lists(l1,l2):
	for each in l2:
		for e in each:
			for i in l1:
				i.append(e)
	return l1
# print(zip_two_lists([[10,20],[3,4]],[[5,6],[7,8]]))

# 90. Write a Python program to count number of lists in a given list of lists. Go to the editor
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# Number of lists in said list of lists:
# 4
# Original list:
# [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# Number of lists in said list of lists:
# 3
def count_lists(l):
	count =0
	for each in l:
		if type(each) == list:
			count = count + 1
	return count
# print(count_lists([[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]))

# 91. Write a Python program to find the list with maximum and minimum length. Go to the editor
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])
def max_min_list(l):
	max = l[0]
	min = l[0]
	# import pdb;pdb.set_trace()
	for each in l:
		if len(max) < len(each):
			max = each
		if len(min) > len(each):
			min = each
	return (len(max),max),(len(min),min)
# print(max_min_list([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]))

# 92. Write a Python program to check if a nested list is a subset of another nested list. Go to the editor
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# [[1, 3], [13, 15, 17]]
# If the one of the said list is a subset of another.:
# True
# Original list:
# [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# [[[3, 4], [5, 6]]]
# If the one of the said list is a subset of another.:
# False
def subset_of_nested_list(l1,l2):
	for each in l2:
		if each not in l1:
			return False
	return True
# print(subset_of_nested_list( [[1, 3], [5, 7], [9, 11], [13, 15, 17]],[[1, 3], [13, 15, 11, 17]]))

# 93. Write a Python program to count the number of sublists contain a particular element. Go to the editor
# Original list:
# [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# Count 1 in the said list:
# 3
# Count 7 in the said list:
# 2
def element_in_sublist(l,a):
	count = 0
	for each in l:
		if a in each:
			count = count + 1
	return count
# print(element_in_sublist([[1, 3], [5, 7], [1, 11], [1, 15, 7]],11))

# 94. Write a Python program to count number of unique sublists within a given list. Go to the editor
# Original list:
# [[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# Number of unique lists of the said list:
# {(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
def unique_sublists(l):
	d = {}
	count = 0
	for each in l:
		each = tuple(each)
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1
	for e in d:
		if d[e] == 1:
			count = count + 1
	return count
# print(unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]))

# 95. Write a Python program to sort each sublist of strings in a given list of lists. Go to the editor
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
def sort_each_sublist(l):
	l.sort()
	return l
# print(sort_each_sublist([ [2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]))

# 97. Write a Python program to remove sublists from a given list of lists, which contains an element outside a given range. Go to the editor
# Original list:
# [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# After removing sublists from a given list of lists, which contains an element outside the given range:
# [[13, 14, 15, 17]]
def remove_sublists(l,leftrange,rightrange):
	for each in l:
		for e in range(len(each)):
			if(each[e] <= leftrange or each[e] >= rightrange):
				l.remove(each[e])
	return l
# print(remove_sublists([[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [1, 20, 2], [13, 14, 15, 17]],13,30))

# 100. Write a Python program to extract common index elements from more than one given list. Go to the editor
# Original lists:
# [1, 1, 3, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 5, 7]
# [0, 1, 2, 3, 4, 5, 7]
# Common index elements of the said lists:
# [1, 7]
def common_index_elements(a,b,c):
	l = []
	for i in range(len(a)):
		if a[i] == b[i] == c[i]:
			l.append(a[i]) 
	return l
# print(common_index_elements([1, 1, 3, 4, 5, 6, 7],[0, 1, 2, 3, 4, 5, 7],[0, 1, 2, 3, 4, 5, 7]))

# 102. Write a Python program to extract specified size of strings from a give list of string values. Go to the editor
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']
def specified_size_of_strings(l,length):
	d = []
	for each in l:
		if(len(each) == length):
			d.append(each)
	return d
# print(specified_size_of_strings(['Python', 'list', 'exercises', 'practice', 'solution'],8))

# 103. Write a Python program to extract specified number of elements from a given list, which follows each other continuously. Go to the editor
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# Extract 2 number of elements from the said list which follows each other continuously:
# [1, 4]
# Original lists:
# [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
# Extract 4 number of elements from the said list which follows each other continuously:
# [4]
def extract_specified_elements(l):
	x = l[0]
	d = []
	for each in l[1:]:
		if x == each:
			if each not in d:
				d.append(each)
		x = each
	return d
# print(extract_specified_elements( [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]))

# 104. Write a Python program to find the difference between consecutive numbers in a given list. Go to the editor
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# Difference between consecutive numbers of the said list:
# [0, 2, 1, 0, 1, 1, 1]
def diff_between_elements(l):
	x = l[0]
	d = []
	for each in l[1:]:
		if x > each:
			d.append((x-each))
		else:
			d.append((each-x))
		x = each
	return d
# print(diff_between_elements([1, 1, 3, 4, 4, 5, 6, 7]))

# 105. Write a Python program to compute average of two given lists.
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 4, 5, 7, 8]
# Average of two lists:
# 3.823529411764706
def average_of_two_lists(l1,l2):
	return sum(l1)/len(l1)
# print(average_of_two_lists([1, 1, 3, 4, 4, 5, 6, 7],[0, 1, 2, 3, 4, 4, 5, 7, 8]))

# 106. Write a Python program to count integer in a given mixed list. Go to the editor
# Original list:
# [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of integers in the said mixed list:
# 6
def count_integers(l):
	count = 0
	for each in l:
		if isinstance(each, int):
		#if type(each) == type(0):
			count = count + 1
	return count
# print(count_integers([1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]))

# 107. Write a Python program to remove a specified column from a given nested list. Go to the editor
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# After removing 1st column:
# [[2, 3], [4, 5], [1, 1]]
def remove_column(l,rem):
	for each in l:
		del each[rem]
	return l
# print(remove_column([[3,2,3],[3,4,5],[5,1,5]],2))

# 109. Write a Python program to rotate a given list by specified number of items to the right or left direction. Go to the editor
# original List:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Rotate the said list in left direction by 4:
# [4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
# Rotate the said list in left direction by 2:
# [3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
def rotate_list(l,s):
	return l[:s:] + l[:s]
# print(rotate_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2))

# 110. Write a Python program to find the item with maximum occurrences in a given list. Go to the editor
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Item with maximum occurrences of the said list:
# 2
def maximum_occurence(l):
	d = {}
	for each in l:
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1
	max = []
	for k,v in d.items():
		if max:
			if v > max[1]:
				max = [k, v]
		else:
			max = [k, v]
	return max[0]
# print(maximum_occurence([2,1,3,1,2,1])

# 111. Write a Python program to access multiple elements of specified index from a given list. Go to the editor
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
# Index list:
# [0, 3, 5, 7, 10]
# Items with specified index of the said list:
# [2, 4, 9, 2, 1]
def multiple_index(l,ind):
	d = []
	for each in ind:
		d.append(l[each])
	return d
# print(multiple_index([2,4,6,8,10],[0,2,4]))

# 112. Write a Python program to check whether a specified list is sorted or not. Go to the editor
# Original list:
# [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
# Is the said list is sorted!
# True
def sorted_or_not(l):
	x = l[0]
	for each in l[1:len(l)]:
		if x > each:
			return 'list is not sorted'
		x = each
	return 'list is sorted'
# print(sorted_or_not([1,3,5,9,7]))

# 116. Write a Python program to sort a list of lists by a given index of the inner list. Go to the editor
# Original list:
# [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
# Sort the said list of lists by a given index ( Index = 0 ) of the inner list
# [('Beau Turnbull', 94, 98), ('Brady Kent', 97, 96), ('Greyson Fulton', 98, 99), ('Wyatt Knott', 91, 94)]
def sort_by_index(l,ind):

	for each in range(len(l)-1):
		for i in range(0,len(l)-each-1):
			if l[i][ind] > l[i+1][ind]:
				l[i+1], l[i] = l[i], l[i+1]
	return l 
# print(sort_by_index([('Greyson', 98, 99), ('Brady', 97, 96), ('Wyatt', 91, 94), ('Beau', 94, 98)],0))


def bubble_sort(l):
	for i in range(len(l)-1):
		for j in range(0, len(l) - i - 1):
			if l[j] > l[j+1]:
				l[j+1], l[j] = l[j], l[j+1]
	return l
# print(bubble_sort([4,2,8,1]))

# 117. Write a Python program to remove all elements from a given list present in another list. Go to the editor
# Original lists:
# list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2: [2, 4, 6, 8]
# Remove all elements from 'list1' present in 'list2:
# [1, 3, 5, 7, 9, 10]
def remove_list_elements(l,rl):
	for each in rl:
		if each in l:
			l.remove(each)
	return l
# print(remove_list_elements([2,1,4,5,6,8,3,7],[2,4,6,8]))

# 121. Write a Python program to find the nested lists elements which are present in another list. Go to the editor
# Original lists:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Intersection of said nested lists:
# [[12], [7, 11], [1, 5, 8]]
def extract_nested_list_elements(l,nl):
	for each in range(len(nl)):
		for e in nl[each]:
			if e not in l:
				nl[each].remove(e)
	return nl
# print(extract_nested_list_elements([1,2,3,4,5,6],[[2,9],[4,1,8],[6,0,3]]))

# 123. Write a Python program to reverse strings in a given list of string values. Go to the editor
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']
# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
def reverse_strings(l):
	for each in range(len(l)):
		l[each] = l[each][::-1]
	return l
# print(reverse_strings(['Red', 'Green', 'Blue', 'White', 'Black']))

# 124. Write a Python program to find the maximum and minimum product from the pairs of tuple within a given list. Go to the editor
# The original list, tuple :
# [(2, 7), (2, 6), (1, 8), (4, 9)]
# Maximum and minimum product from the pairs of the said tuple of list:
# (36, 8)
def max_min_product_tuple(l):
	max = 0
	min = 0
	for each in l:
		if min == 0:
			min = each[0] * each[1]

		else:
			if min > each[0] * each[1]:
				min =  each[0] * each[1]
		if max < each[0] * each[1]:
			max = each[0] * each[1]
	return (min, max) 
# print(max_min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))

# 125. Write a Python program to calculate the product of the unique numbers of a given list. Go to the editor
# Original List : [10, 20, 30, 40, 20, 50, 60, 40]
# Product of the unique numbers of the said list: 720000000
def product_of_unique_numbers(l):
	x = 1
	for each in set(l):
		x = x * each
	return x
# print(product_of_unique_numbers([10, 20, 30, 40, 20, 50, 60, 40]))

# 126. Write a Python program to interleave multiple lists of the same length. Go to the editor
# Original list:
# list1: [1, 2, 3, 4, 5, 6, 7]
# list2: [10, 20, 30, 40, 50, 60, 70]
# list3: [100, 200, 300, 400, 500, 600, 700]
# Interleave multiple lists:
# [1, 10, 100, 2, 20, 200, 3, 30, 300, 4, 40, 400, 5, 50, 500, 6, 60, 600, 7, 70, 700]
def interleave_multiple_lists(a,b,c):
	l = []
	for i in range(len(a)):
		l.append(a[i])
		l.append(b[i])
		l.append(c[i])
	return l
# print(interleave_multiple_lists([1, 2, 3],[10, 20,30],[100, 200, 300]))

# 127. Write a Python program to remove words from a given list of strings containing a character or string. Go to the editor
# Original list:
# list1: ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
# Character list:
# ['#', 'color', '@']
# New list:
# ['Red', '', 'Green', 'Orange', 'White']
def remove_char_string(l,cl):
	final_list = set()
	for each in l:
		flag = False
		for e in cl:
			if e in each:
				flag = True
				final_list.add(each.split(e)[0].strip())
		if not flag:
			final_list.add(each)
	return final_list
# print(remove_char_string( ['Red color', 'Orange#', 'Green', 'Orange @', 'White'],['#', 'color', '@']))

# 128. Write a Python program to calculate the sum of the numbers in a list between the indices of a specified range. Go to the editor
# Original list:
# [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
# Range: 8 , 10
# Sum of the specified range:
# 29
def sum_of_range(l,x,y):
	s = 0
	for each in range(x,y+1):
		s = s + l[each]
	return s
# print(sum_of_range([2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12],8,10))

# 129. Write a Python program to reverse each list in a given list of lists. Go to the editor
# Original list of lists:
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
# Reverse each list in the said list of lists:
# [[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9], [16, 15, 14, 13]]
def reverse_each_list(l):
	for each in l:
		each.reverse()
	return l
# print(reverse_each_list([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])) 	

# 130. Write a Python program to count the same pair in three given lists. Go to the editor
# Original lists:
# [1, 2, 3, 4, 5, 6, 7, 8]
# [2, 2, 3, 1, 2, 6, 7, 9]
# [2, 1, 3, 1, 2, 6, 7, 9]
# Number of same pair of the said three given lists:
# 3
def count_same_pairs(a,b,c):
	count = 0
	for i in range(len(a)):
		if a[i] == b[i] == c[i]:
			count = count + 1
	return count
# print(count_same_pairs([1,2,4,3],[1,2,3,3],[2,2,4,3]))

# 131. Write a Python program to count the frequency of consecutive duplicate elements in a given list of numbers. Go to the editor
# Original lists:
# [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]
# Consecutive duplicate elements and their frequency:
# ([1, 2, 4, 5], [1, 3, 3, 4])
def count_frequency_of_elements(l):
	d = {}
	m = []
	n = []
	for each in l:
		if each not in d: 
			d[each] = 1
		else:
			d[each] = d[each] + 1
	for k,v in d.items():
		m.append(k)
		n.append(v)
	return (m,n)
# print(count_frequency_of_elements([1,2,2,2,4,4,4,5,5,5,5]))

# 132. Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers. Go to the editor
# Original list:
# [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
# Index positions of the maximum value of the said list:
# 7
# Index positions of the minimum value of the said list:
# 3
def min_max_index(l):
	s = l[:]
	for i in range(len(s)-1):
		for j in range(0,len(s)-i-1):
			if s[j] > s[j+1]:
				s[j+1],s[j] = s[j],s[j+1]
	return (l.index(s[0]),l.index(s[-1])) 
# print(min_max_index([12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]))

# 135. Write a Python program to iterate over all pairs of consecutive items in a given list. Go to the editor
# Original lists:
# [1, 1, 2, 3, 3, 4, 4, 5]
# Iterate over all pairs of consecutive items of the said list:
# [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]



# 138. Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings. Go to the editor
# Original list:
# [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings:
# [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']
def sort_integers_strings(l):
	s = []
	for each in l:
		if type(each) == int:
			s.append(each)
	s.sort()
	for each in l:
		if type(each) == str:
			s.append(each)
	s.sort()
	return s 
# print(sort_integers_strings([19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]))

# 139. Write a Python program to sort a given list of strings(numbers) numerically. Go to the editor
# Original list:
# ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
# Sort the said list of strings(numbers) numerically:
# [-500, -12, 0, 4, 7, 12, 45, 100, 200]
def sort_integers(l):
	s = []
	for each in l:
		s.append(int(each))
	s.sort()
	return s 
# print(sort_integers(['4', '12', '45', '7', '0', '100', '200', '-12', '-500']))

# 142. Write a Python program to sum a specific column of a list in a given list of lists. Go to the editor
# Original list of lists:
# [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
# Sum: 1st column of the said list of lists:
# 12
# Sum: 2nd column of the said list of lists:
# 15
# Sum: 4th column of the said list of lists:
# 9
def sum_of_range(l,s):
	d = []
	# import pdb;pdb.set_trace()
	for i in s:
		sum = 0
		for each in l:
			sum = sum + each[i]
		d.append(sum)
	return d
# print(sum_of_range([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]],[0,1,3]))

# 147. Write a Python program to interleave two given list into another list randomly. Go to the editor
# Original lists:
# [1, 2, 7, 8, 3, 7]
# [4, 3, 8, 9, 4, 3, 8, 9]
# Interleave two given list into another list randomly:
# [4, 1, 2, 3, 8, 9, 4, 3, 7, 8, 9, 8, 3, 7]


# 149. Write a Python program to get all possible combinations of the elements of a given list. Go to the editor
# ['orange', 'red', 'green', 'blue']
# All possible combinations of the said list's elements:
# [[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]

# 153. Write a Python program to check if a given element occurs at least n times in a list. Go to the editor
# Original list:
# [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]
# Check if 3 occurs at least 4 times in a list:
# True
# Check if 0 occurs at least 5 times in a list:
# True
# Check if 8 occurs at least 3 times in a list:
# False
def occurs_atleast(l,n,o):
	d = {}
	for each in l:
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1
	if d[n] >= o:
		return True
	return False
# print(occurs_atleast([0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0],1,4))

# 154. Write a Python program to join two given list of lists of same length, element wise. Go to the editor
# Original lists:
# [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# Join the said two lists element wise:
# [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
def join_two_lists(a,b):
	for i in range(len(a)):
		for e in range(len(b[i])):
			a[i].append(b[i][e])
	return a
# print(join_two_lists([[10, 20], [30, 40], [50, 60], [30, 20, 80]],[[61], [12, 14, 15], [12, 13, 19, 20], [12]]))

# 155. Write a Python program to add two given lists of different lengths, start from left. Go to the editor
# Original lists:
# [2, 4, 7, 0, 5, 8]
# [3, 3, -1, 7]
# Add said two lists from left:
# [5, 7, 6, 7, 5, 8]
def add_lists(a,b):
	d = []
	for i in range(len(a)):
		if i < len(b):
			d.append(a[i] + b[i])
		else:
			d.append(a[i])
	return d
# print(add_lists([2, 4, 7, 0, 5, 8],[3, 3, -1, 7]))

# 156. Write a Python program to add two given lists of different lengths, start from right. Go to the editor
# Original lists:
# [2, 4, 7, 0, 5, 8]
# [3, 3, -1, 7]
# Add said two lists from left:
# [2, 4, 10, 3, 4, 15]



# 157. Write a Python program to interleave multiple given lists of different lengths. Go to the editor
# Original lists:
# [2, 4, 7, 0, 5, 8]
# [2, 5, 8]
# [0, 1]
# [3, 3, -1, 7]
# Interleave said lists of different lengths:
# [2, 2, 0, 3, 4, 5, 1, 3, 7, 8, -1, 0, 7, 5, 8]


# 160. Write a Python program to remove first specified number of elements from a given list satisfying a condition. Go to the editor
# Remove the first 4 number of even numbers from the following list:
# [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
# Output:
# [3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]
def remove_even_upto_range(l,r):
	for each in l:
		count = 0
		if each % 2 == 0:
			count = count + 1
			l.remove(each)
			if count == r:
				break;
	return l
# print(remove_even_upto_range([3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5],4))

# 161. Write a Python program to check if a given list is strictly increasing or not. Moreover, If removing only one element from the list results in a strictly increasing list, we still consider the list true. Go to the editor
# True
# True
# True


# 162. Write a Python program to find the last occurrence of a specified item in a given list. Go to the editor
# Original list:
# ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# Last occurrence of f in the said list:
# 7


# 165. Write a Python program to split a given list into specified sized chunks. Go to the editor
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the said list into equal size 3
# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
def split_into_specified_size(l,n):
	s = []
	for i in range(0,len(l),n):
		s.append(l[i:i+n])
		i = i+n
	return s
# print(split_into_specified_size([12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83],4))

# 167. Write a Python program to convert a given list of strings into list of lists. Go to the editor
# Original list of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]
def string_into_lists(l):
	s = []
	for each in l:
		s.append(list(each))
	return s
# print(string_into_lists(['Red', 'Maroon', 'Yellow', 'Olive']))

# 168. Write a Python program to display vertically each element of a given list, list of lists. Go to the editor
# Original list:
# ['a', 'b', 'c', 'd', 'e', 'f']
# Display each element vertically of the said list:
# a
# b
# c
# d
# e
# f
def display_vertically_each_element(l):
	for each in l:
		print(each)
# display_vertically_each_element(['a', 'b', 'c', 'd', 'e', 'f'])

# 169. Write a Python program to convert a given list of strings and characters to a single list of characters. Go to the editor
# Original list:
# ['red', 'white', 'a', 'b', 'black', 'f']
# Convert the said list of strings and characters to a single list of characters:
# ['r', 'e', 'd', 'w', 'h', 'i', 't', 'e', 'a', 'b', 'b', 'l', 'a', 'c', 'k', 'f']
def strings_into_characters(l):
	s = []
	for each in l:
		for i in range(len(each)):
			s.append(each[i])
	return s
# print(strings_into_characters(['red', 'white', 'a', 'b', 'black', 'f']))

# 170. Write a Python program to insert an element in a given list after every nth position. Go to the editor
# Original list:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# Insert a in the said list after 2 nd element:
# [1, 2, 'a', 3, 4, 'a', 5, 6, 'a', 7, 8, 'a', 9, 0]
def insert_element_at_nth_position(l,e,n):
	s = []
	for each in range(0,len(l),n):
		s.extend(l[each:each+n])
		s.append(e)
	s.pop()
	return s
# print(insert_element_at_nth_position([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],'a',4))

# 171. Write a Python program to concatenate element-wise three given lists. Go to the editor
# Original lists:
# ['0', '1', '2', '3', '4']
# ['red', 'green', 'black', 'blue', 'white']
# ['100', '200', '300', '400', '500']
# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']
def concate_element_wise(a,b,c):
	s = []
	for i in range(len(a)):
		s.append(a[i]+b[i]+c[i])
	return s
# print(concate_element_wise(['0','1'],['a','b'],['10','20']))

# 172. Write a Python program to remove the last N number of elements from a given list. Go to the editor
# Original lists:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
# Remove the last 3 elements from the said list:
# [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]
def remove_last_n_elements(l,n):
	return l[:-n]
# print(remove_last_n_elements([2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5],1))

# 173. Write a Python program to merge some list items in given list using index value. Go to the editor
# Original lists:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Merge items from 2 to 4 in the said List:
# ['a', 'b', 'cd', 'e', 'f', 'g']	
def merge_some_items(l,s,n):
	d = []
	for i in range(len(l)):
		if i > s and i < n:
			d[-1] = d[-1] + l[i]
		else:
			d.append(l[i])
	return d
# print(merge_some_items(['a', 'b', 'c', 'd', 'e', 'f', 'g'],3,7))

# 175. Write a Python program to find the minimum, maximum value for each tuple position in a given list of tuples. Go to the editor
# Original list:
# [(2, 3), (2, 4), (0, 6), (7, 1)]
# Maximum value for each tuple position in the said list of tuples:
# [7, 6]
# Minimum value for each tuple position in the said list of tuples:
# [0, 1]
def min_max_each_tuple(l):
	min1 = False
	min2 = False
	max1 = 0
	max2 = 0
	for each in l:
		if min1 == False:
			min1 = each[0]	
		elif min1 > each[0]:
			min1 = each[0]
		if min2 == False:
			min2 = each[1]
		elif min2 > each[1]:
			min2 = each[1]
		if max1 < each[0]:
			max1 = each[0]
		if max2 < each[1]:
			max2 = each[1]
	return[min1,min2],[max1,max2]
# print(min_max_each_tuple([(2, 3), (2, 4), (0, 6), (7, 1)]))

# 176. Write a Python program to create a new list dividing two given lists of numbers. Go to the editor
# Original list:
# [7, 2, 3, 4, 9, 2, 3]
# [9, 8, 2, 3, 3, 1, 2]
# [0.7777777777777778, 0.25, 1.5, 1.3333333333333333, 3.0, 2.0, 1.5]
def dividing_lists(a,b):
	l = []
	for i in range(len(a)):
		l.append(a[i]/b[i])
	return l 
# print(dividing_lists([7, 2, 3, 4, 9, 2, 3],[9, 8, 2, 3, 3, 1, 2]))

# 179. Write a Python program to create the largest possible number using the elements of a given list of positive integers. Go to the editor
# Original list:
# [3, 40, 41, 43, 74, 9]
# Largest possible number using the elements of the said list of positive integers:
# 9744341403


# 180. Write a Python program to create the smallest possible number using the elements of a given list of positive integers. Go to the editor
# Original list:
# [3, 40, 41, 43, 74, 9]
# Smallest possible number using the elements of the said list of positive integers:
# 3404143749

# 184. Write a Python program to form Bigrams of words in a given list of strings.
# ['Sum all the items in a list', 'Find the second smallest number in a list']
# Bigram sequence of the said list:
# [('Sum', 'all'), ('all', 'the'), ('the', 'items'), ('items', 'in'), ('in', 'a'), ('a', 'list'), ('Find', 'the'), ('the', 'second'), ('second', 'smallest'), ('smallest', 'number'), ('number', 'in'), ('in', 'a'), ('a', 'list')]
def bigrams(l):
	d = []
	for each in l:
		' '.join(',')
		for e in range(len(each)):
			d.append((each[e],each[e+1]))
	return d

# print(bigrams(['Sum all the items in a list', 'Find the second smallest number in a list']))

# 186. Write a Python program to swap two sublists in a given list. Go to the editor
# Original list:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Swap two sublists of the said list:
# [0, 6, 7, 8, 9, 3, 4, 5, 1, 2, 10, 11, 12, 13, 14, 15]
def swap_two_sublists(l):
	l[6:10],l[1:3] = l[1:3],l[6:10]
	l[1:3],l[4:6] = l[4:6],l[1:3]
	return l
# print(swap_two_sublists([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))

# 187. Write a Python program to convert a given list of tuples to a list of strings. Go to the editor
# Original list of tuples:
# [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
# Convert the said list of tuples to a list of strings:
# ['red green', 'black white', 'orange pink']
def tuples_into_strings(l):
	d = []
	for each in l:
		d.append(each[0]+' '+each[1])
	return d
# print(tuples_into_strings([('red', 'green'), ('black', 'white'), ('orange', 'pink')]))

# 188. Write a Python program to sort a given list of tuples on specified element. Go to the editor
# Original list of tuples:
# [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
# Sort on 1st element of the tuple of the said list:
# [('item1', 11, 24.5), ('item2', 10, 10.12), ('item3', 15, 25.1), ('item4', 12, 22.5)]
def sort_specified_element(l,n):
	for i in range(len(l)-1):
		for j in range(0,len(l)-i-1):
			if l[j][n-1] > l[j+1][n-1]:
				l[j+1],l[j] = l[j],l[j+1]
	return l
# print(sort_specified_element([('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)],1))

# 190. Write a Python program to find the specified number of largest products from two given list, multiplying an element from each list. Go to the editor
# Original lists:
# [1, 2, 3, 4, 5, 6]
# [3, 6, 8, 9, 10, 6]
# 3 Number of largest products from the said two lists:
# [60, 54, 50]
# 4 Number of largest products from the said two lists:
# [60, 54, 50, 48]



# 192. Write a Python program to remove all strings from a given list of tuples. Go to the editor
# Original list:
# [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]
# Remove all strings from the said list of tuples:
# [(100,), (80,), (90,), (88, 89), (90, 92)]
def remove_strings(l):
	d = []
	for each in l:
		s = []
		for e in each:
			if type(e) != str:
				s.append(e)
		s=tuple(s)
		d.append(s)
	return d
# print(remove_strings([(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]))

# 193. Write a Python program to find the dimension of a given matrix. Go to the editor
# Original list:
# [[1, 2], [2, 4]]
# Dimension of the said matrix:
# (2, 2)
def dimension_of_matrix(l):
	for each in l:
		return(len(l),len(each))
# print(dimension_of_matrix([[1, 2], [2, 4],[5, 6]]))

# 194. Write a Python program to sum two or more lists, the lengths of the lists may be different. Go to the editor
# Original list:
# [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]
# Original list:
# [[1], [2, 4, 4], [1, 2], [4]]
# Sum said lists with different lengths:
# [8, 6, 4]
def sum_of_different_lists(l):
	for each in l:
		pass
# print(sum_of_different_lists([[1, 2, 4], [2, 4, 4], [1, 2]]))

# 195. Write a Python program to traverse a given list in reverse order, also print the elements with original index. Go to the editor
# Original list:
# ['red', 'green', 'white', 'black']
# Traverse the said list in reverse order:
# black
# white
# green
# red
def reverse_order(l):
	i =len(l)-1
	while i>=0:
		print(i,l[i])
		i = i - 1
reverse_order(['red', 'green', 'white', 'black'])

# 198. Write a Python program to compare two given lists and find the indices of the values present in both lists. Go to the editor
# Original lists:
# [1, 2, 3, 4, 5, 6]
# [7, 8, 5, 2, 10, 12]
# Compare said two lists and get the indices of the values present in both lists:
# [1, 4]
def same_element_indices(a,b):
	l = []
	for i in range(len(a)):
		if a[i] in b:
			l.append((a.index(a[i]),b.index(a[i])))
			# return [a.index(a[i]),b.index(a[i])]
	return l
# print(same_element_indices([1, 2, 3, 4, 5, 6],[7, 8, 5, 2, 10, 12]))

# 199. Write a Python program to convert a given unicode list to a list contains strings. Go to the editor
# Original lists:
# ['S001', 'S002', 'S003', 'S004']
# Convert the said unicode list to a list contains strings:
# ['S001', 'S002', 'S003', 'S004']


# 203. Write a Python program to join adjacent members of a given list. Go to the editor
# Original list:
# ['1', '2', '3', '4', '5', '6', '7', '8']
# Join adjacent members of a given list:
# ['12', '34', '56', '78']
def join_adjacent_elements(l):
	d = []
	for i in range(len(l)-1):
		d.append(l[i] + l[i+1])
		i = i + 2
	return d
# print(join_adjacent_elements(['1', '2', '3', '4', '5', '6', '7', '8']))

# 209. Write a Python program to count the number of groups of non-zero numbers separated by zeros of a given list of numbers. Go to the editor
# Original list:
# [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]
# Number of groups of non-zero numbers separated by zeros of the said list: 4
def number_of_non_zero_groups(l):
	pass
# print(number_of_non_zero_groups([1,2,3,0,0,0,4,5,6,0,0,0,7,8,9]))

# 210. Write a Python program to compute the sum of non-zero groups (separated by zeros) of a given list of numbers. Go to the editor
# Original list:
# [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]
# Compute the sum of non-zero groups (separated by zeros) of the said list of numbers: [15, 38, 15, 27]
def sum_of_non_zero_groups(l):
	pass
# print(sum_of_non_zero_groups([1,2,3,0,0,0,4,5,6,0,0,0,7,8,9]))

# 220. Write a Python program to map the values of a list to a dictionary using a function, where the key-value pairs consist of the original value as the key and the result of the function as the value. Go to the editor
# Sample Output:
# {1: 1, 2: 4, 3: 9}
def map_values_to_dictionary(l):
	d = {}
	for each in l:
		d[each] = each * each
	return d
# print(map_values_to_dictionary([1,2,3]))

# 221. Write a Python program to randomize the order of the values of an list, returning a new list. Go to the editor
# Sample Output:
# Original list: [1, 2, 3, 4, 5, 6]
# Shuffle the elements of the said list:
# [3, 2, 4, 1, 6, 5]
def randomize_order(l):
	pass
# print(randomize_order([1, 2, 3, 4, 5, 6]))

# 222. Write a Python program to get the difference between two given lists, after applying the provided function to each list element of both. Go to the editor
# Sample Output:
# [1.2]
# [{'x': 2}]
def difference_between_two_lists(a,b):
	pass
# print(difference_between_two_lists([2.1,1.2], [2.3,3.4]))

# 223. Write a Python program to create a list with the non-unique values filtered out. Go to the editor
# Sample Output:
# [1, 3, 5]
def non_unique_values(l):
	d = {}
	s = []
	for each in l:
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1
	for k in d:
		if d[k] > 1:
			s.append(k)
	return s
# print(non_unique_values([1,2,2,3,4,4,5]))

# 225. Write a Python program to retrieve the value of the nested key indicated by the given selector list from a dictionary or list. Go to the editor
# Sample Output:
# Harwood
# 2
def nested_key(users,freddy,name,last):
	return users[freddy][name][last]

# print(nested_key({
#   'freddy': {
#     'name': {
#       'first': 'Fateh',
#       'last': 'Harwood' 
#     },
#     'postIds': [1, 2, 3]
#   }
# },'freddy','postIds',2))


# 226. Write a Python program to get a list of elements that exist in both lists, after applying the provided function to each list element of both. Go to the editor
# Sample Output:
# [2.1]
def elements_in_both_lists(a,b):
	pass
# print(elements_in_both_lists([2.1,1.2], [2.3,3.4]))

# 227. Write a Python program to get the symmetric difference between two lists, after applying the provided function to each list element of both. Go to the editor
# Sample Output:
# [1.2, 3.4]
def symmetric_difference2(a,b):
	l = []
	pass
	return l
# print(symmetric_difference2([2.1,1.2],[2.3,3.4]))

# 228. Write a Python program to get every element that exists in any of the two given lists once, after applying the provided function to each element of both. Go to the editor
# Sample Output:
# [2.2, 4.1]
def element_in_two_lists_once(a,b):
	l = []
	for i in range(len(a)):
		l.append(a[i])
		l.append(b[i])
		return l
# print(element_in_two_lists_once([2.2][4.1,4.3]))

# 230. Write a Python program to find the indexes of all elements in the given list that satisfy the provided testing function. Go to the editor
# Sample Output:
# [0, 2]
def index_of_all_elements(l):
	d = []
	for each in l:
		if each % 2 == 1:
			d.append(l.index(each))
	return d
# print(index_of_all_elements([1,2,3,4]))

# 231. Write a Python program to split values into two groups, based on the result of the given filter list. Go to the editor
# Sample Output:
# [['red', 'green', 'pink'], ['blue']]
def split_values_into_groups(a,b):
	# d = {}
	# s = []
	# l = []
	# for i in range(len(a)):
	# 	d[a[i]] = a[i]
	# 	d[a[i]] = b[i]
	# 	if d[a[i]] == 1:
	# 		s.append(a[i])
	# 	else:
	# 		l.append(s)
	# 		if d[a[i]] == 0:
	# 	 		l.append([a[i]])

	d = {}
	for i in range(len(b)):
		if b[i] not in d:
			d[b[i]] = [a[i]]
		else:
			d[b[i]].append(a[i])
	return d.values()
# print(split_values_into_groups(['a','b','c','d'],[1,1,0,1]))

# 234. Write a Python program to convert a given number (integer) to a list of digits. Go to the editor
# Sample Output:
# [1, 2, 3]
# [1, 3, 4, 7, 8, 2, 3]
def integer_into_list_of_digits(l):
	d = []
	for i in range(len(l[0])):
		d.append(int(l[0][i]))
	return d
# print(integer_into_list_of_digits(['1347823']))

# 235. Write a Python program to find the index of the last element in the given list that satisfies the provided testing function. Go to the editor
# Sample Output:
# 2
def index_of_last_element(l):
	d = []
	for each in l:
		if each % 2 == 1:
			d.append(each)
	return len(d)
# print(index_of_last_element([1,2,3,4]))

# 236. Write a Python program to find the items that are parity outliers in a given list. Go to the editor
# Sample Output:
# [1, 3]
# [2, 4, 6]
def even_or_odd(l):
	d = []
	for each in l:
		if each % 2 != 0:
			d.append(each)
	return d
# print(even_or_odd([1,2,3,4]))

# 237. Write a Python program to convert a given list of dictionaries into a list of values corresponding to the specified key. Go to the editor
# Sample Output:
# [8, 36, 34, 10]
def dictionary_values_into_list(l):
	d = []
	for each in l:
		for k in each:
			if type(each[k]) == int:
				d.append(each[k])
	return d
# print(dictionary_values_into_list([{'a':1},{'b':'boom'},{'c':3}]))

# 238. Write a Python program to calculate the average of a given list, after mapping each element to a value using the provided function. Go to the editor
# Sample Output:
# 5.0
# 15.0
def average_of_list(l):
	s = 0
	for each in l:
		for e in each:
			s = s + each[e]
	return float(s/len(l))
# print(average_of_list([{'n':4}, {'n':2}, {'n':8}, {'n':6}]))

# 239. Write a Python program to find the value of the first element in the given list that satisfies the provided testing function. Go to the editor
# Sample Output:
# 1
# 2
def value_of_first_element(l):
	for each in l:
		if each % 2 != 0:
			return each
# print(value_of_first_element([2,1,3,4]))

# 240. Write a Python program to find the value of the last element in the given list that satisfies the provided testing function. Go to the editor
# Sample Output:
# 3
# 4
def value_of_last_element(l):
	s = 0
	for each in l:
		if each % 2 != 0:
			s= each
	return s
# print(value_of_last_element([1,2,3,4]))

# 242. Write a Python program to get the symmetric difference between two iterables, without filtering out duplicate values. Go to the editor
# Sample Output:
# [30, 40]
def symmetric_difference(a,b):
	l = []
	for each in a:
		if each not in b:
			l.append(each)
	for each in b:
		if each not in a:
			l.append(each)
	return l
# print(symmetric_difference([10,20,30],[10,20,40]))

# 243. Write a Python program to check if a given function returns True for every element in a list. Go to the editor
# Sample Output:
# True
# False
# False
def returns_true_or_false(l):
	for each in l:
		if(each < 1):
			return False
	return True
# print(returns_true_or_false([1,2,3,4,5]))

# 244. Write a Python program to initialize a list containing the numbers in the specified range where start and end are inclusive and the ratio between two terms is step. Returns an error if step equals 1. Go to the editor
# Sample Output:
# [1, 2, 4, 8, 16, 32, 64, 128, 256]
# [3, 6, 12, 24, 48, 96, 192]
# [1, 4, 16, 64, 256]
def stepping(start,end,step):
	l = []
	while(start<end):
		l.append(start)
		start = start * step
	return l
# print(stepping(1,1000,2))

# 248. Write a Python program to get the maximum value of a list, after mapping each element to a value using a given function. Go to the editor
# Sample Output:
# 8
def max_value(l):
	d = 0
	for each in l:
		for e in each:
			if each[e] > d:
				d = each[e]
	return d
# print(max_value([{'a':7},{'b':3},{'c':9},{'d':4}]))

# 250. Write a Python program to calculate the sum of a list, after mapping each element to a value using the provided function. Go to the editor
# Sample Output:
# 20
def sum_of_values(l):
	s = 0
	for each in l:
		for e in each:
			s = s + each[e]
	return s
# print(sum_of_values([{'a':5},{'b':8},{'c':7}]))

# 252. Write a Python program to get the n maximum elements from a given list of numbers.
# Original list elements:
# [1, 2, 3]
# Two maximum values of the said list: [3, 2]
def n_maximum_elements(l,n):
	l.sort()
	return l[n:]
# print(n_maximum_elements([3,1,4,5,2,6],3))

# 254. Write a Python program to get the weighted average of two or more numbers. Go to the editor
# Sample Output:
# Original list elements:
# [10, 50, 40]
# [2, 5, 3]
# Weighted average of the said two list of numbers:
# 39.0
def weighted_average(l):
	pass
# print(weighted_average([10, 50, 40]))

# 255. Write a Python program to perform a deep flattens a list. Go to the editor
# Sample Output:
# Original list elements:
# [1, [2], [[3], [4], 5], 6]
# Deep flatten the said list:
# [1, 2, 3, 4, 5, 6]
def deep_flattens_a_list(l):
	for each in l:
		pass
# print(deep_flattens_a_list([1, [2], [[3], [4], 5], 6]))

# 256. Write a Python program to get the powerset of a given iterable. Go to the editor
# Sample Output:
# Original list elements:
# [1, 2]
# Powerset of the said list:
# [(), (1,), (2,), (1, 2)]
def powerset_of_iterable(l):
	pass
# print(powerset_of_iterable([1, 2]))

# 257. Write a Python program to check if two given lists contain the same elements regardless of order. Go to the editor
# Sample Output:
# Original list elements:
# [1, 2, 4]
# [2, 4, 1]
# Check two said lists contain the same elements regardless of order!
# True
def two_lists_contain_same_elements(a,b):
	for each in a:
		if each in b:
			b.remove(each)
		else:
			return 'not same elements'
	return 'same elements'	
# print(two_lists_contain_same_elements([1, 2, 4],[2, 4, 1]))

# 264. Write a Python program to create a two-dimensional list from given list of lists. Go to the editor
# Sample Output:
# [(1, 4, 7, 10), (2, 5, 8, 11), (3, 6, 9, 12)]
# [(1, 4), (2, 5)]
def two_dimensional_list(l):
	d = []
	for i in range(len(l)):
		for e in range(len(l[i])):
			d.append(l[i][e])
	return d
# print(two_dimensional_list([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))

# 265. Write a Python program to generate a list, containing the Fibonacci sequence, up until the nth term. Go to the editor
# Sample Output:
# First 7 Fibonacci numbers:
# [0, 1, 1, 2, 3, 5, 8, 13]
global_list = [0, 1]
def fibonacci_numbers(end):
	### solution 1
	if end < len(global_list):
		return global_list[end]
	else:
		global_list.append(fibonacci_numbers(end-1) + fibonacci_numbers(end-2))
		return global_list[end]
# fibonacci_numbers(9)
# print(global_list)

	### solution 2
	# def nth_fib(n):
	# 	if n == 0:
	# 		return 0
	# 	elif n in [1, 2]:
	# 		return 1
	# 	else:
	# 		return nth_fib(n-1) + nth_fib(n-2)
	# l = []
	# for i in range(end):
	# 	l.append(nth_fib(i))
	# return l

	### solution 3
	# n1 = 0
	# n2 = 1
	# count = 0
	# while(count < end):
	# 	print(n1)
	# 	nth = n1 + n2
	# 	n1 = n2
	# 	n2 = nth
	# 	count += 1
#print(fibonacci_numbers(7))

# 267. Write a Python program to get the cumulative sum of the elements of a given list. Go to the editor
# Sample Output:
# Original list elements:
# [1, 2, 3, 4]
# Cumulative sum of the elements of the said list:
# [1, 3, 6, 10]
def cumulative_sum(l):
	d = []
	for i in range(len(l)):
		d.append(sum(l[:i+1]))
	return d
# print(cumulative_sum([1, 2, 3, 4]))

# 275. Write a Python program to add all elements of a list of integers except the number at index. Return the new string. Go to the editor
# Sample Data:
# ([0, 9, 2, 4, 5, 6] -> [26, 17, 24, 22, 21, 20]
# ([-4, 0, 6, 1, 0, 2]) -> [9, 5, -1, 4, 5, 3]
# ([1, 2, 3]) -> [5, 4, 3]
# ([-4, 0, 5, 1, 0, 1]) -> [7, 3, -2, 2, 3, 2]
def add_all_except_same_index_element(l):
	d = []
	for i in range(len(l)):
		d.append(sum(l)-l[i])
	return d
# print(add_all_except_same_index_element([0, 9, 2, 4, 5, 6]))

# 277. Write a Python program to calculate the largest and gap lowest between sorted elements of a list of integers. Go to the editor
# Sample Data:
# {1, 2 ,9, 0, 4, 6} -> 3
# {23, -2, 45, 38, 12, 4, 6} -> 15
def large_gap_lowest_gap(l):
	l=list(l)
	l.sort()
	return l[1] - l[0],l[len(l)-1] - l[len(l)-2]
# print(large_gap_lowest_gap({1, 2 ,9, 0, 4, 6}))

# 279. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False. Go to the editor
# Sample Data:
# ([0, 3, 4, 7, 9]) -> False
# ([3, 5, 7, 13]) -> True
# ([1, 5, 3]) -> False
def not_prime_false(l):
	for each in l:
		pass
# print(not_prime_false([0, 3, 4, 7, 9]))

# 280. Write a Python program to extract the first specified number of vowels from a given string. If the specified number is less than number of vowels present in the string then display "n is less than number of vowels present in the string". Go to the editor
# Sample Data:
# ("Python", 2) -> "n is less than number of vowels present in the string."
# ("Python Exercises", 3) -> "oEe"
# ("aeiou") -> "AEI"
def specified_number_of_vowels(l,n,vowel):
	s = ''
	for i in range(len(l)):
		if l[i] in vowel:
			s = s + l[i]
	if n > len(s):
		return "n is less than number of vowels present in the string."
	return s[:n]
# print(specified_number_of_vowels("aeiou", 3,'AaEeIiOoUu'))

# 281. Write a Python program that takes a list of integers and finds all pairs of integers that differ by three. Return all pairs of integers in a list. Go to the editor
# Sample Data:
# ([0, 3, 4, 7, 9]) -> [[0, 3], [4, 7]]
# [0, -3, -5, -7, -8] -> [[-3, 0], [-8, -5]]
def differ_by_three(l,n):
	d = []
	for i in range(len(l)-1):
		for e in l:
			if l.index(e) >= i:
				if l[i] - e == n or l[i] - e == -n:
					d.append([l[i],e])
	return d		
# print(differ_by_three([0, 3, 4, 7, 9],4))

