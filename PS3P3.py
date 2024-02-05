def calcpostage(weight, zipcode):
  areac = {
      60171: 2.00,
      60172: 2.50,
      60635: 3.00
  }
  
  if weight >= 100:
      weightc = 0.02
  elif weight >= 50:
      weightc = 0.03
  else:
      weightc = 0.05

  
  areac = areac.get(zipcode, 5.00)

  weightc = weight * weightc
  round(weightc,2)

  postage = areac + weightc

  print("Area Charge:   $", round(areac, 2))
  print("Weight Charge: $", round(weightc, 2))
  print("Postage Total: $",round(postage, 2))

  return weightc, areac, postage


weight = float(input("Enter the weight of the package in ounces: "))
zipcode = float(input("Enter your zip code: "))
calcpostage(weight, zipcode)
