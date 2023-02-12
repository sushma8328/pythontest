# x = []
# def adds(y):
# 	print(x)
# 	x = 30
# 	y.append(x)
# 	return x,y
# 	print(10)
# z = x
# print(adds(z))
# print(x)


# a = 10
# b = a 
# def add(a):
# 	print(a)
# 	x = 100
# 	return a + b
# s = add(b)
# print(s)
# add(s)
# print(add(a))


# x = 100
# def aim(a,b):
# 	print(a)

# 	def sum(a):
# 		print(x)
# 		return x + a
# 	return x + a
# 	print(sum(20))

# s = aim(x,x+10)
# print(aim)


# B = 100
# def cal(a):
# 	x = 10
# 	print(10 + x)
# 	c = a
# 	return B * a
# print(cal(2))
# cal(20)


# class A:
# 	x = 0
# 	a = 10
# 	def __init__(self, a, b):
# 		self.a = a 
# 		self.b = b

# class B(A):
# 	def add(self):
# 		return self.a + self.b 

# class C(B):
# 	def test(self,c):
# 		y = 6
# 		return self.add()

# 	def p_test(self):
# 		self.add()
# 		return self.test(1)

# a1 = C(3,4)
# x = a1.p_test()
# print(a1.add())

# print(x + x)
# y = x
# z = x + 2



# class X:
# 	"abc"
# 	a = 10

# 	def greet():
# 		print('hello')
# 	v = greet()
# 	print(v)
# print(X.a)
# print(X.greet())
# print(X.v)


# class V:

# 	def gem(self):
# 		self.a = x
# 		self.b = "monk"

# 	def __init__(self):
# 		self.a = 10
# 		b = 200
# 		self.b = 50
# 		print("ccc")

# v1 = V()
# print(v1.a)
# print(v1.b)


# class R:

# 	def __init__(self):
# 		x = 2
# 		self.x = 20

# 		def min(aa,a,b):
# 			a = x * x
# 			b = a * x
# 			print(a+b)
# 			print(a+x)
# 		print(min(4,5,6))

# r1 = R()		
# print(r1)


# class C:

# 	def __init__(self):
# 		self.a = 3
	
# 	@classmethod
# 	def app(self):
# 		self.i = 10
# 		self.j = 20
# 		return self.i*self.j

# s1 = C()
# print(C.app())

# class K:
# 	pass

# a = K()

# class S:
# 	x =3
# 	a = 100
# 	print("sss")
# c = S()


# class T:
# 	c = 100
# 	print("ss")
# 	def __init__(self):
# 		self.a = 10
# 		self.b = self.c
# t1 = T()
# t1.d =20
# print(t1)
# T.c = 200
# print(t1.c)


# class K:
# 	x = 50

# 	def add(a):
# 		x = a.b 
# 		print("abc")
# 		return x
# class L(K):
# 	def __init__(self,b,c):
# 		self.b = 10 * b
# 		self.q = c * self.b
# 		print(self.b - b)

# k1 = L(2,3)
# print(L.add(k1))
# print(k1.q)

# x = 3
# def get(x):
# 	return x

# def add(a, b=get(9), c=x):
# 	print(a)
# 	print(b)
# 	print(c)

# add(2)

# z = 10
# def add(a,b = 10):
# 	return a + add(5)
# print(add(z,3))


# def sub(a):
# 	return a*a 
# def sub2(a,b=10):
# 		return a*sub(2)
# print(sub(sub2(3)))


# def max(add,b):
# 	print("ss")
# 	def add(m,n = 4):
# 		return m * b
# 	s = add
# 	return add(6) * 2 + b -s(3)
# print(max(3,4))


# class B:
# 	a = 100
# 	b = "xyz"
# 	def fun(cls):
# 		return a * 10, b
# class C(B):
# 	m = a + 100
# 	n = b + "abc"
# 	def __init__(self,x):
# 		self.p = m + x
# 		self.q = "s" + n 
# 	def add(self):
# 		return c1.p + c1.q
# c1 = C(10)
# print(c1.add())
# print(B.fun())


# class X:
# 	a = 10
# 	b = 20
# 	def __init__(self):
# 		self.a = 100
# 		self.b = 50
# class Y(X):
# 	def __init__(self,a,b):
# 		self.x = 2
# 	@classmethod
# 	def add(self):
# 		return z1.a * self.b
# class Z(Y):
# 	def sub(self):
# 		print("abc")
# 		return z1.b * 20
# z1 = Z(3,4)
# print(z1.sub())
# print(z1.add())
# print(z1.a + z1.b + z1.x)



# class G:
# 	shape = "cuboid"
# 	height = 20
# 	width = 30
# 	def __init__(self):
# 		self.height = 30
# 		self.shape = "cube"
# g1 = G()
# print(g1.shape)
# print(g1.height)
# print(g1.width)
# print(G.shape)
# print(G.height)
# print(G.width)


# def add(*args, **kwargs):
# 	a = 0
# 	b = 0
# 	c = 9
# 	if len(args) > 2:
# 		a = args[0]
# 		b = args[1]
# 	if 'c' in kwargs:
# 		c = kwargs['c']
# 	print(a)
# 	print(b)
# 	print(c)

# l = [1,2]
# d = {"c":1,"d":2}

# def test(a,b, c=9):
# 	pass

# add(*[3,4,5,6,7,8], **{'c': 4, 'd': 5})
# add(*[], **{'c': 4})



# x = 20
# def fun(a,b,c = 10):
# 	return a,b,c 
# print(fun(2,3,x))



# def add(a,b):
# 	return a,b
# print(add(*[1,2,3],**{'a':4,'b':5}))


# def add2(*a,**b):
# 	return a[0],b['a']
# print(add2(*[1,2,3],**{'a':4,'b':5}))


# def add3(*a,**b):
# 	a = a[2]
# 	b = b['a']
# 	return a,b
# print(add3(*[1,2,3],**{'a':4,'b':5}))


# def add4(*a,**b):
# 	a = *a
# 	b = **b
# 	return a[2],b['a']
# l = [2,3,4,5]
# d = {'a':6,'b':7,'c':8}
# print(add4(*[1,2,3],**{'a':4,'b':5}))



# def add4(*a,**b):
# 	return *a,**b
# l = [2,3,4,5]
# d = {'a':6,'b':7,'c':8}
# print(add4(*l,**d))


# def add5(*a,**b):
# 	return a[2],b['a']
# l = [2,3,4,5]
# d = {'a':6,'b':7,'c':8}
# print(add5(*l,**d))


# def add6(*a,b):
# 	return a[2],b['a']
# l = [2,3,4,5]
# d = {'a':6,'b':7,'c':8}
# print(add6(*l,d))
	

# def add7(*a,b = {'a':1}):
# 	return a[2],b['a']
# l = [2,3,4,5]
# d = {'a':6,'b':7,'c':8}
# print(add7(*l,**d))


# class A:
# 	def fun(self,a):
# 		e = 0
# 		for each in range(a):
# 			if each%2 == 0:
# 				e = e + each
# 		return e

# a1 = A()
# print(a1.fun(20))																



class D:
	def change_values(self,d):
		for k,v in d.items():
			# if type(d[k]) == type(str) and d[k].isdigit():
			d[k] = int(v)
		return d 
d1 = D()
# print(d1.change_values({'a':"ab",'b':20,'c':"30"}))


def students(list1):
	sec_lowest = []
	lowest = []
	s = []
	for each in list1:
		if not lowest:
			lowest = each
		elif each[1] < lowest[1]:
			sec_lowest = lowest
			lowest = each
		elif not sec_lowest:
			sec_lowest = each
	# s.append(sec_lowest[0])
	# list1.remove(lowest)
	# list1.remove(sec_lowest)
	for each in list1:
		if each[1] == sec_lowest[1]:
			s.append(each[0])
	s.sort()
	return s
# print(students([['Harry', 19], ['Berry', 21], ['Tina', 19], ['Akriti', 19], ['Harsh', 20]]))

        
    # lowest = []
    # sec_lowest = []
    # for each in input():
    #     if not lowest:
    #         lowest = each
    #     elif each[1] < lowest[1]:
    #         sec_max = lowest
    #         lowest = each
    #     elif not sec_max:
    #         sec_max = each
    #     elif each[1] < sec_max[1]:
    #         sec_max = each    
    # for each in input():
    #     if each[1] == sec_max[1]: 
    #         print(each[1])


# def list(l):
# 	l.insert(0,5)
# 	l.insert(1,10)
# 	l.insert(0,6)
# 	print(l)
# 	l.remove(6)
# 	l.append(9)
# 	l.append(1)
# 	l.sort()
# 	print(l)
# 	l.pop()
# 	l.reverse()
# 	print()
# 	return l  
# print(list([]))


customer_data = [[6,55],[6,45],[6,55],[4,40],[18,60],[10,50]]
def list2(l):
	d = {}
	for each in l:
		if each not in d:
			d[each] = 1
		else:
			d[each] = d[each] + 1
	return d 
# print(list2([2 ,3, 4, 5, 6, 8, 7, 6, 5, 18]))


def sum(shoe_pairs,shoe_price):
	total_amount = 0
	for each in shoe_price:
		if each[0] in shoe_pairs:
			total_amount = total_amount + each[1]
			shoe_pairs.remove(each[0])
	return total_amount
# print(sum([2,3,4,5,6,8,7,6,5,18],[[6,55],[6,45],[6,55],[4,40],[18,60],[10,50]]))



def count_sub_strings(s,s1):
	count = 0
	l = len(s1) 
# print(count_sub_strings('ABCDCDC','CDC'))


def mutate_string(string, position, character):
	l = list(string)
	l[position] = character
	return ''.join(l)
# print(mutate_string('abracadabra',5,'k'))



def divisibleSumPairs(n, k, ar):
	count = 0
	for each in range(n):
		for i in range(each+1,n):
			if (ar[each] + ar[i]) % k == 0:
				count = count + 1
	return count
# print(divisibleSumPairs(6,3,[1,3,2,6,1,2]))


# def diagonalDifference(n,arr):
# 	# Write your code here
# 	left = 0
# 	right = 0
# 	# import pdb;pdb.set_trace()
# 	for i in range(len(arr)):
# 		left = left + arr[i][i]
# 	for i in range(len(arr)):
# 		right = right + arr[i][len(arr)-i-1]    
# 	return left - right
# print(diagonalDifference(3,[[11, 2, 4], [4, 5, 6], [10, 8, -12]]))


## camel case

# import sys
# input_data = []
# for each in sys.stdin:
# 	input_data.append(each.strip())
# s = ''

# for each in input_data:
# 	if each[0] == 'S':
# 		s1 = ''
# 		if each[2] == 'M':
# 			for e in each[4:-2]:
# 				if e.isupper():
# 					s1 = s1 + ' ' + e.lower()
# 				else:
# 					s1 = s1 + e
# 			sys.stdout.write(s1)
# 			print('\n')
# 		elif each[2] == 'C':
# 			s2= each[4:]
# 			for e in range(len(s2)):
# 				if e == 0:
# 					s1 = s1 + s2[e].lower()
# 				else:
# 					if s2[e].isupper():
# 						s1 = s1 + ' ' + s2[e].lower()
# 					else:
# 						s1 = s1 + s2[e]
# 			sys.stdout.write(s1)
# 			print('\n',end='')
# 		elif each[2] == 'V':
# 			for e in each[4:]:
# 				if e.isupper():
# 					s1 = s1 + ' ' + e.lower()
# 				else:
# 					s1 = s1 + e
# 			sys.stdout.write(s1)
# 			print('\n',end='')
# 	else:
# 		s1 = ''
# 		if each[2] == 'M':
# 			s2 = each[4:].split(' ')
# 			s1 = s2[0]
# 			for e in range(1,len(s2)):
# 				s1 = s1 + s2[e][0].upper() + s2[e][1:]              
# 			sys.stdout.write(s1 + '()')
# 			print('\n',end='')
# 		elif each[2] == 'C':
# 			s2 = each[4:].split(" ") #["code", "swam"]

# 		# case 1

# 		# data = []
# 		# for e in range(len(s2)):
# 		# 	data.append(s2[e][0].upper() + s2[e][1:])
# 		# s1 = "".join(data)

# 		# case 2

# 		# for e in range(len(s2)):
# 		# 	if e == 0:
# 		# 		s1 = s1 + s2[e][0].upper() + s2[e][1:]
# 		# 	else:
# 		# 		s1 = s1 + s2[e][0].upper() + s2[e][1:]
# 		# case 3

# 		def make_capital(x):
# 			return x[0].upper() + x[1:]
# 		s_list = list(map(make_capital, s2))
# 		s1 = "".join(s_list)

# 		sys.stdout.write(s1)
# 		print('\n',end='')

# def miniMaxSum(arr):
# 	# Write your code here
# 	s = 0
# 	for i in range(len(arr)):
# 		s = s + arr[i]
# 	return s - arr[-1]
# print(miniMaxSum([1,3,5,7,9]))


# def bill(b):
# 	if b <= 50:
# 		return (b*1)
# 	elif b > 50 and b <= 100:
# 		return (b * 1) + ((b-50)*2)
# 	elif b > 100 and b <= 150:
# 		return (b * 1) + ((b-50)*2) + ((b-100)*3)
# 	elif b > 150 and b <= 200:
# 		return (b * 1) + ((b-50)*2) + ((b-100)*3) + ((b-150)*4)
# 	else:
# 		return (b * 1) + ((b-50)*2) + ((b-100)*3) + ((b-150)*4) + ((b-200)*5)
# print(bill(60))


def bill2(b):
	if b <= 50:
		return (b*1)
	elif b > 50 and b <= 100:
		return (50 * 1) + ((b-50)*2)
	elif b > 100 and b <= 150:
		return (50 * 1) + (50*2) + ((b-100)*3)
	elif b > 150 and b <= 200:
		return (50 * 1) + (50*2) + (50*3) + ((b-150)*4)
	else:
		return (50 * 1) + (50*2) + (50*3) + (50*4) + ((b-200)*5)
# print(bill2(160))

def countSort(arr):
    # Write your code here
    # for i in range(1,len(arr)):
		# if arr[i][0] < arr[i-1][0]:
			# arr[i],arr[i-1] = arr[i-1],arr[i]
	l = []
	for i in range(len(arr)):
		l.append([])
	for i in range(len(arr)//2):
		l[int(arr[i][0])].append('-') 
	for i in range(len(arr)//2,len(arr)):
		l[int(arr[i][0])].append(arr[i][1])
	for string in l:
		if string:
			print(*string,end=' ')
# print(countSort([]))

def merge_the_tools(string, k):
	# import pdb; pdb.set_trace()
    # your code goes here
	for i in range(0,len(string),k):
		s = ''
		for e in string[i:i+k]:
			if e not in s:
				s = s + e
		print(s)
# merge_the_tools('AABCAAADA',3)


# import pdb; pdb.set_trace()
# x = [5, 899954391,390010037, 470009874, 789620942, 589990574]
# maxi = 0
# s2 = 0
# for e in range(1,len(x)):
# 	if int(x[e]) > s2:
# 		s2 = int(x[e])
# maxi = maxi + (s2*s2)
# print(maxi % 384)


# n = '1 2 3 4 '
# arr = list(map(int, n.rstrip().split()))
# print(" ".join(map(str,arr[::-1])))


class Person:
	def __init__(self,x):
		if x > 0:
			self.x = x
		else:
			print('Age is not valid')
	def yearPasses(self):
		self.x = self.x + 1
	def amIOld(self):
		if self.x > 0 and self.x <= 10:
			print('you are young')
		elif self.x > 10 and self.x <= 20:
			print('you are a teenager')
		else:
			print('you are older')
# p1 = Person(10)
# p1.yearPasses()
# p1.amIOld()


def divisibleSumPairs(ar,k):
	l = []
	for i in range(len(ar)):
		for j in range(i+1,len(ar)):
			if (ar[i] + ar[j]) % k == 0:
				l.append([ar[i],ar[j]])
	return l
#print(divisibleSumPairs([1,2,3,4,5,6],5))

def reduce(number):
	# import pdb;pdb.set_trace();
	if int(number/10) == 0:
		return number
	new_number = 0
	while (number >= 1):
		new_number +=number%10
		number = int(number/10)
	return reduce(new_number)

# print(reduce(9875))
# print(reduce(123))
# print(reduce(48))

## difference between diagonals
def matrix(l):
	s1 = 0
	s2 = 0
	for i in range(len(l)):
		s1 = s1 + l[i][i]
	# for i in range(len(l)):
		s2 = s2 + l[i][len(l)-i-1]
	if s1 > s2:
		return s1-s2
	return s2-s1

## case - 2
def difference(arr):
	d1 = 0
	d2 = 0
	for i in range(0,n):
		for j in range(0,n):
			if (i==j):
				d1 += arr[i][j]
			if (i == n-j-1):
				d2 += arr[i][j]
	return d1-d2
# print(matrix([[11,-2,4],[4,5,6],[10,8,-12]]))


## count valleys
def countingValleys(n,s):
	level = valley = 0
	for i in range(n):
		if s[i] == 'U':
			level += 1
			if level == 0:
				valley += 1
		else:
			level -= 1
	return valley 
# print(countingValleys(8,'UDDDUDUU'))

## reverse the list
def array(a):
	l = []
	for i in range(1,len(a)+1):
		l.append(str(a[-i]))
	return l
# print(array([1,2,3,4,5,6]))

## table
def table(t,n):
	for i in range(1,n+1):
		print(t+' * '+str(i)+' = ', end='')
		print(int(t)*i)
# table('13',10)

def mealcost(cost,tip,tax): 
	return round(cost + (cost * (tip/100)) + (cost * (tax/100)))
# print(mealcost(12,20,8))


def isBalanced(s):
	stack = []
	balanced_dict = {'}':'{',']':'[',')':'('}
	for each in s:
		if not stack:
			stack.append(each)
		elif each not in balanced_dict:
			stack.append(each)
		elif balanced_dict[each] == stack[-1]:
			stack.pop()
		else:
			stack.append(each)
	if stack:
		return 'NO'
	else:
		return 'YES'		
# print(isBalanced('{{[[(())]]}}'))

## apples and oranges
def countapplesandoranges(s, t, a, b, apples, oranges):
	acount = 0
	bcount = 0
	# for i in range(len(apples)):
	# 	temp = a + apples[i]
	# 	if (temp in range(s, t + 1)):
	# 		acount += 1
	# for i in range(len(oranges)):
	# 	temp = b + oranges[i]
	# 	if (temp in range(s, t + 1)):
	# 		bcount += 1

	## case - 2
	# for each in apples:
	# 	x = a + each
	# 	if x >=7 and x <= 10:
	# 		acount += 1
	# for each in oranges:
	# 	y = b + each
	# 	if y >= 7 and y <= 10:
	# 		bcount += 1

	## case - 3
	for each in apples:
		if s <= a + each <= t:
			acount += 1
	for each in oranges:
		if s <= b + each <= t:
			bcount += 1

	print(acount)
	print(bcount)
# countapplesandoranges(7,11,5,15,(-2,2,1),(5,-6))

## array manipulation
def arraymanipulation(n,queries):
	l = []
	max = 0
	for i in range(n):
		l.append(0)
	for a,b,k in queries:
		for i in range(a-1,b):
			l[i] += k
		if l[i] > max:
			max = l[i]
	return max
# print(arraymanipulation(7,[[1,2,100],[2,5,100],[3,4,100]]))


## between two sets


## birthday cake candles
def candle(l):
	count = 0
	s = 0
	for i in range(len(l)):
		if l[i] > s:
			s = l[i]
	for e in l:
		if e == s:
			count += 1
	return count
# print(candle([3,2,1,3]))

# l = []
def unique_values(d):
	global l
	for k in d:
		if type(d[k]) == dict:
			unique_values(d[k])
		else:
			if type(d[k]) == str:
				for e in d[k]:
					if e.isdigit():
						if int(e) not in l:
							l.append(int(e))
			if type(d[k]) == list:
				for e in d[k]:
					if type(e) == int:
						if e not in l:
							l.append(e)

	return l
# print(unique_values({1:[1,5,3,1],2:{5:'76',6:[4,5,6]},3:"90510",4:"3129"}))


## bon appetit
def bon_appetit(ind,l,b):
	sum1 = 0
	for i in range(len(l)):
		if i != ind:
			sum1 = sum1 + l[i]
	if sum1//2 == b:
		return "bon appetit"
	else:
		return b - sum1//2
# print(bon_appetit(1,[3,10,2,9],7))


## bubble sorting
def bubble_sort(l):
	count = 0
	for i in range(len(l)-1):
		for i in range(len(l)-1):
			if l[i] > l[i+1]:
				l[i],l[i+1] = l[i+1],l[i]
				count += 1

	## case - 2
	# for i in range(len(l)):
	# 	for j in range(len(l)-1):
	# 		if l[j] > l[j+1]:
	# 			temp = l[j]
	# 			l[j] = l[j+1]
	# 			l[j+1] = temp
	# 			count += 1

	return l,count
# print(bubble_sort([5,1,4,2,3,6,4,7,8,0,-1,-4,-7,10,-5]))


## cats and a mouse
def cat_and_mouse(a,b,c):
	catA = abs(a-c)
	catB = abs(b-c)
	if catA == catB:
		return "Mouse C"
	if catA < catB:
		return "Cat A"
	else:
		return "Cat B"
# print(cat_and_mouse(1,4,2))


## day of the programmer
def day_of_the_programmer(year):
	if year == 1918:
		return '26.09.2018'
	elif(year < 1917 and year % 4 == 0) or ((year > 1918)and(year % 400 == 0 or(year % 4 == 0 and year % 100 != 0))):
		return '12.09.'+str(year)
	else:
		return 	'13.09.'+str(year)	

# print(day_of_the_programmer(1915))

## decimal to binary
def decimal_to_binary(n):
	s = ''
	while n:
		r = n % 2
		s = s + str(r)
		n = n//2
	return s[::-1]
# print(decimal_to_binary(100))

## designer pdf viewer
def designer_pdf_viewer(l, word):
    maxi=0
    for i in range(len(word)):
        if(maxi< l[ord(word[i])-97]):
            maxi = l[ord(word[i])-97]
    return maxi*len(word)
# print(designer_pdf_viewer([1,2,3,4,5],'aza'))


## electronic shop
def electronic_shop(b,k,m):
	maxi = -1
	for i in range(len(k)):
		for j in range(len(m)):
			if k[i] + m[j] <= b:
				maxi = max(maxi,k[i] + m[j])
	return maxi
# print(electronic_shop(8,[2,5,4],[10,3,5]))


## exception of string to int
def exception(s):
	try:
		print(int(s))
	except ValueError:
		print('Bad String')
# exception('3')


## magic square
def magic_square(s,magic):
	# s = sum(s,[])
	# mini_cost = sys.maxsize
	# for each in magic:
	# 	d = 0
	# 	for i,j in zip(s,magic):
	# 		d += abs(i-j)
	# 	mini_cost = min(mini_cost,d)
	# return mini_cost

	## case - 2        
    l = []
    for each in magic:
        ab = 0
        for i,j in zip(each,s):
            for x,y in zip(i,j):
                ab += max([x, y]) - min([x, y])
        l.append(ab)
    return min(l)

# print(magic_square([[4,9,2],[3,5,7],[8,1,5]],[[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
									            # [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
									            # [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
									            # [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
									            # [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
									            # [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
									            # [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
									            # [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]))


## fractions
def add(arr):
	negative_count = 0
	positive_count = 0
	zero_count = 0
	for ele in arr:
		if ele > 0:
			positive_count += 1
		elif ele < 0:
			negative_count += 1
		else:
			zero_count += 1
	print(positive_count / len(arr))
	print(negative_count / len(arr))
	print(zero_count / len(arr))
# add([1,2,3,-8,0,0])


## jumping on the clouds
def cloud(c):
	jump = 0
	i = 0
	while i < len(c)-1:
		if i+2 < len(c) and c[i+2] == 0:
			jump += 1
			i += 2
		elif i+1 < len(c) and c[i+1] == 0:
			jump += 1
			i += 1
	return jump

	## case - 2
	# i = 0
	# jumps = 0
	# try :
	# 	while i < len(c)-1:
	# 		if c[i+2] == 1 or i + 2 >= len(c):
	# 			i += 1
	# 			jumps += 1
	# 		else :
	# 			i += 2
	# 			jumps += 1
	# except IndexError:
	# 	i += 1
	# 	jumps += 1
	# return jumps

# print(cloud([0,0,1,0,0,1,0]))


## kangaroo
def kangaroo(x1,v1,x2,v2):
	# if x1 < x2 and v1 < v2:
	# 	return 'NO'
	# else:
	# 	if v1 != v2 and (x2-x1)%(v1-v2) == 0:
	# 		return 'YES'
	# 	else:
	# 		return 'NO'

	## case - 2
	for i in range(10000):
		if ((x1 + v1) == (x2 + v2)):
			return "YES"
		x1 += v1
		x2 += v2
	return "NO"

# print(kangaroo(0,3,4,2))


## list comprehension
def sock_merchant(ar):
	ar.sort()
	previous = ar[0]
	count = 0
	pairs = 0
	for each in range(len(ar)):
		if previous != ar[each]:
			previous = ar[each]
			pairs += count // 2
			count = 1
		elif each +1 == len(ar):
			count += 1
			pairs += count // 2
		else :
			count += 1
			previous = ar[each]
	return pairs
# print(sock_merchant([10,20,30,40,20,20,10,10,30,40]))


## maximum element using stack 
def stack(l):

	# stack = []
	# for i in range(len(l)):
	# 	if l[i][0] == 1:
	# 		if stack:
	# 			stack.append(max(stack[-1],l[i][1]))
	# 		else:
	# 			stack.append(l[i][1])
	# 	elif l[i][0] == 2:
	# 		stack.pop()
	# 	else:
	# 		print(stack[-1])

	## case - 2
	stacklist = []
	max = None
	l1 = []
	for each in l:
		if each[0] == 1:
			if max is None:
				max = each[1]
			elif each[1] > max:
				max = each[1]
			stacklist.append([each[1], max])
		elif each[0] == 2:
			stacklist.pop()
			if stacklist:
				max = stacklist[-1][1]
			else:
				max = None
		else:
			l1.append(stacklist[-1][1])
	return l1

# print(stack([[1,97],[2],[1,20],[2],[1,26],[1,20],[2],[3],[1,91],[3]]))


## migratory birds
def migratory_birds(arr):
	# l = [0] * len(arr)
	# for i in range(len(arr)):
	# 	l[arr[i]] += 1
	# return l.index(max(l))

	# case - 2
	bird_frequency =[0,0,0,0,0,0,0]
	for i in range(len(arr)):
		bird_frequency[arr[i]] += 1
	return bird_frequency.index(max(bird_frequency))

# print(migratory_birds([1,2,2,2,4,5,1,3,6]))

## mini max sum
def mini_max_sum(arr):
    # Write your code here
	arr.sort()
	s = 0
	for i in range(len(arr)):
		s = s + arr[i]
	print(s-arr[-1],end = ' ')
	print(s-arr[0])
# mini_max_sum([1,3,5,7,9])

## strings and queries
def matching_strings(strings, queries):
	count = 0
	final_list = []
	for each_query in range(len(queries)):
		for each_string in range(len(strings)):
			if queries[each_query] == strings[each_string]:
				count += 1
		final_list.append(count)
		count = 0
	return final_list
# print(matching_strings(['ab','cd','ef','rt','op','gh'],['xy','ab','dg','ef']))


## phonebook
def phonebook(l,f):
	phonebook = {}
	for each in l:
		if each[0] not in phonebook:
			phonebook[each[0]] = each[1]

	while True:
		try:
			if f in phonebook:
				print("{}={}".format(f, phonebook[f]))
			else:
				print("Not found")
		except EOFError:
			break
# phonebook([['a','123'],['b','456'],['a','456']],'c')


## picking numbers
from collections import Counter 
def pickingNumbers(a):
	# maximum = 0
	# diff = 1
	# for k in a:
	# 	n1 = a.count(k)
	# 	n2 = a.count(k-diff)
	# 	maximum = max(maximum, n1+n2)
	# return maximum

	## case - 2
	arr = Counter(a)
	maxi_num = 0
	for i in range(100):
		maxi_num = max(maxi_num, arr[i]+arr[i+1])
	return maxi_num

# print(pickingNumbers([3,3,4,1]))


## compare the triplets
def triplets(a,b):
	a1 = b1 = 0
	for i in range(3):
		if a[i] > b[i]:
			a1 += 1
		elif a[i] < b[i]:
			b1 += 1
	return a1,b1
# print(triplets([5,6,7],[3,6,10]))


## repeated string 
def repeated_string(s,n):
	total = 0
	for i in s:
		if i == 'a':
			total += 1
	total = n//len(s) * total 
	for i in s[:n%len(s)]:
		if i == 'a':
			total += 1
	return  total
# print(repeated_string('aba',10))


## reverse array
def reverse_array(a):
	start = 0
	end = len(a)-1
	while start < end :
		a[start],a[end] = a[end],a[start]
		start += 1
		end -= 1
	return a
# print(reverse_array([1,2,3,4,5]))


## scope(maximum difference)
class Difference:
	
	def __init__(self, a):
		self.__elements = a
		self.maximumDifference = 0

	def computeDifference(self):
		for i in a:
			for j in a:
				if self.maximumDifference < i-j:
					self.maximumDifference = i-j
# a = [1,2,5]
# d = Difference(a)
# d.computeDifference()
# print(d.maximumDifference)


## simple text editor
def text_editor(l):
	stack = []
	string = ''
	for i in range(len(l)):
		if l[i][0] == 1:
			string += str(l[i][1])
			stack.append(len(str(l[i][1])))
		if l[i][0] == 2:
			stack.append(string[-int(l[i][1]):])
			string = string[:-int(l[i][1])]
		if l[i][0] == 3:
			print(string[int(l[i][1]) - 1])
		if l[i][0] == 4:
			x = stack.pop()
			if type(x) is int:
				string = string[:-x]
			else:
				string += x
# text_editor([[1,'abc'],[3,3],[2,3],[1,'xy'],[3,2],[4],[4],[3,1]])


## stair case
def stair_case(n):
	# for i in range(1,n+1):
	# 	print(" "*(n-i)+"#"*i)

	## case - 2
	for i in range(1,n+1):
		s = '#' * i 
		print(s.rjust(n))
# stair_case(6)


## two dimensional array
def array_func(arr):
	final_count = -85236974002456
	total = 0
	for i in range(len(arr)-2):
		for j in range(len(arr[i])-2):
			total += (arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
			if final_count < total:
				final_count = total
				total = 0
			else:
				total = 0
	return final_count
# print(array_func([[-1,-1,-1,0,0,0], [0,-1,0,0,0,0], [-1,-1,-1,0,0,0], [0,-9,2,-4,-4,0], [-7,0,0,-2,0,0],[0,0,-1,-2,-4,0]


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

