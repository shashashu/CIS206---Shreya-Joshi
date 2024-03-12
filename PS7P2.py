numbers = []

for number in range(1, 21):
    numbersamount = float(input(f"Enter a number please {number}: "))
    numbers.append(numbersamount)

totalsum = sum(numbers)

averagenum = round(totalsum / 20,2)

maxnum = numbers.index(max(numbers)) + 1
minnum = numbers.index(min(numbers)) + 1

print("Total sum of numbers in list: ", totalsum)
print("Average of numbers in list:   ", averagenum)
print("Largest Number in list:     ", maxnum)
print("Smallest number in list:        ", minnum)
