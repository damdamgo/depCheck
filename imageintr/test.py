import feedparser
from tkinter import Tk,Label,Button,Frame
from tkinter import *
import tkinter as tk
import webbrowser
def Enleve_Accents(elt):
    ch1 ="àâçéèêëîïôùûüÿ"
    ch2 ="aaceeeeiiouuuy"
    s = ""
    for c in elt:
        i = ch1.find(c)
        if i>=0:
            s += ch2[i]
        else:
            s += c
    return s
print("tapez 1 pour l'economie")

choix=input("votre choix :")
if choix=="1":
    listeurl = [[['http://rss.leparisien.fr/leparisien/rss/economie.xml'],["leparsien"]],
                [["https://news.google.com/news/feeds?pz=1&cf=all&ned=fr&hl=fr&topic=b&output=rss"],[""]]]


feeds = []
listemotcle=[]
n=0

                                
for element,journal in listeurl:
    listemotcle.append([])
    MyFeedsConfig =element
    for feed in MyFeedsConfig:
        feeds.append(feedparser.parse(feed))
    for feed in feeds:  
        for item in feed[ "items" ]:
            phrase=item.title
            listemots = phrase.split()
            for elt in listemots:
                elt=elt.lower()
                elt=Enleve_Accents(elt)
                try:
                    if elt[-1]=="s":
                        elt=elt[0:-1]
                    if elt[-1]==","or elt[-1]==".":
                        elt=elt[0:-1]
                    if "'" in elt:
                        elt=elt[2:]
                    if elt[-1]=='"':
                        elt=elt[0:-1]
                    if '"' in elt:
                        elt=elt[1:]
                except:
                    a=[]
                listemotcle[n].append(elt)
    n=n+1
    feeds=[]
listemotcle2=[]
listenon=["de","la",":","une","un","des","le","en","dans","pour","du","a","ou","sur","et","plu","dan","se","est","ver","que","qui","il","elle","va","san",
          "pour","sont","vont","aux","avec","fait","font","!","?","moin","tres","par","en","an","apres","mi","mon","te","je",
          "sa","ca","veut","ont","pa","ne","me","au","tre","leur","son","reste",'depui',
          "tou","avoir","apre"]

for i in range(n):
    for elt in listemotcle[i]:
        for i2 in range(n):
            if i2==i:
                a = []
            else :
                for elt2 in listemotcle[i2]:
                    if elt2.isalpha():
                        if elt==elt2:
                            if elt in listenon:
                                a = []
                            else:
                                listemotcle2.append(elt)                            
listemotcle2=list(set(listemotcle2))
listemotcle3=[]
for elt in listemotcle2:
    n2=0
    for i in range(n):
        for elt2 in listemotcle[i]:
            if elt==elt2:
                n2=n2+1
    if n2>=n-1:
        listemotcle3.append(elt)
print(listemotcle3)
liste=[["co","co","co"]]
for element,journal in listeurl:
    MyFeedsConfig =element
    for feed in MyFeedsConfig:
        feeds.append(feedparser.parse(feed))
    for feed in feeds:
        for item in feed[ "items" ]:
            accept=0
            phrase=item.title
            listemots = phrase.split()
            for elt in listemots:
                elt=elt.lower()
                elt=Enleve_Accents(elt)
                try:
                    if elt[-1]=="s":
                        elt=elt[0:-1]
                    if elt[-1]==","or elt[-1]==".":
                        elt=elt[0:-1]
                    if "'" in elt:
                        elt=elt[2:]
                    if elt[-1]=='"':
                        elt=elt[0:-1]
                    if '"' in elt:
                        elt=elt[1:]
                except:
                    a=[]
                for motcle in listemotcle3:
                    if elt==motcle:
                        accept=1
            if accept==1:
                liste.append([item.title,journal,item.link])
    feeds = []
print(liste)
root=Tk()
root.resizable(False, False)###on peut pas modifier la taille de la fenetre
couleurprin="#DEB887"
couleursec="#FEFEE0"
couleurfrm="#99512B"
frameprincipale = Frame(root,width=1000,height=600,bg=couleurprin)###on cree une frame 1000*600 (taille de la fenetre)
frameprincipale.pack()
frameprincipale.pack_propagate(0)### taille de la frame fixe
frame=Frame(frameprincipale)
frame.pack(side=LEFT)
frameshowrss=Frame(frame)
frameshowrss.grid(row=0, column=0)
cnv = Canvas(frameshowrss,bg=couleursec,width=1000,height=600)
cnv.grid(row=0, column=1)
vScroll = Scrollbar(frameshowrss, orient=VERTICAL, command=cnv.yview)
vScroll.grid(row=0, column=0, sticky='ns')
cnv.configure(yscrollcommand=vScroll.set)
frm = Frame(cnv,bg=couleurfrm)
cnv.create_window(0, 0, window=frm, anchor='nw')
for elment,journal,url in liste:
    c=Button(frm,text="%s - %s"%(elment,journal),command=lambda i=url:choose(i,))
    c.pack(side=TOP)
    def choose(url):
        webbrowser.open(url)
frm.update_idletasks()
cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))

root.mainloop()
