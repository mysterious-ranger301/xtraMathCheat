# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:11:55 2020

@author: alexe
"""

import pyautogui as automation, time

print('Press Ctrl-C to quit.')

try:
    while True:
        x, y = automation.position()
        string = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).ljust(4)
        pixelc = automation.screenshot().getpixel((x, y))
        string += ' RGB: (' + str(pixelc[0]).rjust(4)
        string += ', ' + str(pixelc[1]).rjust(3)
        string += ', ' + str(pixelc[2]).rjust(3) + ')'
        print(string)#, end='')
        # print('\b' * len(string), end='', flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\nDone.')