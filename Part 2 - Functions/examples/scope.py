x = 5 # variables defined outside of functions are considered global, all functions can access
def numbers():
    x = 10 #these variables can only be seen inside the function numbers()
    y = 10


def main():
    numbers() #we called the function numbers, but it is not assigned to anything yet
    #main cannot see that x and y were assigned to 10
    print("x=", x,"\n") # main can see that x was assigned to 5
    print("y=", y) #the program crashes since it never sees that y was defined=



main()








