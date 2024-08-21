import random
players=["bibek","Teknath","jd","bhurtel"]

scores={player: 0 for player in players}

points={
    "king":10,
    "queen":8,
    "police":5,
    "thief":2
}

rounds=5

for i in range(1,rounds+1):
    print(f"---round:{i}---")
    roles=random.sample(players,4)
    king, queen, police, thief = roles

    scores[king] += points["king"]
    scores[queen] += points["queen"]
    scores[police] += points["police"]
    scores[thief] += points["thief"]

    print(f"{police} is a police.")
    print("These are the other players: ")
    for player in players:
        if player != police:
            print(player)
    guess=input("Now guess who may be the thief:")
    if guess==thief:
        print("your guess is correct!")
    else:
        print(f"you choose wrong person.The thief was {thief}!!!")
        scores[police], scores[thief] = scores[thief], scores[police]


    print("\nCurrent Scores:")
    for player, score in scores.items():
        print(f"{player}: {score} points")

print("\n--- Final Scores ---")
for player, score in scores.items():
    print(f"{player}: {score} points")

