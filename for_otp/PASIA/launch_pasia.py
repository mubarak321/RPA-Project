import os
import pathlib

import keyboard

from PASIA.app_details import get_app_details
from PASIA.log import logs
import pyautogui
import time


logger = logs()
pasia_path = get_app_details()

username = "F894897"
pwd = "nji9nji9"

"""screenshot Path"""

# ok button screenshot
ok_button = pathlib.Path.cwd().joinpath('Images', 'ok.png')
ok_button = str(ok_button)

# username field screenshot
uname_field = pathlib.Path.cwd().joinpath('Images', 'user.png')
uname_field = str(uname_field)

# pasia production screenshot
sign_on_check = pathlib.Path.cwd().joinpath('Images', 'production.png')
sign_on_check = str(sign_on_check)

# otp verify
otp_verify = pathlib.Path.cwd().joinpath('Images', 'display_messages.png')
otp_verify = str(otp_verify)


# Launch PASIA app
def launch_app():

    logger.info(f"Launching PASIA application")
    os.startfile(pasia_path)
    pyautogui.moveTo(566, 410)

    logger.info(f"Trying to verify ok button visible or not on screen")
    # wait until login button is visible
    while True:
        if (pyautogui.locateOnScreen(ok_button) is not None):
            logger.info(f"Ok button visible on screen")
            break
        time.sleep(0.5)

    # click on username field
    uname = pyautogui.locateCenterOnScreen(uname_field)
    pyautogui.click(uname)
    pyautogui.write(username + '\t')
    time.sleep(1)
    pyautogui.write(pwd)
    pyautogui.press('enter')

    logger.info(f"Trying to verify login window visible or not on screen")
    # wait until login screen is visible
    while True:
        if (pyautogui.locateOnScreen(sign_on_check, confidence=0.8) is not None):
            logger.info(f"Login page visible on screen")
            break
        time.sleep(0.5)

    pyautogui.write(username + '\t')
    pyautogui.write(pwd)
    pyautogui.press('enter', presses=2)

    print("Press Shift key to continue")
    keyboard.wait('shift')
    print("Shift key pressed")
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
