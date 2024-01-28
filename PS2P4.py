year = int(input("Enter a year"))

if year % 4 == 0:
  print("the year", year, "is a leap year")
elif year % 400 == 0:
  print("the year", year, "is a leap year")
else:
  print("the year", year, "is not a leap year")