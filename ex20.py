def fact (n):
	n_fact = 1
	for x in xrange(1,n+1):
	 	n_fact *= x

	return n_fact

totalSum = 0
factString = str(fact(100))

for x in xrange(0, len(factString)):
	totalSum += int(factString[x])

print totalSum