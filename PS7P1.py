rainfall = []

for month in range(1, 13):
    rainfallamount = float(input(f"Enter rainfall for month {month}: "))
    rainfall.append(rainfallamount)

totalrain = sum(rainfall)

averagerain = round(totalrain / 12,2)

maxrainmonth = rainfall.index(max(rainfall)) + 1
minrainmonth = rainfall.index(min(rainfall)) + 1

print("Total rainfall for the year:", totalrain, "inches")
print("Average monthly rainfall:", averagerain, "inches")
print("Month with the highest rainfall: ", maxrainmonth)
print("Month with the lowest rainfall:  " ,minrainmonth)
