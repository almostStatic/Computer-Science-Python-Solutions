'''
Ask the user to enter three numbers.  Add together the first two numbers and then multiply this total by the third.  Display the answer
'''
def fn():
	n1 = int(input('Please enter your first number: '))
	n2 = int(input("Please enter your second number: "))
	n3 = int(input("Please enter your third number: "))
	ans = (n1 + n2) * n3;
	print("Answer: " + str(ans))