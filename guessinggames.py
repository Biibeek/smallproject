import random
a=random.randint(1,100)
guesses=0
while True:
    b=int(input("Guess the number:"))
    guesses +=1
    if b < a:
        print("Guess a higher number:")
    elif b > a:
        print("Guess a lower number:")
    else:
        print(f"you guess the right number and the number is {a}")
        break
print(f"you took {guesses} guesses!!!")
