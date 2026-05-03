# Take 24-hour time (hours and minutes) and print whether it is AM or PM

hours = int(input("\nenter the hours(0 - 23): "))
minutes = int(input("\nenter the minutes(1 - 60): "))

if hours < 12:
    print("AM")

else:
    print("PM")