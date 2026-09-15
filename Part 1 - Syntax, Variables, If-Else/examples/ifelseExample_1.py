robotBatteryPercent = 90


# Separate "if" statements - both print statements will execute
if robotBatteryPercent != 0:
    print("Robot is not dead.")
if robotBatteryPercent > 50:
    print("Robot is above 50%.")

print("---")

# Single "if" statement - only one print statement of these three will ever execute, even if all the conditions are true
if robotBatteryPercent != 0:
    print("Robot is not dead.")
elif robotBatteryPercent > 50:
    print("Robot is above 50%.")
else:
    print("Robot is not dead, but lower than 50%.")


