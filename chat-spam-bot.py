import pyautogui
import time
inp1=input("Enter the text you want to spam: ")
inp2=float(input("Enter speed of spam(1-50):"))
inp3=int(input("Enter the time you need to switch to your chat app:"))
rate=10/inp2 
def spam(text, speed):
 time.sleep(inp3)
 if speed<50 and speed>=1 :
  while True:
    pyautogui.write(text)
    pyautogui.press("enter")   
    time.sleep(speed)
spam(inp1, rate)