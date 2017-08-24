
########################################################################
################version_evolution 5################################
#########cette version permet par interface graphique:
################creation des dossiers et fichiers necessaires au programme
################depenses par categories 
################gerer des recettes generales
################enregistrement des donnees
################graphiques selon les mois et annees
################gestion d'un historique 
################parametre pour la gestion des donnees et creation de categories
################informations par annee
################prevision de l'annee a venir
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
from PIL import Image, ImageTk
from PIL import *
import glob
import shutil
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
    
if  os.path.isfile("date.npy"):######on verifie si il existe une base de donnees date 
    print()
else:
    newdate=[anneetoday]###### sinon une cree la base de donnees
    numpy.save("date.npy",newdate)
#############################################################
if moistoday==moisw and anneetoday==anneew:#######on verifie l'egalite
    moismod=0
    moismod=int(moistoday)
    moismod=moismod-1#########les listes commencent a  zero ainsi pour lire la valeur correspondant au mois il faut enlever un
    ########################################################################
    ## chargement donnees depense solde recette
    ###########################depense#############################################
    if os.path.isfile("test1.npy"):### on regarde si c'est le premier lancement
        listedepense=numpy.load("%s/%sdepense.npy" % (anneetoday,anneetoday))
        listedepense=listedepense.tolist()
        depense=listedepense[moismod]
        depense=float(depense)########recuperation de la donnée depense associee au mois
    ###########################recette#############################################
        listerecette=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))
        listerecette=listerecette.tolist()
        recette=listerecette[moismod]
        recette=float(recette)########recuperation de la donnee recette associee au mois
    ###########################solde#############################################
        listesolde=numpy.load("%s/%ssolde.npy" % (anneetoday,anneetoday))
        listesolde=listesolde.tolist()
        solde=listesolde[moismod]
        solde=float(solde)########recuperation de la donnee solde associee au mois
    ###########################recuperation categorie#############################################
        categorieini=numpy.load("categories/categorieini.npy")
        categorieini=categorieini.tolist()
    ##########################historique recette##############################################
        listehistorec=numpy.load("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday))########on recupere les historiques de ce mois-ci pour les recettes
        listehistorec=listehistorec.tolist()
    else:
        os.mkdir("%s" % anneetoday)######sinon on en crée un dossier annee
        
        a=[]
        numpy.save("test1.npy",a)
        newliste=[0,0,0,0,0,0,0,0,0,0,0,0]
        numpy.save("%s/%sdepense.npy" % (anneetoday,anneetoday),newliste)
        listedepense=numpy.load("%s/%sdepense.npy" % (anneetoday,anneetoday))
        listedepense=listedepense.tolist()
        depense=listedepense[moismod]
        depense=float(depense)########on cree la liste depense

        numpy.save("%s/%srecette.npy" % (anneetoday,anneetoday),newliste)
        listerecette=numpy.load("%s/%srecette.npy" % (anneetoday,anneetoday))
        listerecette=listerecette.tolist()
        recette=listerecette[moismod]
        recette=float(recette)########on cree la liste recette

        numpy.save("%s/%ssolde.npy" % (anneetoday,anneetoday),newliste)
        listesolde=numpy.load("%s/%ssolde.npy" % (anneetoday,anneetoday))
        listesolde=listesolde.tolist()
        solde=listesolde[moismod]
        solde=float(solde)########on cree la liste solde

        os.mkdir("categories")#########on cree les listes pour les categories
        categorieini=["alimentation","assurance","carburant","chauffage","electricite","frais imprevus","internet","loisirs","taxes","telephone","transport"]
        numpy.save("categories/categorieini.npy",categorieini)
        
        newcategorie=[0,0,0,0,0,0,0,0,0,0,0,0]
        for mot in categorieini:
            os.mkdir("categories/{}".format(mot))
        for mot in categorieini:
            numpy.save("categories/%s/%s%s.npy" % (mot,anneetoday,mot),newcategorie)

        newhisto=["01","02","03","04","05","06","07","08","09","10","11","12"]########on cree dossiers et fichiers pour le fonctionnement de l'historique recettes
        listezero=[]
        os.mkdir("%s/historique" % anneetoday)
        for elt in newhisto:
            os.mkdir("%s/historique/%s" % (anneetoday,elt))
        for elt in newhisto:
            numpy.save("%s/historique/%s/%shistorec.npy" % (anneetoday,elt,elt),listezero)
        listehistorec=numpy.load("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday))###on cree une base de données pour l'historique des recette
        listehistorec=listehistorec.tolist()

        newhisto=["01","02","03","04","05","06","07","08","09","10","11","12"]
        listezero=[]
        for elt in newhisto:
            for nb in categorieini:
                numpy.save("%s/historique/%s/%s%s.npy" % (anneetoday,elt,elt,nb),listezero)###on cree les historiques des depenses

        newdate=[1,2,3,4,5,6,7,8,9,10,11,12]######on cree la liste des mois pour le graphique
        numpy.save("%s/date.npy" % anneetoday,newdate)

        for categorie in categorieini:
            os.mkdir("categories/%s/%sfact%s"%(categorie,anneetoday,categorie))
            for elt in newhisto:
                os.mkdir("categories/%s/%sfact%s/%s"%(categorie,anneetoday,categorie,elt))

        os.mkdir("ajout facture")
    #######################################################################################################################################################################################################################

################################################################################################################################################
#########################################graphiques#######################################################################################################
    def chsolde():
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
                frameboutondep=Frame(framebouton,bg=couleursec)###on cree une frame pour contenir les boutons
                frameboutondep.grid()
                cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
                cnv.grid(row=0, column=0)###le canvas permet la scrollbar dans une frame
                couleurfrm="#99512B"
                hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
                hScroll.grid(row=1, column=0, sticky='we')###on initialise la srollbar du canvas
                cnv.configure(xscrollcommand=hScroll.set)
                frm = Frame(cnv,bg=couleurfrm)###on cree la frame dans le canvas pour mettre les boutons
                cnv.create_window(0, 0, window=frm, anchor='nw')###on place la frame dans le canvas
                for categor in categorieini:###cree bouton de la liste des categories
                    c=Button(frm,text=categor,width=10,height=5,bg=couleursec,command=lambda i=categor:ch(i))
                    c.pack(side=LEFT,padx=10)###on place les boutons dans la frame
                bdepensetotal=Button(frm,text="depense totale",width=10,height=5,bg=couleursec,command=lambda :ch("depense"))
                bdepensetotal.pack(side=LEFT,padx=10)###cree bouton depense total
                frm.update_idletasks()
                cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))###on configure la scrollbar
                def ch(choix):###fonction appelee après clique sur bouton
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
                def ajouter():###fonction qui ajoute les saisies
                    varprobleme.set("")
                    anneetoday=time.strftime('%Y',time.localtime())
                    anneeentry=t.get()###on recupere l'annee saisie
                    ajout=numpy.load("ajout.npy")
                    ajout=ajout.tolist()
                    lim=0
                    possible=0
                    for annee in ajout:###on verifie si l'annee entree est deja presente dans la liste
                        if annee==anneeentry:
                            possible=1
                    if anneeentry==anneetoday:###on verifie si l'annee entree n'est pas cette annee
                        possible=1
                    if possible==0:###si elle verifie alors on l'ajoute a la liste
                        for annee in ajout:
                            lim=lim+1
                        if lim<=2:
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
                    listecons=['b:x','c:x','g:x']
                    ncon=0
                    if choix=="recette" or choix=="depense" or choix=="solde":
                        anneetoday=time.strftime('%Y',time.localtime())
                        possible=0###initialise
                        listechoix=numpy.load("%s/%s%s.npy" % (anneetoday,anneetoday,choix))###on recupere la liste du choix de l'annee
                        ajout=numpy.load("ajout.npy")
                        ajout=ajout.tolist()###on importe la liste des annees a comparer
                        listedategraph=numpy.load("%s/date.npy" % anneetoday)#######on recupere les donnees de l'axe de l'abcisse
                        listedategraph=listedategraph.tolist()
                        x =listedategraph###on associe une liste a un axe
                        z=listechoix
                        l=plot(x,z,'r-x',linewidth=3,label=anneetoday)###on cree la courbe de cette annee
                        info=0
                        ajoutliste=[]
                        indique=0
                        for annee in ajout:
                            try:
                                listechoixcomparer=numpy.load("%s/%s%s.npy" % (annee,annee,choix))#######on regarde si il y a une base de donnee des annees choisies
                                listechoixcomparer=listechoixcomparer.tolist()
                                yn=listechoixcomparer
                                ln=plot(x,yn,listecons[ncon],linewidth=3,label=annee)###si il y a une base on constuit une courbe
                            except:###sinon on informe que c'est impossible de comparer
                                ajoutliste.append(annee)
                                indique=1
                            ncon=ncon+1
                        if indique==1:
                            varindique.set("impossible de construire les courbes des annees %s"%ajoutliste)
                        ylabel("les donnees %s"%choix)###on fixe les legendes
                        xlabel(anneetoday)
                        legend()###on met les legende sur le graphique
                        grid()###on met le graphique sur une grille
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
                        l=plot(x,y,'r-x',linewidth=3,label=anneetoday)###on cree la courbe correspondant a cette annee
                        ajout=numpy.load("ajout.npy")
                        ajout=ajout.tolist()###on importe la liste des annees a comparer
                        info=0
                        ajoutliste=[]
                        indique=0
                        for annee in ajout:
                            try:#####on regarde si il existe des donnees de l'annee derniere
                                categoriegraphchoixcomparer=numpy.load("categories/%s/%s%s.npy" % (categograph,annee,categograph))#######on regarde si il y a une base de donnee de l'annee derniere
                                categoriegraphchoixcomparer=categoriegraphchoixcomparer.tolist()
                                yn=categoriegraphchoixcomparer
                                ln=plot(x,yn,listecons[ncon],linewidth=3,label=annee)###si il y a une base de donnees on constuit une courbe
                            except:###sinon on informe que c'est impossible de comparer
                                ajoutliste.append(annee)
                                indique=1
                            ncon=ncon+1
                        if indique==1:
                            varindique.set("impossible de construire les courbes des annees %s"%ajoutliste)
                        ylabel("depense %s" % categograph)###on fixe les legendes
                        xlabel(anneetoday)
                        legend()###on met les legende sur le graphique
                        grid()###on met le graphique sur une grille
                        ## pour colorer zone use fill_between
                        xticks(x)###on fixe les x
                        show()######on affiche le graphique
                ajout=[]
                numpy.save("ajout.npy",ajout)
                couleurfrm="#99512B"
                framemodif=Frame(framechange,bg=couleursec)###on ajoute une autre frame qui permet de mettre d'autre widgets
                framemodif.pack()
                choix=numpy.load("ch.npy")
                labelchange=Label(framemodif,text=choix,bg=couleursec)###on indique la categorie choisie par l'utilisateur pour les graphiques
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
                labelajoutres=Label(iframeresume,text="resume des annees a comparer :")###indique a quoi correspond la variable 
                labelajoutres.grid(row=0, column=0)
                labelajout=Label(iframeresume,textvariable=varajout)###indique le resume des saisies
                labelajout.grid(row=0, column=1)
                iframeresume.pack(expand=1, fill=X, pady=10, padx=5)
                varprobleme=StringVar()
                labelprobleme=Label(iframeajout,textvariable=varprobleme)###indique si il y a un probleme a l'ajout d'une annee
                labelprobleme.pack()
                bconstruire=Button(framemodif,text="constuire le graphique",command=fin)###bouton qui permet de construire les graphiques
                bconstruire.pack()    
            framechange=Frame(frameprincipale,bg=couleursec)###frame qui va contenir les widgets
            framechange.pack()
            labelinfo=Label(framechange,bg=couleursec,text="veuillez choisir quel graphique vous voulez construire")
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
            labelindique=Label(framechange,textvariable=varindique,bg=couleursec)###label qui permet d'indiquer si on peut comparer avec l'annee anterieure
            labelindique.pack()
            bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principal",command=menu)###on met le bouton qui permet le retour au menu principal
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
            def menu():###fonction qui retourne au menu principal
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
                menuprincipale()###appelle la fonction menu principal
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
                frameboutondep.grid()###on cree une frame
                cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
                cnv.grid(row=0, column=0)###on cree un canvas pour contenir la frame
                hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
                hScroll.grid(row=1, column=0, sticky='we')###on initilaise la scrollbar
                cnv.configure(xscrollcommand=hScroll.set)
                frm = Frame(cnv,bg=couleurfrm)
                cnv.create_window(0, 0, window=frm, anchor='nw')###on ajoute la frame frm dans le canvas
                for categor in categorieini:###cree bouton de la liste des categories
                    c=Button(frm,text=categor,width=10,height=5,bg=couleursec,command=lambda i=categor:ch(i))
                    c.pack(side=LEFT,padx=10)###on place les boutons dans sla frame
                frm.update_idletasks()
                cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))###on configure la scrollbar
                def ch(choix):###fonction appelée apres clique sur bouton
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
                    varprobleme.set("probleme ajout : valeur non detectee")###si on peut pas mettre en float on indique le probleme
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
            def rec():###fonction appelee apres clique sur recette
                newliste=[]
                numpy.save("ajouthisto.npy",newliste)###initialise les fichiers
                numpy.save("ajout.npy",newliste)
                varajout.set("0")###on met a jour les variables
                varajoutotal.set("0")
                var.set("recette")
                varprobleme.set("")
                benregistrer.pack()
                varenregistre.set("enregistrer recette")
                a="recette"###on sauvegarde le choix
                numpy.save("ch.npy",a)
            def fin():###fonction appelee pour l'enregistrement
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
                    chmodif=chmodif+ajoutotal###on ajoute le total des ajouts
                    modif[moismod]=chmodif###on modifie la valeur de recette du mois
                    numpy.save("%s/%s%s.npy" % (anneetoday,anneetoday,ch),modif)###on enregistre la liste recette
                    listehistorec=numpy.load("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday))########on recupere les historiques de ce mois-ci
                    listehistorec=listehistorec.tolist()
                    ajouthisto=numpy.load("ajouthisto.npy")
                    ajouthisto=ajouthisto.tolist()
                    for nb,date,provenance in ajouthisto:
                        listehistorec.append(["ajoute des recettes",nb,date,provenance])###on enregistre dans l'historique les informations
                    numpy.save("%s/historique/%s/%shistorec.npy" % (anneetoday,moistoday,moistoday),listehistorec)###on sauvegarde l'historique
                else:###si le choix est une categorie
                    listecatego=numpy.load("categories/%s/%s%s.npy" % (ch,anneetoday,ch))#####on recupere la depense de cette categorie
                    listecatego=listecatego.tolist()
                    depensecatego=listecatego[moismod]
                    depensecatego=float(depensecatego)###on recupere la valeur du mois correspondant
                    ajout=numpy.load("ajout.npy")
                    ajoutotal=numpy.sum(ajout)
                    ajoutotal=float(ajoutotal)###on ajoute le total des depenses au depense de la categorie
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
                    numpy.save("%s/historique/%s/%s%s.npy" % (anneetoday,moistoday,moistoday,ch),listehistodepcatego)###on sauvegarde l'historique
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
            bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principal",command=menu)###on ajoute le bouton qui permet de revenir au menu principal
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
            def menu():###fonction pour retourner au menu principal
                framechange.destroy()###on detruit les frames utilisees
                bmenuprincipale.destroy()
                menuprincipale()###on appelle la fonction menu principal
            def rec():###fonction appelee quand on clique sur le bouton
                choix=("recette")
                numpy.save("ch.npy",choix)###enregistre le choix
                varhisto.set("L'historique de recette")###met a jout les variables
                button1.pack()
                listbox.delete(0,END)###on efface l interieur de la listbox
                scrollbar.pack_forget()###on cache la listbox
                listbox.pack_forget()
                buttontext.pack_forget()
                varprobleme.set("")
            def dep():###fonction appelee quand on clique sur le bouton
                categorieini=numpy.load("categories/categorieini.npy")
                categorieini=categorieini.tolist()###on va chercher la liste des categories
                bdepense.grid_forget()###on enleve les boutons
                brecette.grid_forget()
                couleurfrm="#99512B"
                categorieini=numpy.load("categories/categorieini.npy")###on amene la liste des categories
                categorieini=categorieini.tolist()
                frameboutondep=Frame(framebouton,bg="brown")
                frameboutondep.grid()
                cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
                cnv.grid(row=0, column=0)###on cree un canvas qui est contenu dans la frame frameboutondep
                hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
                hScroll.grid(row=1, column=0, sticky='we')
                cnv.configure(xscrollcommand=hScroll.set)###on initilaise la scrollbar
                frm = Frame(cnv,bg= couleurfrm)
                cnv.create_window(0, 0, window=frm, anchor='nw')###on ajoute la frame a la scrollbar
                for categor in categorieini:###cree bouton de la liste des categories
                    c=Button(frm,text=categor,width=10,height=5,bg=couleursec,command=lambda i=categor:ch(i))
                    c.pack(side=LEFT,padx=10)###on place les boutons
                bdepensetotal=Button(frm,text="depense totale",bg=couleursec,width=10,height=5,command=lambda :ch("depense"))
                bdepensetotal.pack(side=LEFT,padx=10)###crée bouton depense total
                frm.update_idletasks()
                cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height())) ###on configure la scrollbar
                def ch(choix):###quand on clique sur un bouton
                    frameboutondep.destroy()
                    bdepense.grid(row=0, column=1,padx=10)
                    brecette.grid(row=0, column=2,padx=10)
                    varhisto.set("L'historique de %s"%choix)###met a jour les variables
                    numpy.save("ch.npy",choix)
                    button1.pack()
                    listbox.delete(0,END)###on vide la listbox
                    scrollbar.pack_forget()###on efface la listbox
                    listbox.pack_forget()
                    buttontext.pack_forget()
                    varprobleme.set("")
            def recherchehisto():###fonction recherche de l'historique
                varprobleme.set("")
                scrollbar.pack(side=RIGHT, fill=Y)
                listbox.pack()###met en place la listbox
                buttontext.pack()
                ch=numpy.load("ch.npy")### on recupere le choix
                listbox.delete(0,END)###on vide la listbox
                moischoix=t.get()###on recupere le mois
                t.set("")###on efface le entry
                anneechoix=t2.get()###on recupere l'annee
                t2.set("")###on efface le entry
                try:###on essaye de trouver historique
                    if ch=="depense" or ch=="recette":
                        if ch=="depense":###si choix=depense
                            categorieini=numpy.load("categories/categorieini.npy")
                            categorieini=categorieini.tolist()###on importe la liste des categories
                            listbox.insert(END, "L'historique des depenses "+"du "+moischoix+"/"+anneechoix+" :")###on ecrit dans la listbox des indications sur l'historique demandé
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
                            listbox.insert(END,("       "+"vous avez {} pour un montant de {} euros le {} provenance : {}. ".format(commande,nb,date,provenance)))
                        fichier = open( "histotext.txt", "w")###on ouvre le fichier texte
                        fichier.write("L'historique des "+str(ch)+" du "+str(moischoix)+"/"+str(anneechoix)+" :"+"\n")###on ecrit dans le fichier des indications sur l'historique demandé
                        for commande,nb,date,provenance in listehistocatego:###puis on ecrit l'historique de la categorie
                                fichier.write("      "+"vous avez {} pour un montant de {} euros le {} provenance : {}. ".format(commande,nb,date,provenance)+"\n")
                        fichier.close()
                    listbox.config(yscrollcommand=scrollbar.set)###on configure la listbox ainsi que la scrollbar
                    scrollbar.config(command=listbox.yview)
                except:###si le chargement est impossible
                    scrollbar.pack_forget()###on enleve la listbox
                    listbox.pack_forget()
                    varprobleme.set("probleme de chargement de l'historique")###on indique le probleme
                    buttontext.pack_forget()
            def texte():###fonction texte
                os.startfile('histotext.txt')###on ouvre le fichier texte
            fichier = open( "histotext.txt", "w")###on initialise le fichier histotext
            fichier.close()
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
            bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principal",command=menu)###on cree bouton retour au menu principal
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
            framehisto=Frame(framechange,bg=couleursec)###frame qui contiend le resume de l'historique
            framehisto.pack(pady=20)
            scrollbar = Scrollbar(framehisto)###initialise la listbox qui va contenir le resume
            scrollbar.pack_forget()
            listbox = Listbox(framehisto,width=100)
            listbox.pack_forget()      
            buttontext=Button(framechange ,text="format text",command=texte)###bouton qui appelle la fonction text
            buttontext.pack_forget()
    ################################################################################################################################################
    #######################################################parametre#########################################################################################
        def parametre():###fonction parametre
            def menu():###fonction appelee pour le retour au menu principal
                framechange.destroy()###on detruit les frames
                bmenuprincipale.destroy()
                menuprincipale()###on appelle la fonction menu principal
        ################################################################################################################################################
        ################################################################################################################################################
            def reini():###fonction pour reinitialiser
                varinfo.set("choisissez la categorie a reinitialiser")###on indique que doit faire l'utilisateur
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
                cnv.grid(row=0, column=0)###on cree un canvas dans la frameboutondep
                hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
                hScroll.grid(row=1, column=0, sticky='we')
                cnv.configure(xscrollcommand=hScroll.set)###on initialise la scrollbar
                frm = Frame(cnv,bg=couleurfrm)
                cnv.create_window(0, 0, window=frm, anchor='nw')###on ajoute frm dans le canvas
                for categor in categorieini:###cree bouton de la liste des categories
                    c=Button(frm,text=categor,width=10,height=5,bg=couleursec,command=lambda i=categor:ch(i))
                    c.pack(side=LEFT,padx=10)###on place les boutons
                brecette=Button(frm,text="recette",bg=couleursec,height=5,width=10,command=lambda : ch("recette"))
                brecette.pack(side=LEFT,padx=10)
                frm.update_idletasks()
                cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))###on configure la scrollbar 
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
                        chcategoparametre=numpy.load("categories/%s/%s%s.npy" % (catego,anneetoday,catego))#####on recupere la depense de cette categorie
                        chcategoparametre=chcategoparametre.tolist()
                        enlevedep=chcategoparametre[moismod]
                        enlevedep=float(enlevedep)
                        chcategoparametre[moismod]=0###on reinitialise la valeur du mois correspondant a la categorie
                        listehistoparacatego=numpy.load("%s/historique/%s/%s%s.npy" % (anneetoday,moistoday,moistoday,catego))#####on recupere l'historique de la categories
                        listehistoparacatego=listehistoparacatego.tolist()
                        listehistoparacatego.append(["reinitialisation des depenses","",datehisto,""])###on ajoute des informations a l'historique des categories
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
            def enlever():###fonction pour enlever des valeurs
                def retour():###permet le retour vers le menu des parametres
                    framemodif.destroy()###on detruit la frame
                    frameboutondep.destroy()
                    breini.grid(row=0, column=1,padx=10)###on place les boutons du menu des parametres
                    benlever.grid(row=0, column=2,padx=10)
                    bgestioncatego.grid(row=0, column=3,padx=10)
                varinfo.set("choisissez la categorie a modifier")###on indique a l'utilisateur l'action a effectuer
                breini.grid_forget()###on eneleve les boutons du menu parametre
                benlever.grid_forget()
                bgestioncatego.grid_forget()
                boutonliste=[]
                categorieini=numpy.load("categories/categorieini.npy")
                categorieini=categorieini.tolist()###on recupere la liste des categories
                frameboutondep=Frame(framebouton,bg=couleursec)
                frameboutondep.grid()
                cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
                cnv.grid(row=0, column=0)###on cree un canvas dans la frameboutondep
                hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
                hScroll.grid(row=1, column=0, sticky='we')
                cnv.configure(xscrollcommand=hScroll.set)###on initilasie la scrollbar
                frm = Frame(cnv,bg=couleurfrm)
                cnv.create_window(0, 0, window=frm, anchor='nw')###on ajoute la frm dans le canvas
                for categor in categorieini:###cree bouton de la liste des categories
                    c=Button(frm,text=categor,width=10,height=5,bg=couleursec,command=lambda i=categor:ch(i))
                    c.pack(side=LEFT,padx=10)###on place les boutons
                brecette=Button(frm,text="recette",bg=couleursec,height=5,width=10,command=lambda : ch("recette"))
                brecette.pack(side=LEFT,padx=10)
                frm.update_idletasks()
                cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))###on configure la scrollbar
                framemodif=Frame(framechange,bg=couleursec)###on construit une frame pour contenir des widgets
                framemodif.pack()
                bretour=Button(framemodif,bg=couleursec,text="retour",command=retour)###cree bouton pour retourner au menu principal
                bretour.pack()
                def ch(choix):###la fonction est appelee apres un clique sur un bouton
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
                            varprobleme.set("probleme ajout : valeur negative")###si la valeur rentree est negative alors on l'indique
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
                            if recette<0:###si celle-ci est inferieure a zero
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
                            if depcatego<0:###si celle-ci est inferieure a zero
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
                    varinfo.set("voici les categories qui existent")###on indique a l'utilisateur des informations
                    bretour.pack_forget()###on enleve les boutons 
                    bajoutcatego.pack_forget()
                    benlevecatego.pack_forget()
                    categorieini=numpy.load("categories/categorieini.npy")###on amene la liste des categories
                    categorieini=categorieini.tolist()
                    frameboutondep=Frame(framebouton,bg=couleursec)
                    frameboutondep.grid()
                    cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
                    cnv.grid(row=0, column=0)###on cree un canvas dans la frameboutondep
                    hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
                    hScroll.grid(row=1, column=0, sticky='we')
                    cnv.configure(xscrollcommand=hScroll.set)###on initilase la scrollbare
                    frm = Frame(cnv,bg=couleurfrm)
                    cnv.create_window(0, 0, window=frm, anchor='nw')###on met la frm dans le canvas
                    for categor in categorieini:###cree bouton de la liste des categories
                        c=Button(frm,text=categor,bg=couleursec,width=10,height=5)
                        c.pack(side=LEFT,padx=10)###on place les boutons
                    frm.update_idletasks()
                    cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))##on configure la scrollbar         
                    def ajoute():###fonction qui permet ajout de la categorie
                        frameboutondep.destroy()
                        categorieini=numpy.load("categories/categorieini.npy")
                        categorieini=categorieini.tolist()###charge la liste liste
                        newcategorie=t.get()###permet de recuperer la saisie de l'utilisateur
                        verifcate="%s"%newcategorie
                        lim=0
                        for element in categorieini:
                            lim=lim+1###on regarde combien il y a de categorie
                        if lim>=31:###il y a une limite de 22 categories
                            varprobleme.set("impossible d'ajouter categorie %s limite atteinte"%newcategorie)###si il y a 22 categories on indique l'impossibilite d'ajouter une autre categorie
                        else:
                            possible=1
                            for element in categorieini:
                                if element==verifcate:###on verifie que la categorie n'existe pas
                                    possible=0
                            if possible==1:###sinon on ajoute la categorie
                                try:
                                    newliste=[]
                                    accept=0
                                    newcategorie="%s"%newcategorie
                                    for element in categorieini:##on cree une nouvelle liste de categorie par ordre alphabetique
                                        if element<newcategorie:
                                            newliste.append(element)
                                        if element>newcategorie:
                                            if accept==0:
                                                newliste.append(newcategorie)
                                                accept=1
                                            newliste.append(element)
                                    numpy.save("categories/categorieini.npy",newliste)
                                    os.mkdir("categories/%s" % newcategorie)###on cree dossier de la nouvelle categorie
                                    a=[0,0,0,0,0,0,0,0,0,0,0,0]
                                    b=[]
                                    newhisto=["01","02","03","04","05","06","07","08","09","10","11","12"]
                                    os.mkdir("categories/%s/%sfact%s" %(newcategorie,anneetoday ,newcategorie))
                                    for elt in newhisto:
                                        os.mkdir("categories/%s/%sfact%s/%s" %(newcategorie,anneetoday ,newcategorie,elt))
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
                    varinfo.set("quelle categorie souhaitez-vous enlever")###on indique l'action a effectuer
                    bretour.pack_forget()###on enleve les boutons 
                    bajoutcatego.pack_forget()
                    benlevecatego.pack_forget()
                    categorieini=numpy.load("categories/categorieini.npy")###on amene la liste des categories
                    categorieini=categorieini.tolist()
                    frameboutondep=Frame(framebouton,bg=couleursec)
                    frameboutondep.grid()
                    cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
                    cnv.grid(row=0, column=0)##on cree un canvas dans la frameboutondep
                    hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
                    hScroll.grid(row=1, column=0, sticky='we')
                    cnv.configure(xscrollcommand=hScroll.set)##on initialise la scrollbar
                    frm = Frame(cnv,bg=couleurfrm)
                    cnv.create_window(0, 0, window=frm, anchor='nw')##on ajoute la frm dans la canvas
                    for categor in categorieini:###cree bouton de la liste des categorie
                        c=Button(frm,text=categor,bg=couleursec,width=10,height=5,command=lambda i=categor:ch(i))
                        c.pack(side=LEFT,padx=10)###on place les boutons
                    frm.update_idletasks()
                    cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))##on configure la scrollbar
                    def ch(choix):###quand on clique sur un bouton on appelle cette fonction
                        frameboutondep.destroy()
                        categorieini=numpy.load("categories/categorieini.npy")
                        categorieini=categorieini.tolist()
                        n=0
                        n2=0
                        for elt in categorieini:
                            if elt==choix:
                                n2=n
                            n=n+1
                        del categorieini[n2]###on enleve cette categorie de la liste
                        catego=choix
                        listedate=numpy.load("date.npy")
                        listedate=listedate.tolist()
                        numpy.save("categories/categorieini.npy",categorieini)
                        for annee in listedate:
                            os.remove("categories/%s/%s%s.npy"%(catego,annee,catego))
                        newhisto=["01","02","03","04","05","06","07","08","09","10","11","12"]
                        for annee in listedate:
                            for elt in newhisto:
                                for file in glob.glob("categories/%s/%sfact%s/%s/*.jpg"%(catego,annee,catego,elt)):
                                    os.remove(file)
                                os.rmdir("categories/%s/%sfact%s/%s"%(catego,annee,catego,elt))
                        for annee in listedate:
                            os.rmdir("categories/%s/%sfact%s"%(catego,annee,catego))
                        os.rmdir("categories/%s"%catego)###on supprime les donnees de la categorie
                        for annee in listedate:
                            for elt in newhisto:###on supprime l'historique de la categorie
                                os.remove("%s/historique/%s/%s%s.npy"%(annee,elt,elt,catego))
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
            framechange=Frame(frameprincipale,bg=couleursec)###on construit une frame pour contenir des widgets
            framechange.pack()
            varinfo=StringVar()
            varinfo.set("choisissez les parametres")###on indique l'action a effectue
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
            bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principal",command=menu)###cree le bouton pour revenir au menu principal
            bmenuprincipale.grid(row=0, column=0)
            varprobleme=StringVar()
            labelprobleme=Label(framechange,textvariable=varprobleme,bg=couleursec)###permet d'indiquer les problemes
            labelprobleme.pack()
    ###############################################voir evolution dans l'annee#################################################################################################
        def annee():###fonction appelee pour voir evolution dans l'annee
            def menu():###fonction appelee pour le retour au menu principal
                framechange.destroy()###on detruit les frames
                bmenuprincipale.destroy()
                menuprincipale()###on appelle la fonction menu principal
            def compareannee():
                date=t.get()
                t.set("")
                listbox2.delete(0,END)###on vide la listbox
                scrollbar2.pack(side=RIGHT, fill=Y)
                listbox2.pack()###met en place la listbox pour la comparaison
                try:
                    for elt in categorieini:###pour chaque categorie dans la liste
                        listecatego=numpy.load("categories/%s/%s%s.npy" % (elt,date,elt))
                        categorietotal2=numpy.sum(listecatego)###on fait la somme des depenses de l'annee que l'utilisateur a choisi
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
                    listerecette2=numpy.load("%s/%srecette.npy" % (date,date))###on importe les depenses et recettes de l'annee comparee
                    listedepense2=numpy.load("%s/%sdepense.npy" % (date,date))
                    depensetotal2=numpy.sum(listedepense2)###on en fait la somme
                    recettetotal2=numpy.sum(listerecette2)
                    recettetotal2=float(recettetotal2)
                    depensetotal2=float(depensetotal2)
                    listbox2.insert(END,"---------------------------------------------")
                    difference=depensetotal-depensetotal2###on calcule la difference entre les recettes
                    try:
                        pourcentage=((depensetotal-depensetotal2)/depensetotal2*100)###on calcule le pourcentage de difference
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
                    listbox2.insert(END,"vous avez depense en %s %s euros. %s"%(date,depensetotal2,text))###on inscrit dans la listbox la comparaison
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
                        color="red"
                    if difference<0:
                        pourcentage=abs(pourcentage)                        
                        text="Soit une diminution de %s pourcent"%pourcentage
                        color="green"
                    listbox2.insert(END,"vous avez gagne en %s %s euros. %s"%(date,recettetotal2,text))###on inscrit dans la listbox la comparaison
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
            framechange=Frame(frameprincipale,bg=couleursec)###on cree une frame pour contenir les widgets
            framechange.pack()
            frameanneetoday=Frame(framechange,bg=couleursec)###on cree une frame pour contenir les widgets
            frameanneetoday.pack()
            scrollbar = Scrollbar(frameanneetoday)###on cree une listbox pour contenir les informations
            listbox = Listbox(frameanneetoday,width=100,height=15)
            scrollbar.pack(side=RIGHT, fill=Y,pady=10)
            listbox.pack(pady=10)
            bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principal",command=menu)###cree le bouton pour revenir au menu principal
            bmenuprincipale.grid(row=0, column=0)
            categorieini=numpy.load("categories/categorieini.npy")
            categorieini=categorieini.tolist()###on charge la liste des categories
            for elt in categorieini:###pour chaque categories dans la liste
                listecatego=numpy.load("categories/%s/%s%s.npy" % (elt,anneetoday,elt))
                categorietotal=numpy.sum(listecatego)###on fait la somme des depenses dans l'annee
                listbox.insert(END,"-----------------")
                listbox.insert(END,"vous avez depense en %s dans la categorie %s %s euros"%(anneetoday,elt,categorietotal))###on inscrit les informations
            listbox.insert(END,"---------------------------------------------")
            listbox.insert(END,"vous avez depense en %s %s euros"%(anneetoday,depensetotal))###on inscrit les depenses totales
            listbox.insert(END,"-----------------")
            listbox.insert(END,"vous avez gagne en %s %s euros"%(anneetoday,recettetotal))###on inscrit les recettes
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
            scrollbar2 = Scrollbar(framerecherche,bg=couleursec)###on cree la frame qui va contenir la listbox de l'annee recherchee
            listbox2 = Listbox(framerecherche,width=100,height=15)
            scrollbar2.pack_forget() 
            listbox2.pack_forget()### on affiche pas tout de suite la listbox2
    ###############################################voir les previsions pour l'annee a venir#################################################################################################
        def prevision():###la fonction qui permet la prevision
        couleurfrm="#99512B"
        def menu():###fonction appelee pour le retour au menu principal
            framechange.destroy()###on detruit les frames
            bmenuprincipale.destroy()
            menuprincipale()###on appelle la fonction menu principal
        def construit(choix):
            menu()
            if choix=="depense":
                data=[0,0,0,0,0,0,0,0,0,0,0,0]
                n2=0
                n=0
                N = 12
                width = 1###on initialise les valeurs
                colours=["b","g","r","c","m","y","k","w","b","g","r","c","m","y","k","w"]###on cree une base de couleurs
                for catego in categorieini:
                    a=numpy.load("categories/prevision/%s.npy"%catego)
                    a=a.tolist()###on charge la liste de prevision des ctegories
                    if n==0:
                        p1 = plt.bar( np.arange(0,N)+0.5, a, width, color=colours[n], label=catego )###on cree un histogramme des valeurs de la liste
                        for n2 in range(12):
                            if a[n2]!=0:
                                plt.text(n2+0.8, data[n2]+3,a[n2])###on affiche les valeurs de la depense estimee
                            data[n2]=data[n2]+a[n2]###on ajoute la liste depense a la liste totale des depenses pour que les bar de l'histogramme crees s'ajoutent
                    else:
                        p2 = plt.bar( np.arange(0,N)+0.5, a, width, color=colours[n], bottom=data, label=catego  )
                        for n2 in range(12):
                            if a[n2]!=0:
                                plt.text(n2+0.8, data[n2]+3,a[n2])
                            data[n2]=data[n2]+a[n2]
                    n=n+1
                plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
                plt.xlabel= ('01','02','03','04','05','06','07','08','09','10','11','12')
                plt.ylabel("previsions depenses")###on fixe les legendes 
                plt.xticks( np.arange( 1,N+1 ) )
                title('previsions des depenses')
                show()
            else:###si les recettes ont ete choisi
                liste=numpy.load("categories/prevision/recette.npy")
                liste=liste.tolist()###on charge la liste prevision des recettes
                N=12
                width = 1
                p1 = plt.bar( np.arange(0,N)+0.5, liste, width, color="red", label="recette" )###on cree un histogramme 
                plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
                plt.xlabel= ('01','02','03','04','05','06','07','08','09','10','11','12')###on fixe les valeurs de l'axe x
                plt.ylabel("previsions recettes")
                plt.xticks( np.arange( 1,N+1 ) )
                title('previsions des recettes')###on affiche titre du graphique
                show()
        framechange=Frame(frameprincipale,bg=couleursec)###on cree une frame pour contenir les widgets
        framechange.pack()
        labelinfo=Label(framechange,text="choisissez la prevision que vous souhaitez \n la prevision se base sur des moyennes",bg=couleursec)
        labelinfo.pack(pady=10)###on informe a l'utilisateur de l'action a effectuer
        framebouton=Frame(framechange,bg=couleursec)
        framebouton.pack()
        frameboutondep=Frame(framebouton,bg=couleursec)
        frameboutondep.grid()
        bdepense=Button(framebouton,text="depense",bg=couleursec,width=10,height=5,command=lambda :ch("depense"))
        bdepense.grid(row=0,column=0)###on place les boutons
        brecette=Button(framebouton,text="recette",bg=couleursec,height=5,width=10,command=lambda : ch("recette"))
        brecette.grid(row=0,column=1)###on ajoute un bouton recette
        def ch(choix):###quand on clique sur un bouton on appelle cette fonction
            listedate=numpy.load("date.npy")
            listedate=listedate.tolist()
            if choix=="recette":###si l'utilisateur a choisi recette
                n=0
                for annee in listedate:
                    n=n+1###on regarde combien d'annees sont presentes dans la liste
                recpre=[0,0,0,0,0,0,0,0,0,0,0,0]
                if n<=4:
                    for n2 in range(12):
                        recmoistotal=0
                        for annee in listedate:
                            liste=numpy.load("%s/%srecette.npy" % (annee,annee))
                            recmois=liste[n2]
                            recmois=int(recmois)
                            recmoistotal=recmoistotal+recmois###pour chaque valeurs de chaque annees du meme mois on additionne les valeurs
                        recmoistotal=recmoistotal/n###on divise par le nombre d'annee
                        recpre[n2]=recmoistotal###on sauvegarde la moyenne dans la liste
                    numpy.save("categories/prevision/%s.npy"%choix,recpre)
                    construit("recette")###on appelle la fonction qui construit le graphique
                if n>4:
                    couple1=[]
                    sumcouple1=0
                    sumcouple2=0
                    couple2=[]
                    couple1.append(listedate[0])
                    couple1.append(listedate[1])
                    couple2.append(listedate[n-1])
                    couple2.append(listedate[n-2])
                    recpre=[0,0,0,0,0,0,0,0,0,0,0,0]###on initialise les valeurs
                    for annee in couple1:
                        liste=numpy.load("%s/%srecette.npy" % (annee,annee))
                        liste=sum.numpy(liste)##on fait la somme des recettes de chaque mois
                        sumcouple1=sumcouple1+liste###on ajoute la somme 
                    sumcouple1=sumcouple1/2###on fait une moyenne
                    for annee in couple2:
                        liste=numpy.load("%s/%srecette.npy" % (annee,annee))
                        liste=sum.numpy(liste)
                        sumcouple2=sumcouple2+liste
                    sumcouple2=sumcouple2/2
                    anneedivi=0
                    anneedivi=n-5+1###on regarde combien d'annee separe les deux couples. On ajoute 1 au nombre d'anneee
                    pourcent=0
                    anneediff=0
                    anneediff=sumcouple2-sumcouple1###on calcule la difference des sommes
                    pourcent=anneedivi/sumcouple1###on calcule le pourcentage d'augmentation ou dimunition
                    recmoistotal=0
                    annee=listedate[n-1]###on cherche la date de l'annee precedente
                    for n2 in range(12):
                        liste=numpy.load("%s/%srecette.npy" % (annee,annee))
                        recmois=liste[n2]
                        recmois=int(recmois)
                        recpre[n2]=recmois
                    for n2 in range(12):
                        val=recpre[n2]
                        valajout=val*pourcent###on multiplie chaque mois pour le pourcentage puis on ajoute la valeur trouvée a celle du mois
                        val=val+valajout
                        recpre[n2]=val
                    construit("recette")###on appelle la fonction qui construit le graphique
            else:###si l'utilisateur a choisi la depense
                n=0
                for annee in listedate:
                    n=n+1###on regarde combien d'annees sont presentes dans la liste
                if n<=4:
                    categorieini=numpy.load("categories/categorieini.npy")
                    categorieini=categorieini.tolist()###on charge la liste des categories
                    for catego in categorieini:
                        deppre=[0,0,0,0,0,0,0,0,0,0,0,0]
                        for n2 in range(12):
                            depmoistotal=0
                            for annee in listedate:
                                liste=numpy.load("categories/%s/%s%s.npy" % (catego,annee,catego))
                                liste=liste.tolist()
                                depmois=liste[n2]
                                depmois=int(depmois)
                                depmoistotal=depmoistotal+depmois###pour chaque valeurs de chaque annees du meme mois on additionne les valeurs
                            depmoistotal=depmoistotal/n###on divise pour  faire une moyenne
                            deppre[n2]=depmoistotal###on sauvegarde la valeurs depmoistotal
                        numpy.save("categories/prevision/%s.npy"%catego,deppre)###on sauvegard la liste creee
                    construit("depense")###on construit le graphique
                if n>4:
                    categorieini=numpy.load("categories/categorieini.npy")
                    categorieini=categorieini.tolist()###on charge la liste des categories
                    for catego in categorieini:
                        couple1=[]
                        sumcouple1=0
                        sumcouple2=0
                        couple2=[]
                        couple1.append(listedate[0])
                        couple1.append(listedate[1])
                        couple2.append(listedate[n-1])
                        couple2.append(listedate[n-2])
                        deppre=[0,0,0,0,0,0,0,0,0,0,0,0]
                        for annee in couple1:
                            liste=numpy.load("categories/%s/%s%s.npy" % (catego,annee,catego))
                            liste=sum.numpy(liste)##on fait la somme des depenses de chaque mois
                            sumcouple1=sumcouple1+liste###on ajoute la somme 
                        sumcouple1=sumcouple1/2###on fait une moyenne
                        for annee in couple2:
                            liste=numpy.load("categories/%s/%s%s.npy" % (catego,annee,catego))
                            liste=sum.numpy(liste)
                        sumcouple2=sumcouple2+liste
                        sumcouple2=sumcouple2/2
                        anneedivi=0
                        anneedivi=n-5+1###on regarde combien d'annee separe les deux couples. On ajoute 1 au nombre d'anneee
                        pourcent=0
                        anneediff=0
                        anneediff=sumcouple2-sumcouple1###on calcule la difference des sommes
                        pourcent=anneedivi/sumcouple1###on calcule le pourcentage d'augmentation ou dimunition
                        recmoistotal=0
                        annee=listedate[n-1]###on cherche la date de l'annee precedente
                        for n2 in range(12):
                            liste=numpy.load("categories/%s/%s%s.npy" % (catego,annee,catego))
                            depmois=liste[n2]
                            depmois=int(depmois)
                            deppre[n2]=depmoistotal
                        for n2 in range(12):
                            val=deppre[n2]
                            valajout=val*pourcent###on multiplie chaque mois pour le pourcentage puis on ajoute la valeur trouvée a celle du mois
                            val=val+valajout
                            deppre[n2]=val
                    construit("depense")###on construit le graphique
        bmenuprincipale = Button(framegoprincipale,bg=couleursec, text="menu principal",command=menu)###cree le bouton pour revenir au menu principal
        bmenuprincipale.grid(row=0, column=0)        
       
    ##############################################retour menu principale##################################################################################################
        def menuprincipale():
            def gosolde():###commande qui permet d'acceder au menu solde
                framemenuprincipale.destroy()###detruit la frame menu principal
                bretourfirstmenu.destroy()
                sold()###appelle la fonction sold
            def gographiques():###commande qui permet d'acceder au menu graphique
                framemenuprincipale.destroy()
                bretourfirstmenu.destroy()
                graphiques()###appelle la fonction graphiques
            def gohisto():###commande qui permet d'acceder au menu historique
                framemenuprincipale.destroy()
                bretourfirstmenu.destroy()
                histo()###appelle la fonction histo
            def goparametre():###commande qui permet d'acceder au menu parametre
                framemenuprincipale.destroy()
                bretourfirstmenu.destroy()
                parametre()###appelle la fonction parametre
            def goannee():
                framemenuprincipale.destroy()
                bretourfirstmenu.destroy()
                annee()###appelle la fonction annee
            def goprevision():
                framemenuprincipale.destroy()
                bretourfirstmenu.destroy()
                prevision()###appelle la fonction prevision
            def gofirstmenu():
                frameprincipale.destroy()
                firstmenuprincipal()
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
            labelpres=Label(framemenuprincipale,bg=couleursec,text=("nous sommes le %s vous avez depense %s euros vos recettes de ce mois ci sont de %s euros il vous reste donc %s euros"%(date,depense,recette,solde)))
            labelpres.pack(side=TOP,pady=20)###label qui indique a l'utilisateur ses depenses recettes
            bgraphique = Button(framemenuprincipale,bg=couleursec, text="graphique",height=10,width=18,command=gographiques)
            bgraphique.pack(side=LEFT,padx=10,pady=10)###cree bouton graphique
            bsolde = Button(framemenuprincipale,bg=couleursec, text="solde",height=10,width=18,command=gosolde)
            bsolde.pack(side=LEFT,padx=10)### cree bouton solde
            bannee= Button(framemenuprincipale,bg=couleursec, text="information sur l'annee",height=10,width=18,command=goannee)
            bannee .pack(side=RIGHT,padx=10)### cree bouton parametre 
            bhistorique = Button(framemenuprincipale,bg=couleursec, text="historique",height=10,width=18,command=gohisto)
            bhistorique.pack(side=RIGHT,padx=10)### cree bouton historique
            bparametre = Button(framemenuprincipale,bg=couleursec, text="parametre ",height=10,width=18,command=goparametre)
            bparametre.pack(side=RIGHT)### cree bouton parametre
            bprevision = Button(framemenuprincipale,bg=couleursec, text="prevision",height=10,width=18,command=goprevision)
            bprevision.pack(side=RIGHT,padx=10)### cree bouton prevision
            bretourfirstmenu=Button(framegoprincipale,bg=couleursec,text="retour menu principal",command=gofirstmenu)
            bretourfirstmenu.pack()
    ################################################################################################################################################
    ##############################################Fenetre##################################################################################################
        couleurprin="#DEB887"
        couleursec="#FEFEE0"
        frameprincipale = Frame(root,width=1000,height=600,bg=couleurprin)###on cree une frame 1000*600 (taille de la fenetre)
        frameprincipale.pack()
        frameprincipale.pack_propagate(0)### taille de la frame fixe
        framegoprincipale=Frame(frameprincipale,bg=couleurprin)
        framegoprincipale.pack(side=BOTTOM)###frame qui permet de contenir le bouton : revenir au menu principal
        menuprincipale()
        ################################################################################################################################################
        ################################################################################################################################################

    def chfacture():
        ################chargement de la date locale ################
        date=time.strftime('%d-%m-%Y',time.localtime())
        datehisto=time.strftime('%d',time.localtime())
        moistoday=time.strftime('%m',time.localtime())
        anneetoday=time.strftime('%Y',time.localtime())
        ################recuperation des dates de la derniere utilisation####
        categorieini=numpy.load("categories/categorieini.npy")
        categorieini=categorieini.tolist()
        def facture():
            bgomenu.destroy()
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
                         os.startfile("categories\%s\%sfact%s\%s\%s"%(choix,anneetoday,choix,mois,choix2))       
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
            bgomenu.destroy()
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
            label1=Label(frameajout,bg=couleursec,text="_mettez la facture scannée dans le dossier ajout facture (format en jpg) \n_choisissez la categorie ainsi que le mois et l'année \n_cliquez sur ajouter")
            label1.grid(pady=20)
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
            label2.grid(pady=10)
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
                bgomenu.destroy()
                ajout()
            def gofacture():
                bajout.destroy()
                bfacture.destroy()
                bgomenu.destroy()
                facture()
            bajout=Button(frameprincipale,text="ajouter une facture",command=goajout,bg=couleurprin,width=30,height=5)
            bajout.pack(padx=10,side=RIGHT)
            bfacture=Button(frameprincipale,text="voir les factures",comman=gofacture,bg=couleurprin,width=30,height=5)
            bfacture.pack(padx=10,side=RIGHT)
            bgomenu=Button(frameprincipale,text="retour au menu",comman=gomenu,bg=couleursec)
            bgomenu.pack(side=BOTTOM)
        def gomenu():
            frameprincipale.destroy()
            firstmenuprincipal()
        ch=0
        accept=0
        dic={}
        couleurprin="#DEB887"
        couleursec="#FEFEE0"
        couleurfrm="#99512B"
        frameprincipale = Frame(root,width=1000,height=600,bg=couleursec)###on cree une frame 1000*600 (taille de la fenetre)
        frameprincipale.pack()
        frameprincipale.pack_propagate(0)### taille de la frame fixe
        bajout=Button(frameprincipale,text="ajouter une facture",command=ajout,bg=couleurprin,width=30,height=5)
        bajout.pack(padx=10,side=RIGHT)
        bfacture=Button(frameprincipale,text="voir les factures",comman=facture,bg=couleurprin,width=30,height=5)
        bfacture.pack(padx=10,side=RIGHT)
        bgomenu=Button(frameprincipale,text="retour au menu",comman=gomenu,bg=couleursec)
        bgomenu.pack(side=BOTTOM)
    ################################################################################################################################################
    def firstmenuprincipal():
        def gosolde():
            frameprincipale.destroy()
            chsolde()
        def gofacture():
            frameprincipale.destroy()
            chfacture()
        couleurprin="#DEB887"
        couleursec="#FEFEE0"
        couleurfrm="#99512B"
        frameprincipale = Frame(root,width=1000,height=600,bg=couleurprin)###on cree une frame 1000*600 (taille de la fenetre)
        frameprincipale.pack()
        frameprincipale.pack_propagate(0)### taille de la frame fixe
        labelbonjour=Label(frameprincipale,bg=couleurprin,text="Bonjour, Bienvenue sur le logiciel DEP-CHECK")
        labelbonjour.pack(pady=50)
        framebouton=Frame(frameprincipale,bg=couleurfrm)
        framebouton.pack(pady=50)
        bajout=Button(framebouton,text="solde",command=gosolde,bg=couleursec,width=50,height=15)
        bajout.pack(side=LEFT,padx=50,pady=50)
        bfacture=Button(framebouton,text="factures",comman=gofacture,bg=couleursec,width=50,height=15)
        bfacture.pack(side=RIGHT,padx=50,pady=50)
    def enrevoir():
        global rootacc
        rootacc.destroy()
    def Intercepte():
        print()
    rootacc=Tk()
    rootacc.resizable(False, False)###on peut pas modifier la taille de la fenetre
    rootacc.title('chargement de dep-check')
    frameac=Frame(rootacc,width=1000,height=600)
    frameac.pack()
    frameac.pack_propagate(0)### taille de la frame fixe
    photo=ImageTk.PhotoImage(file ="imageintr/imageintro.jpg")
    canvasacc=Canvas(frameac,width=1000,height=600)
    canvasacc.pack()
    canvasacc.create_image(0, 0, image = photo, anchor = NW)   
    rootacc.protocol("WM_DELETE_WINDOW", Intercepte)
    rootacc.after(10000,enrevoir)
    rootacc.mainloop()
    accept=0
    root = Tk()###on indique que root est une fenetre
    root.resizable(False, False)###on peut pas modifier la taille de la fenetre
    root.title('dep-check')
    firstmenuprincipal()
    root.mainloop()### cree boucle
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
        couleurprin="#DEB887"
        couleursec="#FEFEE0"
        couleurfrm="#99512B"
        frameprincipale = Frame(root,width=1000,height=600,bg=couleurprin)###on cree une frame pour contenir des widgets
        frameprincipale.pack()
        frameprincipale.pack_propagate(0)
        frameinfo=Frame(frameprincipale,bg=couleursec)###on cree une frame pour contenir des widgets
        frameinfo.pack()
        labelinfo=Label(frameinfo,bg=couleursec,text="c'est un nouveau mois qui commence \n mise a jour des donnees \n cliquez sur les boutons ou vous voulez conserver les donnees ")###on informe l'utilisateur des actions a effectuer
        labelinfo.pack()
        categorieini=numpy.load("categories/categorieini.npy")
        categorieini=categorieini.tolist()###on recupere la liste des categories
        framebouton=Frame(frameprincipale,bg=couleursec)
        framebouton.pack()
        frameboutondep=Frame(framebouton,bg=couleursec)
        frameboutondep.grid()
        cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
        cnv.grid(row=0, column=0)###on cree un canvas dans la frameboutondep
        hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
        hScroll.grid(row=1, column=0, sticky='we')
        cnv.configure(xscrollcommand=hScroll.set)###on initialise la scrollbar
        frm = Frame(cnv,bg=couleurfrm)
        cnv.create_window(0, 0, window=frm, anchor='nw')###on ajoute frm dans le canvas
        for categor in categorieini:###cree bouton de la liste des categories
            c=Button(frm,text=categor,width=10,height=5,bg=couleursec,command=lambda i=categor:ch(i))
            c.pack(side=LEFT,padx=10)###on place les boutons
        brecette=Button(frm,text="recette",bg=couleursec,height=5,width=10,command=lambda : ch("recette"))
        brecette.pack(side=LEFT,padx=10)
        frm.update_idletasks()
        cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))###on configure la scrollbar 
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
        couleurprin="#DEB887"
        couleursec="#FEFEE0"
        couleurfrm="#99512B"
        root=Tk()
        frameprincipale = Frame(root,width=1000,height=600,bg=couleurprin)###on cree une frame pour contenir des widgets
        frameprincipale.pack()
        frameprincipale.pack_propagate(0)
        frameinfo=Frame(frameprincipale)###on cree une frame pour contenir des widgets
        frameinfo.pack()
        labelinfo=Label(frameinfo,text="c'est une nouvelle annee qui demarre \n mise a jour des donnees \n cliquez sur les boutons ou vous voulez conserver les donnees ")
        labelinfo.pack()
        os.mkdir("%s" % anneetoday)######sinon on en crée un dossier annee
        newliste=[0,0,0,0,0,0,0,0,0,0,0,0]
        newdate=[1,2,3,4,5,6,7,8,9,10,11,12]
        numpy.save("%s/date.npy" % anneetoday,newdate)######on cree de nouveaux fichiers de sauvegarde des donnees
        numpy.save("%s/%srecette.npy" % (anneetoday,anneetoday),newliste)
        numpy.save("%s/%sdepense.npy" % (anneetoday,anneetoday),newliste)
        numpy.save("%s/%ssolde.npy" % (anneetoday,anneetoday),newliste)
        mon_fichier = open("mois.txt", "w")###on ecrit dans les fichier annee et mois la date actuelle
        mon_fichier.write(moistoday)
        mon_fichier.close()
        mon_fichier = open("annee.txt", "w")
        mon_fichier.write(anneetoday)
        mon_fichier.close()
        listedate=numpy.load("date.npy")
        listedate=listedate.tolist()
        listedate.append(anneetoday)
        numpy.save("date.npy",listedate)
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
        for categorie in categorieini:
            os.mkdir("categories/%s/%sfact%s"%(categorie,anneetoday,categorie))
            for elt in newhisto:
                os.mkdir("categories/%s/%sfact%s/%s"%(categorie,anneetoday,categorie,elt))
        framebouton=Frame(frameprincipale,bg=couleursec)
        framebouton.pack()
        frameboutondep=Frame(framebouton,bg=couleursec)
        frameboutondep.grid()
        cnv = Canvas(frameboutondep,bg=couleursec,width=600,height=100)
        cnv.grid(row=0, column=0)###on cree un canvas dans la frameboutondep
        hScroll = Scrollbar(frameboutondep, orient=HORIZONTAL, command=cnv.xview)
        hScroll.grid(row=1, column=0, sticky='we')
        cnv.configure(xscrollcommand=hScroll.set)###on initialise la scrollbar
        frm = Frame(cnv,bg=couleurfrm)
        cnv.create_window(0, 0, window=frm, anchor='nw')###on ajout frm dans le canvas
        for categor in categorieini:###cree bouton de la liste des categories
            c=Button(frm,text=categor,width=10,height=5,bg=couleursec,command=lambda i=categor:ch(i))
            c.pack(side=LEFT,padx=10)###on place les boutons
        brecette=Button(frm,text="recette",bg=couleursec,height=5,width=10,command=lambda : ch("recette"))
        brecette.pack(side=LEFT,padx=10)
        frm.update_idletasks()
        cnv.configure(scrollregion=(0, 0, frm.winfo_width(), frm.winfo_height()))###on configure la scrollbar 
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
                numpy.save("%s/historique/01/01%s.npy" %(anneetoday,catego),listehisto)###on ajoute des informations dans l'historique
                listedepense=numpy.load("%s/%sdepense.npy" %(anneetoday,anneetoday))
                listedepense=listedepense.tolist()
                newdepense=listedepense[0]
                newdepense=newdepense+depensecatego###on ajoute a la depense generale la depense de la categorie
                listedepense[0]=newdepense
                numpy.save("%s/%sdepense.npy" %(anneetoday,anneetoday),listedepense)
                solde()
        root.mainloop()
