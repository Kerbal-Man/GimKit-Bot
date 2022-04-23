from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def main():
    def click(x, y):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    # Color of center: (255, 219, 195)

    while keyboard.is_pressed('q') == False:
        flag = 0
        pic = pyautogui.screenshot(region=(584, 422, 751, 526))

        width, height = pic.size

        for x in range(0, width, 5):
            for y in range(0, height, 5):

                r, g, b = pic.getpixel((x, y))

                if b == 255 and r == 0 and g == 0:
                    flag = 1
                    click(x + 584, y + 422)
                    time.sleep(0.3)
                    click(960, 865)
                    time.sleep(0.01)
                    break

            if flag == 1:
                break


if __name__ == '__main__':
    main()
