import random
from datetime import datetime

yourdict = {"S": "Snake", "W": "Water", "G" : "Gun"}

# Normal Cheat Mode: 

def normal_cheat_mode():

    total = 0
    score_user = 0
    score_computer = 0
    total_draw = 0
    total_score = 0
    with open("high_score.txt") as f:
        high_score = f.read()
    is_cheat = False
    mode = "Normal Mode"
    

    while 1:

        if(is_cheat == True):
                mode = "Normal_Cheat_Mode"
        else: 
            mode = "Normal Mode"

        computer = random.choice(["S", "W", "G"])
        # print(f"Computer Choose: {yourdict[computer]}")

        if(is_cheat == True):
            print(f"[Cheat Mode Active] Computer Choose: {yourdict[computer]}")
            
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
          print(high_score_func(score_user))
          with open("high_score.txt", "r") as f:
              t_high_score = f.read()
          logs_func(mode, score_user, score_computer, total_draw, t_high_score)
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
                total_score += 1
                print(f"Your Total Score is: {total_score}")

            elif(computer == "G") and (user_choice == "S"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Lose The Game! ")
                score_computer += 1

            elif(computer == "S") and (user_choice == "G"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Win The Game!")
                score_user += 1
                total_score += 1
                print(f"Your Total Score is: {total_score}")

            elif(computer == "G") and (user_choice == "W"):
                print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
                print("You Win The Game!")
                score_user += 1
                total_score += 1
                print(f"Your Total Score is: {total_score}")

            elif(computer == "W") and (user_choice == "G"):
             print(f"Computer choose {yourdict[computer]} & You Choose {yourdict[user_choice]}")
             print("You Lose The Game!")
             score_computer += 1

            elif("C" in user_choice):
                is_cheat = True

            elif("N" in user_choice):
                is_cheat = False

            elif("H" in user_choice):
                show_history()

            else:
                print("Something Went Wrong!")

#  High-Score Function

def high_score_func(score_user):
    with open("high_score.txt", "r") as f:
        high_score = f.read()

    if(high_score != ""):
        high_score = int(high_score)
    else:
        high_score = 0

    if(score_user > high_score):
        with open("high_score.txt" , "w") as f:
            f.write(str(score_user))

        return f"Congratulations!!! You Braked the High-Score,\nYour New High-Score is {score_user}"

    with open("high_score.txt", "r") as f:
        old_high_score = f.read()
    
    return f"High-Score Not Braked, Your Old High-Score is: {old_high_score}"

# logs save function for normal mode

def logs_func(mode, score_user, score_computer, total_draw, high_score):

    current_time = datetime.now().strftime("%d-%b-%Y %I:%M %p")

    time_stamp = f"[{current_time}] Mode: {mode} | You Scored: {score_user} | Computer Scored: {score_computer} | Total Draw: {total_draw} | High-Score: {high_score}"

    with open("logs.txt", "a") as f:
        f.write(time_stamp + "\n\n")

    return time_stamp

# Score Cheat Mode

def score_cheat_mode():

    is_cheat = False

    score_user =  0
    score_computer = 0
    total_draw = 0
    total_rounds = 0
    user_won_rounds = 0
    mode = "Score Mode"
    
    while 1:

        if(is_cheat == True):
            mode = "Score_Cheat_Mode"
        else:
            mode = "Score_Mode"

        computer = random.choice(["S", "W", "G"])
        # print(f"Computer Choose: {yourdict[computer]}")

        if(is_cheat == True):
            print(f"[Cheat Mode Active] Computer choose: {yourdict[computer]}")

        if(score_user == 3 or score_computer == 3):

            total_rounds += 1
          
            if(score_user == 3):
                    user_won_rounds += 1

                    print("You Win The Game!!! Congratulations!!!")
                    print("Want You Play Again? Y OR N ")
                    user_d = input("Enter Your Decision: ")
                    user_decision = user_d.capitalize()
                    if(user_decision == "Y"):
                      score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_won_rounds)
                      score_computer = 0
                      score_user = 0
                      total_draw = 0
                      is_cheat = False
                    else:
                      print("Thank You For Playing!!!")
                      score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_won_rounds)
                      break

            elif(score_computer == 3):
                is_cheat = False
                print("Sorry, computer is Win The Game!!! Batter Luck Next Time!!! ")
                print("Want You Play Again? Y OR N ")
                user_d = input("Enter Your Decision: ")
                user_decision = user_d.capitalize()
                if(user_decision == "Y"):
                        score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_won_rounds)
                        score_user = 0 
                        score_computer = 0
                        total_draw = 0
                else:
                        print("Thank You For Playing!!!")
                        score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_won_rounds)
                        break

        user = input("Enter Your Choice: ")
        user_choice = user.capitalize()

       
        if(user_choice == "E"):
          score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_won_rounds)
          print("Thanks")
          break

          

        if(computer == user_choice):    
            print(f"You Choose {yourdict[user_choice]} & Computer Choose {yourdict[computer]}")
            print("Game is Draw")
            total_draw += 1
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

            elif("H" in user_choice):
                show_history()

            else:
                print("Something Went Wrong!")

# Save Logs For Score Mode Fucntion 

def score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_win_rounds):

    current_time = datetime.now().strftime("%d-%b-%Y %I:%M %p")

    time_stamp = f"[{current_time}] Mode: {mode} | You Scored: {score_user} | Computer Scored: {score_computer} | Total Draw: {total_draw} | Total Rounds Played: {total_rounds} | Rounds Won By User: {user_win_rounds}"

    with open("logs.txt", "a") as f:
        f.write(time_stamp + "\n\n")

    return time_stamp

# Show History Function For Show Game Logs

def show_history():
    with open("logs.txt", "r") as f:
        history = f.read()
    print(history)

    return history

# Main Function

def main():
    while 1:

        print("\t----->Main Menu<-----")
        print("\"S\" For Snake, \"W\" For Water & \"G\" For Gun")
        print("Choose Between 'S','W' & 'G'")
        print("Press 'E' For Exit The Game")
        print("Press 'M' For Back in Main Menu")
        print("Press'H' For Show Game History ")
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

        elif(choose_mode == "H"):
            show_history()
                
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