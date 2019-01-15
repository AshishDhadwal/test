# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 17:01:27 2019

@author: Administrator
"""

import os

os.environ['TCL_LIBRARY'] = "C:\\ProgramData\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\ProgramData\\Anaconda3\\tcl\\tk8.6"
from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Reviewsis.py", base=base)]

packages = ["idna","sys","os"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Textrics",
    options = options,
    version = "1.0",
    description = 'test',
    executables = executables
)