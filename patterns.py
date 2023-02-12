# 1.* * * * *
#   * * * * *
#   * * * * *
#   * * * * *
#   * * * * *
def stars(n):
	for i in range(n):
		print"* "*n
stars(5)

# 2.*
#   * *
#   * * *
#   * * * *
#   * * * * *
def stars2(n):
	for i in range(1,n+1):
		print"* "*i
# stars2(5)

# 3.    *
#      **
#     ***
#    ****
#   *****     
def stars3(n):
	for i in range(1,n+1):
		print(" "*(n-i)+"*"*i)
# stars3(5)

# 4.    *
#      * *
#     * * *
#    * * * *
#   * * * * *
def stars4(n):
	for i in range(1,n+1):
		print(" "*(n-i)+"* "*i)
# stars4(5)

# 5.    *
#      * *
#     * * *
#    * * * *
#   * * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
def stars5(n):
	for i in range(1,n+1):
		print(" "*(n-i)+"* "*i)
	for i in range(n,0,-1):
		print(" "*(n-i)+"* "*i)
# stars5(5)

# 6.    *
#      * *
#     * * *
#    * * * *
#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
def stars6(n):
	for i in range(1,n+1):
		print(" "*(n-i)+"* "*i)
	for i in range(n-1,0,-1):
		print(" "*(n-i)+"* "*i)
# stars6(5)

# 7.* * * * *
#    * * * *
#     * * * 
#      * *
#       *
def stars7(n):
	for i in range(n,0,-1):
		print(" "*(n-i)+"* "*i)
# stars7(5)

# 8.* * * * *
#     * * * *
#       * * *
#         * *
#           *
def stars8(n):
	for i in range(n,0,-1):
		print("  "*(n-i)+"* "*i)
# stars8(5)

# 9.* * * * *
#   * * * *
#   * * *
#   * *
#   *
def stars9(n):
	for i in range(n,0,-1):
		print("* "*i)
# stars9(5)

# 10.*
#    * *
#    * * *
#    * * * *
#    * * * * *
#    * * * *
#    * * * 
#    * *
#    *
def stars10(n):
	for i in range(1,n+1):
		print("* "*i)
	for i in range(n-1,0,-1):
		print("* "*i)
# stars10(5)

# 11.        *
#          * *
#        * * *
#      * * * *
#    * * * * *
#      * * * *
#        * * *
#          * *
#            *
def stars11(n):
	for i in range(1,n+1):
		print("  "*(n-i)+"* "*i)
	for i in range(n-1,0,-1):
		print("  "*(n-i)+"* "*i)
# stars11(5)

#12.
def stars12(n):
	for i in range(n):
		for j in range(n+1):
			if (i == 0 and j % 3 != 0) or (i == 1 and j % 3 ==0) or (i - j == 2) or (i + j == n + 2):
				print"*"
			else:
				print" "
# stars12(6)

#13.
def stars13(num):
	n = num//2
	for i in range(n):
		for j in range(n-i-1):
			print(" ")
		for j in range(i+1):
			print("* ")
		if num%2 == 0:
			for j in range(2*(n-i-1)):
				print(" ")
		else:
			for j in range(2*(n-i-1)+1):
				print(" ")
		for j in range(i+1):
			print("* ")
	for i in range(n,0,-1):
		for j in range(n-i):
			print(" ")
		for i in range(i,0,-1):
			print("* ")
# stars13(8)

#14.
def printings(n):
	for i in range(n+1):
		if i == 1 or i == 2:
			print"*"
		elif i == 4 or i == 5:
			print" "*(n-1)+"*"
		else:
			print("*" * n)
printings(6)
