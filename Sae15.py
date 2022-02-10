## Importations of useful fonctions

import os
import numpy as np
import typing
import datetime

## Treating programme

try:
    #Opening of the .TXT file if he's exist
    with open(r"C:\Users\cleme\Documents\IUT\SAE 15\Fichier_a_traiter.txt", encoding="UTF-8") as fh:
        res = fh.read()
except:
        print("File doesn't exist.' %s", os.path.abspath("--"))
ress = res.split('\n')
Event_Table = np.array([])
#Creation of the .CSV file
fic = open(r"C:\Users\cleme\Documents\IUT\SAE 15\Fichier_Traité.csv", "w")
test = 0
Event = "Hour ; Sender ; Port ; Recipeint ; Flag ; Seq ; Ack ; Win ; Options ; Length"
fic.write(Event + "\n")
characters = ":"
for event in ress:
    #Checking if it's the good line
    texte = event.split(":")
    if len(texte) > 2:
        test = 1
    else :
        test = 0
    #Sorting the line with the informations of the trame
    if test == 1 :
        seq = ''
        ack = ''
        win = ''
        flag = ''
        option = ''
        length = ''
        testip1 = ''
        port = ''
        destination = ''
        Sender = ''
        nbrtrame = nbrtrame + 1
        #Adding Hour
        texte = event.split(' ')
        Hour = texte[0]
        #Sender
        testip1 = texte[2].split(".")
        if len(testip1) > 1 :
            if len(testip1) == 2:
                Sender = testip1[0]
                port = testip1[1]
            if len(testip1) == 3:
                Sender = testip1[0] + '.' + testip1[1]
                port = testip1[2]
            if len(testip1) == 4:
                Sender = testip1[0] + '.' + testip1[1] + '.' + testip1[2]
                port = testip1[3]
            if len(testip1) == 5:
                Sender = testip1[0] + '.' + testip1[1] + '.' + testip1[2] + '.' + testip1[3]
                port = testip1[4]
            if len(testip1) == 6 :
                Sender = testip1[0] + '.' + testip1[1] + '.' + testip1[2] + '.' + testip1[3] + '.' + testip1[4]
                port = testip1[5]
            if len(testip1) == 7 :
                Sender = testip1[0] + '.' + testip1[1] + '.' + testip1[2] + '.' + testip1[3] + '.' + testip1[4] + '.' + testip1[5]
                port = testip1[6]
            if len(testip1) == 8 :
                Sender = testip1[0] + '.' + testip1[1] + '.' + testip1[2] + '.' + testip1[3] + '.' + testip1[4] + '.' + testip1[5] + '.' + testip1[6]
                port = testip1[7]
        else :
            Sender = texte[2]
            port = ''
        #Destination
        destination = texte[4]
        destination = destination.replace(characters,"")#Permit to remove ":" who 
        #Flag
        texte = event.split("[")
        if len(texte) > 1:
            testflag = texte[1].split("]")
            flag = testflag[0]
        #seq et ack
        texte = event.split(",")
        if len(texte) > 3:
            #If it's started by Seq
            if texte[1].startswith(" seq"):
                testseq = texte[1].split(" ")
                seq = testseq[2]
                ack = ''
            #If it's started with Ack and without Seq
            if texte[1].startswith(" ack"):
                testack = texte[1].split(" ")
                ack = testack[2]
                seq = ''
            #If it's Started by Ack with Seq before
            if texte[2].startswith(" ack"):
                testack = texte[2].split(" ")
                ack = testack[2]
            #Win if there not Ack or Seq
            if texte[2].startswith(" win"):
                testwin = texte[2].split(" ")
                win = testwin[2]
            #Win if there is Ack and Seq
            if texte[3].startswith(" win"):
                testwin = texte[3].split(" ")
                win = testwin[2]
        else:
            seq = ''
            ack = ''
            win = ''
            option = ''
        #For length when there is no option 1 and no other one
        if len(texte) == 4:
            if texte[3].startswith(" length"):
                testlength = texte[3].split(" ")
                length = testlength[2]
                length = length.replace(characters,"")
        #For length wen there is no option
        if len(texte) == 5:
            if texte[4].startswith(" length"):
                testlength = texte[4].split(" ")
                length = testlength[2]
                length = length.replace(characters,"")
        #For length with option
        texte = event.split("]")
        if len(texte) > 2 :
            testlength = texte[2].split(" ")
            length = testlength[2]
            length = length.replace(characters,"")
        #Option if there is 3 parts when split [ (flag et option)
        texte=event.split("[")
        if len(texte) > 2:
            texte2 = texte[2].split("]")
            option = texte2[0]
        else:
            option = ''
        Event=Hour + ';' + Sender  + ';' + port + ';' + destination + ';' + flag + ';' + seq + ';' + ack + ';' + win + ";" + option + ';' + length
        fic.write(Event + "\n")