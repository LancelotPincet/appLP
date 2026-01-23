#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2025-08-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : appLP

"""
A library for custom GUI interface creation.
"""



# %% Source import
sources = {

}

from importlib import resources
from contextlib import contextmanager

@contextmanager
def resources_dir():
    with resources.as_file(resources.files("applp.resources")) as path:
        yield path

# %% Hidden imports
if False :




# %% Lazy imports
from corelp import getmodule
__getattr__, __all__ = getmodule(sources)