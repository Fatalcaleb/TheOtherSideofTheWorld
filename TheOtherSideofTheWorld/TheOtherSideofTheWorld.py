from folium	import	Map

print("Would you like to know the antipode of a place?  (y/n)")
antipode_start = input()

if antipode_start == "y":
	print("What is the latitude of the destination?  ")
	latitude = input()
	print("What is the longitude of the destination?  ")
	longitude = input()
	

	antipode_latitude = latitude * -1
	if longitude <= 0:
		antipode_longitude = longitude + 180
	
	elif longitude > 180:
		antipode_longitude = str("Invalid Longitude")
	else:
		antipode_longitude = longitude - 180

	print("The antipode of " + str(latitude) + " , " + str(longitude) + " is " + str(antipode_latitude) + " , " + str(antipode_longitude))
	location = [antipode_latitude, antipode_longitude]
	mymap = Map(location)
	mymap.save("antipode.html")
elif antipode_start == "n":
	print("Please enjoy your day")


