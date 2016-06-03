value = pow(2,1000)
valueStr = str(value)
valueSum = 0

for x in xrange(0,len(valueStr)):
	valueSum += int(valueStr[x])

print valueSum