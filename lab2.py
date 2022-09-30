age = int(input("enter your age:"))

if age >= 9:
    height = float(input("enter your height in cm:"))
    if height > 130:
        print("you may go on this ride")
    else:
        print("you are too short for this ride")
else:
    print("you are too young for this ride")
    
