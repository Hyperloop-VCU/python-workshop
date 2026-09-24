def func(listToModify):
   listToModify.append("hello from inside the function!")

outsideList = [0.3, 0.2, 0.1]
func(outsideList)

print(outsideList)