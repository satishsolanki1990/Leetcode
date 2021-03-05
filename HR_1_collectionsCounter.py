'''
https://www.hackerrank.com/challenges/collections-counter/problem
>>> from collections import Counter
>>>
>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
>>> Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})

Task
Raghu is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only
if they get the shoe of their desired size.

Your task is to compute how much money  earned.

Input Format

The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

'''

from collections import defaultdict, Counter

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_shoes = int(input())
shoes = input().split(' ')

# we can use Counter to convert list into dict
# shoes_dict  = Counter(shoes)

def def_value():
    return 0

shoes_dict = defaultdict(def_value)
for i in shoes:
    shoes_dict[i] += 1

N = int(input())

revenu = 0
for i in range(N):
    temp = input().split(' ')
    size = temp[0]
    price = temp[1]
    if shoes_dict[size] != 0:
        revenu += int(price)
        shoes_dict[size] -= 1

print(revenu)
