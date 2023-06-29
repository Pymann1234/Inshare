

# Here we can see that "float" : returns a decimal value
# And whereas "int" : returns a integer values

weight = float(input("Weight: "))
unit = input("(L)bs or (K)gs: ")
# ".upper()" returns a capital(upper case) letters
if (unit.upper()) == "L":
    converted = weight * 0.45
    print(converted)
    # "f" is used in a print function for a Formatted strings, in other words, to combine a variable and a string
    print(f"You are {converted} kgs")
else:
    converted = weight // 0.45
    # Here "//" is for integer and "/" is for float
    print(f"You are {converted} lbs")
