# Problem 1: Pretty Numbers

# Convert an integer into a pretty string with commas 12345678 to 12,345,678

#Truncates <n> float to <decimals> decimals place.
#Use negative numbers to truncate left of decimal
#truncate(n<float>, decimals<int>=0:default)
def truncate(n, decimales=0):
    multiplier = 10 ** decimales
    return int(n * multiplier) / multiplier
#input = 1000000

#Work Function
#Takes string input, converts to list, inserts commas, then returns as list
#make_pretty_helper(<string>) = list[<num_chars>]
def make_pretty_helper(input):
    output = input
    if len(output) < 4:
        return output
    output = [char for char in output]
    decrementer = len(output) - 3
    while decrementer >= 0:             #01234567
        output.insert(decrementer, ',') #1000000                          
        decrementer -= 3                #1000,000

    #print(output)

    return output

#quiet return
#make_pretty(<int input>):str output
def make_pretty_quiet(input):
    check_num = int(input)
    if type(check_num) == int:
        return make_pretty_helper(input)
    else:
        return "NaN"


#loud return
#make_pretty_lout(<int input>):str output
def make_pretty_loud(input):
    check_num = int(input)
    if type(check_num) == int:
        output = make_pretty_helper(input)
        output = ''.join(output)
        if len(output) <= 3:
            print("No commas inserted")
            return output
        else:
            return output
    else:
        return "NaN"
# #demo code for make_pretty_loud
# def main():
#     while True:
#         print("Enter 0 to quit demo.")
#         check = make_pretty_loud(input("Type digit-only input"))
#         if check == "0":
#             break
#         else:
#             print(check)

#main()