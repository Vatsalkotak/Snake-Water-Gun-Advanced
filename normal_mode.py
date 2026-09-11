import random

yourdict = {"S": "Snake", "W": "Water", "G" : "Gun"}

print("\"S\" For Snake, \"W\" For Water & \"G\" For Gun")
print("Choose Between 'S','W' & 'G'")
print("Press 'E' For Exit The Game")
score_user =  0
score_computer = 0

def normal_mode():
    while 1:

        computer = random.choice(["S", "W", "G"])
        # print(f"Computer Choose: {computer}")

        user = input("Enter Your Choice: ")
        user_choice = user.capitalize()

        if(user_choice == "E"):
          print("Thanks")
          break

        if(computer == user_choice):
            print(f"You Choose {yourdict[user_choice]} & Computer Choose {yourdict[computer]}")
            print("Game is Draw")
        else:
            if(computer == "S") and (user_choice == "W"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Lose The Game!")

            elif(computer == "W") and (user_choice == "S"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Win The Game! ")

            elif(computer == "G") and (user_choice == "S"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Lose The Game! ")

            elif(computer == "S") and (user_choice == "G"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Win The Game!")

            elif(computer == "G") and (user_choice == "W"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Win The Game!")

            elif(computer == "W") and (user_choice == "G"):
             print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
             print("You Lose The Game!")

            else:
                print("Something Went Wrong!")

normal_mode()