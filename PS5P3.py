conversion = {
ord('A'): '2', ord('B'): '2',ord('C'): '2',
ord('D'): '3', ord('E'): '3',ord('F'): '3',
ord('G'): '4', ord('H'): '4',ord('I'): '4',
ord('J'): '5', ord('K'): '5', ord('L'): '5',
ord('M'): '6', ord('N'): '6', ord('O'): '6',
ord('P'): '7', ord('Q'): '7', ord('R'): '7', ord('S'): '7',
ord('T'): '8', ord('U'): '8', ord('V'): '8',
ord('W'): '9', ord('X'): '9', ord('Y'): '9', ord('Z'): '9',
}

phone = input("Please enter a 10 character phone number (XXX-XXX-XXXX)")
convertingphone = str.maketrans(conversion)
translation = phone.translate(convertingphone)
print("Numeric Number: ",translation)