""" 1.5: Fixing a type error caused by input string/int mismatch
Modify the program so that it works correctly.
You may need to add lines of code.
Remember - input("...") gives you a STRING, not a number.
"""

userAge = input("Enter your age: ")

### do not modify below this line ##
if userAge < 18:
    print("Pass")
else:
    print("Smash")