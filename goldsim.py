from numpy import random as r
from collections import Counter
import csv

class Tier:
    def __init__(self, value, heroes):
        self.value = value
        self.heroes = heroes

heroes = ["Black Panther", "Black Widow", "Bucky Barnes", "Captain America", "Enchantress", "Falcon", "Hawkeye", "Hulk", "Iron Man", "J.O.C.A.S.T.A", "Loki", "Mockingbird", "Maria Hill", "Ms. Marvel", "Phil Coulson", "Quake", "Red Hulk", "Spider-Woman", "Thor", "Tigra", "Valkyrie", "Vision", "War Machine", "Wasp", "Wiccan", "Winter Soldier","Rick Jones","Skaar"]

vals = [3, 5, 8, 10, 30]
count = [26, 26, 26, 26, 28]
ts = []

Tiers = [Tier(v,c) for (v,c) in zip(vals, count)]

character = 0

while character != "" and character not in heroes:
    print 'Please enter a character from the following list: \n'
    for h in heroes:
        print h
    character = raw_input("\nEnter a character (or press ENTER to skip): ")
    
print character

N = input("Input number of iterations to run: ")     # number of iterations to run
caps = []

for n in range(N):
    if n%1000 == 0:
        print "Running next 1000 iterations..."
    #print "Running new iteration..."
    inventory = {h:0 for h in heroes}
    success = False
    i = 0

    while not success:
        T = r.choice(Tiers,p=[0.35,0.25,0.2,0.15,0.05])
        
        #print T.value
        H = r.choice(heroes[:T.heroes])
        inventory[H] += T.value
        #print H, inventory[H]
        i += 1
        if character == "":
            print "You did not enter a character."
            success = (inventory[H] >= 10)
        else:
            success = (inventory[character] >= 10)

    caps.append(i)

bins = Counter(caps)

csvfile = open('capsuledata.csv', 'w')
writer = csv.writer(csvfile)

writer.writerow(['Total iterations', N])
writer.writerow(['Capsules','Iterations','Chance of Unlock'])

for j in bins:
    writer.writerow([j, bins[j]])

print bins

