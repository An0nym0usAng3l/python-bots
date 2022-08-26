import pyautogui as pt
import time

count=1
msg = input("Enter message: ")
number = int(input("Number of Times to send: "))

#Time to wait before starting the function
delay = 10  

time.sleep(delay)


while(count <= num):
    pt.typewrite(msg)
    pt.press("enter")
    i+=1

pt.typewrite("Alhaji bot completed its task")
pt.press("enter")