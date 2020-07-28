def is_even(a):
    if a % 2 == 0:
        return "even"
    else:
        return "odd"

running = True
while running == True:
    var = int(input("Enter a number: "))
    print(f"{var} is {is_even(var)}")
    