def fn():
	"config;feel free to change but it will have an effect on the code m8"
	flrs = range(-3, 21)
	timesUsed = 0
	restrictedFloors = [ -3, -2, -1 ] 
	notAllowedFloors = [ 13 ]
	floorsPassed = 0
	authCode = '50171099'

	while True: 
		flr = int(input("Please enter the number of the floor which you like to go to! (-3 to 20) --> "))
		if flr not in flrs or (flr in notAllowedFloors): # invalid floor; restart loop. 
			print("Sorry mate that floor isn't valid.")
		else: # valid floor
			if flr in restrictedFloors: 
				inptd = str(input("That floor is restricted! Please enter your authCode code: "))
				if inptd != authCode: 
					print("Sorry mate you don't have permission to access that floor!")
				else: # correct pin
					timesUsed += 1;
					print("Well done! You passed the test! You're now magically at floor No." + str(flr) + "! That was fast, wasn't it?!")
			else: # not in restricted floor; allow access: 
				print("You're now magically at floor No." + str(flr) + "! That was fast, wasn't it?!")
				timesUsed += 1;