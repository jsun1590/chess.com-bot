<p align="center">
<a href="https://github.com/Panc4kes/chess.com-bot/stargazers"><img src="https://img.shields.io/github/stars/Panc4kes/chess.com-bot" alt="Stars Badge"/></a>
<a href="https://github.com/Panc4kes/chess.com-bot/network/members"><img src="https://img.shields.io/github/forks/Panc4kes/chess.com-bot" alt="Forks Badge"/></a>
<a href="https://github.com/Panc4kes/chess.com-bot/pulls"><img src="https://img.shields.io/github/issues-pr/Panc4kes/chess.com-bot" alt="Pull Requests Badge"/></a></p>
<h1 align="center">Chess.com Bot</h1>
<p align="center">Simple Chess.com bot made in Python with the Chess and Selenium library.</p>

 ### Contents:
  - [Disclosure](#disclosure)
  - [Requirements](#requirements)
      - [Python Packages](#python-packages)
      - [Third Party Binaries](#third-party-binaries)
  - [Installation](#installation)
  - [Usage](#usage)
## Disclosure
- This project is created purely with educational and research purposes in mind. Please only use this bot to play against the computer. **I do not recommend using this bot in public matches for the purpose of cheating.**

## Requirements

#### Python Packages
- This script requires the below packages to run

| Packages |
| --- |
| [chess](https://pypi.org/project/chess/)
| [pywinauto](https://pypi.org/project/pywinauto/) | 
| [selenium](https://pypi.org/project/selenium/) | 

#### Third Party Binaries

- [Stockfish](https://stockfishchess.org/download/) ----> Move the exe to project folder"
- [Chrome Driver](https://chromedriver.chromium.org/downloads) ----> Move this file to project folder and rename as "chromedriver.exe" (if required)


## Installation
- Install required libraries via `pip` through the command `pip3 install -r requirements.txt --user`.
- Install Third Part Binaries as mentioned above.

## Usage
- To use the bot, open main.py and wait until the site has loaded. Press play against computer and click continue until you are at the main game window. Navigate over to your Python window and press any key to start the bot.
- The bot currently cannot detect turn change; it plays a turn every 3 seconds. Detection will be implemented in a future update.
- The bot does not currently support pawn promotions, but this feature will be implemented in a future update.
# [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
