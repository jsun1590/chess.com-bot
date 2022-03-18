import chess
import chess.engine
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pywinauto import application
import time
import os
import sys
import glob
from get_fen import get_fen

running_script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(running_script_directory)

for file in glob.glob("stockfish*"):
    print("Found Stockfish binary version", file.strip("stockfish_").strip(".exe"))
    stockfish = file

try:
    engine = chess.engine.SimpleEngine.popen_uci(stockfish)
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

# url = input("Enter a url\n> ")
# for pawn promotion testing
# url = "https://www.chess.com/play/computer?fen=qkb3nr/ppppppPp/8/8/8/8/PPPPPPP1/RNBQKBNR%20w%20KQ%20-%200%201"
url = "https://www.chess.com/play/computer"
driver.get(url)

def open_chrome():
    '''
    Funtion makes sure that Chrome is open so that check_fen can work properly.
    '''
    app = application.Application().connect(title_re ="Play Chess.*")
    app_dialog = app.top_window()

    if not app_dialog.has_focus():
        app_dialog.set_focus()

def check_fen(extension):
    open_chrome()
    base = get_fen(driver)
    return f"{base} {extension}"
    
        
def find_loc(piece):
    for i, row in enumerate(array):
        for j, col in enumerate(row):
            if col == piece:
                return [j+1, 8-i]


color = input("Whose turn is it right now? Choices are 'w' for white; 'b' for black\n> ")
print("\nCan the white king castle?\nk for king's side; q for queen's side; - for neither")
castle_w = input("Choices are 'kq', 'k', 'q', or '-'\n> ").upper()

print("\nCan the black king castle?\nk for king's side; q for queen's side; - for neither")
castle_b = input("Choices are 'kq', 'k', 'q', or '-'\n> ").lower()

print("\nWhat is the en passant target square in algebraic notation?")
en_passant = input("If a pawn has just made a two-square move, this is origin square.\nIf there is no en passant or you are not sure, put '-'.\n> ").lower()
half_move = input("\nWhat is the number of half moves? Put '0' if you are not sure.\n> ")
full_move = input("\nWhat is the number of full moves? Put 1' if you are not sure.\n> ")


initial_fen = check_fen(f"{color} {castle_w}{castle_b} {en_passant} {half_move} {full_move}")
print(initial_fen, "\n")
while not board.is_game_over():
    piece_size = driver.find_element_by_css_selector("#board-layout-chessboard").size["height"]/8
    print(piece_size)
    while True:
        fen = check_fen(board.fen().split(" ", 1)[1])
        print(fen, "\n")
        if board.fen() != fen or board.fen() == initial_fen:
            board = chess.Board(fen)
            break

    result = engine.play(board, limit)
    origin = find_loc(str(result.move)[:2])
    target = find_loc(str(result.move)[2:4])
    offset = [a - b for a, b in zip(target, origin)]
    offset[0] *= piece_size
    offset[1] *= -piece_size
    
    origin_push = driver.find_element_by_xpath(f"//div[contains(@class, 'piece') and contains(@class, 'square-{origin[0]}{origin[1]}')]")
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop_by_offset(origin_push, offset[0], offset[1]).perform()

    if len(str(result.move)) == 5:
        promotion = driver.find_element_by_css_selector("div.promotion-piece." + fen.split()[1] + str(result.move)[-1].lower())
        promotion.click()
        
    board.push(result.move)
    print(board, "\n")

    time.sleep(3)
