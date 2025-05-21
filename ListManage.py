import math 
import csv

logFileName = "CalcLog.csv" #file to save to whenever calculations are done

def PrintLog(): #For printing results from log file
    with open (logFileName, "r") as logFile:
        calcHistory = csv.reader(logFile)
        a = 1
        for currentRow in calcHistory:
            print(str(a) + ": " + ",".join(currentRow)) # comma and "join" is to make it look cleaner, separate each piece of data out
            a += 1
    print("test")
    return

def WriteCalcString(value): #for writing the calc to a string for user readability
    return