# WRONG - cannot add strings and integers directly
variable1 = "35"
variable2 = 35
print(variable1 + variable2)


# CORRECT - must convert the text to an integer first
variable1 = "35"
variable2 = 35
variable1 = int(variable1)
print(variable1 + variable2)