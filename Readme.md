# 🐍💧🔫 Snake-Water-Gun v2.0 (The Hacker Edition)

## 📝 Description
An advanced, highly optimized, and interactive CLI version of the classic Snake-Water-Gun (Rock-Paper-Scissors) game. Built entirely in Python, this V2.0 upgrade transforms a simple script into a robust software application featuring persistent data storage, a cyberpunk-inspired color terminal UI, and dynamic OS pathing for standalone execution. 

## 🚀 What's New in v2.0?
* **Cyber-Hacker UI:** Fully colorized terminal experience using `colorama` to highlight game states, warnings, and scores.
* **Persistent Data Storage:** Integrated File I/O to permanently save your High Scores and detailed match logs.
* **Smart Analytics:** View your entire gaming history directly from the Main Menu, complete with `datetime` timestamps.
* **Standalone Release:** Dynamic folder generation (`Game_Data`) ensures the executable version runs flawlessly and portably on any Windows machine without manual pathing requirements.

## 📂 Project Architecture
This repository is carefully structured to separate core game logic, UI styling, experimental development, and deployment builds.

* **`main.py`**: The fully featured original runner file. Execute this via Python to experience the complete game with the `colorama` UI.
* **`main_for_exe.py`**: The deployment-ready script injected with `os` and `sys` modules to handle dynamic pathing. It automatically generates the `Game_Data` folder required for the standalone `.exe` release.
* **`main_vanilla.py`**: The legacy functional logic preserving the raw code in standard white text, completely stripped of `colorama` styling.
* **`show_history.py`**: A dedicated module containing the standalone function to retrieve and display the user's match history.
* **`normal_mode.py` & `score_mode.py`**: The original, plain core logic files for both game modes, isolated without any cheat functionalities or UI styling.
* **`normal_cheat_mode.py` & `score_cheat_mode.py`**: The core game logic explicitly integrated with the hidden developer cheat codes.
* **`dev_normal_io.py` & `dev_score_io.py`**: Development modules containing the isolated File I/O logic for tracking high scores and saving match logs for their respective modes.

## ✨ Core Features
* **Main Menu System:** Clean and intuitive navigation between game modes, history, and application exit.
* **Normal Mode:** The classic quick-play game with an automated post-game statistics tracker (Total plays, Wins, Losses, Draws).
* **Score Mode (Best of 3):** A custom competitive tracker that counts rounds and automatically resets upon completion.
* **Developer Cheat Mode:** A hidden backdoor! Press 'C' during input to reveal the computer's choice before making your move. Press 'N' to revert to normal play.
* **Input Validation:** Bulletproof logic using `.isnumeric()` and case-insensitive `.capitalize()` checks to prevent application crashes.

## 📥 Download & Play
You do not need to compile the code yourself or install Python to play! Simply navigate to the **Releases** section on the right side of this repository to download the latest fully packaged `.exe` file for Windows. 

## 👨‍💻 Author
**Vatsal Kotak**

## 💡 Suggestions & Contributions
Feel free to explore the architecture, fork the repository, or test the executable! Changes, suggestions, and optimizations are always welcome.