#filename: lab13-unit_converter.py
#author: Zachary McBride
import math

meters_to_X = {"ft": 3.28, "mi": 1609.344, "in":39.37, "yd":1.09361, "km":0.001}
feet_to_X = {"m": 0.3048, "km":0.0003048, "in":12, "yd":0.333, "mi":0.0001894}
miles_to_X = {"m":1609.344, "km":1.609344, "in":63360, "yd":1760, "ft":5280}
kilom_to_X = {"m":1000, "in":39370, "ft":3280.84, "yd":1093.61, "mi":0.6214}
inches_to_X = {"m":0.0254, "km":0.0000254, "ft":0.0833, "yd":0.0278, "mi":0.0000158}

possible_conversions = ["m", "mi", "km", "in", "yd"]

conversion_table = {"m":meters_to_X, "ft":feet_to_X, "mi":miles_to_X, "km":kilom_to_X, "in":inches_to_X}

def convert(input_units, input_value, output_units): # "m", "1", "km" => 1000
    conversion_factor = conversion_table[input_units][output_units]
    #print(conversion_factor)
    return float(input_value) * conversion_factor

#convert("m", 1, "km")

print("Welcome to the unit conversion suite, to begin, review the following table of supported units for conversion.")
print()
while True:
    for unit in possible_conversions:
        print(unit, end=', ')
    input_units = input("enter units of input data, or type 'quit' to exit program. ").lower()
    if input_units == "quit":
        break
    while input_units not in possible_conversions:
        input_units = input("Invalid entry, please enter units of input data, or type 'quit' to exit program. ").lower()
        if input_units == "quit":
            quit()
    print(f"You have entered {input_units}.")
    input_value = input("Enter value of units to be converted as an integer or decimal, or type 'quit' to exit program. ")
    if input_value == "quit":
        break
    input_value = float(input_value)
    while type(input_value) != float:
        input_value = input("Invalid entry, enter value of units to be converted as an integer or decimal, or type 'quit' to exit program. ")
        if input_value == "quit":
            quit()
    print(f"You have entered {input_value}.")
    output_units = input("Enter units desired for conversion, or type 'quit' to exit program. ").lower()
    if output_units == "quit":
        break
    while output_units not in possible_conversions:
        output_units = input("Invalid entry, please enter units desired for conversion, or type 'quit' to exit program. ").lower()
        if output_units == "quit":
            quit()
    result = convert(input_units, input_value, output_units)
    rounded = 0
    if result*10000 < 1:
        result = round(result,8)
        rounded = 8
    else:
        result = round(result,5)
        rounded = 5
    if input(f"{input_value} {input_units} = {result} {output_units}, rounded to {rounded} decimals. Press ENTER to continue, or type 'quit' to exit.") != "":
        break

    