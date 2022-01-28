# print 
from statistics import mode
from tkinter.ttk import Notebook


print("Hello Worm")
# git bash upload - in git bash
## navigate to cloned folder
## git add .
## git commit -m "comment"
## git push origin main (or master)
# git clone SSH
# execute a python file in VSC 
## right-click : run python file in terminal
# determine a date type
type(3)
# types: float, int, tuple, str, bool, list
# list structure
list = ["item1","item2","item3","item4","item5","item6"]
#lists are mutable, indexing begins at zero
#return the first item in a list
list[0] 
# return the last item in a list
list[-1]
#find the length of a list 
len(list)
#slice a list (return part of it)
##return the items in places 0 and 1 (not including end)
list[0:2]
##or 
list [:2]
##return items in positions 3 onwards
list [2:]
#add items to a list 
list.append("item7")
#return all items in a list 
list 
#insert an item to a list (in position 3)
list.insert(2,"item2.5")
#remove a specific item
list.remove("item4")
#remove and check a position 
list.pop(3)
#change an element in the list (position 3)
list[2] = "item2.6"
#tuple is an immutable list
#make a tuple 
tuple = ( )
#fill the tuple
tuple = ("thing1","thing2","thing3","thing4")
#check the length of a tuple
len(tuple)
#a dictionary hold keys and values
#create a dictionary
dictionary = {}
# add a key and value to the dict 
dictionary["puppy"] = "cute"
# length of dictionary 
len(dictionary)
#get all keys and values 
dictionary.items()
#get only keys 
dictionary.keys()
#get only values
dictionary.values()
#get a specific value 
dictionary.get("puppy")
dictionary['puppy']
#list of dictionaries 
##create an empty list 
listy = []
#add each dictionary 
listy.append({"number":"1","spelling":"one"})
listy.append({"number":"2","spelling":"two"})
# if statements 
if listy > 4 :
    # indent here
    print(listy)
# operators for if statements 
# > (greater than)
# >= (greater than / equal to)
# == (equal to)
# != (not equal to)
# else: 
# membership operators
## in (Returns True if a sequence with the specified value is present in the object.)
## not in (Returns True if a sequence with the specified value is not present in the object.)
# logical operators
## and (Evaluates two Boolean expressions into one compound expression. The compound expression is true if both Boolean expressions are true. If one of the expressions is false, then the compound expression is false.)
## or (Evaluates two Boolean expressions into one compound expression. The compound expression is true if either Boolean expression is true.If one of the expressions is false, then the compound expression is true. If both expressions are false, then the compound expression is false.)
## not (Evaluates a Boolean expression. The expression is true if the conditional is false.)
# types of loops
## condition-controlled (also called a while loop)
## count-controlled (also called a for loop)
## while looop eg
x = 0
while x <= 5:
    print(x)
    x = x + 1
##for loop eg
counties = ["one","two","three"]
for county in counties:
    print(county)
# range e.g. 
for num in range(5):
    print(num)
# range e.g. 2
for i in range(len(counties)):
    print(counties[i])
# to iterate through keys in a dictionary
for county in counties_dict.keys():
    print(county)
#to iterate through values in a dictionary 
for voters in counties_dict.values():
    print(voters)
#another e.g. using .get
for county in counties_dict:
    print(counties_dict.get(county))
# to iterate through key, value pairs 
for key, value in dictionary_name.items():
    print(key, value)
#getting each dictionary in a list of dictionaries 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
# to get the values from a list of dictionaries, we need a nested for loop 
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
# to print a specific value from the dictionaries, we need to use the correct variable from the dicts 
for county_dict in voting_data:
    print(county_dict['county'])
# printing
# print string with integer values converted to string, using concat 
print("Your interest for the year is $" + str(interest))
# f string literals
# put f in front of the string and use curly brackets for variables or expressions
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# f string using for loops and dictionaries - e.g. 
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
# multi line f strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")
print(message_to_candidate)
#formatting floating point decimals
#f'{value:{width}.{precision}}'
# add thousands separator 
# f'{value:{width},.{precision}}'
# activate your anaconda environment (required for jupyter notebook)
## (mine is called PythonData) -- in anaconda powershell
conda activate PythonData
## activate jupyter notebook
jupyter Notebook
## open a file 
file_variable = open(filename, mode)
## file_variable references the file object 
## filename is a string specifying the file 
## mode is what you want to do with it. 
## possible modes - r = read, w = write, x = exclusive creation, a = append data, + = reading and writing 
## if you don't know the file directory: 
os.path.join("Resources", "election_results.csv")
# importing modules
import datetime 
import datetime as dt
now = dt.datetime.now()
## first now is *your* variable. dt = datetime module. datetime = class / function / variable. 2nd now = set variable or "method" within the datetime module / class 
import csv 
## this imports the csv module 
dir(csv) 
## dir outputs all the functions available for that module, dictionary, or data type. also oututs the keys and values for a dictionary
# Assign a variable to load a file from a path.
## file_to_load is your variable. os is the module path.join is how you find a file if you don't know the exact address. 
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
## with open is more convenient than opening and closing the docs. needs an indentations. 
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    ## file_reader is your variable. csv is the module. reader is a regular command. 
    file_reader = csv.reader(election_data)
    for row in file_reader:
        print(row)
