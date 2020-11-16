'''
Ask for the total price of the bill, then asking how many diners there are.  Divide the total bill by the number of diners and show how much each person must pay
'''
def fn(): 
	bill = float(input("Please enter the bill amount in £: "))
	diners = int(input("How many people are dining with you today? "))
	each = bill / diners; 
	print("Each diner must pay £" + str(each))