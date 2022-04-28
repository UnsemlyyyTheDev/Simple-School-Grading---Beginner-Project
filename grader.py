math = int(input("Enter you math grade here:"))

english = int(input("Enter you english grade here:"))

science = int(input("Enter you science grade here:"))


if (math >= 95):
    print("A+")
elif(math >= 90):
    print("A")
elif(math >= 80):
    print("B")
elif(math >= 60):
    print("C")
elif(math >= 50):
    print("D")
elif(math >= 30):
    print("D")
else:
    print("F")

if (english >= 95):
    print("A+")
elif(english >= 90):
    print("A")
elif(english >= 80):
    print("B")
elif(english >= 60):
    print("C")
elif(english >= 50):
    print("D")
elif(english >= 30):
    print("D")
else:
    print("F")

if (science >= 95):
    print("A+")
elif(science >= 90):
    print("A")
elif(science >= 80):
    print("B")
elif(science >= 60):
    print("C")
elif(science >= 50):
    print("D")
elif(science >= 30):
    print("D")
else:
    print("F")

total = (math + english + science // 300)

print("Your total grade is " + str(total))

if (total >= 95):
    print("A+")
elif(total >= 90):
    print("A")
elif(total >= 80):
    print("B")
elif(total >= 60):
    print("C")


if total <= 150:
    print("YOU ARE A DISGRACE NOW GO TO YOUR ROOM!!!")