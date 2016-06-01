sum = 0

fib_ant = 1
fib = 2

while fib < 4000000:

	if fib % 2 == 0:
		sum += fib

	fib_temp = fib
	fib += fib_ant
	fib_ant = fib_temp

print(sum)