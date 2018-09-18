
status1_1 = 1.1
status1_2 = 1.2
status1_3 = 1.3
status2_1 = 2.1
status2_2 = 2.2
status2_3 = 2.3
status3_1 = 3.1
status3_2 = 3.2
status3_3 = 3.3
player = status1_1
while player < 3.4:
    if player == status1_1:
        print("You can travel: (N)orth.")
        
        while True:
            num = input("Direction: ")
            if num == "n":
                
                player = status1_2
                break
            elif num == "N":
                
                player = status1_2
                break
            else: 
                print("Not a valid direction!")
    elif player == status1_2:
            print("You can travel: (N)orth or (E)ast or (S)outh.")
            
            while True:
                num = input("Direction: ")
                if num == "n":
                    
                    player = status1_3
                    break
                elif num == "N":
                    
                    player = status1_3
                    break
                elif num == "e":
                    
                    player = status2_2
                    break
                elif num == "E":
                    
                    player = status2_2
                    break
                elif num == "s":
                    
                    player = status1_1
                    break
                elif num == "S":
                    
                    player = status1_1
                    break
                else:
                    print("Not a valid direction!")
    elif player == status1_3:
            print("You can travel: (E)ast or (S)outh.")
            
            while True:
                num = input("Direction: ")
                if num == "e":
                    
                    player = status2_3
                    break
                elif num == "E":
                    
                    player = status2_3
                    break
                elif num == "s":
                    
                    player = status1_2
                    break
                elif num == "S":
                    
                    player = status1_2
                    break
                else:
                    print("Not a valid direction!")
    elif player == status2_3:
            print("You can travel: (E)ast or (W)est.")
            
            while True:
                num = input("Direction: ")
                if num == "e":
                    
                    player = status3_3
                    break
                elif num == "E":
                    
                    player = status3_3
                    break
                elif num == "w":
                    
                    player = status1_3
                    break
                elif num == "W":
                    
                    player = status1_3
                    break
                else:
                    print("Not a valid direction!")
    elif player == status3_3:
            print("You can travel: (S)outh or (W)est.")
            
            while True:
                num = input("Direction: ")
                if num == "w":
                    
                    player = status2_3
                    break
                elif num == "W":
                    
                    player = status2_3
                    break
                elif num == "s":
                    
                    player = status3_2
                    break
                elif num == "S":
                    
                    player = status3_2
                    break
                else:
                    print("Not a valid direction!")
    elif player == status3_2:
            print("You can travel: (N)orth or (S)outh.")
        
            while True:
                num = input("Direction: ")
                if num == "n":
                    player = status3_3
                    break
                elif num == "N":
                
                    player = status3_3
                    break
                elif num == "s":
                
                    player = status3_1
                    break
                elif num == "S":
                
                    player = status3_1
                    break
                else:
                    print("Not a valid direction!")
    elif player == status2_2:
        print("You can travel: (S)outh or (W)est.")
        
        while True:
            num = input("Direction: ")
            if num == "e":
                
                player = status1_2
                break
            elif num == "E":
                
                player = status1_2
                break
            elif num == "s":
                
                player = status2_1
                break
            elif num == "S":
                
                player = status2_1
                break
            else:
                print("Not a valid direction!")
    elif player == status2_1:
        print("You can travel: (N)orth.")
        
        while True:
            num = input("Direction: ")
            if num == "n":
                
                player = status2_2
                break
            elif num == "N":
                
                player = status2_2
                break
            else: 
                print("Not a valid direction!")
    elif player == status3_1:
        break
print("Victory!")
        


        






