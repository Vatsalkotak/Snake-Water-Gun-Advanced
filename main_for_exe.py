import random
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)

import os
import sys

# 1. DYNAMIC PATH DETECTOR (Pata lagao file kahan run ho rahi hai)
if getattr(sys, 'frozen', False):
    # Agar code .exe ban chuka hai aur chal raha hai
    base_path = os.path.dirname(sys.executable)
else:
    # Agar code VS Code mein .py file ki tarah chal raha hai
    base_path = os.path.dirname(os.path.abspath(__file__))

# 2. FOLDER CREATE KARNA (Usi location par jahan .exe hai)
folder_name = "Game_Data"
folder_path = os.path.join(base_path, folder_name)

# Agar Game_Data naam ka folder nahi hai, toh naya banao
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# 3. FILES KA EXACT PATH SET KARNA
file_high_score = os.path.join(folder_path, "high_score.txt")
file_logs = os.path.join(folder_path, "logs.txt")

# 4. EMPTY FILES CREATE KARNA (Taaki pehli baar run hone par error na aaye)
if not os.path.exists(file_high_score):
    with open(file_high_score, "w") as f:
        f.write("") # Khali file bana do

if not os.path.exists(file_logs):
    with open(file_logs, "w") as f:
        f.write("") # Khali file bana do

yourdict = {"S": "Snake", "W": "Water", "G" : "Gun"}

# Normal Cheat Mode: 

def normal_cheat_mode():

    total = 0
    score_user = 0
    score_computer = 0
    total_draw = 0
    total_score = 0
    with open(file_high_score) as f:
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
            print(Fore.MAGENTA + f"[Cheat Mode Active] Computer Choose: {yourdict[computer]}")
            
        user = input(Fore.CYAN + "Enter Your Choice: ")
        user_choice = user.capitalize()

        if("S" in user_choice or "G" in user_choice or "W" in user_choice):
            total += 1 

        if(user_choice == "E"):
          print(Fore.BLUE + "Thank You For Playing The Game!")
          print(Fore.BLUE + f"You Choose Total {Fore.YELLOW}{total} {Fore.BLUE}Times,")
          print(Fore.BLUE + f"You Win {Fore.YELLOW}{score_user} {Fore.BLUE}Times &")
          print(Fore.BLUE + f"Computer Wins {Fore.YELLOW}{score_computer} {Fore.BLUE}Times &")
          print(Fore.BLUE + f"{Fore.YELLOW}{total_draw} {Fore.BLUE}Times Draw The Game.")
          print(high_score_func(score_user))
          with open(file_high_score, "r") as f:
              t_high_score = f.read()
          logs_func(mode, score_user, score_computer, total_draw, t_high_score)
          break

        if(computer == user_choice):
            print(Fore.CYAN + f"You Choose {Fore.YELLOW}{yourdict[user_choice]} {Fore.MAGENTA}& {Fore.RED}Computer Choose {Fore.YELLOW}{yourdict[computer]}")
            print(Fore.YELLOW + "Game is Draw")
            total_draw += 1
        else:
            if(computer == "S") and (user_choice == "W"):
                print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
                print(Fore.RED + "You Lose The Game!")
                score_computer += 1

            elif(computer == "W") and (user_choice == "S"):
                print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
                print(Fore.GREEN + "You Win The Game! ")
                score_user += 1
                total_score += 1
                print(Fore.CYAN + f"Your Total Score is: {Fore.YELLOW}{total_score}")

            elif(computer == "G") and (user_choice == "S"):
                print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
                print(Fore.RED + "You Lose The Game! ")
                score_computer += 1

            elif(computer == "S") and (user_choice == "G"):
                print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
                print(Fore.GREEN + "You Win The Game!")
                score_user += 1
                total_score += 1
                print(Fore.CYAN + f"Your Total Score is: {Fore.YELLOW}{total_score}")

            elif(computer == "G") and (user_choice == "W"):
                print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
                print(Fore.GREEN + "You Win The Game!")
                score_user += 1
                total_score += 1
                print(Fore.CYAN + f"Your Total Score is: {Fore.YELLOW}{total_score}")

            elif(computer == "W") and (user_choice == "G"):
             print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
             print(Fore.RED + "You Lose The Game!")
             score_computer += 1

            elif("C" in user_choice):
                is_cheat = True

            elif("N" in user_choice):
                is_cheat = False

            elif("H" in user_choice):
                show_history()

            else:
                print(Fore.YELLOW + "Something Went Wrong!")

#  High-Score Function

def high_score_func(score_user):
    with open(file_high_score, "r") as f:
        high_score = f.read()

    if(high_score != ""):
        high_score = int(high_score)
    else:
        high_score = 0

    if(score_user > high_score):
        with open(file_high_score , "w") as f:
            f.write(str(score_user))

        return Fore.GREEN + f"Congratulations!!! You Braked the High-Score,\nYour New High-Score is: {Fore.YELLOW}{score_user}"

    with open(file_high_score, "r") as f:
        old_high_score = f.read()
    
    return Fore.CYAN + f"High-Score Not Braked, Your Old High-Score is: {Fore.YELLOW}{old_high_score}"

# logs save function for normal mode

def logs_func(mode, score_user, score_computer, total_draw, high_score):

    current_time = datetime.now().strftime("%d-%b-%Y %I:%M %p")

    time_stamp = f"[{current_time}] Mode: {mode} | You Scored: {score_user} | Computer Scored: {score_computer} | Total Draw: {total_draw} | High-Score: {high_score}"

    with open(file_logs, "a") as f:
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
            print(Fore.MAGENTA + f"[Cheat Mode Active] Computer choose: {yourdict[computer]}")

        if(score_user == 3 or score_computer == 3):

            total_rounds += 1
          
            if(score_user == 3):
                    user_won_rounds += 1

                    print(Fore.GREEN + "You Win The Game!!! Congratulations!!!")
                    print(Fore.CYAN + "Want You Play Again? Y OR N ")
                    user_d = input(Fore.CYAN + "Enter Your Decision: ")
                    user_decision = user_d.capitalize()
                    if(user_decision == "Y"):
                      score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_won_rounds)
                      score_computer = 0
                      score_user = 0
                      total_draw = 0
                      is_cheat = False
                    else:
                      print(Fore.GREEN + "Thank You For Playing!!!")
                      score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_won_rounds)
                      break

            elif(score_computer == 3):
                is_cheat = False
                print(Fore.RED + "Sorry, computer is Win The Game!!! Batter Luck Next Time!!! ")
                print(Fore.CYAN + "Want You Play Again? Y OR N ")
                user_d = input(Fore.CYAN + "Enter Your Decision: ")
                user_decision = user_d.capitalize()
                if(user_decision == "Y"):
                        score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_won_rounds)
                        score_user = 0 
                        score_computer = 0
                        total_draw = 0
                else:
                        print(Fore.GREEN + "Thank You For Playing!!!")
                        score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_won_rounds)
                        break

        user = input(Fore.CYAN + "Enter Your Choice: ")
        user_choice = user.capitalize()

       
        if(user_choice == "E"):
          score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_won_rounds)
          print(Fore.GREEN + "Thanks")
          break

          

        if(computer == user_choice):    
            print(Fore.CYAN + f"You Choose {Fore.YELLOW}{yourdict[user_choice]} {Fore.MAGENTA}& {Fore.RED}Computer Choose {Fore.YELLOW}{yourdict[computer]}")
            print(Fore.YELLOW + "Game is Draw")
            total_draw += 1
        else:
            if(computer == "S") and (user_choice == "W"):
                print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
                score_computer +=1
                print(Fore.CYAN + f"Your Score: {Fore.YELLOW}{score_user}")
                print(Fore.RED + f"Computer Score: {Fore.YELLOW}{score_computer}")

            elif(computer == "W") and (user_choice == "S"):
                print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
                score_user +=1
                print(Fore.CYAN + f"Your Score: {Fore.YELLOW}{score_user}")
                print(Fore.RED + f"Computer Score: {Fore.YELLOW}{score_computer}")

            elif(computer == "G") and (user_choice == "S"):
                print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
                score_computer += 1
                print(Fore.CYAN + f"Your Score: {Fore.YELLOW}{score_user}")
                print(Fore.RED + f"Computer Score: {Fore.YELLOW}{score_computer}")

            elif(computer == "S") and (user_choice == "G"):
                print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
                score_user += 1
                print(Fore.CYAN + f"Your Score: {Fore.YELLOW}{score_user}")
                print(Fore.RED + f"Computer Score: {Fore.YELLOW}{score_computer}")

            elif(computer == "G") and (user_choice == "W"):
                print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
                score_user += 1 
                print(Fore.CYAN + f"Your Score: {Fore.YELLOW}{score_user}")
                print(Fore.RED + f"Computer Score: {Fore.YELLOW}{score_computer}")

            elif(computer == "W") and (user_choice == "G"):
             print(Fore.RED + f"Computer choose {Fore.YELLOW}{yourdict[computer]} {Fore.MAGENTA}& {Fore.CYAN}You Choose: {Fore.YELLOW}{yourdict[user_choice]}")
             score_computer += 1
             print(Fore.CYAN + f"Your Score: {Fore.YELLOW}{score_user}")
             print(Fore.RED + f"Computer Score: {Fore.YELLOW}{score_computer}")

            elif("C" in user_choice):
                is_cheat = True

            elif("N" in user_choice):
                is_cheat = False

            elif("H" in user_choice):
                show_history()

            else:
                print(Fore.YELLOW + "Something Went Wrong!")

# Save Logs For Score Mode Fucntion 

def score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_win_rounds):

    current_time = datetime.now().strftime("%d-%b-%Y %I:%M %p")

    time_stamp = f"[{current_time}] Mode: {mode} | You Scored: {score_user} | Computer Scored: {score_computer} | Total Draw: {total_draw} | Total Rounds Played: {total_rounds} | Rounds Won By User: {user_win_rounds}"

    with open(file_logs, "a") as f:
        f.write(time_stamp + "\n\n")

    return time_stamp

# Show History Function For Show Game Logs

def show_history():
    with open(file_logs, "r") as f:
        history = f.read()
    print(Fore.YELLOW + history)

    return history

# Main Function

def main():
    while 1:

        print(Fore.CYAN + "\t----->Main Menu<-----")
        print(Fore.CYAN + "\"S\" For Snake, \"W\" For Water & \"G\" For Gun")
        print(Fore.CYAN + "Choose Between 'S','W' & 'G'")
        print(Fore.CYAN + "Press 'E' For Exit The Game")
        print(Fore.CYAN + "Press 'M' For Back in Main Menu")
        print(Fore.CYAN + "Press'H' For Show Game History ")
        print(Fore.CYAN + "Choose Mode: ")
        print(Fore.CYAN + "1. Normal Mode")
        print(Fore.CYAN + "2. Score Mode")
        print(Fore.CYAN + "Enter 1 For Normal Mode.")
        print(Fore.CYAN + "Enter 2 For Score Mode")
        
        choose_mode = input(Fore.CYAN + "Enter The 1 OR 2: ").upper()
        
        if(choose_mode == "E"):
            print(Fore.GREEN + "Thank You")
            input(Fore.CYAN + "Press Any Key To Exit the Application.")
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
                print(Fore.YELLOW + "Invalid Input! Please Enter 1 OR 2")
        else:
            print(Fore.YELLOW + "Something Went Wrong!")

   
main()