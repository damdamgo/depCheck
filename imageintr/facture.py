import codecs
import time
import sys
import os
import datetime as DT
from tkinter import Tk,Label,Button,Frame
from tkinter import *
import tkinter as tk
import numpy
import tkinter as tk
from PIL import Image, ImageTk
import glob
import shutil
import matplotlib.backends.backend_tkagg##pour le point exe

################chargement de la date locale ################
date=time.strftime('%d-%m-%Y',time.localtime())
datehisto=time.strftime('%d',time.localtime())
moistoday=time.strftime('%m',time.localtime())
anneetoday=time.strftime('%Y',time.localtime())
################recuperation des dates de la derniere utilisation####
categorieini=numpy.load("categories/categorieini.npy")
categorieini=categorieini.tolist()
if os.path.isfile("categories/test3.npy"):#####on regarde si il existe les fichiers historiques des depenses par categories
    print()
else:
    liste=["01","02","03","04","05","06","07","08","09","10","11","12"]
    for categorie in categorieini:
        os.mkdir("categories/%s/%sfact%s"%(categorie,anneetoday,categorie))
        for nombre in liste:
            os.mkdir("categories/%s/%sfact%s/%s"%(categorie,anneetoday,categorie,nombre))
    a=0
    numpy.save("categories/test3.npy",a)

def facture():
    def retour():
        frameshowfracture.destroy()
        framecategorie.destroy()
        bmenu.destroy()
        menu()
    bajout.destroy()
    bfacture.destroy()
    frameshowfracture=Frame(frameprincipale,bg=couleursec)
    frameshowfracture.pack(side=RIGHT,fill=BOTH, expand=1)
    framecategorie=Frame(frameprincipale,bg=couleurfrm)
    framecategorie.pack(side=LEFT)
    framefactureshow=Frame(frameshowfracture,bg=couleursec)
    framefactureshow.grid()
    cnv2 = Canvas(framefactureshow,bg=couleursec,width=805,height=600)
    cnv2.grid(row=0, column=0)
    bmenu=Button(framecategorie,text="menuprincipal",command=retour)
    bmenu.grid()
    framefacture=Frame(framecategorie,bg=couleursec)
    framefacture.grid()
    cnv = Canvas(framefacture,bg=couleursec,width=150,height=550)
    cnv.grid(row=0, column=1)
    vScroll = Scrollbar(framefacture, orient=VERTICAL, command=cnv.yview)
    vScroll.grid(row=0, column=0, sticky='ns')
    cnv.configure(yscrollcommand=vScroll.set)
    frm = Frame(cnv,bg=couleurfrm)
    cnv.create_window(0, 0, window=frm, anchor='nw')
    n=0
    n2=0
    for categor in categorieini:###cree bouton de la liste des categorie
        c=Button(frm,text=categor,width=20,height=5,bg=couleursec,command=lambda i=categor:ch(i)).grid(pady=10,row=n, column=n2)
        n=n+1
    frm.update_idletasks()
    cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
    vScroll2 = Scrollbar(framefactureshow, orient=VERTICAL, command=cnv2.yview)
    def ch(choix):###fonction appelée après clique sur bouton
        global accept
        global ch
        ch=choix
        def recherche():
            global accept
            global ch
            choix=ch
            print(choix)
            accept=0
            framemodif.destroy()
            cnv2.delete(ALL)
            mois=t.get()
            annee=t2.get()
            couleurfrm="#99512B"
            vScroll2.grid(row=0, column=1, sticky='ns')
            cnv2.configure(yscrollcommand=vScroll2.set)
            frm2 = Frame(cnv2,bg=couleurfrm)
            cnv2.create_window(0, 0, window=frm2, anchor='nw')
            n=0
            n2=0
            n3=0
            for file in glob.glob("categories/%s/%sfact%s/%s/*.jpg"%(choix,annee,choix,mois)):
                b=os.path.splitext(os.path.basename(file))[0]
                verif=b[-1]
                if verif=="z":
                    btext = b.replace("z", "")
                    photo=ImageTk.PhotoImage(file="categories/%s/%sfact%s/%s/%s.jpg"%(choix,anneetoday,choix,mois,b))
                    bouton = Button(frm2,compound=TOP,height=150,text="%s"%btext, width=150,image=photo,command=lambda i=btext:choose(i))
                    dic['photo%s'%n3]=photo## on sauvegarde dans le dico l'instance
                    bouton.grid(row=n, column=n2,padx=20,pady=10)
                    n2=n2+1
                    n3=n3+1
                    if n2==4:
                        n2=0
                        n=n+1
            frm2.update_idletasks()
            cnv2.configure(scrollregion=(0, 0, frm2.winfo_width(), frm2.winfo_height()))
            def choose(choix2):
                 os.startfile("categories\%s\%sfact%s\%s\%s.jpg"%(choix,anneetoday,choix,mois,choix2))       
        vScroll2.grid_forget()
        if accept==0:
            framemodif=Frame(cnv2)
            framemodif.pack(padx=50,pady=250)
            iframemois = Frame(framemodif, bd=2, relief=RIDGE)###frame qui permet ajout du mois
            Label(iframemois, text='entrer le mois :').pack(side=LEFT, padx=5)###label qui indique ce que doit faire l'utilisateur
            t = StringVar()###on indique la variable qui va prendre la valeur de ce que va rentrer l'utilisateur
            Entry(iframemois, textvariable=t, bg='white').pack(side=LEFT, padx=5)###on place la case qui permet a l'utilisateur d'ecrire
            iframemois.pack(expand=1, fill=X, pady=10, padx=5)
            iframeannee = Frame(framemodif, bd=2, relief=RIDGE)###frame qui permet ajout de l'annee
            Label(iframeannee , text="entrer l'annee :").pack(side=LEFT, padx=5)
            t2 = StringVar()###on indique la variable qui va prendre la valeur de ce que va rentrer l'utilisateur
            Entry(iframeannee , textvariable=t2, bg='white').pack(side=LEFT, padx=5)###on place la case qui permet a l'utilisateur d'ecrire
            iframeannee.pack(expand=1, fill=X, pady=10, padx=5)
            button1=Button(framemodif ,text="rechercher",command=recherche)###le bouton qui appelle fonction recherche
            button1.pack()
            accept=1
def ajout():
    def retour():
        frameshowfracture.destroy()
        framecategorie.destroy()
        bmenu.destroy()
        menu()
    def ajouter():
        global ch
        try:
            choix=ch
            mois=t.get()
            annee=t2.get()
            for infile in glob.glob("ajout facture/*.jpg"):
                size = 128, 128
                file, ext = os.path.splitext(infile)
                im = Image.open(infile)
                im.thumbnail(size, Image.ANTIALIAS)
                im.save(infile + "z.jpg", "JPEG")
            for file in glob.glob("ajout facture/*.jpg"):   
                c=os.path.basename(file)
                shutil.copy("ajout facture\%s"%c,"categories\%s\%sfact%s\%s\%s"%(choix,annee,choix,mois,c))
                os.remove("ajout facture\%s"%c)
            retour()
        except:
            problem.set("imposssible d'ajouter la facture")
    bajout.destroy()
    bfacture.destroy()
    frameshowfracture=Frame(frameprincipale,bg=couleursec)
    frameshowfracture.pack(side=RIGHT,fill=BOTH, expand=1)
    framecategorie=Frame(frameprincipale,bg=couleurfrm)
    framecategorie.pack(side=LEFT)
    frameajout=Frame(frameshowfracture,bg=couleursec)
    frameajout.pack()
    label1=Label(frameajout,text="_mettre la facture scanner dans le dossier ajout facture(format en jpg \n_choisissez la categorie ainsi que le mois et l'année \n_cliquez sur ajouter")
    label1.grid()
    categorieini=numpy.load("categories/categorieini.npy")###on amene la liste des categories
    categorieini=categorieini.tolist()
    frameboutondep=Frame(frameajout,bg=couleursec)
    frameboutondep.grid()
    cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
    cnv.grid(row=0, column=0)
    hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
    hScroll.grid(row=1, column=0, sticky='we')
    cnv.configure(xscrollcommand=hScroll.set)
    frm = Frame(cnv,bg=couleurfrm)
    cnv.create_window(0, 0, window=frm, anchor='nw')
    for categor in categorieini:###cree bouton de la liste des categorie
        c=Button(frm,text=categor,width=10,height=5,bg=couleursec,command=lambda i=categor:ch(i))
        c.pack(side=LEFT,padx=10)###plac
    frm.update_idletasks()
    cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
    def ch(choix):###fonction appelé apres clique sur bouton
        global ch
        ch=choix
        cho.set("vous avez choisie la categorie %s"%choix)
        problem.set("")
    cho=StringVar()
    label2=Label(frameajout,textvariable=cho,bg=couleursec)
    label2.grid()
    problem=StringVar()
    label3=Label(frameajout,textvariable=problem,bg=couleursec)
    label3.grid()
    framemodif=Frame(frameajout)
    framemodif.grid()
    iframemois = Frame(framemodif, bd=2, relief=RIDGE)###frame qui permet ajout du mois
    Label(iframemois, text='entrer le mois :').pack(side=LEFT, padx=5)###label qui indique ce que doit faire l'utilisateur
    t = StringVar()###on indique la variable qui va prendre la valeur de ce que va rentrer l'utilisateur
    Entry(iframemois, textvariable=t, bg='white').pack(side=LEFT, padx=5)###on place la case qui permet a l'utilisateur d'ecrire
    iframemois.pack(expand=1, fill=X, pady=10, padx=5)
    iframeannee = Frame(framemodif, bd=2, relief=RIDGE)###frame qui permet ajout de l'annee
    Label(iframeannee , text="entrer l'annee :").pack(side=LEFT, padx=5)
    t2 = StringVar()###on indique la variable qui va prendre la valeur de ce que va rentrer l'utilisateur
    Entry(iframeannee , textvariable=t2, bg='white').pack(side=LEFT, padx=5)###on place la case qui permet a l'utilisateur d'ecrire
    iframeannee.pack(expand=1, fill=X, pady=10, padx=5)
    button1=Button(framemodif ,text="ajouter",command=ajouter)###le bouton qui appelle fonction recherche
    button1.pack()
    bmenu=Button(frameshowfracture,text="menuprincipal",command=retour)
    bmenu.pack(side=TOP,pady=50)
    
def menu():
    def goajout():
        bajout.destroy()
        bfacture.destroy()
        ajout()
    def gofacture():
        bajout.destroy()
        bfacture.destroy()
        facture()
    bajout=Button(frameprincipale,text="ajouter une facture",command=goajout,bg=couleursec,width=30,height=5)
    bajout.pack(padx=10,side=RIGHT)
    bfacture=Button(frameprincipale,text="voir les factures",comman=gofacture,bg=couleursec,width=30,height=5)
    bfacture.pack(padx=10,side=RIGHT)
    
ch=0
accept=0
dic={}
root = Tk()###on indique que root est une fenetre
root.resizable(False, False)###on peut pas modifier la taille de la fenetre
couleurprin="#DEB887"
couleursec="#FEFEE0"
couleurfrm="#99512B"
frameprincipale = Frame(root,width=1000,height=600,bg=couleursec)###on cree une frame 1000*600 (taille de la fenetre)
frameprincipale.pack()
frameprincipale.pack_propagate(0)### taille de la frame fixe
bajout=Button(frameprincipale,text="ajouter une facture",command=ajout,bg=couleursec,width=30,height=5)
bajout.pack(padx=10,side=RIGHT)
bfacture=Button(frameprincipale,text="voir les factures",comman=facture,bg=couleursec,width=30,height=5)
bfacture.pack(padx=10,side=RIGHT)
root.mainloop()### cree boucle

