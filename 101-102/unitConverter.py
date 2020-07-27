#filename: unitConverter.py
#author: Zachary McBride
import math

unitsToMeters = {"ft": 0.3048, "mi": 1609.344, "in":0.0254}

inOperation = True
while inOperation == True:
    print("Enter units of input data, or type 'quit' to exit program. ")
    userUnits = input("Options are: 'ft'=feet, 'mi'=miles, 'in'=inches ").lower()
    print(f"You have entered {userUnits}.")
    if userUnits == "quit":
        break
    else:
        if userUnits in unitsToMeters:
            conversionFactor = unitsToMeters.get(userUnits)
            userNum = int(input("Enter value: "))
            numConv = userNum * conversionFactor
            print(f"{userNum} {userUnits} = {numConv} m")
        else:
            print("Selection invalid, try again.")
        
