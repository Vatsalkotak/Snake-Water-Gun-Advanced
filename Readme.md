# 🐍💧🔫 Snake-Water-Gun (Advanced Edition)

## 📝 Description
While Snake-Water-Gun (or Rock-Paper-Scissors) is a classic beginner project every programmer builds when learning functions, this repository takes a step further. I built this while following the CodeWithHarry "Ultimate Python Course", but instead of directly following the tutorial, I engineered the logic entirely on my own before watching the solution. 

Beyond the classic game, I have focused on building custom features and maintaining safe code backups.

## ✨ Features
* **Normal Mode:** The classic quick-play game with robust user input handling (case-insensitivity and error catching).
* **Score Mode:** A custom-built "Best of 3" tracking system that keeps round-by-round scores and declares a final winner.
* **Cheat Mode:** *(Coming Soon)*

## 📂 Project Structure
The main game runs entirely from a single file, while keeping separated files as safe backups for testing logic:
* `main.py` - The primary entry point. This contains the main menu, Normal Mode, and Score Mode all integrated together.
* `normal_mode.py` - A backup/testing file containing only the standalone normal mode logic.
* `score_mode.py` - A backup/testing file containing only the standalone score tracking logic.
* **Note:** Please test new logic in the individual separated files before merging them into `main.py` to prevent unexpected errors.

## 👨‍💻 Author
**Vatsal Kotak**

## 💡 Suggestions
Feel free to explore the code! Changes, suggestions, and optimizations are always welcome.