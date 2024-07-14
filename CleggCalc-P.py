#Var definition
numList = [] #list of numbers to use
result = 0 #result of calculation

#Intro (TODO: make into menu)
print("This is CleggCalc-P: a coding exercise in Python to make a calculator!")

#Number input
numList.append(int(input("Input a number: ")))
numList.append(int(input("Input another number: ")))
result = numList[0] + numList[1]
print("The result is %d!" % result)
