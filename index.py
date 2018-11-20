from automagica import *
import csv

# Business Objects


def AttachToNotepad():
    isRunning = ProcessRunning(name="notepad")
    if not isRunning:
        notepad = OpenNotepad()
    else:
        DeleteContentsOnNotepad()
    isRunning = ProcessRunning(name="notepad")

    return isRunning


def DeleteContentsOnNotepad():
    ClickOnPosition(540, 400)
    PressHotkey("ctrl", "a")
    Backspace()


def GetCSVRows(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)
        columns, *rows = [row for row in csv_reader]
        return [columns, rows]


def TypeInNotepad(*data):
    if AttachToNotepad():
        WriteCSVDataInNotepad(*data)


def WriteCSVDataInNotepad(columns, rows):
    for column in columns:
        Type(f"{column} | ")
    Enter()
    for cell in rows:
        Enter()
        for value in map(lambda c: f"{c} | ", cell):
            Type(value)


def CloseNotepad():
    while(ProcessRunning(name="notepad")):
        ClickOnPosition(*closePos)
        ClickOnPosition(*dontSavePos)


def ScreenShot(name="screenshot.jpg"):
    image = PIL.ImageGrab.grab()
    image.save(name)
    return name

# Variables


path = ""
if(len(sys.argv) > 1):
    path = sys.argv[1]
path = rf"{path}" or r"C:\Users\ralph.eclipse\Documents\BluePrism RPA Training\02 - Foundation Course\Orders.csv"
print(path)
closePos = [1140, 189]
dontSavePos = [684, 400]

# Process

data = GetCSVRows(path)
TypeInNotepad(*data)
imagePath = ScreenShot()
OpenImage(imagePath)
CloseNotepad()
