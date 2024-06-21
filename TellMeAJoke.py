import random, sys

print('Tell me your name!')
user_name = input()

print("I DON'T CARE ABOUT YOU NAME " + user_name.upper())
print('You have 3 chances to make me laugh, puny mortal!')
print('Tell me your best joke...')
print()

user_joke = input()

print("Hmmm, " + user_joke + "? I don't know, tell me!")

def my_function():
    user_punchline = input()

    number = random.randint(1, 5)

    if number == 1:
        print(user_punchline + "... HAHAHAHA")
        print("Excellent, you have made me laugh. Goodbye.")
        return True
    else:
        print(user_punchline + "... I don't get it...try again")
        another_joke = input()
        print("What do you mean " + another_joke + "...?")
        return False

jokesTold = 1
made_laugh = False

while (made_laugh == False & jokesTold <= 3):
    if jokesTold == 3:
        print()
        print("Game over, too many unfunny jokes, YOU DIED")
        break

    made_laugh = my_function()
    if made_laugh == False:
        jokesTold+= 1

sys.exit()