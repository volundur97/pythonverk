
counter = 1
while (counter <=18):
    Par= int(input("Par of hole " + str(counter) + ": "))
    Score = int(input("Score on hole " + str(counter) + ": "))
    if Score - Par < -3:
        print("invalid score")
    elif Score - Par == -3:
        print("albatross")
    elif Score - Par == -2:
        print("eagle")
    elif Score - Par == -1:
        print("birdie")
    elif Score - Par == 0:
        print("par")
    elif Score - Par == 1:
        print("bogey")
    elif Score - Par == 2:
        print("double bogey")
    elif Score - Par == 3:
        print("triple bogey")
    elif Score - Par > 3:
        print("bad hole")
    counter +=1



