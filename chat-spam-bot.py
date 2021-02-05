import pyautogui
import time
inp1 = input("Enter the text you want to spam: ")
inp2 = float(input("Enter speed of spam (1-50): "))
inp3 = int(input("Enter the number of texts, you want to send: "))
inp4 = int(input("Enter the time you need to switch to your chat app (in seconds): "))
def spam(text, speed, repeat, switch_time):
 print("Switch to you chat app NOW !")
 time.sleep(switch_time)
 rate = 10/speed 
 if speed<50 and speed>=1 :
  while repeat>0 :
    pyautogui.write(text)
    pyautogui.press("enter")
    repeat -= 1
    time.sleep(rate)
spam(inp1, inp2, inp3, inp4)
