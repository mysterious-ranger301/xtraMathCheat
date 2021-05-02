# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:46:44 2021

@author: Mysterious Ranger

XtraMath cheat machine
Uses PyAutoGUI for automatic answers!
Note: install pyautogui, pytesseract, and pillow using pip install before
running
Note 2: try the default coordinates first and if they don't work, use your
own
Note 3: install the tesseract executable first and set the
t.pytesseract.tesseract_cmd to your tesseract installation
Note 4: set the image paths to your desired
"""

__version__ = '1.0.1'

# import libraries
import pyautogui as p, pytesseract as t, time, os
from PIL import Image

p.FAILSAFE = True
p.PAUSE = 0

# configure pytesseract
t.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def extractNumbers(text):
    text.strip('\n')
    nums = list(range(10))
    nums = [str(num) for num in nums]
    # nums[0] = 'J'
    # nums[2] = 'Z'
    detected = ''
    for char in text:
        print(char)
        if char in nums:
            detected += char
        elif char == 'O':
            detected += '0'
        elif char == 'A':
            detected += '4'
        elif char == 'Z':
            detected += '2'
    return detected

# set coordinates (try these, and if they don't work, insert your own)
im1coor = (915, 434, 1075 - 928, 571 - 434)
im2coor = (915, 576, 1075 - 949, 710 - 576)
path1 = 'C:\\im1.png' # set these to
path2 = 'C:\\im2.png' # your desired paths
print('Press enter to start')
input()

while True:
    im1 = p.screenshot(path1, region=im1coor)
    im2 = p.screenshot(path2, region=im2coor)
    try:
        im1 = Image.open(path1)
        im2 = Image.open(path2)
    except:
        print('Could not open im1 or im2; using screenshots')
    text1 = t.image_to_string(im1, config='--psm 6')
    text2 = t.image_to_string(im2, config='--psm 6')
    text1 = extractNumbers(text1)
    text2 = extractNumbers(text2)
    print('Text: {0} and {1}'.format(text1, text2))
    # if text1 == 'J':
        # text1 = '0'
    # elif text2 == 'J':
        # text2 = '0'
    # elif text1 == 'Z':
        # text1 = '2'
    # elif text2 == 'Z':
        # text2 = '2'
    try:
        text1 = int(text1)
        text2 = int(text2)
    except:
        # just leave it and diagnose
        time.sleep(0.5)
        continue
    print('Result: {0}'.format(text1 * text2))
    p.click(1256, 429)
    p.typewrite(str(text1 * text2))
    try:
        os.remove(path1)
        os.remove(path2)
    except:
        print('Could not remove paths 1 or 2')
    time.sleep(1.2)
# text = t.image_to_string(shot)
# print('Text: ' + text)


