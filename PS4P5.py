r = input("Do you want to do this program? Yes or No?")
r = r.lower()

while True:
  score1 = float(input("Enter test 1 score: "))
  score2 = float(input("Enter test 2 score:"))
  if score1 <= 0 or score1 >= 100 or score2 <= 0 or score2 >= 100:
      print("These scores are out of range")
      r=input("do you want to do this program again? Yes or No")
  else:
      points1 = .6 * score1
      points2 = .4 * score2
      ttlpoints = round(points1 + points2,2)
      print("Your total points are: ",ttlpoints)
      exit()
