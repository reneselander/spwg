#Simple Python script for generating random passwords

import random

#Create list of characters ['a', 'b',] etc...
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#Create list of numbers ['1', '2',] etc...
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Create list of special characters ['#', '+',] etc...
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("SPWG - Python")

nr_of_letters = int(input(f"Enter the amount of letters you want in the password: \n"))

nr_of_numbers = int(input(f"\nAnd now, enter the amount of numbers you want in the password: \n"))

nr_of_symbols = int(input(f"\nNow enter the amount of symbols you would like to have: \n"))


'''
random.sample(population, k)
Return a k length list of unique elements chosen from the population sequence. Used for random sampling without replacement.
'''
r_letters = random.sample(letters, k = nr_of_letters)

r_numbers = random.sample(numbers, k = nr_of_numbers)

r_symbols = random.sample(symbols, k = nr_of_symbols)



list = [*r_letters, *r_symbols, *r_numbers]

random.shuffle(list)

#Print the password, dot separated by the sep operator
#print('\nHere is your password: ', *list, sep = ".")

print('\nHere is your password: ', *list, sep = '')