# Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good
# Evening”, or “Good Night”.

hours = float(input("\n enter the hours: "))

if hours < 0 and  hours > 23:
    print("invalid hours")

elif hours >= 5 and hours < 12:
    print("good morining")

elif hours >= 12 and hours < 17:
    print("good afternoon")

elif hours >= 17 and hours < 21:
    print("good evening")

else:
    print("good night")