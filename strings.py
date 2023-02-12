# 1. Write a Python program to calculate the length of a string.
def len_of_string(s):
	length = 0
	for i in range(len(s)):
		length = i+1
	return length
print(len_of_string('string')) 

# 2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : 'google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
def count(s):
	dict ={}
	for each in s:
		if each not in dict:
			dict[each] = 1
		else:
			dict[each] = dict[each] + 1
	return dict
# print(count('google.com'))

# 3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
def first_2_last_2(s):
	if(len(s) > 2):
		return s[:2] + s[-2:]
	elif(len(s) == 2):
		return s + s
	return 'empty string'
# print(first_2_last_2('w3resource'))

# 4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'
def replace_letter(original_string,special_letter):
	start_letter = original_string[0]
	final_string = ''
	for each_letter in original_string[1:]:
		if(each_letter == start_letter):
			final_string = final_string + special_letter
		else:
			final_string = final_string + each_letter
	return start_letter + final_string
# print(replace_letter('restart','$'))

# 5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
def swap_string(s1,s2):
	return s2[:-1] + s1[-1] + ' ' + s1[:-1] + s2[-1]
# print(swap_string('abc','xyz'))

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'
def add_ing(s):
	if(len(s) > 2):
		if(s[-3:] == 'ing'):
			s = s + 'ly'
		else:
			s = s + 'ing'
	return s
# print(add_ing('string'))

# 7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'
def not_poor(s,s1,s2,add1):
	# import pdb; pdb.set_trace()
	x = s.find(s1)
	y = s.find(s2)
	p1 = s[:x]
	m = y + len(s2)
	p2 = s[m:]
	if(x != -1 and y != -1):
		if(x < y):
			return p1 + add1 + p2
	return s
# print(not_poor('the lyrics is not that poor','not','poor','good'))

# 8. Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9
def longest_word(l):
	long_word = l[0]
	for each_word in l[1:]:
		if(len(each_word) > len(long_word)):
			long_word = each_word
	return long_word,len(long_word)
# print(longest_word(['PHP','exercises','backend']))

# 9. Write a Python program to remove the nth index character from a nonempty string.
#case:1 
def remove_index_char(s,index):
	final_string = ''
	for each in range(len(s)):
		if(each != index):
			final_string = final_string + s[each]
	return final_string
# print(remove_index_char('python', 0))
# print(remove_index_char('python', 3))
# print(remove_index_char('python', 5))

#case: 2
def remove_index_char2(s,letter):
	x = s.index(letter)
	first_part = s[:x]
	second_part = s[x+1:]
	return first_part + second_part
# print(remove_index_char2('largest','g'))

# 10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
def exchange_first_last_chars(s):
	return s[-1] + s[1:-1] + s[0]
# print(exchange_first_last_chars('gorgeous'))

# 11. Write a Python program to remove the characters which have odd index values of a given string.
def remove_odd_index(s):
	final_string = ''
	for i in range(len(s)):
		if(i % 2 == 0):
			final_string = final_string + s[i]
	return final_string
# print(remove_odd_index('stringindex'))

# 12. Write a Python program to count the occurrences of each word in a given sentence.
def count_each_word(s):
	x = s.split(' ')
	d = {}
	for each in x:
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1
	return d
# print(count_each_word('tit for tat and tat for tit'))

# 13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
def case(s):
	return s.upper(),s.lower()
# print(case('development'))

# 14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red
def sorting(s):
	l = []
	x = s.split(',')
	for each in x:
		if each not in l:
			l.append(each)
	l.sort()
	return l
# print(sorting('red, white, black, red, green, black'))

# 15. Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def create_tags(i,s):
	return '<'+i+'>'+s+'</'+i+'>'
# print(create_tags('b','python'))

# 16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
def insert_at_middle(s,t):
	m = len(s)/2
	return s[:m] + t + s[m:]
# print(insert_at_middle('[[]]','python'))

# 17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
def copies_of_last_2_chars(s,n):
	final_string = ''
	for i in range(n):
		final_string = final_string + s[-2:]
	return final_string
# print(copies_of_last_2_chars('python',4))

# 18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt
def first_3_chars(s):
	final_string = ''
	for each in s[:3]:
		final_string = final_string + each
	return final_string 
# print(first_3_chars('python'))

# 19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python
def string_before_specified_part(s,c):
	x = s.index(c)
	return s[:x]
# print(string_before_specified_part('https://www.w3resource.com/python-exercises','-'))

# 20. Write a Python function to reverses a string if it's length is a multiple of 4.
def reverse_a_string(s):
	final_string = ''
	if(len(s) % 4 == 0):
		for i in range(len(s)):
			i = -i - 1
			final_string = final_string + s[i]
	else:
		return s
	return final_string
# print(reverse_a_string('stringlength'))

def insert_string_between_each_letter(s,sp):
	l = ''
	for i in s:
		l = l + i + sp
	return l
# print(insert_string_between_each_letter('abcd','xyz'))

# 21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def upper_case(s):
	count = 0
	for each in s:
		if(each.isupper()):
			count = count + 1 
		if(count == 2):
			break
		if(count >= 2):
			s = s.upper()
	return s
# print(upper_case('ABCDefghi'))

# 22.Write a Python program to sort a string lexicographically.
def lexicographically(s):
	l = []
	x = s.split(',')
	for each in x:
		if each not in l:
			l.append(each)
	x.sort()
	return x
# print(lexicographically('red,orange,green'))

# 23. Write a Python program to remove a newline in Python. 
def remove_newline(s):
	return s.rstrip()
# print(remove_newline('sushma\n'))

# 24. Write a Python program to check whether a string starts with specified characters. 
def specified_char(s,spc):
	x = len(spc)
	if(spc == s[:x]):
		return 'string starts with specified character'
	return "string not starts with specified character"
# print(specified_char('karishma','kari'))

# 25. Write a Python program to create a Caesar encryption. 
def ceaser_encryption(alpha,given):
	final_string =''
	for each in given:
		x = alpha.index(each)
		if(x > 2):
			final_string = final_string + alpha[x-3]
		elif(x < 3):
			final_string = final_string + alpha[x-3]
	return final_string
# print(ceaser_encryption('abcdefghijklmnopqrstuvwxyz','def'))

# 26. Write a Python program to display formatted text (width=50) as output.
def formatted_text(string,value):
	return string[:value]
# print(formatted_text('abcdefghijkl',5))

# 27. Write a Python program to remove existing indentation from all of the lines in a given text.
def intendation(string):
	final_string = ''
	x = string.split('\n')
	for each in x:
		i = each.lstrip()
		final_string = final_string + i + '\n'
	return final_string
# print(intendation('if(a>b):\n   print(a)\n    else:\n    print(b)'))

# 28. Write a Python program to add a prefix text to all of the lines in a string.
def add_prefix(string):
	final_string = ''
	prefix = '<>'
	x = string.split('\n')
	for each in x:
		final_string = final_string + prefix + each + '\n'
	return final_string
# print(add_prefix('if(a>b):\nprint(a)\nelse:\nprint(b)'))

# 29. Write a Python program to set the indentation of the first line.
def first_line(string):
	x = string.split('\n')
	final_string = x[0].lstrip() + '\n'
	for each in x[1:]:
		final_string = final_string + each + '\n'
	return final_string
# print(first_line('   if(a>b):\n   print(a)\n    else:\n    print(b)'))

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

# 31. Write a Python program to print the following floating numbers upto 2 decimal places with a sign.
def add_sign(l,sign):
	f_list = [str(each) for each in l]
	new_list =[]
	for each in f_list: 
		x = each.find('.')
		if(x != -1):
			if(len(each[x:]) >= 3):
				new_list.append(sign + each[:x+3])
	return new_list
# print(add_sign([2.14,10.567,234.1,10.5,45.4567,1.45,1000.1578,20,234.456],'+'))

# 32. Write a Python program to print the following floating numbers with no decimal places.
def no_decimal(l):
	f_list =[str(each) for each in l]
	new_list = []
	for each in f_list:
		x = each.find('.')
		new_list.append(each[:x])
	return new_list
# print(no_decimal([2.1,10.32,345.4444]))

# 33. Write a Python program to print the following integers with zeros on the left of specified width.
def pre_zeroes(l):
	f_list = [str(each) for each in l]
	new_list = []
	for each in f_list:
		s = ''
		for i in range(len(each)):
			s = s + '0'
		new_list.append(s + each)
	return new_list
# print(pre_zeroes([1,20,300]))

# 34. Write a Python program to print the following integers with '*' on the right of specified width. 
def right_star(s):
	new_string = ''
	x = ''
	for i in range(len(s)):
		x = x + '*'
	new_string = s + x 
	return new_string
# print(right_star('12345'))

# 35. Write a Python program to display a number with a comma separator.
def comma_separator(s):
	new_list =[]
	while(len(s) > 2):
		new_list.append(s[-3:])
		s = s[:-3]
	# if s not in ['']:
	new_list.append(s)
	new_list.reverse()
	# print(new_list)
	return ','.join(new_list)
# print(comma_separator('3000000'))

# 36. Write a Python program to format a number with a percentage.
def format_percentage(num):
	pass
# print(format_percentage('0.25'))

# 37. Write a Python program to display a number in left, right and center aligned of width 10.
def display_number(width,s):
	sum = ''
	for i in range(width):
		middle_index = (width -len(s)) / 2
		if i == middle_index:
			for each in s:
				sum = sum + each 
			break
		sum = sum + ' '
	return sum
# print(display_number(10,'abcd'))

# 38. Write a Python program to count occurrences of a substring in a string.
def sub_string(s,sub):
	count = 0
	x = s.split(' ')
	for each in x:
		if(each == sub):
			count = count +1
	return count
# print(sub_string('the man and the women and the girl','and'))

# 39. Write a Python program to reverse a string.
def reverse_a_string2(s):
	final_string = ''
	for each in range(len(s)):
		each = -each -1
		final_string = final_string + s[each]
	return final_string
# print(reverse_a_string2('pythonprogram')) 

# 40. Write a Python program to reverse words in a string.
def reverse_words(s):
	x = s.split(' ')
	final_string = ''
	for each in range(len(x)):
		each = -each -1
		final_string = final_string + x[each]
	return final_string
# print(reverse_words('the quick brown fox'))

# 41. Write a Python program to strip a set of characters from a string.
def strip_char(s,s1):
	final_string = ''
	for each in s:
		if each not in s1:
			final_string = final_string + each
	return final_string
# print(strip_char('tit for tat all is well','tal'))

# 42. Write a Python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output :
# o 4
# e 3
# u 2
# h 2
# r 2
# t 2
def repeated_char(s):
	d = {}
	l = []
	for each in s:
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1
	for each in d:
		if (d[each] != 1):
			l.append((each,d[each]))
	return l  
# print(repeated_char('google')) 

# 43. Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.
# Sample output:
# The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3
def square_and_cube(area,volume):
	pass
# print(square_and_cube(2,3))

# 44. Write a Python program to print the index of the character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
def index_of_the_char(s):
	d = {}
	for i in range(len(s)):
		d[s[i]] = i
	return d
# print(index_of_the_char('string'))

# 45. Write a Python program to check whether a string contains all letters of the alphabet. 
def all_letters(alpha,s):
	l = []
	for each in alpha:
		if each not in s:
			l.append(each)
	x = 'string contains all letters'		
	if l:
		x = 'string not contains all letters'
	return x,l
# print(all_letters('ABCDEFGHIJKLMNOPQRSTUVWXYZ','ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

# 46. Write a Python program to convert a given string into a list of words.
# Sample Output:
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
def list_of_words(s):
	return s.split(' ')
# print(list_of_words('the quick brown fox jumps over the lazy dog'))

# 47. Write a Python program to lowercase first n characters in a string. 
def lower_letters(s,n):
	if(n < len(s)):
		return s[:n].lower() + s[n:]
	return s.lower()
# print(lower_letters('SUSHMA',3))

def lower_letters2(s,n):
	return s[:n].upper() + s[n:]
# print(lower_letters2('sus33hma',5))

# 48. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"
def swapping(s):
	final_string = ''
	for each_letter in s:
		if each_letter == '.':
			each_letter = ','
		elif each_letter == ',':
			each_letter = '.'
		final_string = final_string + each_letter
	return final_string
# print(swapping('12,344,56,10.0'))

# 49. Write a Python program to count and display the vowels of a given text. 
def count_vowels(s,vowels):
	l = []
	count = 0
	for each in s:
		if each in vowels:
			count = count + 1
			if each not in l:
				l.append(each)
	return count,l
# print(count_vowels('sushma','aeiou'))

#case:2
def count_vowels(s,vowels):
	d = {}
	l = []
	for each in vowels:
		if each in s:
			if each not in d:
				d[each] = 1
			else:
				d[each] = d[each] + 1
	for each in d:
		l.append(each)
	return len(d),l
# print(count_vowels('sushma','aeiou'))

# 50. Write a Python program to split a string on the last occurrence of the delimiter. 
def split_last(s):
	return s.split(s[-1])
# print(split_last('hasahasrabhihamha'))

def split_last2(s):
	return s[:-1],s[-1]
# print(split_last2('alphabet'))

# 51. Write a Python program to find the first non-repeating character in given string.
def first_non_reapeat_char(s):
	d = {}
	l = []
	nrc = ''
	for each in s:
		if each not in d:
			d[each] = 1
			l.append(each)
		else:
			d[each] = d[each] + 1
	for each in l:
		if(d[each] == 1):
				return each	
	return nrc
# print(first_non_reapeat_char('abbacbdc'))

# 52. Write a Python program to print all permutations with given repetition number of characters of a given string. 
def all_permutations(s,num):
	l = []
	for each_one in s:
		for each_two in s:
			for each_three in s:
				if (each_three, each_two, each_three) not in l:
					l.append((each_three, each_two, each_three))
	return l
# print(all_permutations('abc',3))

# 53. Write a Python program to find the first repeated character in a given string.
def first_repeated_char(s):
	d = {}
	for each in s:
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1
			return each
	return none  
# print(first_repeated_char('acbcbadbeca'))

# 54. Write a Python program to find the first repeated character of a given string where the index of first occurrence is smallest. 
def first_repeated_char_index(s):
	d = {}
	for each in s:
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1
			return (each,s.index(each))
	return none
# print(first_repeated_char_index('abdcecaghd'))

# 55.Write a Python program to find the first repeated word in a given string.
def first_repeated_word(s):
	x = s.split(' ')
	d = {}
	for each in x:
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1
			return each
	return none
# print(first_repeated_word('girl boy and boy and girl'))

# 56. Write a Python program to find the second most repeated word in a given string.
def second_most_repeated_word(s):
	x = s.split(' ')
	d = {}
	for each in x:
		if each != ' ':
			if each not in d:
				d[each] = 1
			else:
				d[each] = d[each] + 1
	if len(d) > 2:
		second_max = list(set(d.values()))[-2]		
		l = []
		for each in d:
			if d[each] == second_max:
				l.append((each,second_max))
		return l
	else:
		if x[0] == x[1]:
			return [(x[0], 2)]
		return [(x[0], 1), (x[1], 1)]
# print(second_most_repeated_word('abc def abc ghi abc def abc'))

# 57.Write a Python program to remove spaces from a given string.
def remove_spaces(s):
	final_string = ''
	for each in s:
		if(each != ' '):
			final_string = final_string + each
	return final_string
# print(remove_spaces('doc ume nt a ti on'))

# 58. Write a Python program to move spaces to the front of a given string.
def move_space(s):
	x = ''
	for each in s:
		if(each == ' '):
			x = ' ' + x
		else:
			x = x  + each
	return x
# print(move_space('di rec to ry'))

# 59. Write a Python program to find the maximum occurring character in a given string.
def maximum_occuring_char(s):
	d = {}
	compare_list = []
	for each in s:
		if each != ' ':
			if each not in d:
				d[each] = 1
				if not compare_list:
					compare_list = [each, 1]
			else:
				d[each] = d[each] + 1
				if compare_list[1] < d[each]:
					compare_list[0] = each
					compare_list[1] = d[each]
	return compare_list
# print(maximum_occuring_char('who ill welcome to w3resource'))

# 60. Write a Python program to capitalize first and last letters of each word of a given string.
def capitalize_first_last_letters(s):
	x = s.split(' ')
	l = []
	for each in x:
		### case 1
		sum = each[0].upper()
		for e in each[1:-1]:
			sum = sum + e
		sum = sum + each[-1].upper()
		l.append(sum)

		## case 2
		# each_list = [char for char in each]
		# each_list[0] = each_list[0].upper()
		# each_list[-1] = each_list[-1].upper()
		# l.append(''.join(each_list))

		## case 3
		# each_list = [char for char in each]
		# l.append(each_list[0].upper() + ''.join(each_list[1:-1]) + each_list[-1].upper())
	return ' '.join(l)
# print(capitalize_first_last_letters('clean india'))

# 61. Write a Python program to remove duplicate characters of a given string.
def remove_duplicate(s):
	final_string = ''
	for each in s:
		if each not in final_string:
			final_string = final_string + each
	return final_string
# print(remove_duplicate('abcdaefbgcb'))

# 62. Write a Python program to compute sum of digits of a given string.
def sum_digits(s):
	sum = 0
	for each in s:
		if(each.isdigit()):
			sum = sum + int(each) 
	return sum
# print(sum_digits('12abc345'))

# 63. Write a Python program to remove leading zeros from an IP address. 
def remove_zeroes(s):
	## case 1:
	return '.'.join([str(int(each)) for each in s.split('.')])
	## case 2:
	final_string = ''
	for each in s:
		if(each != '0'):
			final_string = final_string + each
	# return final_string
# print(remove_zeroes('225.01.0.05'))

# 64. Write a Python program to find maximum length of consecutive 0's in a given binary string. 
def maximum_length_of_consecutive_zeroes(s):
	### case 1:
	max = 0
	large = 0
	#import pdb;pdb.set_trace();
	for i in range(0, len(s)):
		if i != 0:
			if int(s[i]) == 0:
				if int(s[i-1]) == 0:
					max = max + 1
					if max > large:
						large = max
				else:
					max = 1
			else:
				if int(s[i-1]) == 0:
					if max > large:
						large = max
					max = 0
				#max = 0
		else:
			if int(s[i]) == 0:
				max = 1
	# return large

	### case 2:
	x = s.split('1')
	for each in x:
		if len(each) > max:
			max = len(each)
	return max
# print(maximum_length_of_consecutive_zeroes('0000110010001110000'))

# 65. Write a Python program to find all the common characters in lexicographical order from two given lower case strings. If there are no common letters print "No common characters".
def common_chars(s1,s2):
	l = []
	for each in s1:
		if each not in l:
			if each in s2:
				l.append(each)
	if l:
		return 'there are common letters',l
	return 'there are no common letter'
# print(common_chars('Python','PHP'))

# 66. Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing any characters from any of the strings.
def anagrams(s1,s2):
	x = ''
	y = ''
	for each in s1:
		if each in s2:
			x = x + each
	for each in s2:
		if each in s1:
			y = y + each
	return x,y
# print(anagrams('spearux','pearscn'))

# 67. Write a Python program to remove all consecutive duplicates of a given string.
def remove_consecutive_duplicates(s):
	sum = s[0]
	for each in s:
		if each != sum[-1]:
			sum = sum + each 
	return sum
# print(remove_consecutive_duplicates('abbbbcdcddade'))

# 68. Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string.
def char_occurs_at_once_and_multi_times(s):
	d = {}
	s1 = ''
	s2 = ''
	for each in s:
		if each != ' ':
			if each not in d:
				d[each] = 1
			else:
				d[each] = d[each] + 1
	for each in d:
		if d[each] == 1:
			s1 = s1 + each
		else:
			s2 = s2 + each
	return s1,s2
# print(char_occurs_at_once_and_multi_times('there is nothing'))

# 69. Write a Python program to find the longest common sub-string from two given strings.
def longest_common_substring(s1,s2):
	pass
# print(longest_common_substring('longestsubstring','longestcommansubstring'))

# 70. Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings.
def concatenate_uncommon_chars(s1,s2):
	final_string = ''
	for each in s1:
		if each not in s2:
			final_string = final_string + each
	for each in s2:
		if each not in s1:
			final_string = final_string + each 
	return final_string
# print(concatenate_uncommon_chars('absdf','xabst')) 

# 71. Write a Python program to move all spaces to the front of a given string in single traversal. 
def move_all_spaces(s):
	final_string = ''
	for each in s:
		if each != ' ':
			final_string = final_string + each
	return final_string
# print(move_all_spaces('no one is more'))

# 72. Write a Python code to remove all characters except a specified character in a given string. 
def remove_all(s,s1):
	l=[each for each in s if each == s1]
	return '&'.join(l)
# print(remove_all('sushma','s'))

# 73. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.
def count_all_cases(s):
	d = {'upper_count': 0,
		 'lower_count': 0,
		 'number_count': 0,
		 'special_char_count': 0}
	for each in s:
		if each.isupper():
			d['upper_count'] = d['upper_count'] + 1
		elif each.islower():
			d['lower_count'] = d['lower_count'] + 1
		elif each.isdigit():
			d['number_count'] = d['number_count'] + 1
		else:
			d['special_char_count'] = d['special_char_count'] + 1
	return d
# print(count_all_cases('aBcd&2G4%'))

# 74. Write a Python program to find the minimum window in a given string which will contain all the characters of another given string.
# Example 1
# Input : str1 = " PRWSOERIUSFK "
# str2 = " OSU "
def min_window_contains_all_chars(s1,s2):
	f_list = []
	for each in s2:
		if each in s1:
			f_list.append(s1.index(each))
	f_list.sort() 
	return s1[f_list[0]:f_list[-1]]	
# print(min_window_contains_all_chars(" PRWSOERIUSFK "," OSU "))

# 75. Write a Python program to find smallest window that contains all characters of a given string. 
def all_char(s):
	pass
# print(all_char('substring'))

# 76. Write a Python program to count number of substrings from a given string of lowercase alphabets with exactly k distinct (given) characters. 
def k_distinct_char(s,k):
	l = []
	for each in s:
		if each not in l:
			l.append(each)
	return len(l)//k
# print(k_distinct_char('wolfcat',4))

# 77. Write a Python program to count number of non-empty substrings of a given string.
def count_non_empty(s):
	l = [each for each in s if each != ' ']
	x = len(l)*(len(l) + 1)//2
	return x
# print(count_non_empty('w3resource'))

# 78. Write a Python program to count characters at same position in a given string (lower and uppercase characters) as in English alphabet.
def count_char_at_same_index(s,alphabet):
	count = 0
	for each in s:
		if(s.index(each) == alphabet.index(each)):
			count = count +1
	return count
# print(count_char_at_same_index('xcbjelght','abcdefghijklmnopqrstuvwxyz'))

# 79. Write a Python program to find smallest and largest word in a given string.
def largest_and_smallest_word_in_string(s):
	x = s.split(' ')
	longest_str = x[0]
	shortest_str = x[0]
	for each in x:
		if len(each) > len(longest_str):
			longest_str = each
		if len(each) < len(shortest_str):
			shortest_str = each	
	return longest_str, shortest_str
# print(largest_and_smallest_word_in_string('there is a lion in the forest'))

# 80. Write a Python program to count number of substrings with same first and last characters of a given string. 
def sub_f_and_l(s):
	pass
# print(sub_f_and_l('abc'))

# 81. Write a Python program to find the index of a given string at which a given substring starts. If the substring is not found in the given string return 'Not found'. 
def starting_index_of_sub_string(s,s1):
	if s1 in s:
		x = s.find(s1[0])
		return x
	return 'not found'
# print(starting_index_of_sub_string('reproduction','product'))

# 82. Write a Python program to wrap a given string into a paragraph of given width.
# Sample Output:
# Input a string: The quick brown fox.
# Input the width of the paragraph: 10
# Result:
# The quick
# brown fox.
def para_given_width(s,width):
	start = 0
	end = width
	while(len(s) > end):
		print(s[start:end+1])
		start = start + width
		tail_end = end + width
		if tail_end > len(s):
			print(s[end:])
		end = end + width
	sum = ''
	count = 1
	for i in range(len(s)):
		sum = sum + s[i]
		if count % 5 == 0:
			sum = sum + '\n'
		count = count + 1
	return sum
# print(para_given_width('The quick brown fox.',4))

# 83. Write a Python program to print four values decimal, octal, hexadecimal (capitalized), binary in a single line of a given integer.
# Sample Output:
# Input an integer: 25
# Decimal Octal Hexadecimal (capitalized), Binary
# 25 31 19 11001
def decimal_num(n):
	number = 8
	l = []
	while(n > 0):
		l.append(n % number) 
		n = n//number
	l.reverse()
	return l
# print(decimal_num(25))

# 84. Write a Python program to swap cases of a given string.
# Sample Output:
# pYTHON eXERCISES
# jAVA
# nUMpY
def swap_case(s):
	x = ''
	for each in s:
		if each.isupper():
			x = x + each.lower()
		elif each.islower():
			x = x + each.upper()
	return x 
# print(swap_case('PyThOn'))
# print(swap_case('jaVa'))

# 85. Write a Python program to convert a given Bytearray to Hexadecimal string.
# Sample Output:
# Original Bytearray :
# [111, 12, 45, 67, 109]
# Hexadecimal string:
# 6f0c2d436d



# 86. Write a Python program to delete all occurrences of a specified character in a given string.
# Sample Output:
# Original string:
# Delete all occurrences of a specified character in a given string
# Modified string:
# Delete ll occurrences of specified chrcter in given string
def del_specified_char(s,sp):
	x = ''
	for each in s:
		if each != sp and each != ' ':
			x = x + each
	return x 
# print(del_specified_char('specified character','e'))

# 87. Write a Python program find the common values that appear in two given strings.
# Sample Output:
# Original strings:
# Python3
# Python2.7
# Intersection of two said String:
# Python
def common_values(s1,s2):
	x = ''
	for each in range(len(s1)):
		if s1[each] == s2[each]:
			x = x + s2[each]
	return x			
# print(common_values('python3','python2.7'))	

# 88. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length.
# Sample Output:
# Input the string: W3resource
# ['Valid string.']
def valid_string(s,n):
	if len(s) < n:
		return 'invalid string'
	upper_flag = False
	lower_flag = False
	int_flag = False
	#import pdb; pdb.set_trace();
	for each in s:
		if each.isupper():
			upper_flag = True
		elif each.islower():
			lower_flag = True
		elif each.isdigit():
			int_flag = True

		if upper_flag and lower_flag and int_flag:
			return 'valid string'
	return 'invalid string'
# print(valid_string('3resource', 4))

# 89. Write a Python program to remove unwanted characters from a given string.
# Sample Output:
# Original String : Pyth*^on Exercis^es
# After removing unwanted characters:
# Python Exercises
# Original String : A%^!B#*CD
# After removing unwanted characters:
# ABCD
def remove_unwanted_char(s):
	x = ''
	for each in s:
		if each.isupper() or each.islower() or each == ' ':
			x = x + each
	return x
# print(remove_unwanted_char('Pyt#ho%n Ex&e^rci$ses' ))

# 90. Write a Python program to remove duplicate words from a given string.
# Sample Output:
# Original String:
# Python Exercises Practice Solution Exercises
# After removing duplicate words from the said string:
# Python Exercises Practice Solution
def remove_duplicate_words(s):
	x = s.split(' ')
	y = ''
	for each in x:
		if each not in y:
			y = y + each +' '
	return y
# print(remove_duplicate_words('when there is a will there is a way'))

# 91. Write a Python program to convert a given heterogeneous list of scalars into a string.
# Sample Output:
# Original list:
# ['Red', 100, -50, 'green', 'w,3,r', 12.12, False]
# Convert the heterogeneous list of scalars into a string:
# Red,100,-50,green,w,3,r,12.12,False
def list_of_scalars(l):
	return ','.join([str(each) for each in l])
	# x = ''
	# for i in range(len(l)):
	# 		if i == len(l)-1:
	# 			x = x + str(l[i])
	# 		else: 
	# 			x = x + str(l[i]) + ','
	# return x
# print(list_of_scalars(['Red', 100, -50, 'green', 'w,3,r', 12.12, False]))

# 92. Write a Python program to find the string similarity between two given strings.
# Sample Output:
# Original string:
# Python Exercises
# Python Exercises
# Similarity between two said strings:
# 1.0
# Original string:
# Python Exercises
# Python Exercise
# Similarity between two said strings:
# 0.967741935483871
# Original string:
# Python Exercises
# Python Ex.
# Similarity between two said strings:
# 0.6923076923076923
# Original string:
# Python Exercises
# Python
# Similarity between two said strings:
# 0.5454545454545454
# Original string:
# Java Exercises
# Python
# Similarity between two said strings:
# 0.0
def similar(s1, s2):
	#import pdb;pdb.set_trace()
	each_percentage_wait = 100/len(s1)
	total_percent = 0
	for i in range(len(s2)):
		if s2[i] != s1[i]:
			return int(total_percent)
		total_percent = total_percent + each_percentage_wait
	return int(total_percent)
# print(similar('python exercise', 'python exercis'))

# 93. Write a Python program to extract numbers from a given string.
# Sample Output:
# Original string: red 12 black 45 green
# Extract numbers from the said string: [12, 45]
def extract_numbers(s):
	s1 = s.split(' ')
	l = []
	for each in s1:
		if each.isdigit():
			l.append(int(each))
	return l
# print(extract_numbers('red 12 black 45 green'))

# 94. Write a Python program to convert a hexadecimal color code to a tuple of integers corresponding to its RGB components.
# Sample Output:
# (255, 165, 1)
# (255, 255, 255)
# (0, 0, 0)0
# (255, 0, 0)
# (0, 0, 128)
# (192, 192, 192)
def RGB_components(hc):
	l = []
	for i in range(0, len(hc), 2):
		l.append(int(hc[i:i+ 2], 16))
	return tuple(l)
# print(RGB_components('FFA501'))

# 95. Write a Python program to convert the values of RGB components to a hexadecimal color code.
# Sample Output:
# FFA501
# FFFFFF
# 000000
# 000080
# C0C0C0
def hexadecimal(t):
	x = ''
	for each in t:
		x = x + hex(each)[2:].upper()
	return x
# print(hexadecimal((255, 165, 1)))

# 96. Write a Python program to convert a given string to camelcase.
# Sample Output:
# javascript
# fooBar
# fooBar
# foo.Bar
# fooBar
# foobar
# fooBar





# 97. Write a Python program to convert a given string to snake case.
# Sample Output:
# java_script
# foo_bar
# foo_bar
# foo.bar
# foo_bar
# foo_bar
# foo_bar



# 98. Write a Python program to decapitalize the first letter of a given string.
# Sample Output:
# java Script
# python
def decapital_f_char(s):
	return s[0].lower() + s[1:]
# print(decapital_f_char('Java Script'))

# 99. Write a Python program to split a given multiline string into a list of lines.
# Sample Output:
# Original string: This
# is a
# multiline
# string.
# Split the said multiline string into a list of lines:
# ['This', 'is a', 'multiline', 'string.', '']
def multi_line(l):
	s = l.split('\n')
	return s
# print(multi_line('This\nis a\nmultiline\nstring.'))

# 100. Write a Python program to check whether any word in a given sting contains duplicate characrters or not. Return True or False.
# Sample Output:
# Original text:
# Filter out the factorials of the said list.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# Python Exercise.
# Check whether any word in the said sting contains duplicate characrters or not!
# False
# Original text:
# The wait is over.
# Check whether any word in the said sting contains duplicate characrters or not!
# True
def duplicate_characters(s):
	d = {}
	x = s.split(' ')
	for each in x:
		for e in each:
			if e not in d:
				d[e] = 1
			else:
				d[e] = d[e] + 1
		for each in d:
			if(d[each] > 1):
				return False
	return True
# print(duplicate_characters('education'))

# 101. Write a Python program to add two strings as they are numbers (Positive integer values). Return a message if the numbers are string.
# Sample Output:
# 42
# Error in input!
# Error in input!
def add_two_strings(s1,s2):
	if s1.isdigit() and s2.isdigit():
		return int(s1)+int(s2)
# print(add_two_strings('10','20'))

# 102. Write a Python program to remove punctuations from a given string.
# Sample Output:
# Original text:
# String! With. Punctuation?
# After removing Punctuations from the said string:
# String With Punctuation
def remove_punctuation(s):
	x = ''
	for each in s:
		if each.isupper() or each.islower() or each == ' ':
			x = x + each
	return x
# print(remove_punctuation('String! With. Punctuation?'))

# 103. Write a Python program to replace each character of a word of length five and more with hash character (#).
# Sample Output:
# Original string: Count the lowercase letters in the said list of words:
# Replace words (length five or more) with hash characters in the said string:
# ##### the ######### ####### in the said list of ######
# Original string: Python - Remove punctuations from a string:
# Replace words (length five or more) with hash characters in the said string:
# ###### - ###### ############ from a #######
def replace_with_hash(s):
	x = s.split(' ')
	l = []
	for each in x:
		if (len(each) >= 5):
			l.append('#' * len(each))
		else:
			l.append(each)
	return ' '.join(l)
# print(replace_with_hash('Count the lowercase letters in the said list of words'))

# 104. Write a Python program that capitalizes the first letter and lowercases the remaining letters of a given string.
# Sample Data:
# ("Red Green WHITE") -> "Red Green White"
# ("w3resource") -> "W3resource"
# ("dow jones industrial average") -> "Dow Jones Industrial Average"
def capital_f_l2(s):
	x = s.split(' ')
	#case 1
	# s1 = ''
	# for each in x:
	# 	if x.index(each) == len(x)-1:
	# 		each = each[0].upper() + each[1:].lower()
	# 	else:	
	# 		each = each[0].upper() + each[1:].lower() + ' #'
	# 	s1 = s1 + each
	# return s1

	# case 2
	# s1 = ''
	# for i in range(len(x)):
	# 	if i == len(x) - 1:
	# 		each = x[i][0].upper() + x[i][1:].lower()
	# 	else:
	# 		each = x[i][0].upper() + x[i][1:].lower() + ' #'
	# 	s1 = s1 + each
	# return s1

	#case 3

	# l = []
	# for each in x:
	# 	l.append(each[0].upper() + each[1:].lower())
	# return ' #'.join(l)

	#case 4
	for i in range(len(x)):
		x[i] = x[i][0].upper() + x[i][1:].lower()
	return ' #'.join(x)

# print(capital_f_l2("Red Green WHITE"))

# 105. Write a Python program to extract and display the name from a given email address.
# Sample Data:
# ("john@example.com") -> ("john")
# ("john.smith@example.com") -> ("johnsmith")
# ("fully-qualified-domain@example.com") -> ("fullyqualifieddomain")
def email_address(e):
	x = e.find('@')
	name = e[:x]
	if '.' in name:
		name = name.split('.')
	elif '-' in name:
		name = name.split('-')
	return ''.join(name)
# print(email_address("fully-qualified-domain@example.com"))

# 106. Write a Python program to remove repeated consecutive characters and replace with the single letters and print new updated string.
# Sample Data:
# ("Red Green White") -> "Red Gren White"
# ("aabbbcdeffff") -> "abcdef"
# ("Yellowwooddoor") -> "Yelowodor"
def remove_consecutives(s):
	x = s[0]
	for each in s:
		if each != x[-1]:
			x = x + each
	return x
# print(remove_consecutives("Red Green White"))

# 107. Write a Python program to that takes two strings. Count the number of times each string contains the same three letters at the same index.
# Sample Data:
# ("Red RedGreen") -> 1
# ("Red White Red White) -> 8
# ("Red White White Red") -> 0

def three_letter_count(s1, s2):
	count = 0
	for i in range(len(s1)):
			count = count + 1
	return count
# print(three_letter_count('Red White', 'White Red'))

# 108. Write a Python program to that takes a string and returns # on both sides each element, which are not vowels.
# Sample Data:
# ("Green" -> "-G--r-ee-n-"
# ("White") -> "-W--h-i-t-e"
# ("aeiou") -> "aeiou"
def both_sides(s,vowels):
	x = ''
	for each in s:
		if each not in vowels:
			x = x + '#' +  each + '#'
		else:
			x = x + each	
	return x
# print(both_sides('aeiou','aeiou'))

# 109. Write a Python program that counts the number of leap years within the range of years. The range of years should be accepted as a string.
# Sample Data:
# ("1981-1991") -> 2
# ("2000-2020") -> 6
def count_leap_years(s):
	x = s.split('-')
	count = 0
	for i in range(int(x[0]),int(x[-1])):
		if(int(i) % 4 == 0):
			count = count + 1
	return count
# print(count_leap_years('1981-1991'))

# 110. Write a Python program to insert space before every capital letter appears in a given word.
# Sample Data:
# ("PythonExercises") -> "Python Exercises"
# ("Python") -> "Python"
# ("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"
def space_before_capital(s):
	x = s[0]
	for each in s[1:]:
		if(each.isupper()):
			x = x + ' ' + each
		else: 
			x = x + each
	return x
# print(space_before_capital('PythonExercisesPracticeSolution'))

# 111. Write a Python program that takes a string and replaces all the characters with their respective numbers.
# Sample Data:
# ("Python") -> "16 25 20 8 15 14"
# ("Java") -> "10 1 22 1"
# ("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"
def replace_with_num(s):
	d = {}
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	for i in range(len(alphabet)):
		d[alphabet[i]] = i + 1 
	l = []
	for each in s:
		l.append(d[each])
	return l 

	return [d[each] for each in s]
# print(replace_with_num('python'))

# 112. Write a Python program to calculate the sum of two numbers given as strings. Return the result in the same string representation.
# Sample Data:
# ( "234242342341", "2432342342") -> "236674684683"
# ( "", "2432342342") -> False ( "1000", "0") -> "1000"
# ( "1000", "10") -> "1010"
def sum_2nums(t):
	return int(t[0]) + int(t[1])
# print(sum_2nums(('23457899','98766453')))

# 113. Write a Python program that returns a string sorted alphabetically by the first character of a given string of words.
# Sample Data:
# ("Red Green Black White Pink") -> "Black Green Pink Red White"
# ("Calculate the sum of two said numbers given as strings.") -> ("Calculate as given numbers of sum said strings. the two")
# ("The quick brown fox jumps over the lazy dog.") -> ("The brown dog. fox jumps lazy over quick the")
# def alphabetically(s):
# 	xx = s
# 	x = s.split(' ') 
# 	x.append(3)
# 	second_part =  x[1:]
# 	second_part.sort()
# 	return [x[0]] + second_part
# print(alphabetically('Red Green Black White Pink'))













