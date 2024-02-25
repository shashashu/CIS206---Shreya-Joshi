
def countvowels (word):
  vowels = "aeiou"
  count = 0 
  for char in word:
    if char in vowels:
      count += 1 
  return count

def countcons (word):
  cons = "bcdfghjklmnpqrstvwxy"
  count = 0 
  for char in word: 
    if char in cons: 
      count += 1 
  return count

response = input("Enter any type of string")
string = response.lower()
voewlnum = countvowels(string)
consnum = countcons(string)
print("Number of vowels: ", voewlnum)
print("Number of consonants: ", consnum)