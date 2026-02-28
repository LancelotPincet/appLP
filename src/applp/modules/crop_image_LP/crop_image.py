#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2026-02-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : appLP
# Module        : crop_image

"""
This function creates an app to crop an image.
"""



# %% Libraries
from applp import App, CanvasImage
import numpy as np
from pathlib import Path
from PIL import Image



# %% Function
def crop_image(image, ncrops=1) :
    '''
    This function creates an app to crop an image.
    
    Parameters
    ----------
    image : np.ndarray or pathlib.Path
        Reference to image.
    ncrops : int
        Number of crops to do.

    Returns
    -------
    crop : np.ndarray
        cropped image.

    Examples
    --------
    >>> from applp import crop_image
    ...
    >>> crop = crop_image(image_path)
    '''

    # Open image
    if isinstance(image, str) or isinstance(image, Path('').__class__) :
        path = Path(image)
        image = np.array(Image.open(path))
    else :
        image = np.asarray(image)
    
    # Cropping app
    app = App(title='Crop image')
    canvasimg = CanvasImage(app, image, ncoords=ncrops)
    canvasimg.pack(fill='both', expand=True)
    app.mainloop()

    # Crop image
    crops = []
    for coords in canvasimg.coords :
        x0, y0, x1, y1 = coords
        crops.append(image[y0:y1+1, x0:x1+1])
    return crops



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)