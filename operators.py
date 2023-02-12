##1.BITWISE OPERATORS

# n = 4
# if n & 1 == 1
# n is odd
# else 
# n is even


# if n | 1 == n
# odd
# n | 1 != n
# even

# 100 | 1 == n+1


# 2 power 5
# 2 * 2 * 2 * 2 * 2


# n = 5
# s = 2
# for i in range(1,n):
# 	s = s * i

# n = 5
# res = 1
# for i in range(n):
# 	res = res * 2
# print(res)
# 1
# 2
# 2*2 
# 2*2*2
# 2*2*2*2

# i = 1
# s = 2

# i = 2
# s = 2 * 2 = 4

# i = 3
# s = 4 * 3 = 12


# n = 5
# s = 0
## case - 1:
# for i in range(1,n+1):
# 	s = s + i

## case - 2:
# res = 0
# while(s <= n):
# 	res  = res + s
# 	s += 1

## case - 3:
# while(n!=0):
# 	res = res + n 
# 	n -= 1


## problems on bitwise operators.

	# 1.counting 1's in binary representation of a given number.
	# 2.code for fibonacci series.
	# 	0,1,1,2,3,5,8,13
	# 3.check bit position 
	# 4.placing bits


## 1.counting no.of 1's in binary representation of a given number.

	# n = int(input())
	# for i in range(n):
	# 	s = int(input())
	# 	count = 0
	# 	while s != 0:
	# 		if s & 1 == 1:
	# 			count += 1
	# 		s = s >> 1
	# 	print(count)

## 2.code for fibonacci series
	# 0,1,1,2,3,5,8,13

	# n = 5
	# l = []
	# for i in range(n):
	# 	if i < 2:
	# 		l.append(1) 
	# 	else:
	# 		l.append(l[-1]+l[-2])
	# print(l)

## 3. check bit position

	# n = 10
	# x,y = 2,3
	# n1 = n >> x-1 
	# n2 = n >> y-1 
	# print(n1 & 1)
	# print(n2 & 1)

## 4.placing bits



## 5. given no. of 1's and 0's then convert binary to number.

	# Sample Input 0
	# 3
	# 4 3
	# 2 5
	# 10 15

	# Sample Output 0
	# 120
	# 96
	# 33521664

	# Explanation 0

	# Test Case 1
	# The binary representation of the number that has 4 ones followed by 3 zeros is 1111000 = 120. 

	# n = int(input())
	# for i in range(n):
	# 	x,y = list(map(int,input().strip().split()))
	# 	s = '0'
	# 	for i in range(x):
	# 	    s = s + '1'
	# 	for i in range(y):
	# 	    s = s + '0'
	# 	res = 0
	# 	if x == 0:
	# 		print(x)
	# 	else:
	# 		for i in range(len(s)):
	# 			if i == 0:
	# 				res = res + ((2**i)*int(s[i-1]))
	# 			else:
	# 				res = res + ((2**i)*int(s[-i-1]))
	# 		print(res)

## 6.check bit

	# x,y = list(map(int,input().strip().split()))
	# count = 0
	# while(x!=0):
	# 	count += 1
	# 	x = x >> 1
	# if y <= count:
	# 	print('true')
	# else:
	# 	print('false')

## 7.x and y set bits

	# Sample Input 0
	# 3
	# 4 3
	# 5 0
	# 15 30

	# Sample Output 0
	# 24
	# 33
	# 73774585
	# Explanation 0

	# Test Case 1
	# The binary representation of the number that has bits at position 3 and 4 set is 11000 = 24

	# Test Case 2
	# The binary representation of the number that has the bit at position 5 and 0 set is 100001 = 33

	# n = int(input())
	# for i in range(n):
	# x,y = list(map(int,input().strip().split()))
	# s = ''
	# if y > x:
	# 	for i in range(y+1):
	# 		if i == x or i == y:
	# 			s = s + '1'
	# 		else:
	# 			s = s + '0'
	# else:
	# 	for i in range(x+1):
	# 		if i == x or i == y:
	# 			s = s + '1'
	# 		else:
	# 			s = s + '0'
	# s = s[::-1]
	# res = 0
	# for i in range(len(s)):
	# 	if i == 0:
	# 		res = res + ((2**i)*int(s[i-1]))
	# 	else:
	# 		res = res + ((2**i)*int(s[-i-1]))
	# if res > 10**5:
	# 	print(res % 1000000007)
	# else:
	# 	print(res)




## 2. RECURRSION
	# recurrsion means calling a function within the same function.
	# recurrsive function follows 3 steps:
		# 1.base condition
		# 2.main logic
		# 3.assumption

## sum of natural numbers.

# def func(n):
# 	if n == 1:
# 		return 1
# 	return n + func(n-1)
# print(func(5))

## sum of even numbers.

	# def even_sum(n):
	# 	if n == 0:
	# 		return 0
	# 	if n % 2 == 0:
	# 		return n + even_sum(n-2) 
	# 	else:
	# 		return even_sum(n-1)
	# print(even_sum(6))

## sum of odd numbers.

	# def odd_sum(n):
	# 	if n == 1:
	# 		return 1
	# 	if n % 2 != 0:
	# 		return n + odd_sum(n-2) 
	# 	else:
	# 		return odd_sum(n-1)
	# print(odd_sum(6))

## problems on recurrsion

	#1.fabinocci series
	#2.factorial of a number

## 1.fabinocci series

	# def fib(n):
	# 	if n == 0:
	# 		return 0
	# 	if n == 1:
	# 		return 1
	# 	return fib(n-1) + fib(n-2) 
	# print(fib(6))

## 2.factorial of a number

	# def factorial(n):
	# 	if n == 1:
	# 		return 1
	# 	return n * factorial(n-1)
	# print(factorial(4))

## 3.sum of elements in a list

	# def sum(l):
	# 	if len(l) == 1:
	# 		return l[0]
	# 	return l[0] + sum(l[1:])
	# print(sum([2,3,4]))

## 4.sum of alternative elements in a list.
	
	## case - 1

	# def alternate(l):
	# 	if len(l) <= 2:
	# 		return l[0]
	# 	return l[0] + alternate(l[2:])
	# print(alternate([10,20,30,40,50]))


	## case - 2

	# def alternate(l):
	# 	if len(l) <= 2:
	# 		return l[0]
	# 	if len(l) % 2 == 0:
	# 		return l[len(l)-2] + alternate(l[:len(l)-2])
	# 	else:
	# 		return l[len(l)-1] + alternate(l[:len(l)-1])
	# print(alternate([10,20,30,40,50]))

## 5.sum of elements in list of lists.
	
	## case - 1

	# def sum_of_list_items(l):
	# 	sum = 0
	# 	for each in l:
	# 		if type(each) == list:
	# 			sum = sum + sum_of_list_items(each)
	# 		else:
	# 			sum = sum + each
	# 	return sum
	# print(sum_of_list_items([1,2,[3,4],[5,6]])) 

	## case - 2

	# sum = 0
	# def sum_of_list_items(l):
	# 	global sum
	# 	for each in l:
	# 		if type(each) == int:
	# 			sum = sum + each
	# 		else:
	# 			if type(each) == list:
	# 				sum_of_list_items(each)
	# 	return sum
	# print(sum_of_list_items([1,9,[2,6,3,[5,0,[12,[],60,1],[],4]],5,1,[9,4]]))


## 6.sum of a non-negative integer.

	# def sum_of_integer(n):
	# 	if n == 0:
	# 		return 0
	# 	else:
	# 		return n % 10 + sum_of_integer(int(n/10))
	# print(sum_of_integer(123))


## 7.calculate the value of 'a' to the power of 'b'. 
	# a = 3,b = 4

	## case - 1

	# def power(a,b):
	# 	if b == 0:
	# 		return 1
	# 	if a == 0:
	# 		return 0
	# 	else:
	# 		return a * power(a,b-1)
	# print(power(3,1))

	## case - 2

	# def power(a,b):
	# 	result = 1
	# 	for i in range(b):
	# 		result = result * a
	# 	return result
	# print(power(3,4))

## 8.hormonic sum is the sum of reciprocals.
	# 1 + 1/2 + 1/3 + ...

	# def hormonic_sum(n):
	# 	if n == 0:
	# 		return 0
	# 	else:
	# 		return 1/n + hormonic_sum(n-1)
	# print(hormonic_sum(4))


#	# def replace_next_element(l1,l2):
	# 	for i in range(len(l1)):
	# 		if l1[i] in l2 and l1[i] != l2[len(l2)-1] and l1[i] != l1[len(l1)-1]:
	# 			l1[i] = l1[i+1]
	# 		else:
	# 			l1[i] = -1
	# 	return l1
	# print(replace_next_element([2,1,4],[1,4,3,2]))






















