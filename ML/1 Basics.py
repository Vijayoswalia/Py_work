# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 15:33:38 2018

@author: Vijay
"""

###1
names= ['ashok', 'vijay', 'mahesh']
gender = [0, 0, 1]

type(names)
type(gender)
###

smiles = "C(=N)(N)N.C(=O)(O)O"
smiles.find("(O)")
##

gh='Brotherareallgood'
if "10" in gh:
	print ('contains brother')
else:
     print( 'not there')

email_address = 'ashok'
if "@" not in email_address:
	email_address += '@brandeis.edu'

print(email_address)

###
line = ' # This is a comment line \n'
line.strip()

line.rstrip()

line.rstrip("\n")

##
names= ['ashok', 'vijay', 'mahesh']
", ".join(names)
'ashok'.upper()

##
names= ['ashok', 'vijay', 'mahesh']
names.append('pavan')
names

del names[0]
names

names.sort()
names

names.reverse()
names
#
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
##
"%s lives in %s at latitude %.2f" % ("Andrew", "Sweden", 57.7056)

##
city_population = {"New York City":8550405, "Los Angeles":3971883, "Toronto":2731571, 
                   "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}
city_population["New York City"]

food = {"ham" : "yes", "egg" : "yes", "spam" : "no" }
food

atomic_number_to_name = {
1: "hydrogen",
6: "carbon",
7: "nitrogen",
8: "oxygen",
}

nobel_prize_winners = {
(1979, "physics"): ["Glashow", "Salam", "Weinberg"],
(1962, "chemistry"): ["Hodgkin"],
(1984, "biology"): ["McClintock"],
}

##
capitals = {"Austria":"Vienna", "Germany":"Berlin", "Netherlands":"Amsterdam"}
capital = capitals.pop("Austria" "Vienna")
print(capital)

##
locations = {"Toronto" : "Ontario", "Vancouver":"British Columbia"}
locations["Ottawa"]
if "Ottawa" in locations: 
    print(locations["Ottawa"])
else:
    print('non-available in dictionary')

if "Toronto" in locations: 
    print(locations["Toronto"])
    
##
f = open('E:/TRN/Data 2017/textdata.txt')
f.readline()

lst= [ x for x in open('E:/TRN/Data 2017/textdata.txt','r').readlines() ]
lst
    
input_file = open('E:/TRN/Data 2017/textdata.txt')
output_file = open('E:/TRN/Data 2017/out.txt', 'w')
for line in input_file:
		output_file.write(line)

##
##Creation of a function to check for whether input has letters
def wordonly(inputstring):
    #the below wrongletters can be updated based on users requirement to exclude particular letters or symols
    wrongletters=(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','1','2','3','4','5','6','7','8','9','0','...','..', '\\', '/','//','///',':','\\\\', '#'])
    count=0 #initializing count
    for i in wrongletters:  ##loop function for iterating all the non letters
        for l in inputstring: ##loop function for iterating all the input
            if (l!=i):        #Checking condition whether input doesnot match wrongstrings
                    count=count+1 ##appending for the wrong match iteration
                 
            else:
                print ("\nIncorrect word entry at position:",i,"\nError caused due to matching at:",count,"\nSystem will exit\n")
                raise SystemExit ##raises exception and exits 
    print ("The input has all letters having no other characters")
           
