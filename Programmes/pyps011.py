'''
Task the user to enter a number over 100 and then enter a number under 10 and then tell them how many times the smaller number goes into the larger number in a user-friendly format
'''
def fn(): 
	num = int(input("Please enter a number greater than 100: "))
	small = int(input("Please enter a number less than 10: "))
	goesinto = num / small;
	print(str(small) + " goes into " + str(num) + ": " + str(goesinto) + " times") # 1 goes into 100: 100 times