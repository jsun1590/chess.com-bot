<p align="center">
<a href="https://github.com/Panc4kes/chess.com-bot/stargazers"><img src="https://img.shields.io/github/stars/Panc4kes/chess.com-bot" alt="Stars Badge"/></a>
<a href="https://github.com/Panc4kes/chess.com-bot/network/members"><img src="https://img.shields.io/github/forks/Panc4kes/chess.com-bot" alt="Forks Badge"/></a>
<a href="https://github.com/Panc4kes/chess.com-bot/pulls"><img src="https://img.shields.io/github/issues-pr/Panc4kes/chess.com-bot" alt="Pull Requests Badge"/></a></p>
<h1 align="center">Chess.com Bot</h1>
<p align="center">Simple Chess.com bot made in Python with the Chess and Selenium library.</p>

 ### Contents:
  - [Disclosure](#disclosure)
  - [Requirements](#requirements)
      - [Python Packages](python-packages)
      - [Third Party Binaries](#third-party-binaries)
  - [Installation](#installation)
  - [Usage](#usage)
## Disclosure
- This project is created purely with educational and research purposes in mind. Please only use this bot to play against the computer. **I do not recommend using this bot in public matches for the purpose of cheating.**

## Requirements

#### Python Packages
- This script requires Python packages given below to run

| Package |
| --- |
| ` Chess ` | 
| ` Selenium ` | 

#### Third Party Binaries

- [Stockfish](https://stockfishchess.org/download/) ----> Move this file to root folder and rename as "stockfish.exe"
- [Chrome Driver](https://chromedriver.chromium.org/downloads) ----> Move this file to root folder and rename as "chromedriver.exe"


## Installation
- Install required libraries via `pip` through the command `pip3 install -r requirements.txt --user`.
- Install Third Part Binaries as mentioned at #Third Party Binaries(#third-party-binaries) .

## Usage
- To use the bot, open main.py and wait until the site has loaded. Press play against computer and click continue until you are at the main game window. Navigate over to your Python window and press any key to start the bot.
- The bot currently cannot detect turn change; it plays a turn every 3 seconds. Detection will be implemented in a future update.
- The bot does not currently support pawn promotions, but this feature will be implemented in a future update.
