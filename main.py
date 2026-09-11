import random

yourdict = {"S": "Snake", "W": "Water", "G" : "Gun"}

# Normal Mode: 

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
             print("You Lose The Gam")

            else:
                print("Something Went Wrong!")

# Score Mode

def score_mode():

    print("Score 3 Before Computer To The Win Game")

    score_user =  0
    score_computer = 0

    while 1:
          
        computer = random.choice(["S", "W", "G"])
        # print(f"Computer Choose: {computer}")

        if(score_user == 3 or score_computer == 3):
          
            if(score_user == 3):
                    print("You Win The Game!!! Congratulations!!!")
                    print("Want You Play Again? Y OR N ")
                    user_d = input("Enter Your Decision: ")
                    user_decision = user_d.capitalize()
                    if(user_decision == "Y"):
                      score_computer = 0
                      score_user = 0
                    else:
                      print("Thank You For Playing!!!")
                      break

            elif(score_computer == 3):
                print("Sorry, computer is Win The Game!!! Batter Luck Next Time!!! ")
                print("Want You Play Again? Y OR N ")
                user_d = input("Enter Your Decision: ")
                user_decision = user_d.capitalize()
                if(user_decision == "Y"):
                        score_user = 0 
                        score_computer = 0
                else:
                        print("Thank You For Playing!!!")
                        break

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
                score_computer +=1
                print(f"Your Score: {score_user}")
                print(f"Computer Score: {score_computer}")

            elif(computer == "W") and (user_choice == "S"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                score_user +=1
                print(f"Your Score: {score_user}")
                print(f"Computer Score: {score_computer}")

            elif(computer == "G") and (user_choice == "S"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                score_computer += 1
                print(f"Your Score: {score_user}")
                print(f"Computer Score: {score_computer}")

            elif(computer == "S") and (user_choice == "G"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                score_user += 1
                print(f"Your Score: {score_user}")
                print(f"Computer Score: {score_computer}")

            elif(computer == "G") and (user_choice == "W"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                score_user += 1 
                print(f"Your Score: {score_user}")
                print(f"Computer Score: {score_computer}")

            elif(computer == "W") and (user_choice == "G"):
             print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
             score_computer += 1
             print(f"Your Score: {score_user}")
             print(f"Computer Score: {score_computer}")

            else:
                print("Something Went Wrong!")


def main():
    print("\t Main Menu\n")
    print("\"S\" For Snake, \"W\" For Water & \"G\" For Gun")
    print("Choose Between 'S','W' & 'G'")
    print("Press 'E' For Exit The Game")
    print("Choose Mode: ")
    print("1. Normal Mode")
    print("2. Score Mode")
    print("Enter 1 For Normal Mode.")
    print("Enter 2 For Score Mode")

    choose_mode = int(input("Enter The 1 OR 2: "))

    if(choose_mode == 1):
        normal_mode()
    elif(choose_mode == 2):
        score_mode()
    else:
        print("Something Went Wrong!")

main()