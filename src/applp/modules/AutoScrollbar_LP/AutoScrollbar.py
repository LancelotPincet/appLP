#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2026-02-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : appLP
# Module        : AutoScrollbar

"""
This class adds an automatic scrollbar when necessary.
"""



# %% Libraries
from tkinter import ttk
import tkinter as tk



# %% Class
class AutoScrollbar(ttk.Scrollbar) :
    '''
    This class adds an automatic scrollbar when necessary.
    '''

    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
            ttk.Scrollbar.set(self, lo, hi)
    def pack(self, **kw):
        raise tk.TclError('Cannot use pack with the widget ' + self.__class__.__name__)
    def place(self, **kw):
        raise tk.TclError('Cannot use place with the widget ' + self.__class__.__name__)



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)