
def main():
    sum = subtract(1,4)

    sum2 = subtract (4,1)

    #sum could equal sum2 by naming the variables instead of going in order
    sum = subtract(y=1,x=4)
    print("sum = ", sum, "\n")
    print("sum2 = ", sum2)


    

def subtract(x, y):
    sum = x - y
    return sum


main()
