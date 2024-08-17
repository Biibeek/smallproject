import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)

    return roll
while True:
    players=int(input("Enter the  number of players ranging from (2-5):\n"))
    if 2<=players<=4:
        break
    else:
        print("The players must be 2 to 5!!!")
max_score=50
players_score=[0 for _ in range(players)]
while max(players_score)<max_score:
    for player_idx in range(players):
        print("player number ", player_idx+1,"turn has jst started!" )
        current_score=0
        while True:
            should_roll=input("click y to continue else type n to stop:\n")
            if should_roll.lower()!="y":
                break
            value=roll()
            if value==1:
                print("you rolled 1:Yours turn is over!!!")
                current_score=0
                break
            else:
                current_score+=value
                print(f"you rolled {value}")
            print(f"your score is :{current_score}")
        players_score[player_idx]+=current_score
        print(f"your total score is:{players_score[player_idx]}")

