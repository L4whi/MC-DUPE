import pynput
import time
from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController

mouse = MouseController()
keyboard = KeyboardController()

def hold(key_):
    keyboard.press(key_)

def release(key_):
    keyboard.release(key_)

def wait(sec):
    time.sleep(sec)

def press(key_):
    keyboard.press(key_)
    keyboard.release(key_)

def mouseMove(x, y):
    mouse.position = (x, y)

def click(btn):
    if btn == "right":
        mouse.click(Button.right)
    elif btn == "left":
        mouse.click(Button.left)

    
def click_hold(btn):
    if btn == "right":
        mouse.press(Button.right)
    elif btn == "left":
        mouse.press(Button.left)


def click_release(btn):
    if btn == "right":
        mouse.release(Button.right)
    elif btn == "left":
        mouse.release(Button.left)
