import time
import chess
import chess.engine
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

engine = chess.engine.SimpleEngine.popen_uci("stockfish.exe")
board = chess.Board()
limit = chess.engine.Limit(time=0.2)
driver = webdriver.Chrome("chromedriver.exe")
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('window-size=1920x1480')

with open("board.txt") as f:
    array = [i.split() for i in f]


#url = input("Enter a url\n> ")
url = "https://www.chess.com/play/computer"
driver.get(url)
input("Press any key to continue...")


def check_fen():
    download = driver.find_element_by_class_name("download")
    download.click()
    time.sleep(2)
    form = driver.find_elements_by_class_name("form-input-input")[1]
    close = driver.find_element_by_css_selector(".icon-font-chess.x.icon-font-secondary")
    close.click()
    return form.get_attribute("value")

piece_size = driver.find_element_by_css_selector(".layout-board.board").size["height"]/8

def find_loc(piece):
    for i, row in enumerate(array):
        for j, col in enumerate(row):
            if col == piece:
                return [j+1, 8-i]

board = chess.Board(check_fen())
while not board.is_game_over():
    result = engine.play(board, limit)
    origin = find_loc(str(result.move)[:2])
    target = find_loc(str(result.move)[-2:])

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
    print("\n")
    time.sleep(3)
    
    board = chess.Board(check_fen())
    print(board, "\n")


