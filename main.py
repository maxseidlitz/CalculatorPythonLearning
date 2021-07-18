print("Gib eine Zahl ein:")
x = int(input())
print("Gib die zu addierende Zahl ein:")
y = int(input())

rechenart = input()

if rechenart == "+":
   addieren(x,y)
if rechenart == "-":
    subtrahieren(x,y)
if rechenart == "*":
   multiplizieren(x,y)
if rechenart == "/":
   dividieren(x,y)

def addieren(x, y):
    return print("Das Ergebnis ist: " , x+y)

def subtrahieren(x, y):
    return print("Das Ergebnis ist: ", x - y)

def multiplizieren(x, y):
    return print("Das Ergebnis ist: ", x * y)

def dividieren(x, y):
    return print("Das Ergebnis ist: ", x / y)