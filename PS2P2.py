num1 = int(input("Enter your first number"))
num2 = int(input("Enter your second number"))
operation = input("What number operration do you wish to do?")

if operation == "Multiply":
  output = num1 * num2
  print(output, "is your product")
  print(num1, "*", num2, "=", output)
elif operation == "Divide": 
  if num2 == 0:
    print("Cannot calculate qoutient cannot divide by 0")
  else:
    output = num1 / num2
    print(output ,"is your quotient")
    print(num1, "/", num2, "=", output)
elif operation == "Subtract":
  output = num1 - num2
  print(output, "is your difference")
  print(num1, "-", num2, "=", output)
elif operation == "Add":
  output = num1 + num2
  print(output, "is your sum")
  print(num1, "+", num2, "=", output)
else:
  print("that calculation is not possible")
