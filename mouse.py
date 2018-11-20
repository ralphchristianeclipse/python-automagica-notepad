import win32gui
import time
import win32api


elements = {}
key = ''
start = 'not'
while (key != 'x'):
    if start == 'y':
        flags, hcursor, (x, y) = win32gui.GetCursorInfo()
        time.sleep(0.5)

        key = input(f"Enter element name for x: {x} y: {y} \n")
        elements[key] = [x, y]
        print(elements)
        if key == 'reset':
            start = input("Select an element now? (y/n) \n")
    else:
        start = input("Select an element now? (y/n) \n")
