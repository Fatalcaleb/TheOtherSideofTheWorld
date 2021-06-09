from folium	import	Map

print("Would you like to know the antipode of a place?  (y/n)")
antipode_start = input()

if antipode_start == str("y"):
	print("What is the latitude of the destination?  ")
	latitude = float(input())
	print("What is the longitude of the destination?  ")
	longitude = float(input())
	

	antipode_latitude = latitude.__mul__(int("-1"))
	if longitude.__lt__(float("0")):
		antipode_longitude = longitude.__add__(float("180"))
	elif longitude.__eq__(float("0")):
		antipode_longitude = float("180")
	elif longitude.__gt__(float("180")):
		antipode_longitude = str("Invalid Longitude")
	else:
		antipode_longitude = longitude.__sub__(float("180"))

	print("The antipode of " + str(latitude) + " , " + str(longitude) + " is " + str(antipode_latitude) + " , " + str(antipode_longitude))
	location = list((antipode_latitude, antipode_longitude))
	mymap = Map(location)
	mymap.save(str("antipode.html"))
elif antipode_start == str("n"):
	print("Please enjoy your day")


