
name = input("Enter your full name")
capitalname = name.title()
names = capitalname.split()
firstletter = [name[0] for name in names]
firstletterstring = '. '.join(firstletter)
print(firstletterstring)