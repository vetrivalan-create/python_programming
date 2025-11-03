import random
choice = ['rock','scissors','paper']
game = random.choice(choice)

P_score=0
C_score=0 
for i in range(10):
    n = input("Enter your choice:")
    print("Computer choice is",game)
    if n=="rock" and game == "scissors":
        print("Player wins...!")
        P_score+=1
        print(f"Score:Computer {C_score},Player {P_score}")
    elif n=="scissors" and game=="paper":
        print("Player wins...!")
        P_score+=1
        print(f"Score:Computer {C_score},Player {P_score}")
    elif n=="paper" and game=="rock":
        print("Player wins...!")
        P_score+=1
        print(f"Score:Computer {C_score},Player {P_score}")
    elif n==game:
        print("it's a tie")
    else:
        print("Computer wins...!")
        C_score+=1
        print(f"Score:Computer {C_score},Player {P_score}")
        

if P_score > C_score:
    print("🎉 Player wins the game!")
elif C_score > P_score:
    print("🤖 Computer wins the game!")
else:
    print("😐 It's an overall tie!")


    
        
    
    



