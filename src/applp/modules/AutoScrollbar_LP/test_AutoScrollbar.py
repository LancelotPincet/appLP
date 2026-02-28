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



# %% Instance fixture
@pytest.fixture()
def instance() :
    '''
    Create a new instance at each test function
    '''
    return AutoScrollbar()

def test_instance(instance) :
    '''
    Test on fixture
    '''
    pass


# %% Returns test
@pytest.mark.parametrize("args, kwargs, expected, message", [
    #([], {}, None, ""),
    ([], {}, None, ""),
])
def test_returns(args, kwargs, expected, message) :
    '''
    Test AutoScrollbar return values
    '''
    assert AutoScrollbar(*args, **kwargs) == expected, message



# %% Error test
@pytest.mark.parametrize("args, kwargs, error, error_message", [
    #([], {}, None, ""),
    ([], {}, None, ""),
])
def test_errors(args, kwargs, error, error_message) :
    '''
    Test AutoScrollbar error values
    '''
    with pytest.raises(error, match=error_message) :
        AutoScrollbar(*args, **kwargs)



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)