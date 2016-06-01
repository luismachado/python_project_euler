productStr = ""
maxProduct = 0

for x in xrange(1000, 99, -1):
	for y in xrange(1000, 99, -1):
		productStr = str(x * y)
		if productStr == productStr[::-1] and int(productStr) > maxProduct:
			maxProduct = int(productStr)
			print(x)
			print(y)
			print(productStr)