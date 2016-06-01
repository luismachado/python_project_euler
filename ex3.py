
value = 600851475143
currentMax = 2

while True:
	if value == 1:
		break;
	if value % currentMax == 0:
		print (currentMax)
		value = value / currentMax
	else:
		currentMax = currentMax + 1