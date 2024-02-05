def CompRedPoints(points, redeemcode):
  if redeemcode == "C":
    rewardpnts = points * 2
  elif redeemcode == "X":
    rewardpnts = points * 3
  else:
    rewardpnts = points * 1.5

  return rewardpnts

r = input("Do you want to calculate your reward points? Yes or No")

while r == "Yes":
  points = float(input("Enter the amount of points you have"))
  redeemcode = input("Enter your redeem code")
  rewardpnts = CompRedPoints(points, redeemcode)
  print("Your total amount of reward points redeemed is:",rewardpnts, "points")
  print("Your points are: ", points)
  print("Your redemption code is:" ,redeemcode)
  r = input("Do you want to redeem another code? Yes or No")