# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 16:55:17 2018
code that takes all js files in a directory and minifies them.
The code then uploads them to the device running Mongoose OS

Note: the script will try to convert all files so only put .js files in the dir
@author: jjskaife
"""

import subprocess
import os
from jsmin import jsmin

mosExeLoc = r"C:\Users\jskaife\Desktop\MOS\mos.exe"

for filename in os.listdir(r'c:\tmp\unmin'):
    print (filename)

   
    with open(r'c:\tmp\unmin\\' + filename) as js_file:
        minified = jsmin(js_file.read())
    
    with open(r'c:\tmp\min\\' + filename, "w") as text_file:
        print(minified, file=text_file)
    with open(filename, "w") as text_file:
        print(minified, file=text_file)
    oname = filename
    print ("----------------------")
    subprocess.check_call([mosExeLoc,"put",oname])
