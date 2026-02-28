#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2026-02-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : appLP
# Module        : CanvasImage

"""
This file allows to test CanvasImage

CanvasImage : This class is a tkinter frame where to put an image that can be manipulated.
"""



# %% Libraries
from corelp import debug
from plotlp import color
import numpy as np
import tkinter as tk
from applp import CanvasImage, App
debug_folder = debug(__file__)



# %% Function test
def test_function() :
    '''
    Test CanvasImage function
    '''

    #Generate image
    WL = np.linspace(350,850,250)
    img = np.empty((250,250,3))
    for pos,wl in enumerate(WL) :
        c = color(wl=wl)
        img[:,pos,:] = np.tile(c.RGB, (250, 1))

    crush = False
    app = App(crush=crush)
    canvasimg = CanvasImage(app, img, title='test image', ncoords=3)
    canvasimg.pack(fill='both', expand=True)
    app.mainloop()


# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)