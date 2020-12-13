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
    print("Found Stockfish binary version",file.strip(".exe"))
    stockfish_name = file

try:
    engine = chess.engine.SimpleEngine.popen_uci(stockfish_name)
except:
    print("No Stockfish binary found")
    input("Press any key to exit.")
    sys.exit()

board = chess.Board()
limit = chess.engine.Limit(time=0.2)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--log-level=3")
driver = webdriver.Chrome("chromedriver.exe", options=chrome_options)
with open("board.txt") as f:
    array = [i.split() for i in f]

#url = input("Enter a url\n> ")
url = "https://www.chess.com/play/computer"
driver.get(url)
input("Press any key to continue...")

def open_chrome():
    '''
    THIS FUNCTION ASSURES THAT CHROME IS OPEN SO check_fen() CAN WORK PROPERLY
    '''
    app = application.Application().connect(title_re =".*Chess.*")
    app_dialog = app.top_window()

    if not app_dialog.has_focus():
        app_dialog.set_focus()

def check_fen():
    open_chrome()
    download = driver.find_element_by_css_selector("span.icon-font-chess.download")
    download.click()
    time.sleep(3)
    form = driver.find_elements_by_class_name("form-input-input")[1]
    fen = form.get_attribute("value")
    close = driver.find_element_by_css_selector("span.icon-font-chess.x.icon-font-secondary")
    close.click()
    time.sleep(3)

    return fen
        
def find_loc(piece):
    for i, row in enumerate(array):
        for j, col in enumerate(row):
            if col == piece:
                return [j+1, 8-i]

board = chess.Board(check_fen())
while not board.is_game_over():
    
    piece_size = driver.find_element_by_css_selector(".layout-board.board").size["height"]/8
    
    result = engine.play(board, limit)
    origin = find_loc(str(result.move)[:2])
    target = find_loc(str(result.move)[-2:])
    offset = [a - b for a, b in zip(target, origin)]
    # print(origin, target)
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
        
    board.push(result.move)
    print(board, "\n")

    while True:
        fen = check_fen()
        if board == fen:
            chess.Board(fen)
            continue
        else:
            board = chess.Board(check_fen())
            break


