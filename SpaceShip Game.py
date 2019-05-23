# Ismail Ahmed
# January 20, 2016
# Computer Programming AM
# SpaceshipGame.py
# Verizon 3.0

import time

global score
score = 0
global counter
counter = 0
global scoreslist
scoreslist = []


def placement():  # places the user according to their amount of points after death
    global scoreslist
    global counter
    global score
    global initial
    initial = input("Please enter your three letter initals" + '\n')

    def getKey(item):
        return item[2]

    outfile = open("highscores.txt", "w")
    score = initial, '\t', str(score)
    scoreslist.append(score)

    scoreslist = sorted(scoreslist, key=getKey, reverse=True)

    for i in scoreslist:
        outfile.write(" ".join(i) + "\n")

    outfile.close()
    print("")
    print('\t' + "HIGH SCORES")
    print("===========================")
    infile = open("highscores.txt", "r")
    line = infile.readline()
    while line:
        items = line.split()
        line = infile.readline()
        items = " ".join(items) + '\n'
        print(items)
    infile.close()
    time.sleep(4)
    Menu()


def Earth():
    global name  # variable that can be used anywhere
    global score
    global counter
    print(
        name + ", you are on Earth. Your planet code is, PCEMV012" + '\n')  # tells where you are and the planet's code
    weight = float(input("What is your ship's weight, " + name + "? " + '\n'))  # ship weight
    speed = float(input(name + ", how fast do you want to go(Ve(km/s)):" + '\n'))  # their velocity
    if speed > 13:  # cant go faster than this
        print("I'm sorry, you were too fast and have crashed. Please try again!" + '\n')
        placement()
    if speed < 9:  # cant go slower than this
        print("I'm sorry, you were too slow and have crashed. Please try again!" + '\n')
        placement()
    print("You have left the planet, " + name + "!" + '\n')
    Escape_Earth()  # takes to other planets


def Escape_Earth():
    global name  # variable that can be used anywhere
    global score
    global counter
    new_planet = input("Which planet would you like to go to?" + '\n')
    new_planet = new_planet.title()
    if new_planet == "Mercury":
        counter += 1
        score = counter * 100 + score
        Mercury()  # takes them to Mercury
    elif new_planet == "Venus":
        counter += 1
        score = counter * 100 + score
        Venus()  # takes them to Venus
    elif new_planet == "Earth":
        print("You were already on Earth! Try again" + '\n')
        Escape_Earth()
    elif new_planet == "Mars":
        counter += 1
        score = counter * 100 + score
        Mars()  # takes them to Mars
    elif new_planet == "Jupiter":
        counter += 1
        score = counter * 100 + score
        Jupiter()  # takes them to Jupiter
    elif new_planet == "Saturn":
        counter += 1
        score = counter * 100 + score
        Saturn()  # takes them to Saturn
    elif new_planet == "Uranus":
        counter += 1
        score = counter * 100 + score
        Uranus()  # takes them to Uranus
    elif new_planet == "Neptune":
        counter += 1
        score = counter * 100 + score
        Neptune()  # takes them to Neptune
    else:
        print("Please try again, " + name + "!" + '\n')
        Escape_Earth()


def Escape_Mercury():
    global name  # variable that can be used anywhere
    global score
    global counter
    new_planet = input("Which planet would you like to go to? " + '\n')
    new_planet = new_planet.title()
    if new_planet == "Mercury":
        print("You were already on Mercury! Try again" + '\n')
        Escape_Mercury()
    elif new_planet == "Venus":
        counter += 1
        score = counter * 100 + score
        Venus()  # takes them to Venus
    elif new_planet == "Earth":
        counter += 1
        score = counter * 100 + score
        Earth()  # takes them to Earth
    elif new_planet == "Mars":
        counter += 1
        score = counter * 100 + score
        Mars()  # takes them to Mars
    elif new_planet == "Jupiter":
        counter += 1
        score = counter * 100 + score
        Jupiter()  # takes them to Jupiter
    elif new_planet == "Saturn":
        counter += 1
        score = counter * 100 + score
        Saturn()  # takes them to Saturn
    elif new_planet == "Uranus":
        counter += 1
        score = counter * 100 + score
        Uranus()  # takes them to Uranus
    elif new_planet == "Neptune":
        counter += 1
        score = counter * 100 + score
        Neptune()  # takes them to Neptune
    else:
        print("Please try again, " + name + "!" + '\n')
        Escape_Mercury()


def Escape_Venus():
    global name  # variable that can be used anywhere
    global score
    global counter
    new_planet = input("Which planet would you like to go to? " + '\n')
    new_planet = new_planet.title()
    if new_planet == "Mercury":
        counter += 1
        score = counter * 100 + score
        Mercury()  # takes them to Mercury
    elif new_planet == "Venus":
        print("You were already on Venus! Try again" + '\n')
        Escape_Venus()
    elif new_planet == "Earth":
        counter += 1
        score = counter * 100 + score
        Earth()  # takes them to Earth
    elif new_planet == "Mars":
        counter += 1
        score = counter * 100 + score
        Mars()  # takes them to Mars
    elif new_planet == "Jupiter":
        counter += 1
        score = counter * 100 + score
        Jupiter()  # takes them to Jupiter
    elif new_planet == "Saturn":
        counter += 1
        score = counter * 100 + score
        Saturn()  # takes them to Saturn
    elif new_planet == "Uranus":
        counter += 1
        score = counter * 100 + score
        Uranus()  # takes them to Uranus
    elif new_planet == "Neptune":
        counter += 1
        score = counter * 100 + score
        Neptune()  # takes them to Neptune
    else:
        print("Please try again, " + name + "!" + '\n')
        Escape_Venus()


def Escape_Mars():
    global name  # variable that can be used anywhere
    global score
    global counter
    new_planet = input("Which planet would you like to go to? " + '\n')
    new_planet = new_planet.title()
    if new_planet == "Mercury":
        counter += 1
        score = counter * 100 + score
        Mercury()  # takes them to Mercury
    elif new_planet == "Venus":
        counter += 1
        score = counter * 100 + score
        Venus()  # takes them to Venus
    elif new_planet == "Earth":
        counter += 1
        score = counter * 100 + score
        Earth()  # takes them to Earth
    elif new_planet == "Mars":
        print("You were already on Mars! Try again" + '\n')
        Escape_Mars()
    elif new_planet == "Jupiter":
        counter += 1
        score = counter * 100 + score
        Jupiter()  # takes them to Jupiter
    elif new_planet == "Saturn":
        counter += 1
        score = counter * 100 + score
        Saturn()  # takes them to Saturn
    elif new_planet == "Uranus":
        counter += 1
        score = counter * 100 + score
        Uranus()  # takes them to Uranus
    elif new_planet == "Neptune":
        counter += 1
        score = counter * 100 + score
        Neptune()  # takes them to Neptune
    else:
        print("Please try again, " + name + "!" + '\n')
        Escape_Mars()


def Escape_Jupiter():
    global name  # variable that can be used anywhere
    global score
    global counter
    new_planet = input("Which planet would you like to go to? " + '\n')
    new_planet = new_planet.title()
    if new_planet == "Mercury":
        counter += 1
        score = counter * 100 + score
        Mercury()  # takes them to Mercury
    elif new_planet == "Venus":
        counter += 1
        score = counter * 100 + score
        Venus()  # takes them to Venus
    elif new_planet == "Earth":
        counter += 1
        score = counter * 100 + score
        Earth()  # takes them to Earth
    elif new_planet == "Mars":
        counter += 1
        score = counter * 100 + score
        Mars()  # takes them to Mars
    elif new_planet == "Jupiter":
        print("You were already on Jupiter! Try again" + '\n')
        Escape_Jupiter()
    elif new_planet == "Saturn":
        counter += 1
        score = counter * 100 + score
        Saturn()  # takes them to Saturn
    elif new_planet == "Uranus":
        counter += 1
        score = counter * 100 + score
        Uranus()  # takes them to Uranus
    elif new_planet == "Neptune":
        counter += 1
        score = counter * 100 + score
        Neptune()  # takes them to Neptune
    else:
        print("Please try again, " + name + "!" + '\n')
        Escape_Jupiter()


def Escape_Saturn():
    global name  # variable that can be used anywhere
    global score
    global counter
    new_planet = input("Which planet would you like to go to? " + '\n')
    new_planet = new_planet.title()
    if new_planet == "Mercury":
        counter += 1
        score = counter * 100 + score
        Mercury()  # takes them to Mercury
    elif new_planet == "Venus":
        counter += 1
        score = counter * 100 + score
        Venus()  # takes them to Venus
    elif new_planet == "Earth":
        counter += 1
        score = counter * 100 + score
        Earth()  # takes them to Earth
    elif new_planet == "Mars":
        counter += 1
        score = counter * 100 + score
        Mars()  # takes them to Mars
    elif new_planet == "Jupiter":
        counter += 1
        score = counter * 100 + score
        Jupiter()  # takes them to Jupiter
    elif new_planet == "Saturn":
        print("You were already on Saturn! Try again" + '\n')
        Escape_Saturn()
    elif new_planet == "Uranus":
        counter += 1
        score = counter * 100 + score
        Uranus()  # takes them to Uranus
    elif new_planet == "Neptune":
        counter += 1
        score = counter * 100 + score
        Neptune()  # takes them to Neptune
    else:
        print("Please try again, " + name + "!" + '\n')
        Escape_Saturn()


def Escape_Uranus():
    global name  # variable that can be used anywhere
    global score
    global counter
    new_planet = input("Which planet would you like to go to? " + '\n')
    new_planet = new_planet.title()
    if new_planet == "Mercury":
        counter += 1
        score = counter * 100 + score
        Mercury()  # takes them to Mercury
    elif new_planet == "Venus":
        counter += 1
        score = counter * 100 + score
        Venus()  # takes them to Venus
    elif new_planet == "Earth":
        counter += 1
        score = counter * 100 + score
        Earth()  # takes them to Earth
    elif new_planet == "Mars":
        mcounter += 1
        score = counter * 100 + score
        Mars()  # takes them to Mars
    elif new_planet == "Jupiter":
        counter += 1
        score = counter * 100 + score
        Jupiter()  # takes them to Jupiter
    elif new_planet == "Saturn":
        counter += 1
        score = counter * 100 + score
        Saturn()  # takes them to Saturn
    elif new_planet == "Uranus":
        print("You were already on Uranus! Try again" + '\n')
        Escape_Uranus()
    elif new_planet == "Neptune":
        counter += 1
        score = counter * 100 + score
        Neptune()  # takes them to Neptune
    else:
        ("Please try again, " + name + "!" + '\n')
        Escape_Uranus()


def Escape_Neptune():
    global name  # variable that can be used anywhere
    global score
    global counter
    new_planet = input("Which planet would you like to go to? " + '\n')
    new_planet = new_planet.title()
    if new_planet == "Mercury":
        counter += 1
        score = counter * 100 + score
        Mercury()  # takes them to Mercury
    elif new_planet == "Venus":
        counter += 1
        score = counter * 100 + score
        Venus()  # takes them to Venus
    elif new_planet == "Earth":
        counter += 1
        score = counter * 100 + score
        Earth()  # takes them to Earth
    elif new_planet == "Mars":
        counter += 1
        score = counter * 100 + score
        Mars()  # takes them to Mars
    elif new_planet == "Jupiter":
        counter += 1
        score = counter * 100 + score
        Jupiter()  # takes them to Jupiter
    elif new_planet == "Saturn":
        counter += 1
        score = counter * 100 + score
        Saturn()  # takes them to Saturn
    elif new_planet == "Uranus":
        counter += 1
        score = counter * 100 + score
        Uranus()  # takes them to Uranus
    elif new_planet == "Neptune":
        print("You were already on Neptune! Try again" + '\n')
        Escape_Neptune()
    else:
        print("Please try again, " + name + "!" + '\n')
        Escape_Neptune()


def Mercury():  # Mercury planet function
    global name  # variable can be used anywhere
    global score
    global counter
    print(
        name + ", you are on Mercury and the planet code is, PCM0." + '\n')  # tells where you are and the planet's code
    weight = float(input("What is your ship's weight, " + name + "? " + '\n'))  # their weight
    speed = float(input("How fast do you want to go (Ve(km/s)), " + name + ":" + '\n'))  # their velocity
    if speed > 5:  # cant be greater than this
        print("I'm sorry, you were too fast and have crashed. Please try again!" + '\n')
        placement()
    if speed < 2:  # can't be less than this
        print("I'm sorry, you were too slow and have crashed. Please try again!" + '\n')
        placement()
    print("You have left the planet, " + name + "!" + '\n')
    Escape_Mercury()  # takes to other planets function


def Venus():  # Venus planet function
    global name  # variable can be used anywhere
    global score
    global counter
    print(
        name + ", you are on Venus and the planet code is, PCVM01." + '\n')  # tells where you are and the planet's code
    weight = float(input("What is your ship's weight, " + name + "? " + '\n'))  # their weight
    speed = float(input("How fast do you want to go (Ve(km/s)), " + name + ":" + '\n'))  # their velocity
    if speed > 12:  # can't be greater than this
        print("I'm sorry, you were too fast and have crashed. Please try again!" + '\n')
        placement()
    if speed < 8:  # can't be lower than this
        print("I'm sorry, you were too slow and have crashed. Please try again!" + '\n')
        placement()
    print("You have left the planet, " + name + "!" + '\n')
    Escape_Venus()  # takes to other planets function


def Mars():  # Mars planet function
    global name  # variable can be used anywhere
    global score
    global counter
    print(
        name + ", you are on Mars and the planet code is, PCMMVE0123." + '\n')  # tells where you are and the planet's code
    weight = float(input("What is your ship's weight, " + name + "? " + '\n'))  # their weight
    speed = float(input("How fast do you want to go (Ve(km/s)), " + name + ":" + '\n'))  # their velocity
    if speed > 8:  # can't be greater than this
        print("I'm sorry, you were too fast and have crashed. Please try again!" + '\n')
        placement()
    if speed < 4:  # can't be less than this
        print("I'm sorry, you were too slow and have crashed. Please try again!" + '\n')
        placement()
    print("You have left the planet, " + name + "!" + '\n')
    Escape_Mars()  # takes to other planets function


def Jupiter():  # Jupiter planet function
    global name  # variable can be used anywhere
    global score
    global counter
    print(
        name + ", you are on Jupiter and the planet code is, PCJMVEM01234." + '\n')  # tells where you are and the planet's code
    weight = float(input("What is your ship's weight, " + name + "? " + '\n'))  # their weight
    speed = float(input("How fast do you want to go (Ve(km/s)), " + name + ":" + '\n'))  # their velocity
    if speed > 69:  # can't be greater than this
        print("I'm sorry, you were too fast and have crashed. Please try again!" + '\n')
        placement()
    if speed < 65:  # can't be less than this
        print("I'm sorry, you were too slow and have crashed. Please try again!" + '\n')
        placement()
    print("You have left the planet, " + name + "!" + '\n')
    Escape_Jupiter()  # takes to other planets function


def Saturn():  # Saturn planet function
    global name  # variable can be used anywhere
    global score
    global counter
    print(
        name + ", you are on Saturn and the planet code is, PCSMVEMJ012345." + '\n')  # tells where you are and the planet's code
    weight = float(input("What is your ship's weight, " + name + "? " + '\n'))  # their weight
    speed = float(input("How fast do you want to go (Ve(km/s)), " + name + ":" + '\n'))  # their velocity
    if speed > 41:  # can't be greater than this
        print("I'm sorry, you were too fast and have crashed. Please try again!" + '\n')
        placement()
    if speed < 37:  # can't be less than this
        print("I'm sorry, you were too slow and have crashed. Please try again!" + '\n')
        placement()
    print("You have left the planet, " + name + "!" + '\n')
    Escape_Saturn()  # takes to other planets function


def Uranus():  # Uranus planet function
    global name  # variable can be used anywhere
    global score
    global counter
    print(
        name + ", you are on Uranus and the planet code is, PCUMVEMJS0123456." + '\n')  # tells where you are and the planet's code
    weight = float(input("What is your ship's weight, " + name + "? " + '\n'))  # their weight
    speed = float(input("How fast do you want to go (Ve(km/s)), " + name + ":" + '\n'))  # their velocity
    if speed > 24:  # can't be greater than this
        print("I'm sorry, you were too fast and have crashed. Please try again!" + '\n')
        placement()
    if speed < 20:  # can't be less than this
        print("I'm sorry, you were too slow and have crashed. Please try again!" + '\n')
        placement()
    print("You have left the planet, " + name + "!" + '\n')
    Escape_Uranus()  # takes to other planets function


def Neptune():  # Neptune planet function
    global name  # variable can be used anywhere
    global score
    global counter
    print(
        name + ", you are on Neptune and the planet code is, PCN0." + '\n')  # tells where you are and the planet's code
    weight = float(input("What is your ship's weight, " + name + "? " + '\n'))  # their weight
    speed = float(input("How fast do you want to go (Ve(km/s)), " + name + ":" + '\n'))  # their velocity
    if speed > 33:  # can't be greater than this
        print("I'm sorry, you were too slow and have crashed. Please try again!" + '\n')
        placement()
    if speed < 29:  # can't be lower than this
        print("I'm sorry, you were too slow and have crashed. Please try again!" + '\n')
        placement()
    print("You have left the planet, " + name + "!" + '\n')
    Escape_Neptune()  # takes to planets function


def Menu():
    global name  # variable can be used anywhere
    global score
    global counter
    score = 0
    counter = 0
    name = input("Please enter your name! " + '\n')  # asks user for name to be used as global variable
    print(
        "Welcome to Cosmic Wave, " + name + "!" + '\n' + '\n' + "In this game, you will be exploring planets to earn as many points as possible to win!" + '\n' + "If you are succesful then you can become a self-proclaimed hero! However, if you lose...")
    print("Please remember to enter the correct weight and speeed of the ship!" + '\n' + "Enjoy!" + '\n')
    # ABOVE. It tells you the point of the game and how to play!
    start = input(
        "MENU" + '\n' + "1.Start Game" + '\n' + "2.Planet Code" + '\n' + "3.Quit"'\n' + '\n' + name + ", what do you want to do? " + '\n')  # ABOVE. It gives the choices of what the user can do.
    if start == "1":
        Earth()  # if they chose Start Game they go to Earth
    elif start == "2":  # if they chose Planet code they go to
        while True:  # while loop if they don't choose one of the codes
            code = input("Please enter the planet code! " + '\n')  # asks user for planet code
            if code == "PCM0":
                Mercury()  # if they chose Planet code they go to Mercury
                break  # stops the while loop
            elif code == "PCVM01":
                Venus()  # if they chose Planet code they go to Venus
                break  # stops the while loop
            elif code == "PCEMV012":
                Earth()  # if they chose Planet code they go to Earth
                break  # stops the while loop
            elif code == "PCMMVE0123":
                Mars()  # if they chose Planet code they go to Mars
                break  # stops the while loop
            elif code == "PCJMVEM01234":
                Jupiter()  # if they chose Planet code they go to Jupiter
                break  # stops the while loop
            elif code == "PCSMVEMJ012345":
                Saturn()  # if they chose Planet code they go to Saturn
                break  # stops the while loop
            elif code == "PCUMVEMJS0123456":
                Uranus()  # if they chose Planet code they go to Uranus
                break  # stops the while loop
            elif code == "PCN0":
                Neptune()  # if they chose Planet code they go to Neptune
                break  # stops the while loop
            else:
                print(
                    "Sorry, " + name + ", try again!" + '\n')  # if they didn't choose right code if asks them again till they get it
    elif start == "3":
        quit()  # if they chose Quit it ends the game
    else:
        print("Please try again." + '\n')
        Menu()  # if they chose something other than the choices it restarts function


Menu()