""" 1.4: Fixing syntax errors
    Modify the code so it successfully prints:
        hello
        Variable values: 4 and Alex and Raahil
    Do not add or remove any lines of code.
"""

# ERROR - raw text always needs quotes around it
# since the quotes are missing, python thinks hello is a variable
print(hello)

# ERROR - variables cannot have spaces in their names
my variable = 4

# ERROR - variables cannot start with numbers
3rdPlace = “Alex”

# ERROR - raw text always need quotes around it
# Since the quotes are missing, python thinks Raahil is a variable
President = Raahil

# ERROR - commas are required when printing multiple items
print("Variable values:" my variable "and" 3rdplace "and" President)