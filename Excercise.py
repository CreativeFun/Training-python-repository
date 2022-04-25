"""
#Excercise 1

x = range(2000,3001)

lista = []

for n in x:
    if n % 5 != 0 and n % 7 == 0:
        print(n, end=", ")
"""
"""
#Excercise 2

try:
    value = int(input('Input:'))
except ValueError:

    print("Not a number")

def fact(value):
    wynik = 1
    for n in range(1,value+1):
        wynik=wynik*n
    return wynik

fact(value)
print(fact(value))

#drugi sposób

# def fact(x):
#     if x==0:
#         return 1
#     return x * fact(x-1)
#
# x=int(input())
# print(fact(x))
"""

'''
#Excercise 3

#pobranie wartości
try:
    value = int(input('Input:'))
except ValueError:
    print("Not a number")

wartosci = {}
def squared(value):
    for n in range(1,value+1):
        wartosci [n] = n*n


squared(value)
print(wartosci.items())
'''

""""
#Excercise 4


values = []

for n in range(7):
    try:
        values.append(int(input('Input:')))
    except ValueError:
        print("Not a number")

def convert(values):
    return tuple(values)

print(values)
print(convert(values))
"""