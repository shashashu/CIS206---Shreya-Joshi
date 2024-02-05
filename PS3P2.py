def CompResult(num1, num2,code):
  if code == "A":
    result = num1 + num2
  elif code == "S":
    result = num1 - num2
  elif code == "D":
    if num2 == 0:
      result = -999
      print("UNABLE TO DIVIDE BY 0")
    else:
      result = num1/num2
  elif code == "M":
    result = num1 * num2
  else:
    print("this operation is not possible")

  return result


r = input("Do you want to compute a numerical operation? Yes or No")
while r == "Yes":
  num1 = float(input("Enter the first number"))
  num2 = float(input("Enter the second number"))
  code = input("Enter the operation code you wish to do")
  result = CompResult(num1,num2,code)
  print("The result of the operation:", result)
  print("Numbers Entered:            ", num1, num2)
  print("Operation Done:             ", code)
  r = input("Do you want to computer another numerical operation? Yes or No")