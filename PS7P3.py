# making a tuple
tuple = ("red", "yellow", "blue")

#printing tuple
print("tuple:", tuple)

#printing only certain parts of the tuple
print("first color:", tuple[0])  # prints out red

#slicing
#slicing away the first part of the tuple (red) from the rest of the colors
print(tuple[1:3])  # this will print yellow and blue

# unpacking a tuple
# giving each tuple their own variable
color1, color2, color3 = tuple
print("color 1: ",color1)  # prints red
print("color 2:", color2)  # prints yellow
print("color 3:", color3)  # prints blue



