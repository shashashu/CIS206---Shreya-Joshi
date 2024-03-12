import random

def quiz():
    statesandcptls = {
        'Alabama':	'Montgomery',
        'Alaska':	'Juneau',
        'Arizona':	'Phoenix',
        'Arkansas':	'Little Rock',
        'California':	'Sacramento',
        'Colorado':	'Denver', 
        'Connecticut':	'Hartford',
        'Delaware':'Dover',
        'Florida':	'Tallahassee',
        'Georgia':	'Atlanta',
        'Hawaii':	'Honolulu',
        'Idaho':	'Boise',
        'Illinois':	'Springfield',
        'Indiana':	'Indianapolis',
        'Iowa':	'Des Moines',
        'Kansas':	'Topeka',
        'Kentucky':	'Frankfort',
        'Louisiana':	'Baton Rouge',
        'Maine':	'Augusta',
        'Maryland':	'Annapolis',
        'Massachusetts':	'Boston',
        'Michigan':	'Lansing',
        'Minnesota':	'Saint Paul',
        'Mississippi':	'Jackson',
        'Missouri':	'Jefferson City',
        'Montana':	'Helena',
        'Nebraska':	'Lincoln',
        'Nevada':	'Carson City',
        'New Hampshire':	'Concord', 
        'New Jersey':	'Trenton',
        'New Mexico':	'Santa Fe',
        'New York':	'Albany',
        'North Carolina':	'Raleigh',
        'North Dakota':	'Bismarck',
        'Ohio':	'Columbus',
        'Oklahoma':	'Oklahoma City',
        'Oregon':	'Salem',
        'Pennsylvania':	'Harrisburg',
        'Rhode Island':	'Providence',
        'South Carolina':	'Columbia',
        'South Dakota':	'Pierre',
        'Tennessee':	'Nashville',
        'Texas':	'Austin',
        'Utah	Salt': 'Lake City',
        'Vermont':	'Montpelier',
        'Virginia':	'Richmond',
        'Washington':	'Olympia',
        'West Virginia':	'Charleston',
        'Wisconsin':	'Madison',
        'Wyoming':	'Cheyenne'

    }

    correct = 0
    wrong = 0

    while True:
        state, capital = random.choice(list(statesandcptls.items()))

        r = input(f"What is the capital of {state}? ").strip()

        if r == capital:
            correct += 1
            print("Correct! Good job!")
        else:
            wrong += 1
            print(f"Incorrect. The capital of {state} is {capital}.")

        loop = input("Do you want another state? (Yes or No) ").strip()
        if loop != "yes":
            break

    print("Quiz finished!")
    print("Correct answers:   " ,correct)
    print("Incorrect answers: " , wrong)

quiz()
