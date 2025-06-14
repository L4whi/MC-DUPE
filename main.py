import fcsx
import keyboard


def main(co):
    for i in range(co):
        # Select the bundle, and then dupe it
        fcsx.press("1")
        fcsx.wait(0.5)
        fcsx.mouseMove(856, 465)
        fcsx.wait(2)
        fcsx.click("right")
        fcsx.wait(0.05)
        fcsx.press("q")


        # Take bundle and move to inventory
        fcsx.wait(1.5)
        fcsx.mouseMove(700, 322)
        fcsx.wait(1.5)
        fcsx.click_hold("left")
        fcsx.wait(.5)
        fcsx.click_release("left")
        
        fcsx.wait(1)
        fcsx.mouseMove(637, 588)
        fcsx.wait(0.4)
        fcsx.click_hold("left")
        fcsx.wait(1.2)
        fcsx.click_release("left")
        
        
keyboard.add_hotkey("alt+f", lambda: main(1))
keyboard.wait("`")