# XtraMathCheat
A Python program that does XtraMath by itself!
# Before you run
You're gonna have to install some libraries
in order for the program to work.

*Pillow*
This program uses pillow for its image
detecting. Really simple install, just
_pip install pillow_

*PyTesseract & Tesseract*
This program uses tesseract for its
OCR capabilities. Fairly simple install;
just run _pip install pytesseract_
Installing normal tesseract for Windows is a bit
tricky, but you can install it here:
https://github.com/UB-Mannheim/tesseract/wiki
In the program, the variable
_t.pytesseract.tesseract\_cmd_ is the path
where your tesseract executable lies

*PyAutoGUI*
Again, really simple to install, just run
_pip install pyautogui_

# Coordinates
You could try the default coordinates in the
program, but if they don't work for some
reason then you could just use _mouseNow.py_
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
program. It will automatically click on the Chrome window,
causing it to focus on that, and the rest, you probably
know! It will automatically do the questions for you,
and when it's on the new mode thing, it will stay quiet until
it sees the numbers in the question again. To disable it,
put your cursor on the top-left side of the screen, and it
will activate the PyAutoGUI.FailsafeException, causing the
program to stop.
And that's it! You're free to ace the XtraMath quiz!
You could modify the program for yourself, but if you're
to recreate it, make sure to put my name in there!
