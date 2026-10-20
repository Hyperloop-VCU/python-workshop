#Continue Pantry Example

Pantry = ["Water", "Apples", "Bread", "Flour", "Oranges"]
Shopping_list = ["Milk", "Eggs", "Flour"]

x = 0

while x < len(Shopping_list):
    if Shopping_list[x] in Pantry:
        print("We have", Shopping_list[x], "in the pantry.")
        x += 1
        continue
    print("Don't have", Shopping_list[x], "in the pantry.")
    x += 1