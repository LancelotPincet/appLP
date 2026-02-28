#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2026-02-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : appLP
# Module        : App

"""
This file allows to test App

App : Custom tkinter App window that opens according to the monitor size.
"""



# %% Libraries
from corelp import debug
from applp import App
import tkinter as tk
debug_folder = debug(__file__)



# %% Function test
def test_function() :
    '''
    Test App function
    '''
    
    app = App("Testing")
    label = tk.Label(app, text="Tkinter is working!", font=("Arial", 14))
    label.pack(pady=20)
    button = tk.Button(app, text="Close", command=app.destroy)
    button.pack()
    app.mainloop()



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)