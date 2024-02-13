maxattempts = 3 
attempts = 0

while True:
      num = int(input("Enter a number: "))
      if num <= 10 or num >= 20:
          print("Input is not accepted. Try again please")
          attempts += 1
          remaningattempts = maxattempts - attempts
          if attempts == maxattempts:
            print("Out of tries. Sorry!")
            exit()
      else:
          break

for z in range(0,num + 1,1):
  print(z)