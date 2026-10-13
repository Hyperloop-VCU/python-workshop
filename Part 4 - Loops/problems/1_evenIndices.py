"""
4.1 - print every other number of a list
Fix and modify the loop so it prints every OTHER number in the list, like so:
    0
    9
    12
    7
    11
You may use the given isEven function.
Do not hard-code the answer;
it should still work if I change the list values or list length.
"""
def isEven(num):
    if num % 2 == 0: # num % 2 returns 0 if num is divisible by 2, 1 otherwise
        return True
    else:
        return False

myList = [0, 10, 9, 3, 12, 5, 7, 6, 11, 13]

### do not modify above this line ###

for a in range(2):
    print(myList[a])
