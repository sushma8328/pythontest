l = [1,2,3,4,5]
a = [each for each in l if each % 2 == 0]
print(a)

# def add(a, b):
# 	"add two numbers"
# 	x = a + b
# 	z = x + a
# 	x = x * z
# 	def plus(a, b):
# 		return a + b
# 	return plus

# def test():
# 	print('test')
# # add(4,5)()


# # def num(l,v):
# # 	l.append(v)
# # 	return l
# # l1 = []
# # for i in range(5):
# 	# print(num(l1,i))



# # def cal(l,v):
# # 	l.append(v)
# # 	return l 
# # l1 = []
# # for i in range(5):
# # 	cal(l1,i)
# # 	print(l1)



# def fun(a,b,c,d):
# 	def sub(x,y):
# 		return x+y+a+c
# 	def mul(x, y):
# 		return x * y * a * c
# 	return sub, mul
# sub, mul = fun(2,3,4,5)
# # print(mul(1,1))
# # print(sub(1,2))
# # print(mul(1,3))
# # print(mul(1,4))
# # print(sub(1,5))
# # print(mul(1,6))

# def funn(a, b, c, d, x, y):
# 	return x + y + a + c
# # print(funn(2,3,4,5, 1,2))
# # print(funn(2,3,4,5, 1,3))
# # print(funn(2,3,4,5, 1,4))

# class A:
# 	d = 0
# 	def __init__(self, a, b, c, d):
# 		self.a = a
# 		self.b = b
# 		self.c = c
# 		self.d = d
# 	def sub(self, x, y):
# 		return self.a + self.b + x + y
# 	def mul(self, x, y):
# 		return self.a * self.b * x * y
# a = A(2,3,4,5)
# # print(a.sub(9,1))
# # print(a.sub(9,2))
# # print(a.sub(9,3))
# # print(a.mul(9,3))


# class S:
# 	def __init__(self,a,b):
# 		self.a = a
# 		self.b = b
# 	def add(self):
# 		return self.a*self.b
# x = S(5,2)
# # print(x.add())


# z = 50
# class S1:
# 	a = 10
# 	b = 2
# 	def __init__(self,a,b,c):
# 		self.a = b
# 		self.b = a
# 		self.x = 60
# 		self.dd = a * b
# 	def add(instance):
# 		print(instance)
# 		print(instance.a)
# 		print(instance.b)
# # S1(3,5,6).add()


# class B:
# 	x = 10
# 	y = 20
# 	def __init__(self,m,n):
# 		self.aa = m
# 		self.bb = m*n 
# 	def div(a):
# 		cc = a.aa * a.bb
# 		return cc
# b = B(2,3)
# # print(b.div())


# class C:
# 	x = 10
# 	y = 20
# 	def __init__(self,m,n):
# 		self.aa = C.y
# 		self.bb = C.x * n 
# 	def div(a):
# 		cc = a.aa * a.bb
# 		return cc
# c = C(2,3)
# # print(c.div())


# class D:
# 	x = 10
# 	y = 20
# 	def __init__(self,m,n):
# 		self.aa = C.y
# 		self.bb = C.x * n 
# 	def div(a):
# 		cc = D(10,20)
# 		return cc
# d = D(2,3)
# # print(d.div())


# class E:
# 	x = 10
# 	y = 20
# 	def __init__(self,m,n):
# 		self.aa = m 
# 		self.bb = n 
# 	def fun(instance):
# 		return instance.aa * instance.bb
# e1 = E(2,3) 
# # print(e1)
# # print(e1.fun())


# l = []
# x = 3
# y = 4
# def add(x, y , l):
# 	print(l)
# 	l.append(x)
# 	l.append(y)
# 	print(l)
# # print(add(5, [], l))
# # print(l)
# l.append(9)
# k = l
# # print(k)


# class Employee:
	
# 	def __init__(self,first,last,pay):
# 		self.first = first
# 		self.last = last 
# 		self.pay = pay
# 		self.email = first + '.' + last + '@gmail.com'

# 	def fullname(self):
# 		a = self.first,self.last,self.email,self.pay
# 		return a 

# emp_1 = Employee('sushma','animireddy','50,000')
# emp_2 = Employee('vasanthi','animireddy','50,000')
# emp_2.fullname()
# print(emp_1.email)
# print(emp_1.fullname())
# print(emp_2.fullname())
# print(Employee.fullname(emp_1))



# class student:
# 	rno = 123
# 	name = 'sushma'
# 	group = 'bca'
	
# 	def read(self):
# 		rno = 345
# 		print('rollno=',rno)
# 		print('instance variable=',self.rno)
# 		print('reading..')
# 	def write(self):
# 		print('writing..')

# abc = student()
# print('rno=',student.rno)
# print('name=',abc.name)
# print('group=',abc.group)
# abc.read()
# abc.write()

# class A:
# 	a = 3

# 	def __init__(self, a, b):
# 		self.x = a 
# 		self.y = b

# 	def add(self, a, b):
# 		return self.x * self.y * a * b

# 	@classmethod
# 	def c_add(cls, a, b):
# 		a = cls(a, b)
# 		return a

# print(dir())
# print('--------')
# print(dir(A))
# print("---------")
# a1 = A(1,2)
# print(dir(a1))


class A:
	def __init__(self,a_value):
		self.a = a_value
	def print_a(self):
		print("A value: ",self.a)
class B(A):
	def __init__(self,a_value,b_value):
		A.__init__(self,a_value)
		self.b = b_value
	def print_b(self):
		print("B value: ",self.b)
obj1 = B(10,20)
obj1.print_a()
obj1.print_b()


class Driver:
	def __init__(self,f_name,l_name,age,mobile_no):
		self.f_name = f_name
		self.l_name = l_name
		self.age =  age
		self.mobile_number = mobile_no

	def full_name(self):
		return f"{self.f_name} {self.l_name}"

class License(Driver):
	def __init__(self,f_name, l_name, age, mobile_no,License_id,validity):
		Driver.__init__(self,f_name,l_name,age,mobile_no)
		self.License_id = License_id
		self.validity = validity
	def is_valid_licence(self):
		if validity_year >= 2021:
			return True
		else:
			return False

user1_licence = Licence('user','one',20,1234,101,2022)
user2_licence = Licence('user','two',22,2534,102,20221)

print(user2_licence.full_name())
print("Eligibility of License: ")

		


