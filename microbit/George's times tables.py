choose = input("Pick a number WARNING DO NOT USE 5O OR HIGHER: ")
choose = int(choose)

pick = input("Pick another number WARNING DO NOT USE 1OO OR HIGHER: ")
pick = int(pick)

for i in range(1, pick + 1):
    print("%2d -> " % i, end="")
    
    for j in range(1, choose + 1):
        print("%4d" % (j*i), end="")
        
    print()