latitude = float(input("What is the latitude of the destination?  "))
longitude = float(input("What is the longitude of the destination?  "))

antipode_latitude = latitude.__mul__(int("-1"))
antipode_longitude = longitude.__mul__(int("-1"))

print("The antipode of " + str(latitude) + " , " + str(longitude) + " is " + str(antipode_latitude) + " , " + str(antipode_longitude))
print()
print()
antipode_continue = str(input("Would you like to continue? (y/n)  "))
while antipode_continue == str("y"):
	latitude = float(input("What is the latitude of the next destination?  "))
	longitude = float(input("What is the longitude of the next destination?  "))

	antipode_latitude = latitude.__mul__(int("-1"))
	antipode_longitude = longitude.__mul__(int("-1"))

	print("The antipode of " + str(latitude) + " , " + str(longitude) + " is " + str(antipode_latitude) + " , " + str(antipode_longitude))
	print()
	print()
	antipode_continue = input("Would you like to continue? (y/n)  ")
	if antipode_continue == str("n"):
		break