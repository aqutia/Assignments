from random import randrange, sample

random_number = randrange(1,20)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print("You are about to play TTQ'S Jackpot!")
print("___" * 12)
print("You MUST input 5 choices!")
print("NO DUPLICATE NUMBERS, please!")

winning_numbers = sample(range(1, 21), 5)

def match():
    if winning_numbers == input_numbers:
        print("Correct! You won $5000")
    else: 
        print(" Sorry that is incorrect!")
        print("___" * 10)
        print(winning_numbers)

def input_numbers():
    return (first, second, third, fourth, fifth)

first = int(input("What is your first: "))
for number in numbers:
    if first == 1:
        continue
    elif first == 2:
        continue
    elif first == 3:
        continue
    elif first == 4:
        continue
    elif first == 5:
        continue
    elif first == 6:
        continue
    elif first == 7:
        continue
    elif first == 8:
        continue
    elif first == 9:
        continue
    elif first == 10:
        continue
    elif first == 11:
        continue
    elif first == 12:
        continue
    elif first == 13:
        continue
    elif first == 14:
        continue
    elif first == 15:
        continue
    elif first == 16:
        continue
    elif first == 17:
        continue
    elif first == 18:
        continue
    elif first == 19:
        continue
    elif first == 20:
        continue
    else:
        first = int(input("Try Again: "))
        break
second = int(input("What is your next number: "))
for number in numbers:
    
    if second == 1 or second != first:
        continue
    elif second == 2  or second != first:
        continue
    elif second == 3  or second != first:
        continue
    elif second == 4 or second != first:
        continue
    elif second == 5 or second != first:
        continue
    elif second == 6  or second != first:
        continue
    elif second == 7  or second != first:
        continue
    elif second == 8  or second != first:
        continue
    elif second == 9  or second != first:
        continue
    elif second == 10  or second != first:
        continue
    elif second == 11  or second != first:
        continue
    elif second == 12  or second != first:
        continue
    elif second == 13  or second != first:
        continue
    elif second == 14  or second != first:
        continue
    elif second == 15  or second != first:
        continue
    elif second == 16  or second != first:
        continue
    elif second == 17  or second != first:
        continue
    elif second == 18  or second != first:
        continue
    elif second == 19  or second != first:
        continue
    elif second == 20  or second != first:
        continue
    else:
        second = int(input("Try Again: "))
        break
third = int(input("What is your third choice: "))
for number in numbers:
    if third == 1  or third != first or third != second:
        continue
    elif third == 2  or third != first or third != second:
        continue
    elif third == 3  or third != first or third != second:
        continue
    elif third == 4  or third != first or third != second:
        continue
    elif third == 5  or third != first or third != second:
        continue
    elif third == 6  or third != first or third != second:
        continue
    elif third == 7  or third != first or third != second:
        continue
    elif third == 8  or third != first or third != second:
        continue
    elif third == 9  or third != first or third != second:
        continue
    elif third == 10  or third != first or third != second:
        continue
    elif third == 11  or third != first or third != second:
        continue
    elif third == 12  or third != first or third != second:
        continue
    elif third == 13  or third != first or third != second:
        continue
    elif third == 14  or third != first or third != second:
        continue
    elif third == 15  or third != first or third != second:
        continue
    elif third == 16  or third != first or third != second:
        continue
    elif third == 17  or third != first or third != second:
        continue
    elif third == 18  or third != first or third != second:
        continue
    elif third == 19  or third != first or third != second:
        continue
    elif third == 20  or third != first or third != second:
        continue
    else:
        third = int(input("Try Again: "))
        break
fourth = int(input("Enter the fourth: "))
for number in numbers:
    if fourth == 1  or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 2 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth== 3 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 4 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 5 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 6 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 7 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 8 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 9 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 10 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 11 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 12 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 13 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 14 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 15 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 16 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 17 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 18 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 19 or fourth != first or fourth != second or fourth != third:
        continue
    elif fourth == 20 or fourth != first or fourth != second or fourth != third:
        continue
    else:
        print("SORRY!")
fifth = int(input("Lastly: "))
for number in numbers:
    if fifth == 1 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 2 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 3 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 4 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 5 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 6 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 7 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 8 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 9 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 10 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 11 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 12 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 13 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 14 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 15 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 16 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 17 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 18 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 19 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    elif fifth == 20 or fifth != first or fifth != second or fifth != third or fifth != fourth:
        continue
    else:
        fifth = int(input("Try Again: "))
        break

print("___" * 12)
print(f" Are these numbers correct?", {first}, {second}, {third}, {fourth}, {fifth})
answer = input()

if answer == "yes":
    print("___" *15)
    print("Let's compare yours against the winning numbers!")
    print("..." * 3)
    print("..." * 2)
    print("...")
    print("Gathering your duckies in a row.")
    print("__" * 15)
    if winning_numbers == input_numbers():
        print("YAY! You win $5000!")
    else:
        print("Sorry! You did not win the money!")
        print("No duckies for you. Try another pond!")
        print("___" * 3)
        print(winning_numbers)

else:
    print("Okay. Bye!")