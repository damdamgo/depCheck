
########################################################################
################version_evolution 2---2.6---################################
#########cette version permet par interface graphique:
################creation des dossiers et fichiers necessaires au programme
################depenses par categories 
################gerer des recettes generales
################enregistrement des données
################graphiques selon les mois et années
################gestion d'un historique 
################parametre pour la gestion des données et creation de categories
################informations par annee
################################################################
################programmeurs : Damien villiers, Alexis Leboucher
################################################################
##########pour fonctionner il faut :
################python 
################le module matplotlib
################le module numpy
################################################################
# -*- coding: utf-8 -*-
################modules importés
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

################
################chargement de la date locale ################
date=time.strftime('%d-%m-%Y',time.localtime())
datehisto=time.strftime('%d',time.localtime())
moistoday=time.strftime('%m',time.localtime())
anneetoday=time.strftime('%Y',time.localtime())
################recuperation des dates de la derniere utilisation####
try:
    mon_fichier = open("mois.txt", "r")######si le fichier existe on recupere la valeur moisw
    moisw = mon_fichier.read()
    mon_fichier.close()
except:
    mon_fichier = open("mois.txt", "w")###### si le fichier n'existe pas on cree le fichier puis on recupere moisw
    mon_fichier.write(moistoday)
    mon_fichier.close()
    moisw=moistoday
try:
    mon_fichier = open("annee.txt", "r")######si le fichier existe on recupere la valeur anneew
    anneew = mon_fichier.read()
    mon_fichier.close()
except:
    mon_fichier = open("annee.txt", "w")###### si le fichier n'existe pas on cree le fichier puis on recupere anneew
    mon_fichier.write(anneetoday)
    mon_fichier.close()
    mon_fichier.close()
    anneew=anneetoday

if os.path.isdir("%s"%anneetoday):######on verifie si il existe un dossier de l'annee
    print()
else:
    os.mkdir("%s" % anneetoday)######sinon on en crée un

if  os.path.isfile("%s/date.npy"%anneetoday):######on verifie si il existe une base de donnée date pour les graphiques
    print()
else:
    newdate=[1,2,3,4,5,6,7,8,9,10,11,12]###### sinon une crée la base de donnee
    numpy.save("%s/date.npy" % anneetoday,newdate)
#############################################################
if moistoday==moisw and anneetoday==anneew:#######on verifie l'égalité
    moismod=0
    moismod=int(moistoday)
    moismod=moismod-1#########les listes commencent a  zero ainsi pour lire la valeur correspondant au mois il faut enlever un
    ########################################################################
    ## chargement donnees depense solde recette
    ###########################depense#############################################
    try:
        listedepense=numpy.load("%s/%sdepense.npy" % (anneetoday,anneetoday))
        listedepense=listedepense.tolist()
        depense=listedepense[moismod]
        depense=float(depense)########recuperation de la donnée depense associee au mois
    except:
        newliste=[0,0,0,0,0,0,0,0,0,0,0,0]
        numpy.save("%s/%sdepense.npy" % (anneetoday,anneetoday),newliste)
        listedepense=numpy.load("%s/%sdepense.npy" % (anneetoday,anneetoday))
        listedepense=listedepense.tolist()
        depense=listedepense[moismod]
        depense=float(depense)########si le fichier n'existe pas on cree le fichier puis on recupere la valeur depense ici zero
     ###########################recette#############################################
    try:
        listerecette=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))
        listerecette=listerecette.tolist()
        recette=listerecette[moismod]
        recette=float(recette)########recuperation de la donnee recette associee au mois
    except:
        newliste=[0,0,0,0,0,0,0,0,0,0,0,0]
        numpy.save("%s/%srecette.npy" % (anneetoday,anneetoday),newliste)
        listerecette=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))
        listerecette=listerecette.tolist()
        recette=listerecette[moismod]
        recette=float(recette)########si le fichier n'existe pas on cree le fichier puis on recupere la valeur recette ici zero
    ###########################solde#############################################
    try:
        listesolde=numpy.load("%s/%ssolde.npy" % (anneetoday,anneetoday))
        listesolde=listesolde.tolist()
        solde=listesolde[moismod]
        solde=float(solde)########recuperation de la donnÃ©e solde associÃ©e au mois
    except:
        newliste=[0,0,0,0,0,0,0,0,0,0,0,0]
        numpy.save("%s/%ssolde.npy" % (anneetoday,anneetoday),newliste)
        listesolde=numpy.load("%s/%ssolde.npy" % (anneetoday,anneetoday))
        listesolde=listesolde.tolist()
        solde=listesolde[moismod]
        solde=float(solde)########si le fichier n'existe pas on crée le fichier puis on recupere la valeur solde ici zero
    ###########################recuperation categorie#############################################
    if os.path.isfile("categories/categorieliste.npy"):
        categorie=numpy.load("categories/categorieliste.npy")######### on recupere les listes des categories
        categorie=categorie.tolist()
        categorieini=numpy.load("categories/categorieini.npy")
        categorieini=categorieini.tolist()
    else:
        os.mkdir("categories")#########si on ne les trouve pas alors on crée les listes
        categorie={"alimentation":1,"assurance":2,"carburant":3,"chauffage":4,"electricite":5,"fraisimprevus":6,"internet":7,"loisir":8,"taxe":9,"telephone":10,"transport":11}
        categorieini=["alimentation","assurance","carburant","chauffage","electricite","fraisimprevus","internet","loisir","taxe","telephone","transport"]
        numpy.save("categories/categorieliste.npy",categorie)
        numpy.save("categories/categorieini.npy",categorieini) 
    ###############################depenses selon categories#########################################
    if os.path.isfile("categories/test1.npy"):######on regarde si les bases de données des depenses existent
        print()
    else:
        a=0
        numpy.save("categories/test1.npy",a)
        newcategorie=[0,0,0,0,0,0,0,0,0,0,0,0]
        for mot in categorieini:
            os.mkdir("categories/{}".format(mot))######### sinon crée une base de sauvegarde
        for mot in categorieini:
            numpy.save("categories/%s/%s%s.npy" % (mot,anneetoday,mot),newcategorie)
    ##########################historique recette##############################################
    try:
        listehistorec=numpy.load("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday))########on recupere les historiques de ce mois-ci pour recettes
        listehistorec=listehistorec.tolist()
    except:
        newhisto=["01","02","03","04","05","06","07","08","09","10","11","12"]########sinon on cree dossiers et fichiers pour le fonctionnement de l'historique recettes
        listezero=[]
        os.mkdir("%s/historique" % anneetoday)
        for elt in newhisto:
            os.mkdir("%s/historique/%s" % (anneetoday,elt))
        for elt in newhisto:
            numpy.save("%s/historique/%s/%shistorec.npy" % (anneetoday,elt,elt),listezero)
        listehistorec=numpy.load("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday))
        listehistorec=listehistorec.tolist()
    ##############################historique depense##########################################
    if os.path.isfile("%s/historique/test2.npy" % anneetoday):#####on regarde si il existe les fichiers historiques des depenses par categories
        print()
    else:#########sinon on crée une base de sauvegarde par categories
        a=0
        numpy.save("%s/historique/test2.npy" % anneetoday,a)
        categorieini={"alimentation","assurance","carburant","chauffage","electricite","fraisimprevus","internet","loisir","taxe","telephone","transport"}
        newhisto=["01","02","03","04","05","06","07","08","09","10","11","12"]
        listezero=[]
        for elt in newhisto:
            for nb in categorieini:
                numpy.save("%s/historique/%s/%s%s.npy" % (anneetoday,elt,elt,nb),listezero)
    #######################################################################################################################################################################################################################

################################################################################################################################################
#########################################graphiques#######################################################################################################
    def graphiques():###debut fonction graphiques
        def menu():
            framechange.destroy()
            bmenuprincipale.destroy()
            menuprincipale()
        def graphdep():###permet le choix de la categorie
            bdepense.grid_forget()###on enleve les boutons de la framebouton
            brecette.grid_forget()
            bsolde.grid_forget()
            categorieini=numpy.load("categories/categorieini.npy")###on amene la liste des categories
            categorieini=categorieini.tolist()
            frameboutondep=Frame(framebouton,bg=couleursec)
            frameboutondep.grid()
            cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
            cnv.grid(row=0, column=0)
            couleurfrm="#99512B"
            hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
            hScroll.grid(row=1, column=0, sticky='we')
            cnv.configure(xscrollcommand=hScroll.set)
            frm = Frame(cnv,bg=couleurfrm)
            cnv.create_window(0, 0, window=frm, anchor='nw')
            for categor in categorieini:###cree bouton de la liste des categorie
                c=Button(frm,text=categor,width=10,height=5,bg=couleursec,command=lambda i=categor:ch(i))
                c.pack(side=LEFT,padx=10)###plac
            bdepensetotal=Button(frm,text="depense total",width=10,height=5,bg=couleursec,command=lambda :ch("depense"))
            bdepensetotal.pack(side=LEFT,padx=10)###crée bouton depense total
            frm.update_idletasks()
            cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
            def ch(choix):###fonction appelée après clique sur bouton
                frameboutondep.destroy()
                numpy.save("ch.npy",choix)###on sauvegarde le choix
                comparer()###on appelle la fonction qui construit les graphiques
        def graphrec():###on sauvegarde le choix recette
            bdepense.grid_forget()###on enleve les boutons de la framebouton
            brecette.grid_forget()
            bsolde.grid_forget()
            ch="recette"
            numpy.save("ch.npy",ch)###sauvegarde
            comparer()###on appelle la fonction qui construit les graphiques
        def graphsol():###on sauvegarde le choix solde
            bdepense.grid_forget()###on enleve les boutons de la framebouton
            brecette.grid_forget()
            bsolde.grid_forget()
            ch="solde"
            numpy.save("ch.npy",ch)###sauvegarde
            comparer()###on appelle la fonction qui construit les graphiques
        def comparer():###permet a l'utilisateur de pouvoir comparer les graphiques
            def ajouter():###fonction qui ajoute les saisie
                varprobleme.set("")
                anneetoday=time.strftime('%Y',time.localtime())
                anneeentry=t.get()###on recupere l'annee saisie
                ajout=numpy.load("ajout.npy")
                ajout=ajout.tolist()
                lim=0
                possible=0
                for annee in ajout:###on verifie si l'annee entrée est deja presente dans la liste
                    if annee==anneeentry:
                        possible=1
                if anneeentry==anneetoday:###on verifie si l'annee entrée n'est pas cette année
                    possible=1
                if possible==0:###si elle verifie alors on l'ajoute a la liste
                    for annee in ajout:
                        lim=lim+1
                    if lim<=4:
                        ajout.append(anneeentry)
                        numpy.save("ajout.npy",ajout)###on enregistre l'anne dans la liste
                        varajout.set(ajout)
                    else:###si on arrive a la limite on l'indique a l'utilisateur
                        varprobleme.set("impossible de rajouter une annee")
                if possible==1:###si elle est deja presente on l'indique
                    varprobleme.set("impossible de rajouter cette annee car elle est deja presente")
                t.set("")
            def fin():###fonction qui construit les graphiques
                framemodif.destroy()
                bdepense.grid(row=0, column=1,padx=10)###on place les boutons du menu graphique
                brecette.grid(row=0, column=2,padx=10)
                bsolde.grid(row=0, column=3,padx=10)
                if choix=="recette" or choix=="depense" or choix=="solde":
                    anneetoday=time.strftime('%Y',time.localtime())
                    possible=0###initialise
                    listechoix=numpy.load("%s/%s%s.npy" % (anneetoday,anneetoday,choix))###on recupere la liste du choix de l'annee
                    ajout=numpy.load("ajout.npy")
                    ajout=ajout.tolist()###on importe la liste des années a comparer
                    listedategraph=numpy.load("%s/date.npy" % anneetoday)#######on recupere les donnees de l'axe de l'abcisse
                    listedategraph=listedategraph.tolist()
                    x =listedategraph###on associe une liste a un axe
                    z=listechoix
                    l=plot(x,z,'r-x',linewidth=3,label=anneetoday)###on cree la courbe de cette annee  
                    info=0
                    for annee in ajout:
                        try:
                            listechoixcomparer=numpy.load("%s/%s%s.npy" % (annee,annee,choix))#######on regarde si il y a une base de donnee des annees choisies
                            listechoixcomparer=listechoixcomparer.tolist()
                            yn=listechoixcomparer
                            ln=plot(x,yn,'g:x',linewidth=3,label=annee)###si il y a une base on constuit une courbe
                            del ajout[annee]
                        except:###sinon on informe que c'est impossible de comparer
                            varindique.set("impossible de construire les courbes des annees %s"%ajout)
                    ylabel("les donnees %s"%choix)###on fixe les legendes
                    xlabel(anneetoday)
                    legend()###on met les legende sur le graphique
                    grid()###on met le graphique sur une grill
                    ## pour colorer zone use fill_between
                    xticks(x)###on fixe les x
                    show()######on affiche le graphique
                else:###si le choix est une categorie
                    anneetoday=time.strftime('%Y',time.localtime())
                    categograph=choix
                    categoriegraph=numpy.load("categories/%s/%s%s.npy" % (categograph,anneetoday,categograph))###on recupere la liste depense de la categorie
                    categoriegraph=categoriegraph.tolist()
                    listedategraph=numpy.load("%s/date.npy" % anneetoday)#######on recupere les donnees de l'axe de l'abcisse
                    listedategraph=listedategraph.tolist()
                    x=listedategraph###on associe une liste a un axe
                    y=categoriegraph
                    l=plot(x,y,'r-x',linewidth=3,label=anneetoday)###on cree la courbe correspondant a cette année
                    ajout=numpy.load("ajout.npy")
                    ajout=ajout.tolist()###on importe la liste des années a comparer
                    info=0
                    listecouleur=['b:x',' g:x', 'r:x', 'c:x',' m:x',' y:x']
                    for annee in ajout:
                        try:#####on regarde si il existe des donnees de l'annee derniere
                            categoriegraphchoixcomparer=numpy.load("categories/%s/%s%s.npy" % (categograph,annee,categograph))#######on regarde si il y a une base de donnee de l'annee derniere
                            categoriegraphchoixcomparer=categoriegraphchoixcomparer.tolist()
                            yn=categoriegraphchoixcomparer
                            couleur=listecouleur[n]
                            ln=plot(x,yn,couleur,linewidth=3,label=annee)###si il y a une base de donnees on constuit une courbe
                            del ajout[annee]
                        except:###sinon on informe que c'est impossible de comparer
                            varindique.set("impossible de construire les courbes des annees %s"%ajout)
                    ylabel("depense %s" % categograph)###on fixe les legendes
                    xlabel(anneetoday)
                    legend()###on met les legende sur le graphique
                    grid()###on met le graphique sur une grill
                    ## pour colorer zone use fill_between
                    xticks(x)###on fixe les x
                    show()######on affiche le graphique
            ajout=[]
            numpy.save("ajout.npy",ajout)
            couleurfrm="#99512B"
            framemodif=Frame(framechange,bg=couleursec)###on ajoute une autre frame qui permet de mettre d'autre widgets
            framemodif.pack()
            choix=numpy.load("ch.npy")
            labelchange=Label(framemodif,text=choix)###on indique la categorie choisie par l'utilisateur pour les graphiques
            labelchange.pack()
            iframeajout = Frame(framemodif, bd=2, relief=RIDGE)###frame qui permet d'ajouter des annees
            Label(iframeajout, text='entrer une annee a comparer :').pack(side=LEFT, padx=5)###label qui indique l'action
            t = StringVar()###on indique la variable qui va prendre la valeur de ce que va rentrer l'utilisateur
            Entry(iframeajout, textvariable=t, bg='white').pack(side=LEFT, padx=5)###on place la case qui permet a l'utilisateur d'ecrire
            iframeajout.pack(expand=1, fill=X, pady=10, padx=5)
            iframeorigine = Frame(framemodif, bd=2, relief=RIDGE)###frame qui permet d'indiquer la provenance
            button1=Button(framemodif ,text="ajouter",command=ajouter)###bouton qui permet l'ajout des donnees saisies par l'utilisateur
            button1.pack()
            varajout= StringVar()
            iframeresume = Frame(framemodif, bd=2, relief=RIDGE)###frame qui resume les entrees
            labelajoutres=Label(iframeresume,text="resume des annee a comparer :")###indique a quoi correspond la variable 
            labelajoutres.grid(row=0, column=0)
            labelajout=Label(iframeresume,textvariable=varajout)###indique le resume des saisies
            labelajout.grid(row=0, column=1)
            iframeresume.pack(expand=1, fill=X, pady=10, padx=5)
            varprobleme=StringVar()
            labelprobleme=Label(iframeajout,textvariable=varprobleme)###indique si il y a un probleme a l'ajout d'une annee
            labelprobleme.pack()
            bconstruire=Button(framemodif,text="constuire le graphique",command=fin)###bouton qui permet de construire les graphiques
            bconstruire.pack()    
        framemenuprincipale.destroy()###detruit frame menu principale du lancement
        framechange=Frame(frameprincipale,bg=couleursec)###frame qui va contenir les widgets
        framechange.pack()
        labelinfo=Label(framechange,bg=couleursec,text="veuillez choisir quel graphique voulez vous construire")
        labelinfo.pack(pady=10)
        framebouton=Frame(framechange,bg=couleursec)###frame qui possede les boutons
        framebouton.pack(pady=75)
        bdepense=Button(framebouton,bg=couleursec,text="depense",height=5,width=20,command=graphdep)
        bdepense.grid(row=0, column=1,padx=10)###bouton depense
        brecette=Button(framebouton,bg=couleursec,text="recette",height=5,width=20,command=graphrec)
        brecette.grid(row=0, column=2,padx=10)###bouton recette
        bsolde=Button(framebouton,bg=couleursec,text="solde",height=5,width=20,command=graphsol)
        bsolde.grid(row=0, column=3,padx=10)###bouton solde
        varindique = StringVar()
        labelindique=Label(framechange,textvariable=varindique,bg=couleursec)###label qui permet d'indiquer si on peut comparer avec l'annee anterieur
        labelindique.pack()
        bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principale",command=menu)###on met le bouton qui permet le retour au menuprincipale
        bmenuprincipale.grid(row=0, column=0)
################################################################################################################################################
#######################################ajout de valeurs#########################################################################################################
    def sold():###fonction qui permet ajout de valeur
        moistoday=time.strftime('%m',time.localtime())
        anneetoday=time.strftime('%Y',time.localtime())
        date=time.strftime('%d-%m-%Y',time.localtime())
        moismod=0
        moismod=int(moistoday)
        moismod=moismod-1#########les listes commencent a  zero ainsi il faut enlever 1 au mois
        def menu():###fonction qui retourne au menu principale
            framechange.destroy()###detuit la frame
            framemodif.destroy()###detuit la frame
            bmenuprincipale.destroy()###detuit le bouton
            listerecette=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))
            listerecette=listerecette.tolist()
            recette=listerecette[moismod]
            recette=float(recette)###mise a jour des donnees recette
            listedepense=numpy.load("%s/%sdepense.npy" % (anneetoday,anneetoday))
            listedepense=listedepense.tolist()
            depense=listedepense[moismod]
            depense=float(depense)###mise a jour des donnees depense
            solde=recette-depense
            listesolde=numpy.load("%s/%ssolde.npy" % (anneetoday,anneetoday))
            listesolde[moismod]=solde###mise a jour des donnees soldes
            numpy.save("%s/%ssolde.npy" % (anneetoday,anneetoday),listesolde)
            menuprincipale()###appelle la fonction menu principale
        def dep():###fonction depense
            categorieini=numpy.load("categories/categorieini.npy")
            categorieini=categorieini.tolist()###charge les listes categories
            newliste=[]
            couleurfrm="#99512B"
            numpy.save("ajout.npy",newliste)###initialise des fichiers avant utilisation
            numpy.save("ajouthisto.npy",newliste)
            varajout.set("0")###initialisation des variables
            varajoutotal.set("0")
            bdepense.grid_forget()###on enleve les boutons
            brecette.grid_forget()
            categorieini=numpy.load("categories/categorieini.npy")###on amene la liste des categories
            categorieini=categorieini.tolist()
            frameboutondep=Frame(framebouton,bg=couleursec)
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
                frameboutondep.destroy()
                bdepense.grid(row=0, column=1,padx=10)###on remet les boutons en place du menu
                brecette.grid(row=0, column=2,padx=10)
                var.set(choix)###on met a jour les variables
                benregistrer.pack()
                varenregistre.set("enregistre %s"%choix)
                numpy.save("ch.npy",choix)###on sauvegarde le choix
                varprobleme.set("")
        def ajout():###fonction apres clique sur bouton ajout
            provenance=t2.get()###on recupere les donnes entry
            varprobleme.set("")
            a=t.get()
            try:
                a=float(a)###indique que a est un nombre a virgule
            except:
                varprobleme.set("probleme ajout : valeur non detectée")###si on peut pas mettre en float on indique le probleme
            if a<0:
                varprobleme.set("probleme ajout : valeur negative")###si le nombre est negatif on indique le probleme
            if a>0:
                try:
                    ajoutdep=a#####on verifie que la donnee saisie a maximum 2 decimales
                    ajoutdep1="%.2f"%ajoutdep
                    ajoutdep1=float(ajoutdep1)
                    ajoutdepverif=ajoutdep1-ajoutdep
                    if ajoutdepverif<0 or ajoutdepverif>0:
                        varprobleme.set("probleme ajout : plus de deux décimales")###on indique si le nombre comporte plus de trois decimales
                    if ajoutdepverif==0:#####sinon on ajoute la donnee saisie a la valeur depense recuperee si dessus 
                        ajout=numpy.load("ajout.npy")
                        ajout=ajout.tolist()
                        ajout.append(a)
                        numpy.save("ajout.npy",ajout)###on sauvegarde l'ajout
                        ajout=numpy.load("ajout.npy")
                        ajoutotal=numpy.sum(ajout)###on fait la somme des ajouts
                        ajout=ajout.tolist()
                        varajout.set(ajout)###on met a jour les variables
                        varajoutotal.set(ajoutotal)
                        ajouthisto=numpy.load("ajouthisto.npy")
                        ajouthisto=ajouthisto.tolist()
                        ajouthisto.append([a,datehisto,provenance])###on ajoute a la liste histo la valeur de l'ajout la date ainsi que la provenance
                        numpy.save("ajouthisto.npy",ajouthisto)
                except:
                    varprobleme.set("probleme ajout")###sinon on indique qu'il y a un probleme
            t.set("")###on vide les entry
            t2.set("")
        def rec():###function appele apres clique sur recette
            newliste=[]
            numpy.save("ajouthisto.npy",newliste)###initialise les fichiers
            numpy.save("ajout.npy",newliste)
            varajout.set("0")###on met a jour les variables
            varajoutotal.set("0")
            var.set("recette")
            varprobleme.set("")
            benregistrer.pack()
            varenregistre.set("enregistre recette")
            a="recette"###on sauvegarde le choix
            numpy.save("ch.npy",a)
        def fin():###function appele pour l'enregistrement
            ch=numpy.load("ch.npy")###on recupere le choix 
            varajout.set("0")###met a jour les vaiables
            varajoutotal.set("0")
            var.set("")
            moismod=0
            moismod=int(moistoday)
            moismod=moismod-1#########les listes commencent a  zero ainsi il faut enlever 1 au mois
            if ch=="recette":###si le choix est recette
                modif=numpy.load("%s/%s%s.npy" % (anneetoday,anneetoday,ch))
                modif=modif.tolist()
                chmodif=modif[moismod]
                chmodif=float(chmodif)########recuperation de la donnee recette associee au mois
                ajout=numpy.load("ajout.npy")
                ajoutotal=numpy.sum(ajout)
                ajoutotal=float(ajoutotal)
                chmodif=chmodif+ajoutotal###on ajout le total des ajouts
                modif[moismod]=chmodif###on modifie la valeur de recette du mois
                numpy.save("%s/%s%s.npy" % (anneetoday,anneetoday,ch),modif)###on enregistre la liste recette
                listehistorec=numpy.load("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday))########on recupere les historiques de ce mois-ci
                listehistorec=listehistorec.tolist()
                ajouthisto=numpy.load("ajouthisto.npy")
                ajouthisto=ajouthisto.tolist()
                for nb,date,provenance in ajouthisto:
                    listehistorec.append(["ajoute des recettes",nb,date,provenance])###on enregistre dans l'historique les informations
                numpy.save("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday),listehistorec)###on sauvegarde l'historiques
            else:###si le choix est une categrorie
                listecatego=numpy.load("categories/%s/%s%s.npy" % (ch,anneetoday,ch))#####on recupere la depense de cette categories
                listecatego=listecatego.tolist()
                depensecatego=listecatego[moismod]
                depensecatego=float(depensecatego)###on recupere la valeur du mois correspondant
                ajout=numpy.load("ajout.npy")
                ajoutotal=numpy.sum(ajout)
                ajoutotal=float(ajoutotal)###on ajout le total des depenses au depense de la categorie
                depensecatego=ajoutotal+depensecatego
                listecatego[moismod]=depensecatego
                numpy.save("categories/%s/%s%s.npy" % (ch,anneetoday,ch),listecatego)
                listedepense=numpy.load("%s/%sdepense.npy" % (anneetoday,anneetoday))
                listedepense=listedepense.tolist()
                depense=listedepense[moismod]
                depense=float(depense)
                depense=depense+depensecatego###on modifie aussi la valeur de la depense 
                listedepense[moismod]=depense
                numpy.save("%s/%sdepense.npy" % (anneetoday,anneetoday),listedepense)###on sauvegarde la liste depense
                listehistodepcatego=numpy.load("%s/historique/%s/%s%s.npy" % (anneetoday,moistoday,moistoday,ch))#####on recupere l'historique de la categories
                listehistodepcatego=listehistodepcatego.tolist()
                ajouthisto=numpy.load("ajouthisto.npy")
                ajouthisto=ajouthisto.tolist()
                for nb,date,provenance in ajouthisto:
                    listehistodepcatego.append(["ajouté des despenses",nb,date,provenance])###on enregistre dans l'historique les informations
                numpy.save("%s/historique/%s/%s%s.npy" % (anneetoday,moistoday,moistoday,ch),listehistodepcatego)###on sauvegarde l'historiques
        framemenuprincipale.destroy()###detruit frame menu principale du lancement
        framechange=Frame(frameprincipale,bg=couleursec)###cree une frame qui va contenir les widgets
        framechange.pack()
        vardepense = StringVar()
        varrecette = StringVar()
        solde=recette-depense
        labelpre=Label(framechange,bg=couleursec,text="choisissez ce que vous voulez modifier")###on indique ce que doit faire l'utilisateur
        labelpre.pack(side=TOP,pady=10)
        framebouton=Frame(framechange,bg=couleursec)###frame qui contient les boutons
        framebouton.pack(pady=50)
        bdepense=Button(framebouton,text="depense",bg=couleursec,height=5,width=20,command=dep)### cree bouton depense
        bdepense.grid(row=0, column=1,padx=10)
        brecette=Button(framebouton,text="recette",bg=couleursec,height=5,width=20,command=rec)###cree bouton recette
        brecette.grid(row=0, column=2,padx=10)
        bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principale",command=menu)###on ajoute le bouton qui permet de revenir au menu principal
        bmenuprincipale.grid(row=0, column=0)
        framemodif=Frame(framechange,bg=couleursec)###on ajoute une autre frame qui permet de mettre d'autre widgets
        framemodif.pack()
        var = StringVar()
        labelchange=Label(framemodif,bg=couleursec,textvariable=var)###on indique la categorie choisie par l'utilisateur
        labelchange.pack()
        iframeajout = Frame(framemodif, bd=2, relief=RIDGE)###frame qui permet d'ajouter des valeurs
        Label(iframeajout, text='entrer la somme :').pack(side=LEFT, padx=5)###label qui indique l'action
        t = StringVar()###on indique la variable qui va prendre la valeur de ce que va rentrer l'utilisateur
        Entry(iframeajout, textvariable=t, bg='white').pack(side=LEFT, padx=5)###on place la case qui permet a l'utilisateur d'ecrire
        iframeajout.pack(expand=1, fill=X, pady=10, padx=5)
        iframeorigine = Frame(framemodif, bd=2, relief=RIDGE)###frame qui permet d'indiquer la provenance
        Label(iframeorigine , text='entrer la provenance :').pack(side=LEFT, padx=5)###label qui indique l'action
        t2 = StringVar()###on indique la variable qui va prendre la valeur de ce que va rentrer l'utilisateur
        Entry(iframeorigine , textvariable=t2, bg='white').pack(side=LEFT, padx=5)###on place la case qui permet a l'utilisateur d'ecrire
        iframeorigine .pack(expand=1, fill=X, pady=10, padx=5)
        button1=Button(framemodif ,text="ajouter",command=ajout)###bouton qui permet l'ajout des donnees saisies par l'utilisateur
        button1.pack()
        varprobleme=StringVar()
        labelprobleme=Label(iframeajout,textvariable=varprobleme)###indique si il y a un probleme
        labelprobleme.pack()
        varajout= StringVar()
        varajoutotal =StringVar()
        varenregistre=StringVar()
        iframeresume = Frame(framemodif, bd=2, relief=RIDGE)###frame qui resume les entrees
        labelajoutres=Label(iframeresume,text="resume de vos saisies :")###indique a quoi correspond la variable 
        labelajoutres.grid(row=0, column=0)
        labelajout=Label(iframeresume,textvariable=varajout)###indique resume des saisies
        labelajout.grid(row=0, column=1)
        labelajoutres=Label(iframeresume,text="total de vos saisies :")###indique a quoi correspond la variable 
        labelajoutres.grid(row=1, column=0)
        labelajout1=Label(iframeresume,textvariable=varajoutotal)###indique resume des saisies
        labelajout1.grid(row=1, column=1)
        iframeresume.pack(expand=1, fill=X, pady=10, padx=5)
        benregistrer=Button(framemodif,textvariable=varenregistre,command=fin)###bouton qui permet d'enregistrer
        benregistrer.pack_forget()
################################################################################################################################################
########################################historique########################################################################################################
    def histo():###fonction historique
        def menu():###fonction pour retourner au menuprincipale
            framechange.destroy()###on detruit les frames utilisées
            bmenuprincipale.destroy()
            menuprincipale()###on appelle la fonction menuprincipales
        def rec():###fonction appele quand on clique sur le bouton
            choix=("recette")
            numpy.save("ch.npy",choix)###enregistre le choix
            varhisto.set("L'historique de recette")###met a jout les variables
            button1.pack()
            listbox.delete(0,END)###on efface linterieur de la listbox
            scrollbar.pack_forget()###on cache la listbox
            listbox.pack_forget()
            buttontext.pack_forget()
            varprobleme.set("")
        def dep():###fonction appele quand on clique sur le bouton
            categorieini=numpy.load("categories/categorieini.npy")
            categorieini=categorieini.tolist()###on va chercher la liste des categorie
            bdepense.grid_forget()###on enleve les boutons
            brecette.grid_forget()
            couleurfrm="#99512B"
            categorieini=numpy.load("categories/categorieini.npy")###on amene la liste des categories
            categorieini=categorieini.tolist()
            frameboutondep=Frame(framebouton,bg="brown")
            frameboutondep.grid()
            cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
            cnv.grid(row=0, column=0)
            hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
            hScroll.grid(row=1, column=0, sticky='we')
            cnv.configure(xscrollcommand=hScroll.set)
            frm = Frame(cnv,bg= couleurfrm)
            cnv.create_window(0, 0, window=frm, anchor='nw')
            for categor in categorieini:###cree bouton de la liste des categorie
                c=Button(frm,text=categor,width=10,height=5,bg=couleursec,command=lambda i=categor:ch(i))
                c.pack(side=LEFT,padx=10)###plac
            bdepensetotal=Button(frm,text="depense total",bg=couleursec,width=10,height=5,command=lambda :ch("depense"))
            bdepensetotal.pack(side=LEFT,padx=10)###crée bouton depense total
            frm.update_idletasks()
            cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height())) 
            def ch(choix):###quand on clique sur un bouton
                frameboutondep.destroy()
                bdepense.grid(row=0, column=1,padx=10)
                brecette.grid(row=0, column=2,padx=10)
                varhisto.set("L'historique de %s"%choix)###met a jour les variables
                numpy.save("ch.npy",choix)
                button1.pack()
                listbox.delete(0,END)###on vide la liste boxe
                scrollbar.pack_forget()###on efface la listbox
                listbox.pack_forget()
                buttontext.pack_forget()
                varprobleme.set("")
        def recherchehisto():###function recherche de l'historique
            varprobleme.set("")
            scrollbar.pack(side=RIGHT, fill=Y)
            listbox.pack()###met en place la listbox
            buttontext.pack()
            ch=numpy.load("ch.npy")### on recupere le choix
            listbox.delete(0,END)###on vide la liste boxe
            moischoix=t.get()###on recupere le mois
            t.set("")###on efface le entry
            anneechoix=t2.get()###on recupere l'annee
            t2.set("")###on efface le entry
            try:###on essaye de trouver historique
                if ch=="depense" or ch=="recette":
                    if ch=="depense":###si choix=depense
                        categorieini=numpy.load("categories/categorieini.npy")
                        categorieini=categorieini.tolist()###on importe la liste des categories
                        listbox.insert(END, "L'historique des depenses "+"du "+moischoix+"/"+anneechoix+" :")###on ecrit dans la listebox des indications sur l'historique demandé
                        for elt in categorieini:
                            listehistocatego=numpy.load("%s/historique/%s/%s%s.npy" % (anneechoix,moischoix,moischoix,elt))
                            listehistocatego=listehistocatego.tolist()
                            listbox.insert(END, elt+" :")###on ecrit la categorie
                            for commande,nb,date,provenance in listehistocatego:###puis on ecrit l'historique des categories
                                listbox.insert(END,("       "+"vous avez {} pour un montant de {} euros le {} provenance : {}. ".format(commande,nb,date,provenance)))
                        fichier = open( "histotext.txt", "w")###on ouvre le fichier texte
                        fichier.write("L'historique des depenses "+"du "+str(moischoix)+"/"+str(anneechoix)+" :"+"\n")###on ecrit dans le fichier des indications sur l'historique demandé
                        for elt in categorieini:
                            listehistocatego=numpy.load("%s/historique/%s/%s%s.npy" % (anneechoix,moischoix,moischoix,elt))
                            listehistocatego=listehistocatego.tolist()
                            fichier.write(str(elt)+" :"+"\n")###on ecrit la categorie
                            for commande,nb,date,provenance in listehistocatego:###puis on ecrit l'historique des categories
                                fichier.write("      "+"vous avez {} pour un montant de {} euros le {} provenance : {}. ".format(commande,nb,date,provenance)+"\n")
                        fichier.close()###on ferme le fichier
                    else:###si le choix est recette
                        choixhistorec=numpy.load("%s/historique/%s/%shistorec.npy" % (anneechoix,moischoix,moischoix))
                        choixhistorec=choixhistorec.tolist()###on importe l'historique des recettes
                        listbox.insert(END,"L'historique des recettes "+"du "+moischoix+"/"+anneechoix+" :")###on ecrit dans la listbox des indications sur l'historique demandé
                        for commande,nb,date,provenance in choixhistorec:###puis on ecrit l'historique des recettes
                           listbox.insert(END,("        "+"vous avez {} pour un montant de {} euros le {} provenance : {}. ".format(commande,nb,date,provenance)))
                        fichier = open( "histotext.txt", "w")###on ouvre le fichier texte
                        fichier.write("L'historique des recettes "+" du "+str(moischoix)+"/"+str(anneechoix)+" :"+"\n")###on ecrit dans le fichier des indications sur l'historique demandé
                        for commande,nb,date,provenance in choixhistorec:###puis on ecrit l'historique des recettes
                                fichier.write("      "+"vous avez {} pour un montant de {} euros le {} provenance : {}. ".format(commande,nb,date,provenance)+"\n")
                        fichier.close()
                else:###si le choix est une categorie
                    ch=str(ch)
                    listehistocatego=numpy.load("%s/historique/%s/%s%s.npy" % (anneechoix,moischoix,moischoix,ch))
                    listehistocatego=listehistocatego.tolist()###on importe l'historique de la categorie
                    listbox.insert(END, "L'historique "+ch+" du "+moischoix+"/"+anneechoix+" :")###on ecrit dans la listbox des indications sur l'historique demandé
                    for commande,nb,date,provenance in listehistocatego:###puis on ecrit l'historique de la categorie
                        listbox.insert(END,("       "+"vous avez {} pour un montant de {} euros le {} provenance :{}. ".format(commande,nb,date,provenance)))
                    fichier = open( "histotext.txt", "w")###on ouvre le fichier texte
                    fichier.write("L'historique des "+str(ch)+" du "+str(moischoix)+"/"+str(anneechoix)+" :"+"\n")###on ecrit dans le fichier des indications sur l'historique demandé
                    for commande,nb,date,provenance in listehistocatego:###puis on ecrit l'historique de la categorie
                            fichier.write("      "+"vous avez {} pour un montant de {} euros le {} provenance :{}. ".format(commande,nb,date,provenance)+"\n")
                    fichier.close()
                listbox.config(yscrollcommand=scrollbar.set)###on configure la listbox ainsi que la scrollbar
                scrollbar.config(command=listbox.yview)
            except:###si le chargement est impossible
                scrollbar.pack_forget()###on enleve la listbox
                listbox.pack_forget()
                varprobleme.set("probleme de chargement de l'historique")###on indique le probleme
                buttontext.pack_forget()
        def texte():###function texte
            os.startfile('histotext.txt')###on ouvre le fichier texte
        fichier = open( "histotext.txt", "w")###on initialise le fichier histotext
        fichier.close()
        framemenuprincipale.destroy()###detruit frame menu principale du lancement
        framechange=Frame(frameprincipale,bg=couleursec)###on cree une frame qui va contenir des widgets
        framechange.pack()
        labelpre=Label(framechange,bg=couleursec,text="choisissez l'historique")###on informe a l'utilisateur l'action a faire
        labelpre.pack(side=TOP,pady=10)
        framebouton=Frame(framechange,bg=couleursec)###cree une frame qui va contenir les boutons
        framebouton.pack(pady=20)
        bdepense=Button(framebouton,bg=couleursec,text="depense",height=5,width=20,command=dep)###on cree bouton depense
        bdepense.grid(row=0, column=1,padx=10)
        brecette=Button(framebouton,bg=couleursec,text="recette",height=5,width=20,command=rec)###on cree bouton recette
        brecette.grid(row=0, column=2,padx=10)
        bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principale",command=menu)###on cree bouton retour au menu principale
        bmenuprincipale.grid(row=0, column=0)
        framemodif=Frame(framechange,bg=couleursec)###on cree une frame qui va contenir des widgets
        framemodif.pack()
        varhisto = StringVar()
        labelchange=Label(framemodif,bg=couleursec,textvariable=varhisto)###on indique l'historique choisie par l'utilisateur
        labelchange.pack()
        varprobleme=StringVar()
        labelprobleme=Label(framemodif,bg=couleursec,textvariable=varprobleme)###label qui permet d'indiquer si il y a un probleme
        labelprobleme.pack()
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
        button1=Button(framemodif ,text="rechercher",command=recherchehisto)###le bouton qui appelle fonction recherche
        button1.pack_forget()
        framehisto=Frame(framechange,bg=couleursec)###frame qui contiend le resumé de l'historique
        framehisto.pack(pady=20)
        scrollbar = Scrollbar(framehisto)###initialise la liste box qui va contenir le resumé
        scrollbar.pack_forget()
        listbox = Listbox(framehisto,width=100)
        listbox.pack_forget()      
        buttontext=Button(framechange ,text="format text",command=texte)###bouton qui appelle la fonction text
        buttontext.pack_forget()
################################################################################################################################################
#######################################################parametre#########################################################################################
    def parametre():###fonction parametre
        def menu():###fonction appele pour le retour au menuprincipal
            framechange.destroy()###on detruit les frames
            bmenuprincipale.destroy()
            menuprincipale()###on appelle la fonction menuprincipal
    ################################################################################################################################################
    ################################################################################################################################################
        def reini():###fonction pour reinitialiser
            varinfo.set("choisissez la categories a reinitialiser")###on indique que doit faire l'utilisateur
            def retour():###permet le retour vers le menu des parametres
                framemodif.destroy()###on detruit la frame
                frameboutondep.destroy()
                breini.grid(row=0, column=1,padx=10)###on place les boutons du menu des parametres
                benlever.grid(row=0, column=2,padx=10)
                bgestioncatego.grid(row=0, column=3,padx=10)
            breini.grid_forget()###on enleve les boutons du menu parametre
            benlever.grid_forget()
            bgestioncatego.grid_forget()
            categorieini=numpy.load("categories/categorieini.npy")###on amene la liste des categories
            categorieini=categorieini.tolist()
            frameboutondep=Frame(framebouton,bg=couleursec)
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
            brecette=Button(frm,text="recette",bg=couleursec,height=5,width=10,command=lambda : ch("recette"))
            brecette.pack(side=LEFT,padx=10)
            frm.update_idletasks()
            cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height())) 
            framemodif=Frame(framechange,bg=couleursec)###on construit une frame pour contenir des widgets
            framemodif.pack()
            bretour=Button(framemodif,bg=couleursec,text="retour",command=retour)###cree bouton pour retourner au menu principal
            bretour.pack()
            def ch(choix):###la function est appele apres un clique sur un bouton
                frameboutondep.destroy()
                if choix=="recette":###si le choix=recette
                    recette=0
                    listerecette[moismod]=recette###on reinitialise la valeur recette
                    numpy.save("%s/%srecette.npy" % (anneetoday,anneetoday),listerecette)
                    listehistorec.append(["reinitialise les recettes","",datehisto,""])###on ajoute des informations a l'historique des recettes
                    numpy.save("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday),listehistorec)
                else:###si le choix est une categorie
                    catego=choix
                    chcategoparametre=numpy.load("categories/%s/%s%s.npy" % (catego,anneetoday,catego))#####on recupere la depense de cette categories
                    chcategoparametre=chcategoparametre.tolist()
                    enlevedep=chcategoparametre[moismod]
                    enlevedep=float(enlevedep)
                    chcategoparametre[moismod]=0###on reinitialise la valeur du mois correspondant a la categorie
                    listehistoparacatego=numpy.load("%s/historique/%s/%s%s.npy" % (anneetoday,moistoday,moistoday,catego))#####on recupere l'historique de la categories
                    listehistoparacatego=listehistoparacatego.tolist()
                    listehistoparacatego.append(["reinitialiqation des depenses","",datehisto,""])###on ajoute des informations a l'historique des categorie
                    numpy.save("%s/historique/%s/%s%s.npy" % (anneetoday,moistoday,moistoday,catego),listehistoparacatego)
                    numpy.save("categories/%s/%s%s.npy" % (catego,anneetoday,catego),chcategoparametre)
                    listedepense=numpy.load("%s/%sdepense.npy" % (anneetoday,anneetoday))###on recupere la valeur de la depense
                    listedepense=listedepense.tolist()
                    depense=listedepense[moismod]
                    depense=float(depense)
                    depense=depense-enlevedep###on enleve a la depense l'ancienne valeur de la categorie
                    listedepense[moismod]=depense
                    numpy.save("%s/%sdepense.npy" % (anneetoday,anneetoday),listedepense)###on enregistre la liste des depenses generales
                framemodif.destroy()###detruit la frame
                breini.grid(row=0, column=1,padx=10)###on place les boutons du menu parametre
                benlever.grid(row=0, column=2,padx=10)
                bgestioncatego.grid(row=0, column=3,padx=10)
    ################################################################################################################################################
    ################################################################################################################################################
        def enlever():###function pour enlever des valeurs
            def retour():###permet le retour vers le menu des parametres
                framemodif.destroy()###on detruit la frame
                frameboutondep.destroy()
                breini.grid(row=0, column=1,padx=10)###on place les boutons du menu des parametres
                benlever.grid(row=0, column=2,padx=10)
                bgestioncatego.grid(row=0, column=3,padx=10)
            varinfo.set("choisissez la categories a modifier")###on indique a l'utilisateur l'action a effectuer
            breini.grid_forget()###on eneleve les boutons du menu parametre
            benlever.grid_forget()
            bgestioncatego.grid_forget()
            boutonliste=[]
            categorieini=numpy.load("categories/categorieini.npy")
            categorieini=categorieini.tolist()###on recupere la liste des categorie
            frameboutondep=Frame(framebouton,bg=couleursec)
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
            brecette=Button(frm,text="recette",bg=couleursec,height=5,width=10,command=lambda : ch("recette"))
            brecette.pack(side=LEFT,padx=10)
            frm.update_idletasks()
            cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
            framemodif=Frame(framechange,bg=couleursec)###on construit une frame pour contenir des widgets
            framemodif.pack()
            bretour=Button(framemodif,bg=couleursec,text="retour",command=retour)###cree bouton pour retourner au menu principal
            bretour.pack()
            def ch(choix):###la function est appele apres un clique sur un bouton
                frameboutondep.destroy()
                bretour.destroy()
                varinfo.set("enlevez des valeurs")###on indique l'action a effectuer
                def ajoute():###fonction qui ajoute
                    varprobleme.set("")
                    a=t.get()###on rcupere la saisie
                    try:
                        a=float(a)###on transforme en float la saisie
                    except:
                        varprobleme.set("probleme ajout : valeur non detectée")###si cela est impossible on l'indique
                    if a<0:
                        varprobleme.set("probleme ajout : valeur negative")###si la valeur rentrée est negative alors on l'indique
                    if a>0:
                        try:
                            ajoutdep=a#####on verifie que la donnee saisie a maximum 2 decimales
                            ajoutdep1="%.2f"%ajoutdep
                            ajoutdep1=float(ajoutdep1)
                            ajoutdepverif=ajoutdep1-ajoutdep
                            if ajoutdepverif<0 or ajoutdepverif>0:
                                varprobleme.set("probleme ajout : plus de deux décimales")###si il y a plus de deux decimales on l'indique
                            if ajoutdepverif==0:#####sinon on ajoute la donnee saisie a la valeur depense recuperee si dessus 
                                ajout=numpy.load("ajout.npy")
                                ajout=ajout.tolist()
                                ajout.append(a)###on ajoute la saisie a la liste ajout
                                numpy.save("ajout.npy",ajout)
                                ajout=numpy.load("ajout.npy")
                                ajoutotal=numpy.sum(ajout)
                                ajout=ajout.tolist()###on met a jour les variables
                                varajout.set(ajout)
                                varajoutotal.set(ajoutotal)
                        except:
                            varprobleme.set("probleme ajout")###si cela n'est pas possbile on l'indique
                    t.set("")###on vide le entry
                def enregistrer():###fonction qui enregistre
                    ch=numpy.load("ch.npy")###on recupere le choix
                    if ch=="recette":###si le choix est recette
                        ajout=numpy.load("ajout.npy")
                        ajoutotal=numpy.sum(ajout)###on fait la somme des ajouts
                        listerecette=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))
                        listerecette=listerecette.tolist()
                        recette=listerecette[moismod]###on recupere la valeur recette
                        ajoutotal=float(ajoutotal)
                        recette=float(recette)
                        recette=recette-ajoutotal###on met a jour la valeur recette
                        if recette<0:###si celle-ci est inferieur a zero
                            varprobleme.set("probleme ajout : recette passe en negative")###on indique que c'est impossible d'enlever la valeur
                            varajout.set("")
                            varajoutotal.set("")
                        else:###sinon on enregistre la nouvelle recette
                            listerecette[moismod]=recette###on enregistre la recette
                            numpy.save("%s/%srecette.npy" % (anneetoday,anneetoday),listerecette)
                            listehistorec=numpy.load("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday))
                            listehistorec=listehistorec.tolist()
                            listehistorec.append(["enleve des recettes",ajoutotal,datehisto,""])###on ajoute a l'historique des informations
                            numpy.save("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday),listehistorec)###on enregistre l'historique
                            framemodif.destroy()###detruit la frame
                            breini.grid(row=0, column=1)###on met en place les boutons du menu parametre
                            benlever.grid(row=0, column=2)
                            bgestioncatego.grid(row=0, column=3)
                            bannee.grid(row=0, column=4)
                            varajout.set("")###on reinitialise les variables
                            varajoutotal.set("")
                    else:###si le choix est une categorie
                        ajout=numpy.load("ajout.npy")###on recupere le choix
                        ajoutotal=numpy.sum(ajout)###on fait la somme des ajouts
                        ajoutotal=float(ajoutotal)
                        catego=choix
                        chcategopara=numpy.load("categories/%s/%s%s.npy" % (catego,anneetoday,catego))
                        chcategopara=chcategopara.tolist()
                        depcatego=chcategopara[moismod]###on recupere la donnee de la categorie coorespondant au mois
                        depcatego=depcatego-ajoutotal###on enleve la valeur
                        if depcatego<0:###si celle-ci est inferieur a zero
                            varprobleme.set("probleme ajout : %s passe en negative"%catego)###on indique que c'est impossible d'enlever la valeur
                            varajout.set("")
                            varajoutotal.set("")
                        else:###sinon on enregistre la nouvelle valeur
                            chcategopara[moismod]=depcatego###on enregistre la valeur
                            numpy.save("categories/%s/%s%s.npy" % (catego,anneetoday,catego),chcategopara)
                            listehistoparacatego=numpy.load("%s/historique/%s/%s%s.npy" % (anneetoday,moistoday,moistoday,catego))#####on recupere l'historique de la categorie
                            listehistoparacatego=listehistoparacatego.tolist()
                            listehistoparacatego.append(["enlevée des depenses",ajoutotal,datehisto,""])###on ajoute a l'historique des informations
                            numpy.save("%s/historique/%s/%s%s.npy" % (anneetoday,moistoday,moistoday,catego),listehistoparacatego)###on enregistre l'historique
                            listedepense=numpy.load("%s/%sdepense.npy" % (anneetoday,anneetoday))
                            listedepense=listedepense.tolist()
                            depense=listedepense[moismod]###on recupere la valeur de la depense
                            depense=float(depense)
                            depense=depense-ajoutotal###on enleve le total des ajouts a la depense
                            listedepense[moismod]=depense
                            numpy.save("%s/%sdepense.npy" % (anneetoday,anneetoday),listedepense)###on sauvegarde la liste depense
                            framemodif.destroy()###detruit la frame
                            breini.grid(row=0, column=1)###on met en place les boutons du menu parametre
                            benlever.grid(row=0, column=2)
                            bgestioncatego.grid(row=0, column=3)
                            varajout.set("")###on reinitialise les variables
                            varajoutotal.set("")
                def retour():###permet le retour vers le menu des parametres
                    framemodif.destroy()###on detruit la frame
                    breini.grid(row=0, column=1,padx=10)###on place les boutons du menu des parametres
                    benlever.grid(row=0, column=2,padx=10)
                    bgestioncatego.grid(row=0, column=3,padx=10)
                numpy.save("ch.npy",choix)###on recupere le choix
                framemodif=Frame(framechange,bg=couleursec)###on construit une frame qui va contenir les widgets
                framemodif.pack()
                varajout=StringVar()
                varajoutotal=StringVar()
                ajout=[]
                numpy.save("ajout.npy",ajout)###on initialise la liste ajout
                iframeajout = Frame(framemodif, bd=2, relief=RIDGE)
                labelinfo=Label(framemodif,bg=couleursec,text=("modifier %s"%choix))###on indique la categorie a modifier
                labelinfo.pack()
                Label(iframeajout, text='entrer la somme a enlever :').pack(side=LEFT, padx=5)###label qui indique ce que doit faire l'utilisateur
                t = StringVar()###on indique la variable qui va prendre la valeur de ce que va rentrer l'utilisateur
                Button(iframeajout,text="enlever",command=ajoute).pack(side=RIGHT,padx=5)###bouton qui accede a la fonction ajouter
                Entry(iframeajout, textvariable=t, bg='white').pack(side=LEFT, padx=5)###on place la case qui permet a l'utilisateur d'ecrire
                iframeajout.pack(expand=1, fill=X, pady=10, padx=5)
                varprobleme=StringVar()
                labelprobleme=Label(iframeajout,textvariable=varprobleme)###permet d'indiquer a l'utilisateur un probleme
                labelprobleme.pack()
                iframeresume = Frame(framemodif, bd=2, relief=RIDGE)###cree la frame resume
                labelajoutres=Label(iframeresume,text="resume de vos saisies :")###indique a quoi correspond la variable 
                labelajoutres.grid(row=0, column=0)
                labelajout=Label(iframeresume,textvariable=varajout)###indique les saisies de l'utilisateur
                labelajout.grid(row=0, column=1)
                labelajoutres=Label(iframeresume,text="total de vos saisies :")###indique a quoi correspond la variable 
                labelajoutres.grid(row=1, column=0)
                labelajout1=Label(iframeresume,textvariable=varajoutotal)###indique le total des saisies
                labelajout1.grid(row=1, column=1)
                iframeresume.pack(expand=1, fill=X, pady=10, padx=5)
                benregistrer=Button(framemodif,text="enregistrer",command=enregistrer)###permet d'enregistrer
                benregistrer.pack()
                bretour1=Button(framemodif,bg=couleursec,text="retour",command=retour)###bouton qui permet de retourner au menu parametre
                bretour1.pack(pady=10)
    ################################################################################################################################################
    ################################################################################################################################################
        def gestioncatego():###fonction qui permet la gestion des categories
            breini.grid_forget()###on enleve les boutons du menu parametre
            benlever.grid_forget()
            bgestioncatego.grid_forget()
            def retour():###la fonction permet le retour au menu parametre
                framemodif.destroy()###on detruit la frame
                framebouton2.destroy()
                breini.grid(row=0, column=1,padx=10)###on place les boutons du menu des parametres
                benlever.grid(row=0, column=2,padx=10)
                bgestioncatego.grid(row=0, column=3,padx=10)
            def ajoutcatego():###fonction qui permet l'ajout de categorie
                varinfo.set("")
                varinfo.set("voici les categories qui existe")###on indique a l'utilisateur des informations
                bretour.pack_forget()###on enleve les boutons 
                bajoutcatego.pack_forget()
                benlevecatego.pack_forget()
                categorieini=numpy.load("categories/categorieini.npy")###on amene la liste des categories
                categorieini=categorieini.tolist()
                frameboutondep=Frame(framebouton,bg=couleursec)
                frameboutondep.grid()
                cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
                cnv.grid(row=0, column=0)
                hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
                hScroll.grid(row=1, column=0, sticky='we')
                cnv.configure(xscrollcommand=hScroll.set)
                frm = Frame(cnv,bg=couleurfrm)
                cnv.create_window(0, 0, window=frm, anchor='nw')
                for categor in categorieini:###cree bouton de la liste des categorie
                    c=Button(frm,text=categor,bg=couleursec,width=10,height=5)
                    c.pack(side=LEFT,padx=10)###plac
                frm.update_idletasks()
                cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))             
                def ajoute():###fonction qui permet ajout de la categorie
                    frameboutondep.destroy()
                    categorie=numpy.load("categories/categorieliste.npy")
                    categorie=categorie.tolist()###charge la liste des categories
                    categorieini=numpy.load("categories/categorieini.npy")
                    categorieini=categorieini.tolist()###charge une deuxieme liste
                    newcategorie=t.get()###permet de recuperer la saisie de l'utilisateur
                    verifcate="%s"%newcategorie
                    lim=0
                    for element in categorieini:
                        lim=lim+1###on regarde combien il y a de categorie
                    if lim>=31:###il y a une limite de 22 categorie
                        varprobleme.set("impossible d'ajouter categorie %s limite atteinte"%newcategorie)###si il y a 22 categorie on indique l'impossibilité d'ajouter une autre categorie
                    else:
                        possible=1
                        for element in categorieini:
                            if element==verifcate:###on verifie que la categorie n'existe pas
                                possible=0
                        if possible==1:###sinon on ajoute la categorie
                            try:
                                newcategorie="cnn"
                                categori=["aa","ccaa","ctp","nn","tt"]
                                newliste=[]
                                accept=0
                                for element in categori:
                                    if element<newcategorie:
                                        newliste.append(element)
                                    if element>newcategorie:
                                        if accept==0:
                                            newliste.append(newcategorie)
                                            accept=1
                                        newliste.append(element)  
                                categorieini.append(newcategorie)###on ajoute la categorie dans la liste
                                categorienewliste={}
                                i=1
                                for  mot in categorieini:
                                    categorienewliste[mot]=i
                                    i=i+1                   
                                numpy.save("categories/categorieliste.npy",categorienewliste)###on sauvegarde les nouvelles listes
                                numpy.save("categories/categorieini.npy",categorieini)
                                os.mkdir("categories/%s" % newcategorie)###on cree dossier de la nouvelle categorie
                                a=[0,0,0,0,0,0,0,0,0,0,0,0]
                                b=[]
                                newhisto=["01","02","03","04","05","06","07","08","09","10","11","12"]
                                numpy.save("categories/%s/%s%s.npy"%(newcategorie,anneetoday,newcategorie),a)###on sauvegarde la liste pour les depenses de la categorie
                                for elt in newhisto:
                                    numpy.save("%s/historique/%s/%s%s.npy" % (anneetoday,elt,elt,newcategorie),b)###on ajoute les listes pour gerer l'historique
                            except:
                                varprobleme.set("impossible d'ajouter la categorie %s"%newcategorie)###si cela est impossible on l'indique
                        else:
                            varprobleme.set("impossible d'ajouter une categorie qui existe deja")###si la categorie existe on l'indique
                    retour()###appelle la fonction retour au menu parametre
                iframeajout = Frame(framemodif, bd=2, relief=RIDGE)###on cree une frame qui permet l'ajout de la categorie
                Label(iframeajout, text='entrer le nom de la categorie :').pack(side=LEFT, padx=5)###label qui indique ce que doit faire l'utilisateur
                t = StringVar()###on indique la variable qui va prendre la valeur de ce que va rentrer l'utilisateur
                Entry(iframeajout, textvariable=t, bg='white').pack(side=LEFT, padx=5)###on place la case qui permet a l'utilisateur d'ecrire
                Button(iframeajout,text="ajouter",command=ajoute).pack(side=RIGHT,padx=5)###on cree le bouton qui permet l'ajout de la categorie
                iframeajout.pack(expand=1, fill=X, pady=10, padx=5)
            def enlevecatego():###fonction qui permet d'enlever une categorie
                varinfo.set("")
                varinfo.set("quel categorie souhaitez-vous enlever")###on indique l'action a effectuer
                bretour.pack_forget()###on enleve les boutons 
                bajoutcatego.pack_forget()
                benlevecatego.pack_forget()
                categorieini=numpy.load("categories/categorieini.npy")###on amene la liste des categories
                categorieini=categorieini.tolist()
                frameboutondep=Frame(framebouton,bg=couleursec)
                frameboutondep.grid()
                cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
                cnv.grid(row=0, column=0)
                hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
                hScroll.grid(row=1, column=0, sticky='we')
                cnv.configure(xscrollcommand=hScroll.set)
                frm = Frame(cnv,bg=couleurfrm)
                cnv.create_window(0, 0, window=frm, anchor='nw')
                for categor in categorieini:###cree bouton de la liste des categorie
                    c=Button(frm,text=categor,bg=couleursec,width=10,height=5,command=lambda i=categor:ch(i))
                    c.pack(side=LEFT,padx=10)###plac
                frm.update_idletasks()
                cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))
                def ch(choix):###quand on clique sur un bouton on appelle cette fonction
                    frameboutondep.destroy()
                    categorie=numpy.load("categories/categorieliste.npy")
                    categorie=categorie.tolist()###on charge les listes
                    categorieini=numpy.load("categories/categorieini.npy")
                    categorieini=categorieini.tolist()
                    catego=choix
                    chcate=0
                    chcate=categorie[catego]###on recupere le placement dans la liste de la categorie
                    chcate=chcate-1
                    del categorie[catego]###on enleve cette categorie de la liste
                    del categorieini[chcate]
                    categorienewliste={}
                    i=1
                    for  mot in categorieini:
                        categorienewliste[mot]=i
                        i=i+1
                    numpy.save("categories/categorieliste.npy",categorienewliste)###on sauvegarde une nouvelle liste de categorie
                    numpy.save("categories/categorieini.npy",categorieini)
                    os.remove("categories/%s/%s%s.npy"%(catego,anneetoday,catego))
                    os.rmdir("categories/%s"%catego)###on supprime les donnees de la categories
                    newhisto=["01","02","03","04","05","06","07","08","09","10","11","12"]
                    for elt in newhisto:###on supprime l'historique de la categorie
                        os.remove("%s/historique/%s/%s%s.npy"%(anneetoday,elt,elt,catego))
                    retour()###on appelle la fonction retour au menu parametre
            varprobleme.set("")
            varinfo.set("choisissez le parametre des categories")###on indique l'action a effectuer
            framebouton2=Frame(framechange,bg=couleursec)###on cree la frame pour contenir des widgets
            framebouton2.pack()
            framemodif=Frame(framechange,bg=couleursec)###on cree la frame pour contenir des widgets
            framemodif.pack()
            bajoutcatego=Button(framebouton2,bg=couleursec,text="ajouter categorie",height=5,width=20,command=ajoutcatego)###on cree bouton ajouter categorie
            bajoutcatego.pack(side=RIGHT,padx=10,pady=10)
            benlevecatego=Button(framebouton2,bg=couleursec,text="enlever categorie",height=5,width=20,command=enlevecatego)###on cree bouton enlever categorie
            benlevecatego.pack(side=RIGHT,padx=10)
            bretour=Button(framemodif,bg=couleursec,text="retour",command=retour)###on cree le bouton qui permet le retour au menu parametre 
            bretour.pack()
        couleurfrm="#99512B"
        framemenuprincipale.destroy()###detruit frame menu principale du lancement
        framechange=Frame(frameprincipale,bg=couleursec)###on construit une frame pour contenir des widgets
        framechange.pack()
        varinfo=StringVar()
        varinfo.set("choisir les parametres")###on indique l'action a effectuer
        labelpre=Label(framechange,bg=couleursec,textvariable=varinfo)
        labelpre.pack(side=TOP,pady=10)
        framebouton=Frame(framechange,bg=couleursec)###on cree la frame bouton pour contenir des boutons
        framebouton.pack(pady=35)
        breini=Button(framebouton,text="reinitialiser",bg=couleursec,height=5,width=20,command=reini)###cree bouton reinitialiser
        breini.grid(row=0, column=1,padx=10)
        benlever=Button(framebouton,text="enlever des valeurs",bg=couleursec,height=5,width=20,command=enlever)### cree bouton enlever des valeurs
        benlever.grid(row=0, column=2,padx=10)
        bgestioncatego=Button(framebouton,text="gestion des categories",bg=couleursec,height=5,width=20,command=gestioncatego)###cree bouton pour la gestion des categories
        bgestioncatego.grid(row=0, column=3,padx=10)
        bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principale",command=menu)###cree le bouton pour revenir au menu principal
        bmenuprincipale.grid(row=0, column=0)
        varprobleme=StringVar()
        labelprobleme=Label(framechange,textvariable=varprobleme,bg=couleursec)###permet d'indiquer les problemes
        labelprobleme.pack()
###############################################voir evolution dans l'annee#################################################################################################
    def annee():###fonction appelé pour voir evolution dans l'annee
        def menu():###fonction appele pour le retour au menuprincipal
            framechange.destroy()###on detruit les frames
            bmenuprincipale.destroy()
            menuprincipale()###on appelle la fonction menuprincipal
        def compareannee():
            date=t.get()
            t.set("")
            listbox2.delete(0,END)###on vide la liste boxe
            scrollbar2.pack(side=RIGHT, fill=Y)
            listbox2.pack()###met en place la listbox pour la comparaison
            try:
                for elt in categorieini:###pour chaque categorie dans la liste
                    listecatego=numpy.load("categories/%s/%s%s.npy" % (elt,date,elt))
                    categorietotal2=numpy.sum(listecatego)###on fait la somme des depenses de l'annee que l'utilisateur a choisie
                    categorietotal2=float(categorietotal2)
                    listecatego=numpy.load("categories/%s/%s%s.npy" % (elt,anneetoday,elt))
                    categorietotal=numpy.sum(listecatego)###on fait la somme des depenses de l'annee
                    categorietotal=float(categorietotal)
                    difference=categorietotal-categorietotal2###on fait la difference
                    try:
                        pourcentage=((categorietotal-categorietotal2)/categorietotal2*100)###on calcule le pourcentage de difference
                        pourcentage="%.2f"%pourcentage
                        pourcentage=float(pourcentage)
                    except:
                        pourcentage=" : impossible de donner un pourcentage"
                    if difference==0:###selon la difference on indique a l'utilisateur une comparaison
                        text="Soit la meme depense que l'annee derniere"
                        color="white"
                    if difference>0:
                        text="Soit une augmentation de %s pourcent"%pourcentage
                        color="red"
                    if difference<0:
                        pourcentage=abs(pourcentage)                        
                        text="Soit une diminution de %s pourcent"%pourcentage
                        color="green"
                    listbox2.insert(END,"-----------------") 
                    listbox2.insert(END,"vous avez depense en %s dans la categorie %s %s euros. %s"%(date,elt,categorietotal2,text))###on inscrit dans la liste box la comparaison
                    listbox2.itemconfig(END, {'bg':color}) 
                listerecette2=numpy.load("%s/%srecette.npy" % (date,date))###on importe les depenses et recettes de l'annee comparée
                listedepense2=numpy.load("%s/%sdepense.npy" % (date,date))
                depensetotal2=numpy.sum(listedepense2)###on en fait la somme
                recettetotal2=numpy.sum(listerecette2)
                recettetotal2=float(recettetotal2)
                depensetotal2=float(depensetotal2)
                listbox2.insert(END,"---------------------------------------------")
                difference=depensetotal-depensetotal2###on calcule la difference entre les recettes
                try:
                    pourcentage=((dpensetotal-depensetotal2)/depensetotal2*100)###on calcule le pourcentage de difference
                    pourcentage="%.2f"%pourcentage
                    pourcentage=float(pourcentage)
                except:
                    pourcentage=" : impossible de donner un pourcentage"
                if difference==0:###selon la difference on indique a l'utilisateur une comparaison
                    text="Soit la meme depense que l'annee derniere"
                    color="white"###on determine une couleur pour le fond
                if difference>0:
                    text="Soit une augmentation de %s pourcent"%pourcentage
                    color="red"
                if difference<0:
                    pourcentage=abs(pourcentage)                        
                    text="Soit une diminution de %s pourcent"%pourcentage
                    color="green"
                listbox2.insert(END,"vous avez depense en %s %s euros. %s"%(date,depensetotal2,text))###on inscrit dans la liste box la comparaison
                listbox2.itemconfig(END, {'bg':color}) ###on fixe un fond de couleur
                listbox2.insert(END,"-----------------") 
                try:
                    pourcentage=(recettetotal-recettetotal2)/recettetotal2*100###on calcule la difference entre les depenses
                    pourcentage="%.2f"%pourcentage
                    pourcentage=float(pourcentage)
                except:
                    pourcentage=" : impossible de donner un pourcentage"
                if difference==0:###selon la difference on indique a l'utilisateur une comparaison
                    text="Soit la meme depense que l'annee derniere"
                    color="white"
                if difference>0:
                    text="Soit une augmentation de %s pourcent"%pourcentage
                    color="green"
                if difference<0:
                    pourcentage=abs(pourcentage)                        
                    text="Soit une diminution de %s pourcent"%pourcentage
                    color="red"
                listbox2.insert(END,"vous avez gagne en %s %s euros. %s"%(date,recettetotal2,text))###on inscrit dans la liste box la comparaison
                listbox2.itemconfig(END, {'bg':color})
            except:
                listbox2.insert(END,"impossible d'importer les donnees de l'annee %s"%(date))###on indique a l'utilisateur que c'est impossible a comparer
            listbox2.config(yscrollcommand=scrollbar2.set)###on configure la listbox ainsi que la scrollbar
            scrollbar2.config(command=listbox2.yview)
        listerecette=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))###on importe les recettes et depenses de cette annee
        listedepense=numpy.load("%s/%sdepense.npy" % (anneetoday,anneetoday))
        depensetotal=numpy.sum(listedepense)###on en fait la somme
        depensetotal=float(depensetotal)
        recettetotal=numpy.sum(listerecette)
        recettetotal=float(recettetotal)
        framemenuprincipale.destroy()
        framechange=Frame(frameprincipale,bg=couleursec)###on cree une frame pour contenir les widgets
        framechange.pack()
        frameanneetoday=Frame(framechange,bg=couleursec)###on cree une frame pour contenir les widgets
        frameanneetoday.pack()
        scrollbar = Scrollbar(frameanneetoday)###on cree une listebox pour contenir les informations
        listbox = Listbox(frameanneetoday,width=100,height=15)
        scrollbar.pack(side=RIGHT, fill=Y,pady=10)
        listbox.pack(pady=10)
        bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principale",command=menu)###cree le bouton pour revenir au menu principal
        bmenuprincipale.grid(row=0, column=0)
        categorieini=numpy.load("categories/categorieini.npy")
        categorieini=categorieini.tolist()###on charge la listes des categories
        for elt in categorieini:###pour chaque categories dans la liste
            listecatego=numpy.load("categories/%s/%s%s.npy" % (elt,anneetoday,elt))
            categorietotal=numpy.sum(listecatego)###on fait la somme des depenses dans l'annee
            listbox.insert(END,"-----------------")
            listbox.insert(END,"vous avez depense en %s dans la categorie %s %s euros"%(anneetoday,elt,categorietotal))###on inscrit les informations
        listbox.insert(END,"---------------------------------------------")
        listbox.insert(END,"vous avez depense en %s %s euros"%(anneetoday,depensetotal))###on inscrit les depenses totales
        listbox.insert(END,"-----------------")
        listbox.insert(END,"vous avez gagne en %s %s euros"%(anneetoday,recettetotal))###on inscrit les recetets
        listbox.config(yscrollcommand=scrollbar.set)###on configure la listbox ainsi que la scrollbar
        scrollbar.config(command=listbox.yview)
        iframeajout = Frame(framechange, bd=2, relief=RIDGE)###on cree une frame qui permet l'ajout de la categorie
        Label(iframeajout, text='entrer la date a comparer  :').pack(side=LEFT, padx=5)###label qui indique ce que doit faire l'utilisateur
        t = StringVar()###on indique la variable qui va prendre la valeur de ce que va rentrer l'utilisateur
        Entry(iframeajout, textvariable=t, bg='white').pack(side=LEFT, padx=5)###on place la case qui permet a l'utilisateur d'ecrire
        Button(iframeajout,text="comparer",command=compareannee).pack(side=RIGHT,padx=10)###on cree le bouton qui permet l'ajout de la categorie
        iframeajout.pack(expand=1, fill=X, pady=10, padx=5)
        framerecherche=Frame(framechange,bg=couleursec)
        framerecherche.pack()
        scrollbar2 = Scrollbar(framerecherche,bg=couleursec)###on cree la frame qui va contenir la listebox de l'annee recherchée
        listbox2 = Listbox(framerecherche,width=100,height=15)
        scrollbar2.pack_forget() 
        listbox2.pack_forget()### on affiche pas tout de suite la listebox2
##############################################retour menu principale##################################################################################################
    def menuprincipale():
        def gosolde():###commande qui permet d'acceder au menu solde
            framemenuprincipale.destroy()###detruit la frame menu principal
            sold()###appelle la fonction sold
        def gographiques():###commande qui permet d'acceder au menu graphique
            framemenuprincipale.destroy()
            graphiques()###appelle la fonction graphiques
        def gohisto():###commande qui permet d'acceder au menu historique
            framemenuprincipale.destroy()
            histo()###appelle la fonction histo
        def goparametre():###commande qui permet d'acceder au menu parametre
            framemenuprincipale.destroy()
            parametre()###appelle la fonction parametre
        def goannee():
            framemenuprincipale.destroy()
            annee()###appelle la fonction annee          
        listerecette=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))
        listerecette=listerecette.tolist()
        recette=listerecette[moismod]
        recette=float(recette)### met a jout les recettes
        listedepense=numpy.load("%s/%sdepense.npy" % (anneetoday,anneetoday))
        listedepense=listedepense.tolist()
        depense=listedepense[moismod]
        depense=float(depense)### met a jour les depenses
        framemenuprincipale=Frame(frameprincipale,bg=couleursec)###frame du menu principal
        framemenuprincipale.pack(pady=150)
        solde=recette-depense
        labelpres=Label(framemenuprincipale,bg=couleursec,text=("nous sommes le %s vous avez depense %s euro vos recettes de ce mois ci sont de %s euros il vous reste donc %s euros"%(date,depense,recette,solde)))
        labelpres.pack(side=TOP,pady=20)###label qui indique a l'utilisateur ses depenses recettes
        bgraphique = Button(framemenuprincipale,bg=couleursec, text="graphique",height=10,width=20,command=gographiques)
        bgraphique.pack(side=LEFT,padx=10,pady=10)###cree bouton graphique
        bsolde = Button(framemenuprincipale,bg=couleursec, text="solde",height=10,width=20,command=gosolde)
        bsolde.pack(side=LEFT,padx=10)### cree bouton solde
        bannee= Button(framemenuprincipale,bg=couleursec, text="information sur l'annee",height=10,width=20,command=goannee)
        bannee .pack(side=RIGHT,padx=10)### cree bouton parametre 
        bhistorique = Button(framemenuprincipale,bg=couleursec, text="historique",height=10,width=20,command=gohisto)
        bhistorique.pack(side=RIGHT,padx=10)### cree bouton historique
        bparametre = Button(framemenuprincipale,bg=couleursec, text="parametre ",height=10,width=20,command=goparametre)
        bparametre.pack(side=RIGHT)### cree bouton parametre
################################################################################################################################################
##############################################Fenetre##################################################################################################
    root = Tk()###on indique que root est une fenetre
    root.resizable(False, False)###on peut pas modifier la taille de la fenetre
    couleurprin="#DEB887"
    couleursec="#FEFEE0"
    frameprincipale = Frame(root,width=1000,height=600,bg=couleurprin)###on cree une frame 1000*600 (taille de la fenetre)
    frameprincipale.pack()
    frameprincipale.pack_propagate(0)### taille de la frame fixe
    framemenuprincipale=Frame(frameprincipale,bg=couleursec)###frame du menu principale
    framemenuprincipale.pack(pady=150)###marge autour de la frame en y
    solde=recette-depense
    labelpres=Label(framemenuprincipale,bg=couleursec,text=("nous sommes le %s vous avez depense %s euro vos recettes de ce mois ci sont de %s euros il vous reste donc %s euros"%(date,depense,recette,solde)))
    labelpres.pack(side=TOP,pady=20)###label qui indique a l'utilisateur ses depenses recettes
    bgraphique = Button(framemenuprincipale,bg=couleursec, text="graphique",height=10,width=20,command=graphiques)
    bgraphique.pack(side=LEFT,padx=10,pady=10)###cree bouton graphique
    bsolde = Button(framemenuprincipale,bg=couleursec, text="solde",height=10,width=20,command=sold)
    bsolde.pack(side=LEFT,padx=10)### cree bouton solde
    bannee= Button(framemenuprincipale,bg=couleursec, text="information sur l'annee",height=10,width=20,command=annee)
    bannee .pack(side=RIGHT,padx=10)### cree bouton parametre 
    bhistorique = Button(framemenuprincipale,bg=couleursec, text="historique",height=10,width=20,command=histo)
    bhistorique.pack(side=RIGHT,padx=10)### cree bouton historique
    bparametre = Button(framemenuprincipale,bg=couleursec, text="parametre ",height=10,width=20,command=parametre)
    bparametre .pack(side=RIGHT,padx=10)### cree bouton parametre   
    framegoprincipale=Frame(frameprincipale,bg=couleurprin)
    framegoprincipale.pack(side=BOTTOM)###frame qui permet de contenir le bouton : revenir au menu principal
    root.mainloop()### cree boucle
    ################################################################################################################################################
    ################################################################################################################################################
    ##################################################quand on change de mois ou/et d'annee##############################################################################################
else:
    if anneew==anneetoday:######dans la cas ou c'est le debut du mois
        mon_fichier = open("mois.txt", "w")######on enregistre le nouveau mois dans le fichier
        mon_fichier.write(moistoday)
        mon_fichier.close()
        def solde():###fonction permet de mettre a jour les soldes
            listerecette=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))###on importe les recettes
            listerecette=listerecette.tolist()
            recettenew=listerecette[moismod1]
            listedepense=numpy.load("%s/%sdepense.npy" %(anneetoday,anneetoday))###on importe les depenses
            listedepense=listedepense.tolist()
            newdepense=listedepense[moismod1]
            solde=recettenew-newdepense
            soldenew=numpy.load("%s/%ssolde.npy" % (anneetoday,anneetoday))###on importe les soldes
            soldenew[moismod1]=solde
            numpy.save("%s/%ssolde.npy" % (anneetoday,anneetoday),soldenew)###on enregistre la mise a jour
        moismod=int(moistoday)
        moismod1=moismod-1
        moismod2=moismod1-1###cela permet de lire la bonne case de la liste
        moisliste=["01","02","03","04","05","06","07","08","09","10","11","12"]
        moishisto=moisliste[moismod1]
        root=Tk()
        frameprincipale = Frame(root,width=1000,height=600,bg="brown")###on cree une frame pour contenir des widgets
        frameprincipale.pack()
        frameprincipale.pack_propagate(0)
        frameinfo=Frame(frameprincipale)###on cree une frame pour contenir des widgets
        frameinfo.pack()
        labelinfo=Label(frameinfo,text="c'est un nouveau mois qui commence \n mise a jour des donnees \n cliquez sur les boutons ou vous voulez conserver les donnees ")###on informe l'utilisateur des actions a effectuer
        labelinfo.pack()
        categorieini=numpy.load("categories/categorieini.npy")
        categorieini=categorieini.tolist()###on recupere la liste des categories
        boutonliste=[]
        n=0
        n2=0
        for categor in categorieini:
            c=Button(frameinfo,text=(categor),height=5,width=10)
            c.grid(row=n2, column=n)###on cree les boutons des categories
            if n<11:
                n=n+1
            if n>=11:
                n=0
                n2=n2+1
            boutonliste.append(c)
        brecette=Button(frameinfo,text="recette",height=5,width=9,command=lambda :ch("recette"))###on cree le bouton pour la recette
        brecette.pack(side=RIGHT)
        def ch(choix):###après un clique on appelle cette fonction
            if choix=="recette":
                listerecette=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))
                listerecette=listerecette.tolist()
                recettenew=listerecette[moismod2]###on recupere la valeur de la recette du mois dernier
                recettenew=float(recettenew)
                listerecette[moismod1]=recettenew###on ajoute a la valeur recette de ce mois la recette du mois dernier
                numpy.save("%s/%srecette.npy" % (anneetoday,anneetoday),listerecette)
                listehistorec=numpy.load("%s/historique/%s/%shistorec.npy" %(anneetoday,moishisto,moishisto))
                listehistorec=listehistorec.tolist()
                listehistorec.append(["conserve les recettes",recettenew,"",""])###on ajoute des informations dans l'historique
                numpy.save("%s/historique/%s/%shistorec.npy" %(anneetoday,moishisto,moishisto),listehistorec)
                solde()
            else:###si il clique sur une categorie
                newdepense=0
                catego=choix
                listecatego=numpy.load("categories/%s/%s%s.npy" % (catego,anneetoday,catego))
                listecatego=listecatego.tolist()
                depensecatego=listecatego[moismod2]###on recupere la valeur de la depense du dernier mois
                depensecatego=float(depensecatego)
                newdepense=newdepense+depensecatego###on ajoute a la valeur de la depense de ce mois ci la depense du mois dernier
                listecatego[moismod1]=depensecatego
                numpy.save("categories/%s/%s%s.npy" % (catego,anneetoday,catego),listecatego)
                listedepense=numpy.load("%s/%sdepense.npy" %(anneetoday,anneetoday))
                listedepense[moismod1]=newdepense###on ajoute a la depense generale la depense de la categorie
                numpy.save("%s/%sdepense.npy" %(anneetoday,anneetoday),listedepense)
                listehisto=numpy.load("%s/historique/%s/%s%s.npy" %(anneetoday,moishisto,moishisto,catego))
                listehisto=listehisto.tolist()
                listehisto.append(["conserve les depenses",depensecatego,"",""])###on ajoute des informations dans l'historique
                numpy.save("%s/historique/%s/%s%s.npy" %(anneetoday,moishisto,moishisto,catego),listehisto)
                solde()###on appelle la fonction mise a jour des soldes
        root.mainloop()
    else :######dans le cas ou c'est une nouvelle annee
        def solde():###cette fonction permet la mise a jour de la solde
            listerecette2=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))
            listerecette2=listerecette2.tolist()
            recettenew=listerecette2[0]###on importe la recette de cette annee
            listedepense=numpy.load("%s/%sdepense.npy" %(anneetoday,anneetoday))
            listedepense=listedepense.tolist()
            newdepense=listedepense[0]###on importe la depense de cette annee
            soldenew=numpy.load("%s/%ssolde.npy" % (anneetoday,anneetoday))
            soldenew=soldenew.tolist()
            solde=recettenew-newdepense###on met a jour la solde
            soldenew[0]=solde
            numpy.save("%s/%ssolde.npy" % (anneetoday,anneetoday),soldenew)
        root=Tk()
        frameprincipale = Frame(root,width=1000,height=600,bg="brown")###on cree une frame pour contenir des widgets
        frameprincipale.pack()
        frameprincipale.pack_propagate(0)
        frameinfo=Frame(frameprincipale)###on cree une frame pour contenir des widgets
        frameinfo.pack()
        labelinfo=Label(frameinfo,text="c'est une nouvelle annee qui demarre \n mise a jour des donnees \n cliquez sur les boutons ou vous voulez conserver les donnees ")
        labelinfo.pack()
        newliste=[0,0,0,0,0,0,0,0,0,0,0,0]
        newdate=[1,2,3,4,5,6,7,8,9,10,11,12]
        numpy.save("%s/date.npy" % anneetoday,newdate)######on cree de nouveaux fichiers de sauvegarde des donnees
        numpy.save("%s/%srecette.npy" % (anneetoday,anneetoday),newliste)
        numpy.save("%s/%sdepense.npy" % (anneetoday,anneetoday),newliste)
        numpy.save("%s/%ssolde.npy" % (anneetoday,anneetoday),newliste)
        mon_fichier = open("mois.txt", "w")###on ecrit dans les fichier annee et mois la date actuel
        mon_fichier.write(moistoday)
        mon_fichier.close()
        mon_fichier = open("annee.txt", "w")
        mon_fichier.write(anneetoday)
        mon_fichier.close()
        listezero=[]
        newhisto=["01","02","03","04","05","06","07","08","09","10","11","12"]
        categorieini=numpy.load("categories/categorieini.npy")
        categorieini=categorieini.tolist()###on recupere la liste des categories
        newcategorie=[0,0,0,0,0,0,0,0,0,0,0,0]
        os.mkdir("%s/historique" % anneetoday)######creation de dossiers et fichiers
        for elt in newhisto:
            os.mkdir("%s/historique/%s" % (anneetoday,elt))
        for elt in newhisto:
            numpy.save("%s/historique/%s/%shistorec.npy" % (anneetoday,elt,elt),listezero)###creation de la liste historique pour les recettes
        for elt in newhisto:
            for nb in categorieini:
                numpy.save("%s/historique/%s/%s%s.npy" % (anneetoday,elt,elt,nb),listezero)###creaion de l'historique pour les categories
        for mot in categorieini:
            numpy.save("categories/%s/%s%s.npy" % (mot,anneetoday,mot),newcategorie)
        boutonliste=[]
        n=0
        n2=0
        for categor in categorieini:
            c=Button(frameinfo,text=(categor),height=5,width=10)
            c.grid(row=n2, column=n)###on cree les boutons des categories
            if n<11:
                n=n+1
            if n>=11:
                n=0
                n2=n2+1
            boutonliste.append(c)
        brecette=Button(frameinfo,text="recette",height=5,width=9,command=lambda :ch("recette"))
        brecette.grid(row=n2, column=n)
        def ch(choix):###après un clique on appelle cette fonction
            if choix=="recette":###si l'utilisateur clique sur le bouton recette
                listerecette=numpy.load("%s/%srecette.npy" % (anneew,anneew))
                listerecette=listerecette.tolist()
                recettenew=listerecette[11]
                recettenew=float(recettenew)###on recupere la valeur de la recette du dernier mois
                listerecette2=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))
                listerecette2=listerecette2.tolist()
                listerecette2[0]=recettenew###on ajoute a la valeur recette de ce mois la recette du mois dernier
                numpy.save("%s/%srecette.npy" % (anneetoday,anneetoday),listerecette2)
                listehistorec=numpy.load("%s/historique/12/12historec.npy"%anneew)
                listehistorec=listehistorec.tolist()
                listehistorec.append(["conservees les recettes",recettenew,"",""])###on ajoute des informations dans l'historique
                numpy.save("%s/historique/01/01historec.npy" %anneetoday,listehistorec)
                solde()
            else:
                catego=choix
                listecatego=numpy.load("categories/%s/%s%s.npy" % (catego,anneew,catego))
                listecatego=listecatego.tolist()
                depensecatego=listecatego[11]###on recupere la valeur de la depense du dernier mois
                depensecatego=float(depensecatego)
                listecatego2=numpy.load("categories/%s/%s%s.npy" % (catego,anneetoday,catego))
                listecatego2=listecatego2.tolist()
                listecatego2[0]=depensecatego###on ajoute a la valeur de la depense de ce mois ci la depense du mois dernier
                numpy.save("categories/%s/%s%s.npy" % (catego,anneetoday,catego),listecatego2)
                listehisto=numpy.load("%s/historique/12/12%s.npy" %(anneetoday,catego))
                listehisto=listehisto.tolist()
                listehisto.append(["conservees les depenses",depensecatego,"",""])
                numpy.save("%s/historique/01/01%s.npy" %(anneetoday,catego),listehisto)###on ajoute des informations dans l'historiques
                listedepense=numpy.load("%s/%sdepense.npy" %(anneetoday,anneetoday))
                listedepense=listedepense.tolist()
                newdepense=listedepense[0]
                newdepense=newdepense+depensecatego###on ajoute a la depense generale la depense de la categorie
                listedepense[0]=newdepense
                numpy.save("%s/%sdepense.npy" %(anneetoday,anneetoday),listedepense)
                solde()
        root.mainloop()
