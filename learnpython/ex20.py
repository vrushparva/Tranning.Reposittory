from sys import exit


def gold_room():
    print("This room is fully of gold, how much do you like to take")


    next = input(">")

    if next is "0" or next is "1":
        how_much = int(next)
    else:
        print("Dead man, ypu have to learn about numbers ")

    if how_much < 50:
        print("Nice !! , You are not Greedy , YOU WON")
        exit(0)
    else:
        print("Bull shit ! ,You are Greedy bastard")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("how are you going to move the bear?")
    bear_moved = False

    while True:

        next = input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved form the door.you can go though it ")
        elif next == "taunt bear" and bear_moved:
            print("The bear get pissed off and chews you leg off. ")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def chthulu_room():
    print("here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head.")

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to you right and left.")
    print("which one do you take?.")

    next =  input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        chthulu_room()
    else:
        dead("You stumble around the room untill you starve.")


start()
