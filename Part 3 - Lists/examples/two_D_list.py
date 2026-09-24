grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0]
]

# you can append() a whole new list too
grid.append([0, 0, 1, 0, 0])

print(len(grid)) # how many sub-lists are in the main list
print(len(grid[0])) # how many elements are in the 1st sub-list

print(grid[-1])    # the last sub-list
print(grid[-1][2]) # the 3rd element of the last sub-list