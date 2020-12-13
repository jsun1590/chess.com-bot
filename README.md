
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)<br><br>

<div style="text-align:center">
<a href="https://github.com/Panc4kes/chess.com-bot/stargazers"><img src="https://img.shields.io/github/stars/Panc4kes/chess.com-bot" alt="Stars Badge"/></a>
<a href="https://github.com/Panc4kes/chess.com-bot/network/members"><img src="https://img.shields.io/github/forks/Panc4kes/chess.com-bot" alt="Forks Badge"/></a>
<a href="https://github.com/Panc4kes/chess.com-bot/pulls"><img src="https://img.shields.io/github/issues-pr/Panc4kes/chess.com-bot" alt="Pull Requests Badge"/></a>
<h1 align="center">Chess.com Bot</h1>
<i>Simple Chess.com bot made in Python with the Chess and Selenium library.</i>
</div>
 


Disclosure
This project is created purely with educational and research purposes in mind. Please only use this bot to play against the computer. **I do not condone using this bot in public matches for the purpose of cheating.**

 Installation
This script requires the Chess (https://pypi.org/project/chess/) and Selenium (https://pypi.org/project/selenium/) to run.
 requirements.txt
The required aforementioned libraries can be installed via `pip` through the command `pip3 install -r requirements.txt --user`
 3rd party binaries
Stockfish: https://stockfishchess.org/download/
Chrome Driver: https://chromedriver.chromium.org/downloads

You need to download both binaries and put them in the project folder. The stockfish binary should be named "stockfish.exe" and the chrome driver binary should be named "chromedriver.exe".

To use the bot, open main.py and wait until the site has loaded. Press play against computer and click continue until you are at the main game window. Navigate over to your Python window and press any key to start the bot.

The bot currently cannot detect turn change; it plays a turn every 3 seconds. Detection will be implemented in a future update.
The bot does not currently support pawn promotions, but this feature will be implemented in a future update.
