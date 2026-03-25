#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Date          : 2026-02-28
# Author        : Lancelot PINCET
# GitHub        : https://github.com/LancelotPincet
# Library       : appLP
# Module        : CanvasImage

"""
This class is a tkinter frame where to put an image that can be manipulated.
"""



# %% Libraries
import tkinter as tk
from tkinter import font
from applp import AutoScrollbar
import PIL
from PIL import ImageTk
import numpy as np
from plotlp import color
from corelp import prop, AnyObject



# %% Class
class CanvasImage(tk.Frame) :
    '''
    This class is a tkinter frame where to put an image that can be manipulated.
    
    Parameters
    ----------
    a : int or float
        TODO.

    Attributes
    ----------
    _attr : int or float
        TODO.

    Examples
    --------
    >>> from applp import CanvasImage
    ...
    >>> instance = CanvasImage(TODO)
    '''

    _image = None
    @property
    def image(self) :
        return self._image
    @image.setter
    def image(self,value) :
        value = np.asarray(value)
        if (value < 0).any() : raise ValueError('Image cannot be negative')
        if np.max(value) != 0 : value = value/np.max(value) * 255
        img = (value).astype(np.uint8)
        self._image = PIL.Image.fromarray(img) #open image
        self.imwidth, self.imheight = self.image.size
    n_bkgd = 100
    def bkgd(self) :
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        mini = min(width, height)
        width, height = int(width / mini * self.n_bkgd), int(height / mini * self.n_bkgd)
        x, y = np.arange(width), np.arange(height)
        X, Y = np.meshgrid(x, y)
        mask = (X %2 == 0) == (Y%2 == 0)
        img = np.empty_like(mask,dtype=np.uint8)
        img[mask] = 255
        img[~mask] = 191
        img = PIL.Image.fromarray(img)
        width, height = self.canvas.winfo_width(),self.canvas.winfo_height()
        img = img.resize((width,height),resample=PIL.Image.NEAREST)
        return img
    def update_bkgd(self, event=None):
        self.bkgdtk = ImageTk.PhotoImage(self.bkgd())
        if not hasattr(self, 'bkgd_id'):
            self.bkgd_id = self.canvas.create_image(0, 0, image=self.bkgdtk, anchor=tk.NW, tags='fixed')
        else:
            self.canvas.itemconfig(self.bkgd_id, image=self.bkgdtk)


    title = ''
    title_size = 16
    def __init__(self, master, image, title='', ncoords=None, *args, **kwargs) :
        self.image = image
        self.title = title
        self.ncoords = ncoords
        super().__init__(master=master, *args, **kwargs)

        # Scrollbars
        self.vbar = AutoScrollbar(self, orient='vertical')
        self.hbar = AutoScrollbar(self, orient='horizontal')
        self.vbar.configure(command=self.scroll_y) #bind scrollbars to the canvas
        self.hbar.configure(command=self.scroll_x)

        #header
        self.header = tk.Frame(self)
        title_font = font.Font(size=self.title_size, weight="bold")
        self.titler = tk.Label(self.header,text=self.title,font=title_font)
        self.pointer = tk.Label(self.header, text='')
        self.shaper = tk.Label(self.header, text='')

        # Canvas
        self.canvas = tk.Canvas(self, highlightthickness=0, xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.container = self.canvas.create_rectangle(0, 0, self.imwidth, self.imheight , width=0, outline='', fill='')

        # Make the canvas expandable
        self.grid_rowconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=100)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=100)
        self.grid_columnconfigure(1, weight=1)

        # Bind events to the Canvas
        self.canvas.bind('<Configure>', self.show_image) #canvas is resized
        self.canvas.bind('<Configure>', self.update_bkgd, add='+') # Resizing background when window size changes
        self.canvas.bind('<ButtonPress-2>', self.move_from)
        self.canvas.bind('<B2-Motion>', self.move_to)
        self.canvas.bind('<MouseWheel>', self.wheel) #with Windows and MacOS, but not Linux
        self.canvas.bind('<Button-5>', self.wheel) #only with Linux, wheel scroll down
        self.canvas.bind('<Button-4>', self.wheel) #only with Linux, wheel scroll up
        if not(self.draw_shape is None) :
            self.drawing = None
            self.canvas.bind('<ButtonPress-1>', self.left_press)
            self.canvas.bind('<B1-Motion>', self.left_move)
            self.canvas.bind('<ButtonRelease-3>', self.right_release)
        self.canvas.bind('<Motion>', self.pointing)
        self.canvas.bind('<B1 - Motion>', self.pointing, add='+')
        self.canvas.bind('<Leave>', self.pointer_exit)



    #Making placing
    def place_widgets(self) :
        #Bars
        self.vbar.grid(row=0, column=1, sticky='ns',rowspan=3)
        self.hbar.grid(row=2, column=0, sticky='we')
        #Header
        self.header.grid(row=0,column=0, sticky='nsew')
        self.titler.pack(expand=True)
        self.pointer.pack(expand=True)
        self.shaper.pack(expand=True)
        #Images
        self.canvas.grid(row=1, column=0, sticky='nswe')
        self.canvas.update()
        self.update_bkgd()
        # Put image into container rectangle and use it to set proper coordinates to the image
        scalex, scaley = self.canvas.winfo_width()/self.imwidth , self.canvas.winfo_height()/self.imheight
        if scalex != scaley :
            if scalex < scaley :
                scale = scalex
                shiftx = None
                shifty = int(round((self.canvas.winfo_height() - self.imheight * scale) / 2))
            else :
                scale = scaley
                shifty = None
                shiftx = int(round((self.canvas.winfo_width() - self.imwidth * scale) / 2))
        else :
            scale = scalex
            shiftx,shifty = None, None
        self.imscale *= scale
        self.canvas.scale('all', 0, 0, self.imscale, self.imscale)
        if shiftx is not None :
            event = AnyObject(x=0, y=0)
            self.move_from(event)
            event = AnyObject(x=shiftx, y=0)
            self.move_to(event)
        if shifty is not None :
            event = AnyObject(x=0, y=0)
            self.move_from(event)
            event = AnyObject(y=shifty, x=0)
            self.move_to(event)
        #Init images
        self.show_image()

    def pack(self, *args, **kwargs):
        """
        Pack the widget and initialize internal layout.

        Calls :meth:`place_widgets` after packing to set up
        scrollbars, header, and canvas.

        Parameters
        ----------
        *args
            Positional arguments forwarded to :meth:`tk.Frame.pack`.
        **kwargs
            Keyword arguments forwarded to :meth:`tk.Frame.pack`.
        """
        super().pack(*args, **kwargs)
        self.place_widgets()

    def grid(self, *args, **kwargs):
        """
        Grid the widget and initialize internal layout.

        Calls :meth:`place_widgets` after gridding to set up
        scrollbars, header, and canvas.

        Parameters
        ----------
        *args
            Positional arguments forwarded to :meth:`tk.Frame.grid`.
        **kwargs
            Keyword arguments forwarded to :meth:`tk.Frame.grid`.
        """
        super().grid(*args, **kwargs)
        self.place_widgets()

    def place(self, *args, **kwargs):
        """
        Place the widget and initialize internal layout.

        Calls :meth:`place_widgets` after placing to set up
        scrollbars, header, and canvas.

        Parameters
        ----------
        *args
            Positional arguments forwarded to :meth:`tk.Frame.place`.
        **kwargs
            Keyword arguments forwarded to :meth:`tk.Frame.place`.
        """
        super().place(*args, **kwargs)
        self.place_widgets()



    ### Making zoom ###
    delta = 1.1 #Zoom magnitude factor step
    imscale = 1.0 #Initial scale parameter for image zoom

    def show_image(self, event=None):
        ''' Show image on the Canvas '''
        #Get effective bbox
        bbox1 = self.canvas.bbox(self.container) #get image area
        bbox1 = (bbox1[0] + 1, bbox1[1] + 1, bbox1[2] - 1, bbox1[3] - 1) #Remove 1 pixel shift at the sides of the bbox1
        bbox2 = (self.canvas.canvasx(0), #get visible area of the canvas
                 self.canvas.canvasy(0),
                 self.canvas.canvasx(self.canvas.winfo_width()),
                 self.canvas.canvasy(self.canvas.winfo_height()))
        bbox = [min(bbox1[0], bbox2[0]), min(bbox1[1], bbox2[1]), #get scroll region box
                max(bbox1[2], bbox2[2]), max(bbox1[3], bbox2[3])]
        if bbox[0] == bbox2[0] and bbox[2] == bbox2[2]: #whole image in the visible area
            bbox[0] = bbox1[0]
            bbox[2] = bbox1[2]
        if bbox[1] == bbox2[1] and bbox[3] == bbox2[3]: #whole image in the visible area
            bbox[1] = bbox1[1]
            bbox[3] = bbox1[3]
        self.canvas.configure(scrollregion=bbox) #set scroll region

        #Put image
        x1 = max(bbox2[0] - bbox1[0], 0) #get coordinates (x0,y0,x1,y1) of the image tile
        y1 = max(bbox2[1] - bbox1[1], 0)
        x2 = min(bbox2[2], bbox1[2]) - bbox1[0]
        y2 = min(bbox2[3], bbox1[3]) - bbox1[1]
        if int(x2 - x1) > 0 and int(y2 - y1) > 0: #show image if it is in the visible area
            x = min(int(x2 / self.imscale), self.imwidth) #sometimes it is larger on 1 pixel...
            y = min(int(y2 / self.imscale), self.imheight) #...and sometimes not
            image = self.image.crop((int(x1 / self.imscale), int(y1 / self.imscale), x, y))
            imagetk = ImageTk.PhotoImage(image.resize((int(x2 - x1), int(y2 - y1)), resample=PIL.Image.NEAREST))
            self.canvas.create_image(max(bbox2[0], bbox1[0]), max(bbox2[1], bbox1[1]),anchor='nw', image=imagetk, tags='moved')
            self.canvas.imagetk = imagetk #keep an extra reference to prevent garbage-collection

        #Puts back every object
        for coords in self.shapes :
            if coords is not None :
                x0,y0,x1,y1 = coords
                self.drawing = self.draw_func(x0,y0,x1,y1, width=self.width_shape, **self.draw_kwargs, tags='moved')

    def scroll_y(self, *args):
        ''' Scroll canvas vertically and redraw the image '''
        y1 = self.canvas.canvasy(0)
        self.canvas.yview(*args) #scroll vertically
        self.show_image() # redraw the image
        #Correct background
        y2 = self.canvas.canvasy(0)
        dy = y1-y2
        self.canvas.move("fixed", 0, -dy)
    def scroll_x(self, *args):
        ''' Scroll canvas horizontally and redraw the image '''
        x1 = self.canvas.canvasx(0)
        self.canvas.xview(*args) #scroll horizontally
        self.show_image() # redraw the image
        #Correct background
        x2 = self.canvas.canvasx(0)
        dx = x1-x2
        self.canvas.move("fixed", -dx, 0)

    def move_from(self, event):
        ''' Remember previous coordinates for scrolling with the mouse '''
        self.canvas.scan_mark(event.x, event.y)
    def move_to(self, event):
        ''' Drag (move) canvas to the new position '''
        x1 = self.canvas.canvasx(0)
        y1 = self.canvas.canvasy(0)
        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.show_image() # redraw the image
        #Correct background
        x2 = self.canvas.canvasx(0)
        y2 = self.canvas.canvasy(0)
        dx = x1-x2
        dy = y1-y2
        self.canvas.move("fixed", -dx, -dy)

    def wheel(self, event):
        ''' Zoom with mouse wheel '''
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        bbox = self.canvas.bbox(self.container) #get image area
        if bbox[0] < x < bbox[2] and bbox[1] < y < bbox[3]: #zoom only inside image area
            scale = 1.0
            # Respond to Linux (event.num) or Windows (event.delta) wheel event
            if event.num == 5 or event.delta == -120: #scroll down
                i = min(self.imwidth,self.imheight)
                if int(i * self.imscale) >= 30: #image is less than 30 pixels
                    self.imscale /= self.delta
                    scale /= self.delta
                    s = 1/self.delta
                else :
                    s = 1
            elif event.num == 4 or event.delta == 120: #scroll up
                i = min(self.canvas.winfo_width(), self.canvas.winfo_height())
                if i >= self.imscale: #1 pixel is bigger than the visible area
                    self.imscale *= self.delta
                    scale *= self.delta
                    s = self.delta
                else :
                    s = 1
            else :
                s = 1
            for pos,coords in enumerate(self.shapes) :
                if coords is not None :
                    (x0, y0, x1, y1) = coords
                    self.shapes[pos] = s * (x0 - x) + x, s * (y0 - y) + y, s * (x1 - x) + x, s * (y1 - y) + y
            self.canvas.scale('all', x, y, scale, scale) #rescale all canvas objects
            self.canvas.scale('fixed', x, y, 1/scale, 1/scale) #Correct background
            self.show_image()

    ### Making shape ###
    _color_shape = color(name='orange').noalpha
    @property
    def color_shape(self) :
        return self._color_shape
    @color_shape.setter
    def color_shape(self,value) :
        self._color_shape = color(value).noalpha
    width_shape = 2 #Width of shape to draw
    drawing_corner = 10 #Number of pixel for uncertainty of point
    draw_shape = 'Rectangle' #Shape to draw 'Rectangle' / 'Line' or None for not shape
    @property
    def draw_func(self) :
        if self.draw_shape is None : return None
        if self.draw_shape.lower() in ['rectangle','rect'] :
            return self.canvas.create_rectangle
        if self.draw_shape.lower() in ['line'] :
            return self.canvas.create_line
    @property
    def draw_kwargs(self) :
        if self.draw_shape is None : return None
        if self.draw_shape.lower() in ['rectangle','rect'] :
            return {"outline":self.color_shape}
        if self.draw_shape.lower() in ['line'] :
            return {"fill":self.color_shape}
    @prop(cache=True)
    def shapes(self) :
        return [None]
    def shaper_text(self) :
        return f'{self.draw_shape}: (x0, y0, x1, y1) = {self.coords[-1]}'




    def paste_shape(self, event=None) :
        '''Keep the last shape on canvas and resets a new shape'''
        self.drawing = None

    def left_press(self, event=None) :
        '''Remember first coordinates of drawing'''
        x = int(self.canvas.canvasx(event.x))
        y = int(self.canvas.canvasy(event.y))
        self.left_press_coord = (x,y)
        #Chosing mode of drawing
        if self.drawing is not None :
            self.drawing_coords = self.canvas.coords(self.drawing)
            if self.drawing_coords[0]+self.drawing_corner < x < self.drawing_coords[2]-self.drawing_corner and self.drawing_coords[1]+self.drawing_corner < y < self.drawing_coords[3]-self.drawing_corner :
                self.drawing_mode = ('Moving',None)
            elif abs(self.drawing_coords[0] - x) < self.drawing_corner and abs(self.drawing_coords[1] - y) < self.drawing_corner :
                self.drawing_mode = ('Corner',0)
            elif abs(self.drawing_coords[2] - x) < self.drawing_corner and abs(self.drawing_coords[1] - y) < self.drawing_corner :
                self.drawing_mode = ('Corner',1)
            elif abs(self.drawing_coords[0] - x) < self.drawing_corner and abs(self.drawing_coords[3] - y) < self.drawing_corner :
                self.drawing_mode = ('Corner',2)
            elif abs(self.drawing_coords[2] - x) < self.drawing_corner and abs(self.drawing_coords[3] - y) < self.drawing_corner :
                self.drawing_mode = ('Corner',3)
            else :
                self.drawing_mode = ('Drawing',None)
                self.shaper.config(text='')
            self.canvas.delete(self.drawing)
            self.shapes[-1] = None
        else :
            self.drawing_mode = ('Drawing',None)
        self.drawing = None

    def left_move(self, event=None) :
        '''Draws shape while dragging mouse'''
        bbox = self.canvas.bbox(self.container)
        xmin = bbox[0] + 1
        ymin = bbox[1] + 1
        xmax = bbox[2] - 1
        ymax = bbox[3] - 1
        if self.drawing is not None :
            self.canvas.delete(self.drawing)
            self.shapes[-1] = None
        if self.drawing_mode[0] == 'Drawing' :
            x0 = self.left_press_coord[0]
            y0 = self.left_press_coord[1]
            x1 = int(self.canvas.canvasx(event.x))
            y1 = int(self.canvas.canvasy(event.y))
        elif self.drawing_mode[0] == 'Moving' :
            x0,y0,x1,y1 = self.drawing_coords
            dx = int(self.canvas.canvasx(event.x)) - self.left_press_coord[0]
            dy = int(self.canvas.canvasy(event.y)) - self.left_press_coord[1]
            if x0 + dx < xmin :
                x0, x1 = xmin, xmin + (x1-x0)
            elif x1 + dx > xmax :
                x0, x1 = xmax - (x1-x0), xmax
            else :
                x0 += dx
                x1 += dx
            if y0 + dy < ymin :
                y0, y1 = ymin, ymin + (y1-y0)
            elif y1 + dy > ymax :
                y0, y1 = ymax - (y1-y0), ymax
            else :
                y0 += dy
                y1 += dy
        elif self.drawing_mode[0] == 'Corner' :
            x0,y0,x1,y1 = self.drawing_coords
            dx = int(self.canvas.canvasx(event.x)) - self.left_press_coord[0]
            dy = int(self.canvas.canvasy(event.y)) - self.left_press_coord[1]
            if self.drawing_mode[1] == 0 :
                x0 += dx
                y0 += dy
            if self.drawing_mode[1] == 1 :
                x1 += dx
                y0 += dy
            if self.drawing_mode[1] == 2 :
                x0 += dx
                y1 += dy
            if self.drawing_mode[1] == 3 :
                x1 += dx
                y1 += dy
        x0 = max(x0,xmin)
        x0 = min(x0,xmax)
        x1 = max(x1,xmin)
        x1 = min(x1,xmax)
        y0 = max(y0,ymin)
        y0 = min(y0,ymax)
        y1 = max(y1,ymin)
        y1 = min(y1,ymax)
        self.shapes[-1] = (x0, y0, x1, y1)
        self.show_image()
        (x0, y0, x1, y1) = self.get_coord()
        self.coords[-1] = (x0, y0, x1, y1)
        shaper_text = self.shaper_text()
        self.shaper.config(text=shaper_text)
        self.shaper.update()

    @prop(cache=True)
    def coords(self) :
        return [None]
    def right_release(self, event=None) :
        '''Makes new shape'''
        if self.ncoords is None and len(self.coords) > 1 and (self.shapes[-1] is None or self.shapes[-1] == self.shapes[-2]) :
            self.coords = self.coords[:-1]
            self.master.destroy()
            return
        if len(self.shapes) < 2 or self.shapes[-1] != self.shapes[-2] :
            self.coords.append(self.coords[-1])
            self.shapes.append(self.shapes[-1])
        if self.ncoords is not None and len(self.coords) > self.ncoords :
            self.coords = self.coords[:-1]
            self.master.destroy()
            return
    def get_coord(self, event=None) :
        '''Getting coordinates of last drawn shape (x0,y0,x1,y1)'''
        if self.drawing is None :
            return (np.nan,np.nan,np.nan,np.nan)
        else :
            bbox = self.canvas.bbox(self.container)
            Coords = self.canvas.coords(self.drawing)
            coords = tuple()
            coords += int((Coords[0] - bbox[0])/self.imscale),
            coords += int((Coords[1] - bbox[1])/self.imscale),
            coords += int((Coords[2] - bbox[0])/self.imscale),
            coords += int((Coords[3] - bbox[1])/self.imscale),
            return coords



    #Pointer
    def pointing(self, event) :
        bbox = self.canvas.bbox(self.container)
        x = str(int((self.canvas.canvasx(event.x) - bbox[0])/self.imscale))
        y = str(int((self.canvas.canvasy(event.y) - bbox[1])/self.imscale))
        if 0>int(x) or int(x)>self.imwidth or 0>int(y) or int(y)>self.imheight :
            text = ''
        else :
            text = f'Mouse : ({x},{y})'
        self.pointer.config(text=text)
        self.pointer.update()
    def pointer_exit(self, event) :
        self.pointer.config(text='')
        self.pointer.update()



# %% Test function run
if __name__ == "__main__":
    from corelp import test
    test(__file__)