import math 
from os import system, name
from enum import Enum
import csv

class Operators(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    INDICE = 5

#Var definition
numList = [] #list of numbers to use
opList = [] #list of operators to use
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
            menuChoice = input("Choose what you want to do with these numbers (Add, Subtract, Multiply, Divide, Indice): ")
            match menuChoice[0].lower():
                case "a":
                    inputValid = True
                    result = Add(numList[0], numList[1])
                case "s":
                    inputValid = True
                    result = Subtract(numList[0], numList[1])
                case "m":
                    inputValid = True
                    result = Multiply(numList[0], numList[1])
                case "d":
                    inputValid = True
                    result = Divide(numList[0], numList[1])
                case "i":
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
    NewCalcChoice()
    return

def WriteCalcString(value): #for writing the calc to a string for user readability
    return

def NewCalcChoice(): #for after a calculation is done, letting the user return to the menu
    inputValid = False
    while inputValid == False:
        menuChoice = int(input("What do you want to do now?\n1: Return to main menu\n2: Quit Program"))
        match menuChoice:
            case 1:
                inputValid = True
                clear()
                MainMenu()
            case 2:
                inputValid = True
                quit()
        if inputValid == False:
            clear()
            print("Sorry, please input a correct choice.\n")
    return

def PrintLog(): #For printing results from log file
    with open (logFileName, "r") as logFile:
        calcHistory = csv.reader(logFile)
        a = 1
        for currentRow in calcHistory:
            print(str(a) + ": " + ",".join(currentRow)) # comma and "join" is to make it look cleaner, separate each piece of data out
            a += 1
    print()
    NewCalcChoice()
    return

def MainMenu(): #Main choice selection
    inputValid = False
    while inputValid == False:
        #try: #look out for errors (TODO: figure out why the except breaks when uncommented)
            menuChoice = int(input("What do you want to do?\n1: Calculate something\n2: Look at calculation history\n3: Quit program\n"))
            match menuChoice:
                case 1:
                    inputValid = True
                    clear()
                    Calculation()
                case 2:
                    clear()
                    PrintLog()
                    inputValid = True
                case 3:
                    inputValid = True
                    quit()
            if inputValid == False:
                clear()
                print("Sorry, please input a correct choice.\n")
        #except:
            #error = system.exc_info()[0]
            #clear()
            #print("Invalid input\n")
            #print(error)
    return

clear()
print("This is CleggCalc-P: a coding exercise in Python to make a calculator!\n")
MainMenu()