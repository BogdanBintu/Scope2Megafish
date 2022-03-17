#!/usr/bin/env python
"""
Standardized HAL message boxes. Use these for 
messages instead of rolling your own!

Hazen 01/17
"""

from PyQt5 import QtWidgets

def halMessageBoxInfo(message, is_error = False):
    """
    Display an informational message box.
    """
    msg_box = QtWidgets.QMessageBox()
    msg_box.setText(message)
    if is_error:
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
    else:
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
    msg_box.exec_()

def halMessageBoxResponse(source, header, message):
    """
    Display a simple chooser message box.
    """
    return QtWidgets.QMessageBox.question(source,
                                          header,
                                          message,
                                          QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.No)    

#
# The MIT License
#
# Copyright (c) 2017 Zhuang Lab, Harvard University
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

