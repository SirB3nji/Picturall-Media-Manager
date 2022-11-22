#Script Made by Benji

from ftplib import FTP
import os
import subprocess
import time
import progressbar
import pyautogui
import paramiko
from tkinter import *



folder_media = "C:/Users/benjamin.cherchi/OneDrive - Analog Way SAS/Bureau/Projet_Stage/default_media/"
dest_ml = "C:/Users/benjamin.cherchi/OneDrive - Analog Way SAS/Bureau/Projet_Stage/misc/"

def clearoutput():
    os.system('cls')

def main():
    clearoutput()

    print("Bienvenue sur Picturall Media Manager ! ")
    chxmain = int(input("Que voulez vous faire ? \n\n 1 - Ce connecter au Picturall \n 2 - Quitter. \n\n PMM-Accueil => "))
    if chxmain == 1:
        clearoutput()

        chxconnexionpicturall = int(input("Que voulez vous faire ? \n\n 1 - Connexion avec ID par défaut \n 2 - Connexion avec ID personnalisé (Soon) \n 0 - Accueil \n\n PMM-Connexion => "))
        if chxconnexionpicturall == 1:
            ftp_login_default()
        if chxconnexionpicturall == 2:
            ftp_login_edited()
        if chxconnexionpicturall == 3:
            main()        


def ftp_login_default():
    clearoutput()

    ftp = FTP('192.168.2.161') 
    ftp.login(user='picmedia', passwd = 'aidemcip')
    ftp.cwd('picturall/media')

    print(ftp.getwelcome())

    chxmediaimp = int(input("\n\nQue voulez vous importez ? \n\n 1 - Media par défaut (~64) \n 2 - Media perso \n 3 - Supprimer les médias par défaut \n 0 - Accueil \n\n PMM-Media => "))

    if chxmediaimp == 1:
        ftp.mkd('default_media')
        ftp.cwd('default_media')

        for x in range(1, 65):
            clearoutput()
            print("Installation des medias en cours ... ")

            print("\n Téléchargement de => " + "media_ ("+str(x)+").mp4 \n")

            file = open(folder_media + "media_ ("+str(x)+").mp4",'rb')                 
            ftp.storbinary('STOR media_ ('+str(x)+').mp4', file) 
            for i in progressbar.progressbar(range(100)):
                time.sleep(0.01)
        print("\nInstallation des médias terminés !")
        ftp.cwd('../../server/system')

        print("\nPlacement des médias dans la collection 255 'PMM' ")
        
        ftp.delete("media_library.xml")

        time.sleep(0.5)

        file = open(dest_ml + "media_library.xml",'rb')                  # file to send
        ftp.storbinary('STOR media_library.xml', file)     # send the file
        file.close()                                    # close file and FTP
        ftp.quit()


        for i in progressbar.progressbar(range(100)):
            time.sleep(0.01)

        
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('192.168.2.161', username='root', password='picturall')
        stdin, stdout, stderr = client.exec_command("reboot")
        client.close()


        return main()
        
        


        





    if chxmediaimp == 2:
        print("soon..")
        input("Appuyez sur Enter pour retourner à l'accueil !")
        main()    

    if chxmediaimp == 3:
        for i in progressbar.progressbar(range(100)):
                time.sleep(0.01)
        ftp.cwd('default_media')
        for x in range(1, 65):
            ftp.delete("media_ ("+str(x)+").mp4")
        ftp.cwd('../') 
        time.sleep(1)
        ftp.rmd('default_media')  
        print("Suppression terminés !")
        return ftp_login_default() 

def ftp_login_edited():
    return main()







########## INTERFACE GRAPHIQUE ###################




main()