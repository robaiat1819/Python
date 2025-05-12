import pyautogui
import time


n = int(input("Enter a number: "))


print("You have 5 seconds to click in the text area...")
time.sleep(5)


for i in range(1, n + 1):
    pyautogui.typewrite("#" * i)
    pyautogui.press("enter")
