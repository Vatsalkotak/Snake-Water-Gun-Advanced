import random

yourdict = {"S": "Snake", "W": "Water", "G" : "Gun"}

print("\"S\" For Snake, \"W\" For Water & \"G\" For Gun")
print("Choose Between 'S','W' & 'G'")
print("Press 'E' For Exit The Game")

def normal_cheat_mode():

    total = 0
    score_user = 0
    score_computer = 0
    total_draw = 0

    is_cheat = False
    while 1:


        computer = random.choice(["S", "W", "G"])
        # print(f"Computer Choose: {yourdict[computer]}")

        if(is_cheat == True):
            print(f"[Cheat Mode Active] Computer Choose {yourdict[computer]}")
            
        user = input("Enter Your Choice: ")
        user_choice = user.capitalize()

        if("S" in user_choice or "G" in user_choice or "W" in user_choice):
            total += 1 

        if(user_choice == "E"):
          print("Thank You For Playing The Game!")
          print(f"You Choose Total {total} Times,")
          print(f"You Win {score_user} Times &")
          print(f"Computer Wins {score_computer} Times &")
          print(f"{total_draw} Times Draw The Game.")
          break

        if(computer == user_choice):
            print(f"You Choose {yourdict[user_choice]} & Computer Choose {yourdict[computer]}")
            print("Game is Draw")
            total_draw += 1
        else:
            if(computer == "S") and (user_choice == "W"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Lose The Game!")
                score_computer += 1

            elif(computer == "W") and (user_choice == "S"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Win The Game! ")
                score_user += 1 

            elif(computer == "G") and (user_choice == "S"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Lose The Game! ")
                score_computer += 1

            elif(computer == "S") and (user_choice == "G"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Win The Game!")
                score_user += 1

            elif(computer == "G") and (user_choice == "W"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Win The Game!")
                score_user += 1

            elif(computer == "W") and (user_choice == "G"):
             print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
             print("You Lose The Game!")
             score_computer += 1

            elif("C" in user_choice):
                is_cheat = True

            elif("N" in user_choice):
                is_cheat = False

            else:
                print("Something Went Wrong!")

normal_cheat_mode()