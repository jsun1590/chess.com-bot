import chess
import chess.engine
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pywinauto import application
from pywinauto import Desktop
import time
import os
import sys
import glob

running_script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(running_script_directory)

for file in glob.glob("stockfish*"):
    print("Found Stockfish binary version",file.strip("stockfish_").strip(".exe"))
    stockfish_name = file

try:
    engine = chess.engine.SimpleEngine.popen_uci(stockfish_name)
except:
    print("No Stockfish binary found")
    input("Press any key to exit.")
    sys.exit()

board = chess.Board()
limit = chess.engine.Limit(time=0.2)
driver = webdriver.Chrome("chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
<<<<<<< Updated upstream
=======
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
>>>>>>> Stashed changes

with open("board.txt") as f:
    array = [i.split() for i in f]

#url = input("Enter a url\n> ")
url = "https://www.chess.com/play/computer?fen=qkb3nr/ppppppPp/8/8/8/8/PPPPPPP1/RNBQKBNR%20w%20KQ%20-%200%201"
driver.get(url)
input("Press any key to continue...")

def open_chrome():
    '''
    Funtion makes sure that Chrome is open so that check_fen can work properly.
    '''
    app = application.Application().connect(title_re ="Play Chess.*")
    app_dialog = app.top_window()

    if not app_dialog.has_focus():
        app_dialog.set_focus()

    

def check_fen():
    open_chrome()
    download = driver.find_element_by_class_name("download")
    download.click()
    time.sleep(2)

    form = driver.find_elements_by_class_name("form-input-input")[1]
    close = driver.find_element_by_css_selector(".icon-font-chess.x.icon-font-secondary")
    close.click()
    return form.get_attribute("value")

def find_loc(piece):
    for i, row in enumerate(array):
        for j, col in enumerate(row):
            if col == piece:
                return [j+1, 8-i]

<<<<<<< Updated upstream
while not board.is_game_over():
    board = chess.Board(check_fen())
=======
initial_fen = check_fen()
while not board.is_game_over():    
>>>>>>> Stashed changes
    piece_size = driver.find_element_by_css_selector(".layout-board.board").size["height"]/8
    while True:
        fen = check_fen()
        if board.fen() != fen or board.fen() == initial_fen:
            board = chess.Board(fen)
            break

    result = engine.play(board, limit)
    origin = find_loc(str(result.move)[:2])
    target = find_loc(str(result.move)[2:4])
    offset = [a - b for a, b in zip(target, origin)]
    offset[0] *= piece_size
    offset[1] *= -piece_size
    
    origin_push = iter(driver.find_elements_by_class_name(f"square-{origin[0]}{origin[1]}"))
    while True:
        try:
            action_chains = ActionChains(driver)
            action_chains.drag_and_drop_by_offset(next(origin_push), offset[0], offset[1]).click().perform()
            break
        except:
            pass
    # Make GUI Responses to the promotion from the engine pick
    if len(str(result.move)) > 4:
        promotion_button = driver.find_element_by_class_name("promotion-piece.w" + str(result.move)[-1].lower())
        promotion_button.click()
        time.sleep(2)
    board.push(result.move)
<<<<<<< Updated upstream
=======

    if len(str(result.move)) == 5:
        promotion = driver.find_element_by_css_selector("div.promotion-piece." + fen.split()[1] + str(result.move)[-1].lower())
    print(board, "\n")

>>>>>>> Stashed changes

    time.sleep(3)
    print(board, "\n")