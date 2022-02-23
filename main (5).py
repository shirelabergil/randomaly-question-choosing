import random
'''
Randomly select questions by ID
'''

# Author's ID's :
shirel = '206645103'
gitit = '212280911'
demi = '323134577'

id = shirel + gitit + demi


# A function returns a double-digit number randomly selected from the ID's string
def get_number(id):
    return int(id[random.randint(0, 26)] + id[random.randint(0, 26)])


ex1 = get_number(id) % 9
ex2 = get_number(id) % 8 + 10
ex3 = get_number(id) % 11 + 19
ex4 = get_number(id) % 5 + 31

print("ex1 : ", ex1, "\nex2 : ", ex2, "\nex3 : ", ex3, "\nex4 : ", ex4)
