from random import randint

players = []
nplayers = 0
while True:
    try:
        nplayers = int(input("How many players wants to play ? : "))
        # nplayers = int(npl)
        break
    except ValueError:
        print('Please enter valid number of players')

for i in range(1, nplayers + 1):
    name = input("Enter player %d name :" % i)
    players.append(name)

print("Player names", players)

results = {}

for player in players:
    print("Now its %s \'s turn :" % player)

    num = (randint(1, 20))
    print(num)

    counter = 0
    while True:
        counter += 1
        try:
            user = int(input("Please guess the number between 1-20 : "))

            # print(num)

            if user > 20 or user < 1:
                print("Please guess the number between the given range. THANK YOU!!!")
            if type(user) is not int:
                print("Please enter valid input")

            elif num > user:
                print("Guess higher!!!")
            elif num < user:
                print("Guess lower!!!")
            elif num == user:
                print("Well guessed!!!")
                break
        except ValueError:
            print("PLease enter valid input")

    results.update({player: counter})
    print("%s has taken %d chances " % (player, counter))


win_val = min(results.values())
tie = (results.values())
tie1 = set(tie)

tie_players = []

win_counter = 0
for key, value in results.items():
    if win_val == value:
        win_counter += 1
        tie_players.append(key)

Joinstring = ", ".join(tie_players)
tittle = Joinstring.title()

if win_counter > 1:
    print("Its a tie between following players : %s" % tittle)
else:
    print("Winner is %s " % spl)
