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
print("tapez 2 pour la politique")
print("tapez 3 pour le sport")
print("tapez 4 pour actualité du monde")
print("tapez 5 pour la france")
choix=input("votre choix :")
if choix=="1":
    listeurl = [[['http://rss.leparisien.fr/leparisien/rss/economie.xml'],["leparsien"]],
                [["http://rss.lemonde.fr/c/205/f/3055/index.rss"],["le monde"]],
                [["http://www.bfmtv.com/rss/economie.rss"],["bmttv"]],
                [["http://www.lefigaro.fr/rss/figaro_economie.xml"],["lefigaro"]],
                [["https://news.google.com/news/section?pz=1&cf=all&ned=us&topic=b&ict=ln&siidp=e4045ea810906befe3bfeb3107f66adb9d3e"],[""]],
                [["http://liberation.fr.feedsportal.com/c/32268/fe.ed/rss.liberation.fr/rss/13/"],["liberation"]],
                [["http://fr.news.yahoo.com/rss/economie"],["yahoo"]],
                [["http://www.tf1.fr/xml/rss/0,,3,00.xml"],["tf1"]],
                [["https://news.google.com/news/feeds?pz=1&cf=all&ned=fr&hl=fr&topic=b&output=rss"],[""]]]
if choix=="2":
    listeurl = [[["http://liberation.fr.feedsportal.com/c/32268/fe.ed/rss.liberation.fr/rss/11/"],["liberation"]],
                [["http://rss.leparisien.fr/leparisien/rss/politique.xml"],["leparsien"]],
                [["http://www.lefigaro.fr/rss/figaro_politique.xml"],["lefigaro"]],
                [["http://www.bfmtv.com/rss/politique.rss"],["bmttv"]],
                [["http://rss.lemonde.fr/c/205/f/3067/index.rss"],["le monde"]],
                [["http://fr.news.yahoo.com/rss/politique"],["yahoo"]],
                [["http://tf1.lci.fr/xml/rss/0,,492,00.xml"],["tf1"]],
                [["https://news.google.com/news/section?pz=1&cf=all&ned=fr&topic=n&ict=ln&siidp=2ad7d8d5a06d2085d0251ccf9ca609d5c35c"],[""]]]
if choix=="3":
    listeurl = [[["http://liberation.fr.feedsportal.com/c/32268/fe.ed/rss.liberation.fr/rss/14/"],["liberation"]],
                [["http://rss.leparisien.fr/leparisien/rss/sports.xml"],["leparsien"]],
                [["http://www.lefigaro.fr/rss/figaro_sport.xml"],["lefigaro"]],
                [["http://rss.lemonde.fr/c/205/f/3058/index.rss"],["le monde"]],
                [["http://www.bfmtv.com/rss/sport.rss"],["bmttv"]],
                [["http://fr.news.yahoo.com/rss/sports"],["yahoo"]],
                [["http://www.20min.ch/rss/rss.tmpl?type=channel&get=23"],["20minutes"]],
                [["https://news.google.com/news/feeds?pz=1&cf=all&ned=us&hl=en&topic=s&output=rss"],[""]],
                [["https://news.google.com/news/feeds?pz=1&cf=all&ned=fr&hl=fr&topic=s&output=rss"],[""]]]
if choix=="4":    
    listeurl = [[["http://liberation.fr.feedsportal.com/c/32268/fe.ed/rss.liberation.fr/rss/10/"],["liberation"]],
                [["http://rss.leparisien.fr/leparisien/rss/international.xml"],["leparsien"]],
                [["http://feeds.lefigaro.fr/c/32266/f/438192/index.rss"],["lefigaro"]],
                [["http://rss.lemonde.fr/c/205/f/3052/index.rss"],["le monde"]],
                [["https://news.google.com/news/feeds?pz=1&cf=all&ned=fr&hl=fr&topic=w&output=rss"],["google"]],
                [["http://www.bfmtv.com/rss/international.rss"],["bmttv"]],
                [["https://news.google.com/news/feeds?pz=1&cf=all&ned=us&hl=en&output=rss"],["google"]],
                [["http://rss.lemonde.fr/c/205/f/3053/index.rss"],["le monde"]],
                [["http://fr.news.yahoo.com/rss/world"],["yahoo"]],
                [["http://www.tf1.fr/xml/rss/0,,2,00.xml"],["tf1"]],
                [["http://www.20min.ch/rss/rss.tmpl?type=channel&get=17"],["20minutes"]],
                [["https://news.google.com/news/feeds?pz=1&cf=all&ned=us&hl=en&topic=w&output=rss"],["googleang"]],
                [["https://news.google.com/news/feeds?pz=1&cf=all&ned=us&hl=en&output=rss"],["googleang"]]]
if choix=="5":
    listeurl = [[["https://news.google.com/news/feeds?pz=1&cf=all&ned=fr&hl=fr&topic=n&output=rss"],["google"]],
                [["http://liberation.fr.feedsportal.com/c/32268/fe.ed/rss.liberation.fr/rss/9/"],["liberation"]],
                [["http://liberation.fr.feedsportal.com/c/32268/fe.ed/rss.liberation.fr/rss/12/"],["liberation"]],
                [["http://rss.leparisien.fr/leparisien/rss/societe.xml"],["leparsien"]],
                [["http://rss.leparisien.fr/leparisien/rss/une.xml"],["leparsien"]],
                [["http://rss.leparisien.fr/leparisien/rss/actualites-a-la-une.xml"],["leparsien"]],
                [["http://www.bfmtv.com/rss/societe.rss"],["bmttv"]],
                [["http://rss.lefigaro.fr/lefigaro/laune"],["lefigaro"]],
                [["http://www.lefigaro.fr/rss/figaro_actualite-france.xml"],["lefigaro"]],
                [["http://rss.lemonde.fr/c/205/f/3050/index.rss"],["le monde"]],
                [["http://rss.lemonde.fr/c/205/f/3054/index.rss"],["le monde"]],
                [["http://fr.news.yahoo.com/rss/france"],["yahoo"]],
                [["http://fr.news.yahoo.com/rss/societe"],["yahoo"]],
                [["http://www.tf1.fr/xml/rss/0,,1,00.xml"],["tf1"]],
                [["http://www.20min.ch/rss/rss.tmpl?type=channel&get=6"],["20minutes"]],
                [["http://www.20min.ch/rss/rss.tmpl?type=channel&get=17"],["20minutes"]],
                [["http://www.francetvinfo.fr/titres.rss"],["francetv"]]]

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
          "tou","avoir","apre","contre","nouveau","ce","un","deux","trois","quatre","cinq","six","sept","huit","neuf",
          "in","place"]

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
    if n2>=n-2:
        listemotcle3.append(elt)
print(listemotcle3)
liste=[]
for element,journal in listeurl:
    MyFeedsConfig =element
    for feed in MyFeedsConfig:
        feeds.append(feedparser.parse(feed))
    for feed in feeds:
        for item in feed[ "items" ]:
            accept=0
            motcate=[]
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
                        motcate.append(elt)
            if accept==1:
                for elt in motcate:
                    liste.append([elt,item.title,journal,item.link])
    feeds = []

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
for motcle in listemotcle3:
    labelinfo=Button(frm,text="%s"%motcle,bg="red")
    labelinfo.pack(side=TOP)
    for motc,elment,journal,url in liste:
        if motc==motcle:
                c=Button(frm,text="%s - %s"%(elment,journal),command=lambda i=url:choose(i,))
                c.pack(side=TOP)
def choose(url):
    webbrowser.open(url)
frm.update_idletasks()
cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))

root.mainloop()

