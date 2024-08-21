
while True:
    a=input("enter the command:").lower()
    if a=="start":
        print("start the car:")
    elif a=="stop":
        print("stop the car:")
    elif a=="help":
        print("start: to start the car,\t stop: to stop the car ")
    elif a=="quit":
        break
    else:
        print("sry i cant understand")
        