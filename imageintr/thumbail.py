import codecs
import time
import sys
import os
import datetime as DT
from tkinter import Tk,Label,Button,Frame
from tkinter import *
import tkinter as tk
import numpy
import glob
from PIL import Image
anneetoday=time.strftime('%Y',time.localtime())
choix="alimentation"
for infile in glob.glob("categories/%s/%sfact%s/01/*.jpg"%(choix,anneetoday,choix)):
    size = 128, 128

    file, ext = os.path.splitext(infile)
    print(file)
    im = Image.open(infile)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(file + "z.jpg", "JPEG")
