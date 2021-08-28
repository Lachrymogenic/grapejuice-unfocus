from tkinter import *
from pynput import mouse
import psutil
from gi.repository import Notify
import resource
Notify.init("grapejuice-unfocus")
Notify.Notification.new("Running").show()

def checkIfProcessRunning(processName): #FROM: https://thispointer.com/python-check-if-a-process-is-running-by-name-and-find-its-process-id-pid/
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def on_click(x, y, button, pressed):
    if not pressed and button == mouse.Button.right:
        root = Tk()
        root.geometry('2x1')
        root.update()
        root.destroy()
        del root
    elif button == mouse.Button.right:
        #detect if roblox is running
        if checkIfProcessRunning('RobloxPlayerBet'):
            pass
        else:
            print('No roblox process running, quitting')
            Notify.Notification.new("No roblox process running, quitting").show()
            exit()

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
