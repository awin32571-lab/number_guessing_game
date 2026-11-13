secret = 4
while True:
    guess = int(input("guess secret: "))
    if guess > secret:
        print("lower")
    elif guess < secret:
        print("higher")
    else:
        print("Correcto")
        break
