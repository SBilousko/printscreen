# pip install pyautogui Pillow
import pyautogui, os, os.path
from datetime import datetime

root_folder = os.path.dirname(__file__)

pic = pyautogui.screenshot()

path = root_folder + "\\" + str(datetime.now()).split(" ")[0] + "\\"
if os.path.exists(path) == False:
    os.makedirs(path)

pic_name = path + "-".join("_".join(str(datetime.now())[:str(datetime.now()).index(".")].split(" ")).split(":")) + ".png"

pic.save(pic_name)
