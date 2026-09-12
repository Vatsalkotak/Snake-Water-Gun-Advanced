# 🐍💧🔫 Snake-Water-Gun (Advanced Edition)

## 📝 Description
This is an advanced CLI version of the classic Snake-Water-Gun (Rock-Paper-Scissors) game. Built from scratch with custom logic, it features a complete Main Menu, robust error handling, and hidden developer cheat codes. 

## ✨ Features
* **Main Menu System:** Navigate easily between different game modes or exit the application.
* **Normal Mode:** The classic quick-play game with a post-game statistics tracker (Total plays, Wins, Losses, Draws).
* **Score Mode:** A custom "Best of 3" tracking system that automatically resets upon completion.
* **Developer Cheat Mode:** A hidden backdoor! Press 'C' during input to reveal the computer's choice before making your move. Press 'N' to revert to normal play.
* **Input Validation:** Prevents crashes using `.isnumeric()` and case-insensitive `.capitalize()` checks.

## 📂 Project Architecture
The project is built with a modular approach, keeping the main runner clean while preserving backup logic:
* `main.py` - The central runner containing the Main Menu and integrated game modes.
* `normal_cheat_mode.py` / `score_cheat_mode.py` - Core logic files with the active cheat switch.
* `normal_mode.py` / `score_mode.py` - Safe backup files containing the classic logic without the cheat integration.

## 👨‍💻 Author
**Vatsal Kotak**

## 💡 Suggestions
Feel free to explore the code! Changes, suggestions, and optimizations are always welcome.