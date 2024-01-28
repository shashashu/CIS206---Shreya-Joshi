nprice = float(input("Enter the net price the novel will be sold at"))
copies= float(input("Enter the estimated amount of copies to be sold"))

optiona = 5000 + 20000

royaltyb = .125 * nprice
optionb = round(royaltyb * copies, 2)

optionc = 0
if copies <= 4000:
  firstroyalty = (.1 * nprice)*copies
  
  optionc = firstroyalty
elif copies > 4000:
  oldsales = 4000
  newsales = copies - 4000
  firstroyalty = (.1 *nprice)*oldsales
  fixedroyalty = (.14 * nprice)*newsales
  
  optionc = round(firstroyalty + fixedroyalty, 2)
  

if optiona > optionb and optionb > optionc:
  print("Option A is the best choice the author can make they will make $", optiona)
elif optionb > optionc and optionc > optiona:
  print("Option B is the best choice the author can make they will earn $", optionb, "in royalties")
else:
  print("Option C is the best option the author can make they will earn $", optionc, "in royalties")
