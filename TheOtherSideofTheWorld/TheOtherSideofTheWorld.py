latitude = float(input("What is the latitude of your destination? "))
longitude = float(input("What is the longitude of your destination? "))

antipode_latitude = latitude.__mul__(int("-1"))
antipode_longitude = longitude.__mul__(int("-1"))

print("The antipode of " + str(latitude) + " , " + str(longitude) + " is " + str(antipode_latitude) + " , " + str(antipode_longitude))