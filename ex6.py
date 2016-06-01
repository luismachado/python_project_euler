def sum_square_difference(maxValue): 
	sumCount = 0
	sumSquared = 0

	for i in xrange(1, maxValue+1):
		sumCount = sumCount + i
		sumSquared = sumSquared + i*i

	return sumCount * sumCount - sumSquared	


print (sum_square_difference(100))


#numbers = xrange(1 ,101)
#a = sum (numbers)
#print a * a - sum(i*i for i in numbers)