nameslist = ['Peter', 'Jacky', 'Zuha', 'Eun', 'Chaewon', 'Kiana', 'Ada', 'Luigi', 'Kai', 'MJ']

while True:
  namesearch = input("Please enter a name")
  if namesearch in nameslist:
    print("Name", namesearch, "has been found in list")
    exit()
  else:
    print("Name not found please try another name")
