'''Additional comment'''

from random import randint as rd

guess_number = rd(1, 20)  # Подбираем случайное число

while True:
    # Здесь хранится ответ пользователя
    user_input = int(input("Enter the number: "))

    # Здесь прописана логика игры
    if user_input == guess_number:
        print("Its guess number!")
        break
    elif user_input > guess_number:
        print("Guess number is less")
    else:
        print("Guess nubmer is greater")
