myList = ["outside list"]

def some_function():
    myList = ["inside list"]
    myList.append(1.0)
    print(myList)


some_function()