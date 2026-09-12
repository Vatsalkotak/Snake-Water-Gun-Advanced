import random

yourdict = {"S": "Snake", "W": "Water", "G" : "Gun"}

# Normal Cheat Mode: 

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
          input("Press Any Key To Close the Game")
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

            elif("M" in user_choice):
                main()

            else:
                print("Something Went Wrong!")


# Score Cheat Mode

def score_cheat_mode():

    is_cheat = False

    score_user =  0
    score_computer = 0
    
    while 1:
          

        computer = random.choice(["S", "W", "G"])
        # print(f"Computer Choose: {yourdict[computer]}")

        if(is_cheat == True):
            print(f"[Cheat Mode Active] Computer choose: {yourdict[computer]}")

        if(score_user == 3 or score_computer == 3):
          
            if(score_user == 3):
                    is_cheat = False
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
                is_cheat = False
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
          print("Thank You For Playing Game!")
          input("Press Any Key To Exit the Application.")
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

            elif("C" in user_choice):
                is_cheat = True

            elif("N" in user_choice):
                is_cheat = False

            elif("M" in user_choice):
                main()

            else:
                print("Something Went Wrong!")

# Main Function

def main():
    while 1:

        print("\t----->Main Menu<-----")
        print("\"S\" For Snake, \"W\" For Water & \"G\" For Gun")
        print("Choose Between 'S','W' & 'G'")
        print("Press 'E' For Exit The Game")
        print("Press 'M' For Back in Main Menu")
        print("Choose Mode: ")
        print("1. Normal Mode")
        print("2. Score Mode")
        print("Enter 1 For Normal Mode.")
        print("Enter 2 For Score Mode")
        
        choose_mode = input("Enter The 1 OR 2: ").upper()
        
        if(choose_mode == "E"):
            print("Thank You")
            input("Press Any Key To Exit the Application.")
            break
        
        elif(choose_mode == "M"):
            continue
                
        elif(choose_mode.isnumeric()):
            choose_mode1 = int(choose_mode)
        
            if(choose_mode1 == 1):
                normal_cheat_mode()
            elif(choose_mode1 == 2):
                score_cheat_mode()
            else:
                print("Invalid Input! Please Enter 1 OR 2")
        else:
            print("Something Went Wrong!")

   
main()