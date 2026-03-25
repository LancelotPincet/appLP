#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2026-02-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : appLP
# Module        : App

"""
Custom tkinter App window that opens according to the monitor size.
"""



# %% Libraries
from corelp import prop, selfkwargs, icon
import tkinter as tk
import os
import json
import subprocess



# %% Class
class App(tk.Tk) :
    '''
    Custom tkinter App window that opens according to the monitor size.
    
    Parameters
    ----------
    title : str
        Title of the App.

    Examples
    --------
    >>> from applp import App
    ...
    >>> app = App(title="MyApp")
    >>> app.mainloop()
    '''



    def __init__(self, title='MyApp', **kwargs) :
        super().__init__()
        selfkwargs(self,kwargs)
        self.title(title)
        self.geometry(self.widthxheight)
        img = tk.PhotoImage(file=icon())
        self.iconphoto(True, img)
        self._icon_img = img  # keep reference
        self.update_idletasks()
        self.deiconify() # Unminimizes window
        self.attributes('-topmost', True) # Puts this window above the others
        self.update()
        self.focus_force()



    #Geometry
    screen_proportion = 2/3 #proportion of the screen used in the app in height
    @prop()
    def ratio(self) :
        return self.winfo_screenwidth() / self.winfo_screenheight()
    @ratio.setter
    def ratio(self,value) :
        ratios = {
                "1:1": 1,
                "2:1": 2,
                "1:2": 1 / 2,
                "4:3": 4 / 3,
                "3:4": 3 / 4,
                "16:9": 16 / 9,
                "9:16": 9 / 16,
                "gold": (1 + 5 ** 0.5) / 2,
                "gold:1": (1 + 5 ** 0.5) / 2,
                "1:gold": 1 / ((1 + 5 ** 0.5) / 2),
        }
        if isinstance(value,str) :
            if value in ratios:
                value = ratios[value]
            else:
                raise SyntaxError("Ratio of App was not recognized")
        self._ratio = value
    @prop(iterable=2, dtype=float)
    def fact(self) :
        return 1.
    @prop()
    def height(self) :
        if self.winfo_screenheight() < self.winfo_screenwidth() :
            return int(round(self.winfo_screenheight() * self.screen_proportion * self.wsl_proportion * self.fact[1]))
        return int(round(self.width / self.ratio * self.fact[1]/self.fact[0]))
    @prop()
    def width(self) :
        if self.winfo_screenheight() < self.winfo_screenwidth() :
            return int(round(self.height * self.ratio * self.fact[0]/self.fact[1]))
        return int(round(self.winfo_screenwidth() * self.screen_proportion * self.wsl_proportion * self.fact[0]))

    @property
    def widthxheight(self) :
        return f"{self.width}x{self.height}"



    # WSL [Running in WSL is just for me]
    @property
    def run_in_wsl(self) :
        """True if WSL."""
        if os.name != "posix":
            return False
        try:
            with open("/proc/version", "r") as f:
                return "microsoft" in f.read().lower()
        except FileNotFoundError:
            return False
    wsl_percent = 150
    @property
    def wsl_proportion(self) :
        if self.run_in_wsl : return self.wsl_percent / 100
        return 1.
    @prop(cache=True)
    def windows_primary_monitor_size(self):
        try:
            cmd = [
                "powershell.exe",
                "-Command",
                """
                Add-Type -AssemblyName System.Windows.Forms;
                $screen = [System.Windows.Forms.Screen]::PrimaryScreen;
                $obj = @{
                    Width = $screen.Bounds.Width;
                    Height = $screen.Bounds.Height
                };
                $obj | ConvertTo-Json
                """
            ]
            result = subprocess.check_output(cmd, text=True)
            data = json.loads(result)
            return data["Width"], data["Height"]
        except Exception:
            return None
    def winfo_screenwidth(self) :
        if self.run_in_wsl : return self.windows_primary_monitor_size[0]
        return super().winfo_screenwidth()
    def winfo_screenheight(self) :
        if self.run_in_wsl : return self.windows_primary_monitor_size[1]
        return super().winfo_screenheight()
    

    #Mainloop
    crush = False #Put to True to skip testings
    def mainloop(self) :
        if self.crush :
            self.destroy()
        super().mainloop()


# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)