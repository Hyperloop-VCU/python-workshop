"""
4.2 - print the even values of a list
Fix and modify the loop so it prints every EVEN number in the list.
Also, print the index of each even number, like so:
    index 0 value 0
    index 1 value 10
    index 4 value 12
    index 7 value 6
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

for a in range(4):
    print("index", a, "value", myList[a])

