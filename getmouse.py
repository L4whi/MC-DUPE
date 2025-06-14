import pynput
import time
import fcsx

def get_coords():
    print("Waiting 3.5s before printing coords.")
    time.sleep(3.5)
    pos = fcsx.mouse.position
    print(f"{pos}")



get_coords()