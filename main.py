import random
number = random.randint(1, 5)
leo = 0
while number != leo:
    leo = input("введите цифру: ")
    leo = int(leo)
    print("ваша цифра -", leo)
    if leo == number:
        print("угадал")
    else:
        if leo > number:
            print("цифра слишком большая")
        else:
            print("цифра слишком маленькая")

