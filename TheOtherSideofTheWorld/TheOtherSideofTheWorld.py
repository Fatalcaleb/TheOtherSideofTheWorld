print("Would you like to know the antipode of a place?  (y/n)")
antipode_start = input()

if antipode_start == str("y"):
	print("What is the latitude of the destination?  ")
	latitude = float(input())
	print("What is the longitude of the destination?  ")
	longitude = float(input())
	

	antipode_latitude = latitude.__mul__(int("-1"))
	if longitude._le_(float("0")):
		antipode_longitude = longitude.__add__(float("180"))
	else:
		antipode_longitude = longitude._sub_(float("180"))

	print("The antipode of " + str(latitude) + " , " + str(longitude) + " is " + str(antipode_latitude) + " , " + str(antipode_longitude))
	print()
	print("Would you like to continue? (y/n)  ")
	antipode_continue = str(input())

	while antipode_continue == str("y"):
		print("What is the latitude of the next destination?  ")
		latitude = float(input())
		print("What is the longitude of the next destination?  ")
		longitude = float(input())

		antipode_latitude = latitude.__mul__(int("-1"))
		if longitude._le_(float("0")):
			antipode_longitude = longitude.__add__(float("180"))
		else:
			antipode_longitude = longitude._sub_(float("180"))

		print("The antipode of " + str(latitude) + " , " + str(longitude) + " is " + str(antipode_latitude) + " , " + str(antipode_longitude))
		print()
		print("Would you like to continue? (y/n)  ")
		antipode_continue = input()
		if antipode_continue == str("n"):
			break
elif antipode_start == str("n"):
	print("Please enjoy your day")


