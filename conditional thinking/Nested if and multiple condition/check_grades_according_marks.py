#Take marks (0–100) and print the corresponding grade (A/B/C/D/F).

marks = float(input("enter the marks: "))

if marks >= 90 and marks <= 100:
    print("A grade = excellent")

elif marks >= 70 and marks <= 89:
    print("B grade = very good")

elif marks >= 50 and marks <= 69:
    print("C grades = good")

elif marks >= 33 and marks <= 59:
    print("D grade = average")

else:
    print("F grade = fail")
