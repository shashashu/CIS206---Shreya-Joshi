side1 = float(input("Enter the length of the longest side of the triangle"))
side2 = float(input("Enter the length of the second side of the triangle"))
side3 = float(input("Enter the length of the third side of your triangle"))

if (side1)**2 == (side2)**2 + (side3)**2: 
  print("Your triangle is a right triangle")
else:
  print("Your triangle is not a right triangle")