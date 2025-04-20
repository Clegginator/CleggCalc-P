import math 
from os import system, name
import csv

#Var definition
numList = [] #list of numbers to use
result = float(0) #result of calculation
numberChoice = float(0)
menuChoice = " " #choice in menus (i.e, choose between add, subtract, multiply or divide)
inputValid = False #make sure menu input is valid
logFileName = "CalcLog.csv" #file to save to whenever calculations are done

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    return


#functions for calculations
def Add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def Divide(x, y):
    return x / y

def Multiply(x, y):
    return x * y

def Incice(x, y):
    return pow(x, y)

def InputNumber():
    numList.append(int(input("Input a number: ")))
    return

def Calculation():
    logFile = open (logFileName, "a") #use w for writing (read, wiping and rewriting the file every time), use a for append (read, adding to it every time)

    #Number input
    numList.append(float(input("Input a number: ")))
    numList.append(float(input("Input another number: ")))

    #Choosing calculation
    inputValid = False
    while inputValid == False:
        try: #look out for error
            menuChoice = input("Choose what you want to do with these numbers (add, subtract, multiply, divide, indice): ")
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
                case "indice":
                    inputValid = True
                    result = Incice(numList[0], numList[1])
            if inputValid == False:
                print("Sorry, please input a correct choice.\n")
        except:
            error = system.exc_info()[0]
            clear()
            print("Invalid input\n")
            print(error)


    print("The result is %f!" % result)
    logFile.write(str(numList[0]) + ","  + menuChoice + "," + str(numList[1]) + ",=," + str(result) + "\n")
    logFile.close
    return


#Intro (TODO: make into menu)
clear()
print("This is CleggCalc-P: a coding exercise in Python to make a calculator!\n")

while inputValid == False:
    try: #look out for errors
        menuChoice = str(input("What do you want to do?\n1: Calculate something\n2: Look at your previous calculation\n"))
        if str(menuChoice) == "1":
                clear()
                Calculation()
        elif str(menuChoice) == "2":
                with open (logFileName, "r") as logFile:
                    calcHistory = csv.reader(logFile)
                    
                    for currentRow in calcHistory:
                        print(",".join(currentRow)) # comma and "join" is to make it look cleaner
        if inputValid == False:
            clear()
            print("Sorry, please input a correct choice.\n")
    except:
        error = system.exc_info()[0]
        clear()
        print("Invalid input\n")
        print(error)


