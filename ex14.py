counter = 0
inicialValue = 0

for x in xrange(999999,0,-1):
	value = x
	currentCounter = 1
	while value > 1:
		currentCounter += 1
		if value % 2 == 0:
			value /= 2
		else:
			value = value * 3 + 1
	
	if currentCounter > counter:
		counter = currentCounter
		inicialValue = x

print "InitVal:", inicialValue
print "Length:", counter
