import codecs
import time
import sys
import os
import datetime as DT
from matplotlib import pyplot as plt
from pylab import *
import numpy as np
import numpy
from matplotlib.pyplot import *
from tkinter import Tk,Label,Button,Frame
from tkinter import *
import tkinter as tk
import matplotlib.backends.backend_tkagg##pour le point exe

a=numpy.load("categories/categorieini.npy")
a=a.tolist()
n=0
niveaux=[]
depense=[]
couleurs = ['b', 'r', 'g']
couleur=[]
for categor in a:
    dep=numpy.load("categories/%s/2013%s.npy"%(categor,categor))
    dep=numpy.sum(dep)
    niveaux.append(categor)
    depense.append(dep)
    couleur.append(couleurs[n])
    n=n+1
    if n==3:
        n=0


pie(depense, labels=niveaux, colors=couleurs, autopct='%1.1f%%')
axis('equal')

show()
