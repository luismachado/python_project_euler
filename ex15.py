def coeficient (n,k):
	n_fact = 1
	for x in xrange(1,n+1):
	 	n_fact *= x

	k_fact = 1
	for x in xrange(1,k+1):
		k_fact *= x
	
	nAndkFact = 1
	for x in xrange(1,n-k+1):
		nAndkFact *= x

	return n_fact / (nAndkFact*k_fact)

print coeficient(40,20)
