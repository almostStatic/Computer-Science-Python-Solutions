'''
Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days
'''
def fn(): 
	days = int(input("How many days? "))
	hours = days * 24;
	minutes = hours * 60;
	seconds = minutes * 60;
	print("There are: " + str(hours) + " hours in " + str(days) + " days")
	print("There are: " + str(minutes) + " minutes in " + str(days) + " days")
	print("There are: " + str(seconds) + " seconds in " + str(days) + " days")		