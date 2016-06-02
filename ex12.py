def findTriangular():

    triangular_num = 0
    currentPos = 1

    while True:
        triangular_num = currentPos * (currentPos + 1) / 2 
        divisors = 0

        #run from 1 to sqrt of the number. the number of divisor of a sqrt is half of the original number
        for x in xrange(1,int((triangular_num+1)**0.5)):
            if triangular_num % x == 0:
                divisors += 1

        divisors *= 2      

        if divisors > 500:
            print triangular_num
            break

        currentPos += 1

import time
start_time = time.time()

findTriangular()

print("--- %s seconds ---" % (time.time() - start_time))