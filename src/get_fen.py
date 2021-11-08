from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def get_fen(driver):
    fen = ""
    for i in range(8, 0, -1):
        nums = 0
        for j in range(1, 9):
            try:
                piece = driver.find_element_by_xpath(f"//div[contains(@class, 'piece') and contains(@class, 'square-{j}{i}')]")
                fen += str(nums) if nums != 0 else ""
                nums = 0
                if piece.get_attribute("class").split()[1][0] != "s":
                    piece_name = piece.get_attribute("class").split()[1]
                else:
                    piece_name = piece.get_attribute("class").split()[2]

                fen += piece_name[1].upper() if piece_name[0] == "w" else piece_name[1].lower()
            except:
                nums += 1

        fen += str(nums) if nums != 0 else ""
        nums = 0
        fen += "/"
    return fen[:-1]
