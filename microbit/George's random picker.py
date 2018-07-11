import random

number = random.randint(1, 100001)

print(number)
print ("pick a random number from 1 to 100,000")

while True:
    pick = input("Pick a number: ")
    pick = int(pick)

    if pick == number:
        print("ggrrrrr!! well done LOSER you were just lucky...")
        print("""
    /@
    \\ \\
    _> \\
 (__O)  \\
(____@)  \\
(____@)   \\
 (__o)_    \\
       \\    \\
""")
        break
    else:
        print("wrong! MUA HA HA HA HAAAAAAAA!!\ni have created the IMPOSSIBLE CHALLENGE *throws back his head and giggles evilly whilst stroking a deformed black cat and spinning slowly in his chair")
        if pick > number:
            print("its smaller than that!")
        else:
            print("its bigger than that!")