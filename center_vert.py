#!/usr/bin/env python
# -*- coding: utf-8  -*-

# ****************************************************************************
#  This program is free software; you can redistribute it and/or modify 
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# 
# ****************************************************************************


"""

© 2012 by Gregory Pittman

centervert.py

Centers text vertically in a text frame. Uses the fixed linespacing setting, even
if you're actually using automatic linespacing.

USAGE

Select a text frame, run script.

"""

try:
    import scribus
except ImportError:
    print "Unable to import the 'scribus' module. This script will only run within"
    print "the Python interpreter embedded in Scribus. Try Script->Execute Script."
    sys.exit(1)

if not scribus.haveDoc():
    scribus.messageBox('Scribus - Script Error', "No document open", scribus.ICON_WARNING, scribus.BUTTON_OK)
    sys.exit(1)

if scribus.selectionCount() == 0:
    scribus.messageBox('Scribus - Script Error',
            "There is no object selected.\nPlease select a text frame and try again.",
            scribus.ICON_WARNING, scribus.BUTTON_OK)
    sys.exit(2)
if scribus.selectionCount() > 1:
    scribus.messageBox('Scribus - Script Error',
            "You have more than one object selected.\nPlease select one text frame and try again.",
            scribus.ICON_WARNING, scribus.BUTTON_OK)
    sys.exit(2)
textbox = scribus.getSelectedObject()
pageitems = scribus.getPageItems()
scribus.setRedraw(False)

for item in pageitems:
    if (item[0] == textbox):
        if (item[1] != 4):
            scribus.messageBox('Scribus - Script Error', 
                          "This is not a textframe. Try again.", scribus.ICON_WARNING, scribus.BUTTON_OK)
            sys.exit(2)
            
        lines = scribus.getTextLines(textbox)
        distances = scribus.getTextDistances(textbox)
        linespace = scribus.getLineSpacing(textbox)
        dimensions = scribus.getSize(textbox) # (width, height)
        if (scribus.textOverflows(textbox, 1) > 0):
            scribus.messageBox('User Error', "This frame is already overflowing", scribus.ICON_WARNING, scribus.BUTTON_OK)
            sys.exit(2)
        newtopdist = (dimensions[1] - linespace * lines)/2
        scribus.setTextDistances(distances[0],distances[1],newtopdist,distances[3],textbox)

scribus.setRedraw(True)