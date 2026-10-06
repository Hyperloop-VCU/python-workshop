robotBatteryPercent = 10
robotBatteryDraw = 50

if robotBatteryPercent < 25:
    print("Battery low.")
    if robotBatteryDraw > robotBatteryPercent:
        print("Robot needs more power.")
else:
    print("Battery above 25%")
    if robotBatteryDraw >= 25:
        print("Robot is using maximum power.")