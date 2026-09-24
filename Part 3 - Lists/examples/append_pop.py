rappers = [] # creates an empty list

rappers.append("Future")
rappers.append("Logic")
rappers.append("Kendrick Lamar")
rappers.append("A-dawg")
rappers.append("D-money")
rappers.pop()

# List is now ['Future', 'Logic', 'Kendrick Lamar', 'A-dawg']

rappers[0] = "Lil Wayne" # replace future with lil wayne

print(rappers[0])
print(rappers[3])
print(rappers[-1]) # the "-1" index is an easy way to get the last element of the list