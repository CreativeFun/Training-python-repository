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

"""
#Excercise 5

class ExampleClass(object):
    def __init__(self):
        self.s = ""

    def getstring(self):
        try:
            self.s = input("Wpisz tekst do powiększenia: ")
        except TypeError:
            print("Nie mozna tego wczytac")

    def printstring(self):
        try:
            print(self.s.upper())
        except TypeError:
            print("Nie mozna tego wczytac")

strObj = ExampleClass()
strObj.getstring()
strObj.printstring()
"""

"""
#Excercise 6

C = 50
H = 30
D = []
Q = []

x = int(input("Ile wartosci chcesz dodac?"))

for n in range(x):
    try:
        D.append(int(input('Input:')))
        Q.append(int(math.sqrt(((2*D[n]*C)/H))))
    except ValueError:
        print("Not a number")

print(Q)
"""

"""
#Excercise 7

#Variables
X = int(input("Podaj wartosc X:"))
Y = int(input("Podaj wartosc Y:"))

Table = []

for n in range(X):
    Tuple = ()
    for m in range(Y):
        Tuple += (m*n,)
    Table.insert(n, Tuple)
    del Tuple

print(Table)
"""

"""
#Excercise 8

Words = [n for n in input().split(',')]

Words.sort()
print(','.join(Words))
"""

"""
#Excercise 9

n = 0
Tablica = []

while(True):
    Tablica.insert(n,input())
    n += 1
    if "" in Tablica:
        break

for row in Tablica:
        print(row.upper())

"""

"""
#Excercise 10

Lista =  input().split()


Lista2 = list(set(Lista))

Lista2.sort()

print(Lista2)
"""

#Excercise 11

x = input().split()

for i in range(len(x)):
    x[i] = int(x[i],2)
    if x[i] % 5 == 0:
        x[i] = bin(x[i])
        print(x[i][2:],end=' ')



