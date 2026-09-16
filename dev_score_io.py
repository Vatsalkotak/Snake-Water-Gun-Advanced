import random
from datetime import datetime

yourdict = {"S": "Snake", "W": "Water", "G" : "Gun"}

print("\"S\" For Snake, \"W\" For Water & \"G\" For Gun")
print("Choose Between 'S','W' & 'G'")
print("Press 'E' For Exit The Game")

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

            else:
                print("Something Went Wrong!")

# Save Logs For Score Mode Fucntion 

def score_logs_func(mode, score_user, score_computer, total_draw, total_rounds, user_win_rounds):

    current_time = datetime.now().strftime("%d-%b-%Y %I:%M %p")

    time_stamp = f"[{current_time}] Mode: {mode} | You Scored: {score_user} | Computer Scored: {score_computer} | Total Draw: {total_draw} | Total Rounds Played: {total_rounds} | Rounds Won By User: {user_win_rounds}"

    with open("logs.txt", "a") as f:
        f.write(time_stamp + "\n\n")

    return time_stamp

score_cheat_mode()