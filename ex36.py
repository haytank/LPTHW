from sys import exit
import time

def delayedPrint(stringToPrint, delay = 0.7):
    time.sleep(delay)
    print(stringToPrint)

def throne_room():
    print "Congratulations! You will be rewarded for your chivalry!"
    print "Please kneel and be knighted, Sir Mordred!"
    print "(Oooooo plot twist!) Bet you didn't see that one coming!"
    exit(0)


def dungeon():
    print "The dungeon is no place for a knight-to-be. You might wake up the Great Dragon!"
    print "You spy the dragon guarding his large treasure."
    print "Do you sneak down and steal some for yourself?"

    dragon_next = raw_input("> ")

    if dragon_next == "no":
        throne_room()
    else:
        dead("Are you crazy?! Don't you know a dragon's treasure is cursed.")


def grand_hall():
    print "Welcome to the Grand Hall. You must be thirsty from your quest. Two goblets sit before you."
    print "One is filled with a harmless liquid, the other is poison."
    print "Choose carefully - left or right. Drink up!"

    goblet_next = raw_input("> ")

    if goblet_next == "left":
        throne_room()
    else:
        dead("Did that wine taste a bit like poison to you? Don't be such a princess - it's your quest after all!")


def court_yard():
    print "You have one last challenge to prove you're worthy of knighthood."
    print "Pick door 1 or door 2 to face your foe."

    door_next = raw_input("> ")

    if door_next == "door 1":
        grand_hall()
    else:
        dungeon()


def outer_court():
    print "You dismount your horse and greet Queen Guinevere with a bow."
    print "As you do, Lancelot and a flash mob of Knights begin dancing."
    print "Lancelot declares his undying love for Guinevere with flowers and chocolates."
    delayedPrint (".......................")
    delayedPrint ("You've already pledged your allegiance to King Arthur. What do you do:")
    print "A) take Guinevere and Camelot for yourself"
    print "B) side with Arthur"
    print "C) side with Lancelot"
    print "D) other"
    pledged_allegiance = False

    while True:
        next = raw_input("> ")

        if next == "take Guinevere and Camelot for yourself":
            dead("Guinevere is the real power of the kingdom. She kills you after you've kill the man she loves.")
        elif next == "side with Arthur" and not pledged_allegiance:
            print "Do you arrest Guinevere and Lancelot on the spot or kill them?"
            side_with_arthur_next = raw_input("> ")
            if side_with_arthur_next == "arrest them":
                court_yard()
            elif side_with_arthur_next == "kill them":
                print "Way to go, Sir Galahad, you've killed your father. Talk about daddy issues."
                exit(0)
            else:
                dead("What a mess! What a medieval muddle!")
        elif next == "side with Lancelot" and not pledged_allegiance:
            print "Will you kill King Arthur for Sir Lancelot the Brave?"
            side_with_lancelot_next = raw_input("> ")
            if side_with_lancelot_next == "yes":
                court_yard()
            else:
                dead("A dark age indeed! Age of inconvenience!")
        else:
            dead("Merlin was wondering if you'd ever considered being a squirrel?")


def castle_moat():
    print "The castle moat is surprisingly deep."
    print "Your clothes are getting heavy and you think something touched your foot."
    print "Do you swim back towards shore or keep trudging through the muck?"

    next = raw_input("> ")

    if "swim back" in next:
        start()
    elif "keep trudging" in next:
        outer_court()
    else:
        dead("Looks like chivalry is dead - Gawain and Percival are flipping to see who has to get you out"
             "so you try to get away.")


def dead(why):
    print why, "It would have worked if it weren't for this infernal beard!"
    exit(0)


def start():
    print "You've made it to Camelot."
    print "You can ride across the drawbridge or swim through the castle moat."
    print "Which do you do?"

    next = raw_input("> ")

    if next == "ride across":
        outer_court()
    elif next == "swim":
        castle_moat()
    else:
        dead("What in thunder is a monster like that doing in the moat? By George, I'll turn him into a minnow.")


start()
