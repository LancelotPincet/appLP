#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2026-02-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : appLP
# Module        : AutoScrollbar

"""
This file allows to test AutoScrollbar

AutoScrollbar : This class adds an automatic scrollbar when necessary.
"""



# %% Libraries
from corelp import debug
import pytest
from applp import AutoScrollbar
debug_folder = debug(__file__)



# %% Function test
def test_function() :
    '''
    Test AutoScrollbar function
    '''
    print('Hello world!')



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)