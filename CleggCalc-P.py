#functions for calculations
def Add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def Divide(x, y):
    return x / y

def Multiply(x, y):
    return x * y

#Var definition
numList = [] #list of numbers to use
result = 0 #result of calculation
menuChoice = " " #choice in menus (i.e, choose between add, subtract, multiply or divide)
inputValid = False #make sure menu input is valid

#Intro (TODO: make into menu)
print("This is CleggCalc-P: a coding exercise in Python to make a calculator!")

#Number input
numList.append(int(input("Input a number: ")))
numList.append(int(input("Input another number: ")))

#Choosing calculation
while inputValid == False:
    menuChoice = input("Choose what you want to do with these numbers (add, subtract, multiply, divide): ")
    match menuChoice.lower():
        case "add":
            inputValid = True
            result = Add(numList[0], numList[1])
        case "subtract":
            inputValid = True
            result = Subtract(numList[0], numList[1])
        case "multiply":
            inputValid = True
            result = Multiply(numList[0], numList[1])
        case "divide":
            inputValid = True
            result = Divide(numList[0], numList[1])
    if inputValid == False:
        print("Sorry, please input a correct choice.")

print("The result is %d!" % result)

