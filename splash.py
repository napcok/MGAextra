#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Eve Installer splash screen
#
# Copyright (C) 2010 Roy Alayn
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

import pygtk
pygtk.require('2.0')
import gtk
import cairo
import gobject
import sys

# Function for splash screen drawing
def window_draw(drawing_area, event, user_data=None):
    
    cr = drawing_area.window.cairo_create()
    
    # Make window transparent
    cr.set_operator(cairo.OPERATOR_CLEAR)    
    cr.paint()
    
    cr.set_operator(cairo.OPERATOR_OVER)
    cr.set_line_width(1.0)
    
    # background and outer border
    w = drawing_area.allocation.width -2
    h = drawing_area.allocation.height -2
    
    x = 1
    y = 1
    r = 1
    
    cr.move_to(x+r,y+0.5)
    cr.line_to(x+w-r,y+0.5)
    cr.curve_to(x+w,y,x+w,y,x+w-0.5,y+r)
    cr.line_to(x+w-0.5,y+h-r)
    cr.curve_to(x+w,y+h,x+w,y+h,x+w-r,y+h-0.5)
    cr.line_to(x+r,y+h-0.5)
    cr.curve_to(x,y+h,x,y+h,x+0.5,y+h-r)
    cr.line_to(x+0.5,y+r)
    cr.curve_to(x,y,x,y,x+r,y+0.5)
    
    pat = cairo.LinearGradient (9, 9, 9, h)
    pat.add_color_stop_rgba (0, 0.9, 0.9, 0.9, 0.95)
    pat.add_color_stop_rgba (8, 0.8, 0.8, 0.8, 0.95);
    #pat.add_color_stop_rgba (0, 0.2, 0.2, 0.2, 0.95)
    #pat.add_color_stop_rgba (1, 0.1, 0.1, 0.1, 0.95);
    
    cr.set_source(pat)    
    cr.fill_preserve()
    
    cr.set_source_rgb (9, 9, 9)
    cr.stroke ()
    
    # inner border
    w = drawing_area.allocation.width -4
    h = drawing_area.allocation.height -4
    
    x = 2
    y = 2
    r = 2
    
    cr.move_to(x+r,y+0.5)
    cr.line_to(x+w-r,y+0.5)
    cr.curve_to(x+w,y,x+w,y,x+w-0.5,y+r)
    cr.line_to(x+w-0.5,y+h-r)
    cr.curve_to(x+w,y+h,x+w,y+h,x+w-r,y+h-0.5)
    cr.line_to(x+r,y+h-0.5)
    cr.curve_to(x,y+h,x,y+h,x+0.5,y+h-r)
    cr.line_to(x+0.5,y+r)
    cr.curve_to(x,y,x,y,x+r,y+0.5)
    
    cr.set_source_rgb ( 0.3, 0.3, 0.3)
    cr.stroke();
    
    # Eve Installer logo and title
    surface = cairo.ImageSurface.create_from_png(sys.path[0] + "/images/splash.png")    
    cr.set_source_surface(surface, 10.0, 10.0)
    cr.paint()
    
    return False

alpha = 0.0

# Function for fade splash screen
def fade_window(data=None):
    global alpha
    
    data.set_opacity(alpha)
    alpha += 0.05;
    
    if alpha <= 1.0:
        gobject.timeout_add(20, fade_window, data);
    
    return False;
 
# init window
splash = gtk.Window(gtk.WINDOW_TOPLEVEL)

# enable RGBA colormap for opacity
screen = splash.get_screen()
colormap = screen.get_rgba_colormap()

if colormap:
    gtk.widget_set_default_colormap(colormap)

# Set width and height
splash.set_size_request (595, 218)
# Set window hint spashscreen
splash.set_type_hint (gtk.gdk.WINDOW_TYPE_HINT_SPLASHSCREEN)
# Set window centered
splash.set_position (gtk.WIN_POS_CENTER)
# Set window above the others
splash.set_keep_above (True)
# _I_ draw the window
splash.set_app_paintable(True)
# Draw window
splash.realize()
# Set null background
splash.window.set_back_pixmap(None, False)

# Signals
splash.connect("delete-event", gtk.main_quit, None)
splash.connect_after("expose-event", window_draw, None)

splash.show()

# Fade in splash screen
fade_window(splash)

# read delay time from command line
if len(sys.argv) < 2:
    delay = 3
else:
    delay = int(sys.argv[1])

# Close splash screen after X seconds
gobject.timeout_add_seconds(delay, gtk.main_quit, None);

gtk.main()
