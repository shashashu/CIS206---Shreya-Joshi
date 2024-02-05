def CompRedPoints(points, redeemcode):
  if redeemcode == "C":
    rewardpnts = points * 2
    dollarval = rewardpnts * 1.5
  elif redeemcode == "X":
    rewardpnts = points * 3
    dollarval = rewardpnts * 1.5
  else:
    rewardpnts = points * 1.5
    dollarval = rewardpnts * 1.5

  return rewardpnts

def CompDollarVal(rewardpnts):
  dollarval = rewardpnts * 1.5

  return dollarval

r = input("Do you want to calculate your reward points? Yes or No")

while r == "Yes":
  points = float(input("Enter the amount of points you have"))
  redeemcode = input("Enter your redeem code")
  rewardpnts = CompRedPoints(points, redeemcode)
  dollarval = CompDollarVal(rewardpnts)
  print("Your total amount of reward points redeemed is:",rewardpnts, "points")
  print("Your points entered were: ", points)
  print("Your redemption code is:  " ,redeemcode)
  print("The dollar value of your points is: $", dollarval)
  r = input("Do you want to redeem another code? Yes or No")