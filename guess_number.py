from random import randint as rd

guess_number = rd(1, 20)

while True:

    user_input = int(input("Enter the number: "))
    
    if user_input == guess_number:
        print("Its guess number!")
        break
    elif user_input > guess_number:
        print("Guess number is less")
    else:
        print("Guess nubmer is greater")
        
