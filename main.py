def addieren(x, y):
    return print("Das Ergebnis ist: " , x+y)

def subtrahieren(x, y):
    return print("Das Ergebnis ist: ", x - y)

def multiplizieren(x, y):
    return print("Das Ergebnis ist: ", x * y)

def dividieren(x, y):
    return print("Das Ergebnis ist: ", x / y)

print("Gib eine Zahl ein:")
x = int(input())
print("Gib die zweite Zahl ein:")
y = int(input())

print("Welche Operation möchtest du durchführen? (+, -, *, /)")
rechenart = input()

if rechenart == "+":
   addieren(x,y)
elif rechenart == "-":
    subtrahieren(x,y)
elif rechenart == "*":
   multiplizieren(x,y)
elif rechenart == "/":
   dividieren(x,y)


