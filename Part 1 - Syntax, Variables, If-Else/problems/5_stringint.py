""" 1.5: Fixing a type error caused by input string/int mismatch
Modify the program so that it works correctly.
You may need to add lines of code.
Remember - input("...") gives you a STRING, not a number.
"""

inches = input("Enter value in inches: ")

### do not modify below this line ##
if inches < 12:
    print("Under 1 foot")
elif inches == 12:
    print("Exactly 1 foot")
else:
    print("Over 1 foot")