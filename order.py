from automagica import *


elementPositions = {
    'username': [675, 387],
    'password': [675, 432],
    'login': [675, 515],
    'find': [229, 213],
    'findFirstName': [619, 382],
    'findButton': [638, 424],
}


file = "Surface Automation Training.exe"
directory = r"C:\Users\ralph.eclipse\Documents\BluePrism RPA Training\03 - Introduction to Surface Automation"
path = fr"{directory}\{file}"


def click(name):
    ClickOnPosition(*elementPositions[name])


if(ProcessRunning(file)):
    click('username')
    Type("HEY")
    click('password')
    Type("HEY")
    click('login')

Wait(10)
click('find')
Wait(5)
click('findFirstName')
Type("a*")
Wait(5)
click('findButton')
