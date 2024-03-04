import csv

def listing(csv_line):
  last_name = csv_line[0]
  first_name = csv_line[1]
  hours = float(csv_line[2])
  rate = float(csv_line[3])
  initial = first_name[0]
  grosspay = hours * rate
  email = f"{initial}{last_name}@gm.com"  
  return last_name, first_name, grosspay, email


with open('CSV.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  

    for line in csv_reader:
      last_name, first_name, grosspay, email = listing(line)
      print(f"{last_name}, {first_name}, {grosspay:.2f}, {email}")
