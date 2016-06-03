from num2words import num2words

count = 0

for x in xrange(1,1001):
	numStr = num2words(x).replace(",","").replace(" ","").replace("-","")
	count += len(numStr)

print count