print("Leap year finder.")
year = input("enter the year you want to check ")
year =int(year)

year_4 = year % 4
year_100 = year % 100
year_400 = year % 400

if year_4 == 0 :
	if year_100 == 0 :
		if year_400 == 0 :
			print("Year entered is a leap year.")

		else :
			print("Year entered is not a leap year.")

	else :
		print("Year entered is not a leap year.")

else :
	print("Year entered is not a leap year.")