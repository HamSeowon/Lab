ideal_credit_score = 720

userScore = int(input("please enter your credit score:"))
housePrice = int(input("please enter the price of the house:"))

if userScore >= ideal_credit_score:
    downPayment = 0.1*housePrice
elif userScore < ideal_credit_score and userScore > 600 :
    downPayment = 0.2*housePrice
else:
    downPayment = 0.3*housePrice

print("your down payment is: ${}".format(downPayment))
