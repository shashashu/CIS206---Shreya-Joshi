import re

#PROBLEM 1
def specialchars(givenstring):
    return bool(re.match(r'^[a-zA-Z0-9]+$', givenstring))

tests = [
    "ABCDEFabcdef123450",
    "*&%@#!}{"
]

for test in tests:
    if specialchars(test):
        print(test, "contains the specified characters")
    else:
        print(test, "contains characters other that are not specified")
      
#PROBLEM 2

def lettercheck(string):
    pattern = r'ab*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

letters = ["ab", "abc", "a", "ab", "abb"]

for letter in letters:
    if lettercheck(letter):
        print(letter, "matches the pattern.")
    else:
        print(letter, "does not match.")

#PROBLEM 3 
def lettercheck2(string):
    pattern = r'ab+'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

letters2 = ["ab", "abc", "a", "ab", "abb"]

for letter in letters2:
    if lettercheck2(letter):
        print(letter, "matches the pattern.")
    else:
        print(letter, "does not match.")
#PROBLEM 4
def findsequences(string):
  pattern = r'[a-z]+_[a-z]+'
  matches = re.findall(pattern, string)
  return matches

letters3 = [
  "aab_cbbbc",
  "aab_Abbbc",
  "Aaab_abbbc"
]
for letter in letters3:
  sequences = findsequences(letter)
  if sequences:
      print("In", letter, ": Found sequences:", ", ".join(sequences))
  else:
      print("In", letter, ": No sequences found")

#PROBLEM 5
def wordmatching(string):
    pattern = r'^\b\w+\b'
    match = re.match(pattern, string)
    if match:
        return match.group()
    else:
        return None

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    " The quick brown fox jumps over the lazy dog."
]

for sentence in sentences:
    word = wordmatching(sentence)
    if word:
        print("In", sentence, ": Found word at the beginning:", word)
    else:
        print("In", sentence, ": No word at the beginning")

#PROBLEM 6
def zmatching(string):
    pattern = r'\b\w*z\w*\b'
    matches = re.findall(pattern, string)
    return matches

sentence2 = [
    "The quick brown fox jumps over the lazy dog.",
    "Python Exercises."
]
for sentence in sentence2:
    zwords = zmatching(sentence)
    if zwords:
        print("In", sentence, ": Words containing 'z':", ", ".join(zwords))
    else:
        print("In", sentence, ": No words containing 'z' found")

#PROBLEM 7
def removezeros(ipaddress):
  pattern = r'\b0+(\d+)\b'
  fixedip = re.sub(pattern, r'\1', ipaddress)
  return fixedip

ipaddress = "216.08.094.196"
fixedip = removezeros(ipaddress)
print("Corrected IP address:", fixedip)

#PROBLEM 8
def searchwords(text, search):
  foundwords = []
  for word in search:
      if re.search(word, text):
          foundwords.append(word)
  return foundwords

givensentence = 'The quick brown fox jumps over the lazy dog.'
search = ['fox', 'dog', 'horse']

found_words = searchwords(givensentence, search)
print("Sample text:", givensentence)
print("Searched words:", search)
print("Found words:", found_words)

#PROBLEM 9
def searchloc(text, wordsearch):
  return [(match.start(), match.end()) for match in re.finditer(wordsearch, text)]

test9 = 'The quick brown fox jumps over the lazy dog.'
wordsearch = 'fox'

locations = searchloc(test9, wordsearch)
if locations:
  print("Sample text:", test9)
  print("Searched word:", wordsearch)
  print("Locations where occurs:")
  for start, end in locations:
      print("Start:", start, "End:", end)
else:
  print("Searched word not in test.")

#PROBLEM 10
def nowhitespace(text):
  textunderscore = text.replace(" ", "_")
  textwhitespace = textunderscore.replace("_", " ")
  return textunderscore, textwhitespace

text1 = "Regular Expressions"
text2 = "Code_Examples"

text1underscore, text1whitespace = nowhitespace(text1)
text2underscore, text2whitespace = nowhitespace(text2)

print("Text with whitespaces replaced with underscores:" ,text1underscore)
print("Text with underscores replaced with whitespaces:" ,text2whitespace)

#PROBLEM 11
def finddate(url):
    pattern = r'/(\d{4})/(\d{2})/(\d{2})/'
    match = re.search(pattern, url)
    if match:
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
        return year, month, day
    else:
        return None

url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
result = finddate(url)
if result:
    year, month, day = result
    print("Year:", year)
    print("Month:", month)
    print("Day:", day)
else:
    print("No info found in the URL.")

#PROBLEM 12
def findletter(text):
    pattern = r'\b[a|e]\w+\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return matches

test12 = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

foundletter = findletter(test12)
print("Words starting with 'a' or 'e':", foundletter)

#PROBLEM 13
def replacement(string):
  pattern = r'[ ,.]'
  replacement = re.sub(pattern, ":", string)
  return replacement

test13 = 'Python Exercises, PHP exercises.'
replacementfull = replacement(test13)
print("Text with spaces, commas, and dots replaced with colons:", replacementfull)

#PROBLEM 14
def findwords(text):
  pattern = r'\b[a|e]\w+\b'
  matches = re.findall(pattern, text, re.IGNORECASE)
  return matches

test14 = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

wordsfound = findwords(test14)
print("Words starting with 'a' or 'e':", wordsfound)

#PROBLEM 15
def nospace(string):
  spacegone = re.sub(r'\s+', ' ', string)
  return spacegone

test15 = 'Python      Exercises'
spacegone = nospace(test15)
print("test with spaces removed:", spacegone)








