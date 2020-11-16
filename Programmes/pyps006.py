'''
Ask how many slices of pizza the user started with and ask how many slices they have eaten.  Work out how many slices they have left and display the answer in a user friendly format
'''
def fn(): 
	slices = int(input("How many slices of pizza have you started with? "))
	eaten = int(input("How many pizza slices have you eaten? "))
	slicesleft = slices - eaten;
	print("You have " + str(slicesleft) + " pizza slices left.")