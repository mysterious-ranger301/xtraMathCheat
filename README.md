# XtraMathCheat
A Python program that does XtraMath by itself!

Version: 1.0.1

Last update: 2021/05/28

IMPORTANT: Usage has updated, read it carefully!
# Before you run
You're gonna have to install some libraries
in order for the program to work. (I assume you installed Python already, but if you didn't, go to http://python.org and install _Python 3_, not Python 2, because it
won't work with Python 2. In the installer, make sure to check the _Add Python to PATH_ checkbox in the bottom of the window, enabling you to use _pip_ in the command line, 
ensuring you could install the libraries below with ease. If you _did_ forget, don't worry, you just have to run an extra line in the command line, which is 
_cd C:\YourPythonInstallation\Scripts_ replacing _YourPythonInstallation_ with where you actually installed Python. (You have to run this once every time you open a new terminal 
window)). Also, when I say "just run pip install _library_" I mean, _open the command line, then run pip install _library__.

*Pillow*

This program uses pillow for its image
detecting. Really simple install, just
_pip install pillow_

*PyTesseract & Tesseract*

This program uses tesseract for its
OCR capabilities. Fairly simple install;
just run _pip install pytesseract_

Installing actual tesseract (pytesseract is just a wrapper) for Windows is a bit
tricky, but you can install it here:
https://github.com/UB-Mannheim/tesseract/wiki

For Linux, just run _sudo apt install tesseract-ocr_

In the program, the variable
_t.pytesseract.tesseract\_cmd_ is the path
where your tesseract executable lies

*PyAutoGUI*

This module is for the keyboard & mouse emulating
for the automatic answers.

Again, really simple to install, just run
_pip install pyautogui_

# Coordinates
You could try the default coordinates in the
program, but if they don't work for some
reason (they should) then you could just use _mouseNow.py_
to determine some new ones. The coordinates
themselves are box tuples (left, top, width, height).
In the program, the _im1coor_ and _im2coor_ are the
coordinates for the first number and second number
in the XtraMath question. The _path1_ and _path2_
variables are where the screenshots will be taken,
change them for your own paths.

# Usage
Open a command line terminal, and shrink it so it's
on the left side of the screen. Then open Chrome,
go on XtraMath, and right before the first question
appears, click on the terminal and run the _xtracheats.py_
program. It will automatically click on the Chrome window (if you shrank the terminal correctly),
causing it to focus on that, and the rest, you probably
know! It will automatically do the questions for you,
and when it's on the new mode thing, it will stay quiet until
it sees the numbers in the question again. Just to let you know, 
there is a 2% chance that the program will purposefully enter 
a question incorrect, just for your teachers to think it's you. 
To stop the program,
put your cursor on the top-left side of the screen, and it
should activate the PyAutoGUI.FailsafeException, causing the
program to stop. (If it doesn't work, click on the terminal window and press Ctrl+C, and it will stop).
And that's it! You're free to ace the XtraMath quiz!
You could modify the program for yourself, but if you're
to recreate it, make sure to put my name in there!
