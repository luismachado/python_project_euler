months = {1: 31, 2: 28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def daysOfFebruary(year):
	if year % 100 == 0 and year % 400 == 0:
		return 29
	if year % 4 == 0:
		return 29
	return 28

year = 1900
dayOfTheWeek = 0 #Monday = 0; Sunday = 6
counter = 0

while year < 2001:
	for month in xrange(1,13):

		if year > 1900 and dayOfTheWeek == 6:
			counter += 1

		numberOfDays = 0
		if month == 2:
			numberOfDays = daysOfFebruary(year)
		else:
			numberOfDays = months[month]

		dayOfTheWeek = (dayOfTheWeek + numberOfDays) % 7

	year += 1

print counter




	