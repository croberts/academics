"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
 begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, 
 multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
 So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""


from os import read
from turtle import position



with open('names.txt', encoding="utf-8") as f:
    read_data = f.read()
    
read_data = read_data.split(',')

names = []

for name in read_data:
    name = name[1:-1]
    names.append(name)

names.sort()

position = 1
ttl = 0

for name in names:
    name_ttl = 0

    for letter in name:
        value = ord(letter.lower()) - 96
        #print(value)
        #exit
        name_ttl += value

    name_ttl *= position
    position += 1
    ttl += name_ttl

print(ttl)
