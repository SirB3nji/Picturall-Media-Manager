from tkinter import *
from tkinter import messagebox
from ftplib import FTP
import os
import subprocess
import time
import progressbar
import pyautogui
import paramiko
from plyer import notification
import keyboard


def clearoutput():
    os.system('cls')

root = Tk()

root.geometry("800x400")
root.geometry("+600+200")

root.minsize(width='800', height='400')

root.maxsize(width='800', height='400')

root.title('Picturall Media Manager.')

root.config(background='#014976')

root.iconbitmap('logo.ico')




def secondwindows():

    root.wm_state('iconic')

    secondwindows = Toplevel(root)
    secondwindows.geometry("800x400")
    secondwindows.geometry("+600+200")
    secondwindows.minsize(width='800', height='400')
    secondwindows.maxsize(width='800', height='400')
    secondwindows.title('Picturall Media Manager.')
    secondwindows.config(background='#014976')
    secondwindows.iconbitmap('logo.ico')

    title_label = Label(secondwindows, text='Picturall Media Manager.', font=('Inter-Black.ttf', 20,'bold'), background='#014976', foreground='white')    
    title_label.place(x=260, y=1)

    

    




    def function_dwnlmdi_btn():
        

        
        folder_media = "C:/Users/benjamin.cherchi/OneDrive - Analog Way SAS/Bureau/Projet_Stage/default_media/"
        dest_ml = "C:/Users/benjamin.cherchi/OneDrive - Analog Way SAS/Bureau/Projet_Stage/misc/"

        ftp = FTP('192.168.2.161') 
        ftp.login(user='picmedia', passwd = 'aidemcip')
        ftp.cwd('picturall/media')

        print(ftp.getwelcome())

        notification.notify(title = 'Picurall Media Manager', message = 'You are connected to the Picturall.', app_icon = 'logo.ico', timeout = 3)

        ftp.mkd('default_media')
        ftp.cwd('default_media')


        notification.notify(title = 'Picurall Media Manager', message = 'Medias are being uploaded!', app_icon = 'logo.ico', timeout = 5)
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

        

        secondwindows.wm_state('normal')

        os.system("start cmd")
        time.sleep(1)
        keyboard.write("telnet 192.168.2.161 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")
        time.sleep(1)
        for x in range(1, 9):   #add source
            time.sleep(1.5)
            keyboard.write("set source"+str(x)+" selection slot="+str(x)+",collection=255")
            keyboard.press("enter")
            time.sleep(1.5)
            keyboard.write("set source"+str(x)+" control play_state_req=0")
            keyboard.press("enter")
            print("source "+str(x)+" done !")
            time.sleep(1.5)
        keyboard.press("ctrl")
        keyboard.press("$")
        keyboard.release("ctrl")
        keyboard.release("$")
        keyboard.write("close")
        keyboard.press("enter")
        keyboard.write("quit")
        keyboard.press("enter")
        keyboard.write("exit")
        keyboard.press("enter")

        notification.notify(title = 'Picurall Media Manager', message = 'Medias download is finished!', app_icon = 'logo.ico', timeout = 3)
        messagebox.showinfo(title="PMM - INFO", message="Press 'OK' for reboot the Picturall.")


        

        notification.notify(title = 'Picurall Media Manager', message = 'The picturall restart!', app_icon = 'logo.ico', timeout = 10)




    def function_trashmdi_btn():   
        ftp = FTP('192.168.2.161') 
        ftp.login(user='picmedia', passwd = 'aidemcip')
        ftp.cwd('picturall/media')

        print(ftp.getwelcome())
        notification.notify(title = 'Picurall Media Manager', message = 'You are connected to the Picturall.', app_icon = 'logo.ico', timeout = 0.5)
        time.sleep(1)
        notification.notify(title = 'Picurall Media Manager', message = 'Medias are being deleted!', app_icon = 'logo.ico', timeout = 0.5)

        

        os.system("start cmd")
        time.sleep(1)
        keyboard.write("telnet 192.168.2.161 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")
        time.sleep(1)
        for x in range(1, 9):   #remove source
            time.sleep(1.5)
            keyboard.write("set source"+str(x)+" control play_state_req=6")
            keyboard.press("enter")
            time.sleep(1.5)
            keyboard.write("set source"+str(x)+" selection slot=0,collection=255")
            keyboard.press("enter")
            print("source "+str(x)+" done !")
            time.sleep(1.5)
        keyboard.press("ctrl")
        keyboard.press("$")
        keyboard.release("ctrl")
        keyboard.release("$")
        keyboard.write("close")
        keyboard.press("enter")
        keyboard.write("quit")
        keyboard.press("enter")
        keyboard.write("exit")
        keyboard.press("enter")

        for i in progressbar.progressbar(range(100)):
                time.sleep(0.01)
        ftp.cwd('default_media')
        for x in range(1, 65):
            ftp.delete("media_ ("+str(x)+").mp4")
        ftp.cwd('../') 
        time.sleep(1)
        ftp.rmd('default_media')  
        ftp.quit()



        print("Suppression terminés !")
        notification.notify(title = 'Picurall Media Manager', message = 'Deleting completed medias.', app_icon = 'logo.ico', timeout = 1)


    def function_playmdi_btn():
        os.system("start cmd")
        time.sleep(1)
        keyboard.write("telnet 192.168.2.161 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")
        time.sleep(0.2)
        for x in range(1, 9):   #add source
            time.sleep(1.5)
            keyboard.write("set source"+str(x)+" selection slot="+str(x)+",collection=255")
            keyboard.press("enter")
            time.sleep(1.5)
            keyboard.write("set source"+str(x)+" control play_state_req=0")
            keyboard.press("enter")
            print("source "+str(x)+" done !")
        keyboard.press("ctrl")
        keyboard.press("$")
        keyboard.release("ctrl")
        keyboard.release("$")
        keyboard.write("close")
        keyboard.press("enter")
        keyboard.write("quit")
        keyboard.press("enter")
        keyboard.write("exit")
        keyboard.press("enter")
        print("the medias playback has started")
        notification.notify(title = 'Picurall Media Manager', message = 'The medias playback has started.', app_icon = 'logo.ico', timeout = 2)

    def function_stopmdi_btn():
        os.system("start cmd")
        time.sleep(1)
        keyboard.write("telnet 192.168.2.161 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")
        time.sleep(0.2)
        for x in range(1, 9):   #remove source
            time.sleep(1.5)
            keyboard.write("set source"+str(x)+" control play_state_req=6")
            keyboard.press("enter")
            time.sleep(1.5)
            keyboard.write("set source"+str(x)+" selection slot=0,collection=255")
            keyboard.press("enter")
            print("source "+str(x)+" done !")
        keyboard.press("ctrl")
        keyboard.press("$")
        keyboard.release("ctrl")
        keyboard.release("$")
        keyboard.write("close")
        keyboard.press("enter")
        keyboard.write("quit")
        keyboard.press("enter")
        keyboard.write("exit")
        keyboard.press("enter")
        print("the medias playback has stopped")
        notification.notify(title = 'Picurall Media Manager', message = 'The medias playback has stopped.', app_icon = 'logo.ico', timeout = 2)
    

    def function_pausemdi_btn():
        os.system("start cmd")
        time.sleep(1)
        keyboard.write("telnet 192.168.2.161 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")
        time.sleep(0.2)
        for x in range(1, 9):   #remove source
            time.sleep(1.5)
            keyboard.write("set source"+str(x)+" control play_state_req=5")
            keyboard.press("enter")
            time.sleep(1.5)
            keyboard.write("set source"+str(x)+" selection slot=0,collection=255")
            keyboard.press("enter")
            print("source "+str(x)+" done !")
        keyboard.press("ctrl")
        keyboard.press("$")
        keyboard.release("ctrl")
        keyboard.release("$")
        keyboard.write("close")
        keyboard.press("enter")
        keyboard.write("quit")
        keyboard.press("enter")
        keyboard.write("exit")
        keyboard.press("enter")
        print("the medias playback has stopped")
        notification.notify(title = 'Picurall Media Manager', message = 'The medias playback has paused.', app_icon = 'logo.ico', timeout = 2)
    

    def function_rebootpic_btn():
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('192.168.2.161', username='root', password='picturall')
        stdin, stdout, stderr = client.exec_command("reboot")
        client.close()
        notification.notify(title = 'Picurall Media Manager', message = 'The Picturall reboot!', app_icon = 'logo.ico', timeout = 2)




    



        



















    dwnldmdi = PhotoImage(file='download.png')
    dwnldmdi_btn = Button(secondwindows, image=dwnldmdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_dwnlmdi_btn)
    dwnldmdi_btn.place(x=285, y=100)

    download_label = Label(secondwindows, text="Install Media.", font=('Inter-Black.ttf', 20,'bold'), background='#014976', foreground='white')
    download_label.place(x=340, y=110)

    trashmdi = PhotoImage(file='trash.png')
    trashmdi_btn = Button(secondwindows, image=trashmdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_trashmdi_btn)
    trashmdi_btn.place(x=283, y=197)

    trash_label = Label(secondwindows, text="Delete Media.", font=('Inter-Black.ttf', 20,'bold'), background='#014976', foreground='white')
    trash_label.place(x=340, y=210)

    playmdi = PhotoImage(file="playmdi.png")
    playmdi_btn = Button(secondwindows, image=playmdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_playmdi_btn)
    playmdi_btn.place(x=10, y=340)

    stopmdi = PhotoImage(file="stopmdi.png")
    stopmdi_btn = Button(secondwindows, image=stopmdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_stopmdi_btn)
    stopmdi_btn.place(x=70, y=340)

    pausemdi = PhotoImage(file="pausemdi.png")
    pausemdi_btn = Button(secondwindows, image=pausemdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_pausemdi_btn)
    pausemdi_btn.place(x=130, y=340)

    rebootpic = PhotoImage(file="reboot.png")
    rebootpic_btn = Button(secondwindows, image=rebootpic, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_rebootpic_btn)
    rebootpic_btn.place(x=743, y=340)


    secondwindows.mainloop()

title_label = Label(root, text='Picturall Media Manager.', font=('Inter-Black.ttf', 20,'bold'), background='#014976', foreground='white')    
title_label.place(x=260, y=1)


login_label = Label(root, text='login.', font=('Inter-Black.ttf', 16,'bold'), background='#014976', foreground='white')
login_label.place(x=380, y=155)


cmd_login_btn = secondwindows
login_image_btn = PhotoImage(file='login2.png')
login_btn = Button(root, image=login_image_btn, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=cmd_login_btn)
login_btn.place(x=380, y=90)

cmd_quit_btn = root.quit
quit_image_btn = PhotoImage(file='quit2.png')
quit_btn = Button(root, image=quit_image_btn, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=cmd_quit_btn)
quit_btn.place(x=378, y=220)

quit_label = Label(root, text='quit.', font=('Inter-Black.ttf', 16,'bold'), background='#014976', foreground='white')
quit_label.place(x=382, y=280)

mainloop()
