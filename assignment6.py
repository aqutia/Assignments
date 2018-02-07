import time
from sys import exit


print("Welcome to the Where My Boo At?")
print("Are you ready to find your boo?")
time.sleep(3)
print("Okay enter your information below.")
print("---" * 15)

name = input("Enter the name you would like to go by in this quest: ")
age = int(input("What is your age: "))
if age<21:
    print("You cannot play this game, you need to be in school.")
elif age == "21" or age == "22" or age == "23" or age == "24": 
    print("Okay young buck, there are a couple of different ages I hope that is okay. :)")
elif age>= 25:
    print("You might know a little something. Well maybe not, you're still single. :/")
else:
    print("Okay. We need to get you off the market Moses!")
height = input("Describe your height: ")
weight = input("Describe your body type: ")
eyes = input("Describe the way your eyes look: ")
fact = input("A fact you want your date to know about you: ")
print("---" * 15)

sex = input("Are you a male or female: ")
if sex == "male":
    print("---" * 15)
    print(f"The bio that we will be showing  to the contestants is as follows: ")
    print(f"The bachelor that you selected is {name}. He is {age}, standing at {height}, {weight} and has {eyes} eyes.")
    print(f"One interesting thing about me is {fact}.")
    print("---" * 15)

    print(""" You have 3 lovely ladies to choose from.
    Who do you pick, 1, 2, or 3?""")

    ladies = input("> ")

    if ladies == "1":
        print("     You got Miley. Miley is 22 years old, has tanned skin and a tonned body to match.")
        print("     Miley's source of income is working on Instagram as a model.")
        print("     Miley has never worked a day in her life and does not plan to.")
        print("     Although Miley doesn't want to work, she does want to have a large family and a house on the hills.")
        print("     You may have seen her on a Fashion Nova ad or two.")
        print("     Want to change Miley into a Martha Stewart?")
        print("     What do you do?")
        print("---" * 15)
        print("Leave Miley where she is or take a chance on Miley?")

        miley = input("> ")

        if miley == "Leave Miley where she is":
            print("Your lose, Miley just signed a 100 million dollar contract with Tyra Banks")
            print("She is about to be ballin'")
        elif miley == " Take a chance on Miley":
            print("You and Miley meet and you guys hit it off.")
            print("You guys get engaged.")
            print("During the process of getting to know each other, Miley finds out that you cannot have kids.")
            print("Miley leaves you and runs off and marries a player from the New Orleans Saints.")
        else:
            print(f" Well, doing {miley} is probably better.")



    elif ladies == "2":
        print("     You got the illustrious Jessica.")
        print("     Jessica is drop dead beautiful and is up for partner at the law firm that she works at.")
        print("     She is 35 and has no plans of slowing down.")
        print("     Jessica hates kids and can not cook.")
        print("     She just wants a guy with an open schedule so she can control when she see's him.")
        print("     Jess wants you to quit your job and leave in her home.")
        print("     What do you do?")
        print("---" * 15)
        print("skip or pass")

        jessica = input("> ")

        if jessica == "quit":
            print("You go live with Jessica but she is never home.")
            print("She goes on a business trip with Thomas and they end of falling in love.")
            print("Jessica sends a U-Hal to the house and a note to tell you have 24 hours to vaccate.")
        elif jessica == "pass":
            print("Cool.")
            print("You ended up with Miley, you and Miley are now getting a divorce.")
            print("Jessica justs so happens to be Miley's lawyer.")
            print("After comparing notes, they get together and plan to kill you if the case didn't work out.")

    elif ladies == "3":
        print("     You have selected Taylor.")
        print("     Taylor is in her third year of school. She is pursuing a business degree.")
        print("     Taylor has one child, a beautiful 3 year old daughter.")
        print("     She wants a husband and a nice sized family. As well as to work.")
        print("     What do you do.")
        print("---" * 15)
        print("Take a chance or pass")
        
        taylor = input("> ")

        if taylor == "take a chance":
            print("You fall in love with Tayor.")
            print("Every time that you are with her, you fill like you are walking on air.")
            print("She has you singing the song by India Arie.")
            print("Your new favorite lyrics are : ")
            time.sleep(.5)
            from love_song import Lovesong
            print (Lovesong)
        if taylor == "pass":
            print("Loser.")
            print("Taylor graduates and buys the building you work at and fires you the first chance she gets.")
            print("Now you are a homeless shallow bum.")
            
    else:
        print("Uh, Hello? What are you doing?")
        
elif sex == "female":
    print("---" * 15)
    print(f"The bio that we will be showing  to the contestants is as follows: ")
    print(f"The bachelorette that you selected is {name}. She is {age}, standing at {height}, {weight} and has {eyes} eyes.")
    print(f"One interesting thing about me is {fact}.")

    print(""" You have 3 handsome gentleman to choose from.
    Who do you pick, 1, 2, or 3?""")

    man = input("> ")

    if man == "1":
        print("     You got Patrick. Patrick is 22 years old, has caramel skin and a tonned body to match.")
        print("     Patrick spends the majority of his days at the gym or on the football field.")
        print("     Patrick goes to MSU and is on a football scholarship.")
        print("     Patrick is not that bright, He pays a nerd to do his class work.")
        print("     His last girlfriend broke up with him because she caught him in be with her roommate.")
        print("     Patrick is being drafted into the NFL in 6 months?")
        print("     What do you do?")
        print("---" * 15)
        print("follow him or don't waste time?")

        patrick = input("> ")

        if patrick == "follow him":
            print("Your lose, Miley just signed a 100 million dollar contract with Tyra Banks")
            print("She is about to be ballin'")
        elif patrick == " Take a chance on Miley":
            print("You and Miley meet and you guys hit it off.")
            print("You guys get engaged.")
            print("During the process of getting to know each other, Miley finds out that you cannot have kids.")
            print("Miley leaves you and runs off and marries a player from the New Orleans Saints.")
        else:
            print(f" Well, doing {patrick} is probably better.")



    elif ladies == "2":
        print("     You got the distinguised James.")
        print("     James drives a 2018 drop top Audi.")
        print("     He is 35, a new partner at his law firm and has no plans of slowing down.")
        print("     James does not want to committ, he has been hurt before.")
        print("     But he still wants to date.")
        print("     James wants you to be his girl without the title.")
        print("     What do you do?")
        print("---" * 15)
        print("try or pass")

        james = input("> ")

        if james == "try":
            print("You and James have been dating for 10 years.")
            print("James is more dedicated to work than he is to you.")
            print("You end up having an affair with Rick and James kills you both.")
        elif james == "pass":
            print("Cool.")
            print("You ended up with Rick, you and James are now getting a divorce.")
            print("James justs so happens to be Rick's lawyer.")
            print("After comparing notes, they get together and plan to kill you if the case didn't work out.")

    elif ladies == "3":
        print("     You have selected Taylor.")
        print("     Taylor is in his third year of school. He is pursuing a business degree.")
        print("     Taylor has one child, a beautiful 3 year old daughter.")
        print("     He wants a wife and a nice sized family. As well as to work.")
        print("     What do you do.")
        print("---" * 15)
        print("Take a chance or pass")
        
        taylor = input("> ")

        if taylor == "take a chance":
            print("You fall in love with Taylor.")
            print("Every time that you are with him, you fill like you are walking on air.")
            print("He has you singing the song by India Arie.")
            print("Your new favorite lyrics are : ")
            time.sleep(.5)
            from love_song import Lovesong
            print (Lovesong)
        if taylor == "pass":
            print("Loser.")
            print("Taylor graduates and buys the building you work at and fires you the first chance he gets.")
            print("Now you are a homeless shallow bum.")           
    else:
        print("Uh, Hello? What are you doing?")
else:
    print("L O S E R ! GAME OVER !")

