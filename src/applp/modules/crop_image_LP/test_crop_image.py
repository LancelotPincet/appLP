#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2026-02-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : appLP
# Module        : crop_image

"""
This file allows to test crop_image

crop_image : This function creates an app to crop an image.
"""



# %% Libraries
from corelp import debug
import pytest
from applp import crop_image
debug_folder = debug(__file__)



# %% Function test
def test_function() :
    '''
    Test crop_image function
    '''
    print('Hello world!')



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)