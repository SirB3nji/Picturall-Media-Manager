#Script Made by Benji
#Windows Version

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
import telnet_stopmdi
import telnet_pausemdi
import telnet_playmdi
import telnet_setupmdi
import telnet_trashmdi

os.system('mode con: cols=100 lines=7')

def clearoutput():
    os.system('cls')

root = Tk()

root.geometry("800x400")
root.geometry("+600+200")

root.minsize(width='800', height='400')

root.maxsize(width='800', height='400')

root.title('Picturall Media Manager.')

root.config(background='#014976')

root.iconbitmap('misc/logo.ico')

ip_picturall = '192.168.2.140'  #default IP

global iplabel

iplabel = Label(root, text=ip_picturall, font=('misc/Inter-Black.ttf', 15,'bold'), background='#014976', foreground='white')
iplabel.place(x=1, y=372)

def cmd_ippic_btn():
    global ip_picturall
    global promptpicip
    global iplabel
    promptpicip = pyautogui.prompt("Picturall IP ? ")  
    ip_picturall = promptpicip
    root.update_idletasks()
    iplabel.destroy()
    iplabel = Label(root, text=ip_picturall, font=('misc/Inter-Black.ttf', 15,'bold'), background='#014976', foreground='white')
    iplabel.place(x=1, y=372)   
    print("Picturall IP updated => " + promptpicip)

picipimg = PhotoImage(file='misc/ipimg.png')
picipimg_btn = Button(root, image=picipimg, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=cmd_ippic_btn)
picipimg_btn.place(x=740, y=1)








def secondwindows():

    root.wm_state('iconic')

    secondwindows = Toplevel(root)
    secondwindows.geometry("800x400")
    secondwindows.geometry("+600+200")
    secondwindows.minsize(width='800', height='400')
    secondwindows.maxsize(width='800', height='400')
    secondwindows.title('Picturall Media Manager.')
    secondwindows.config(background='#014976')
    secondwindows.iconbitmap('misc/logo.ico')

    title_label = Label(secondwindows, text='Picturall Media Manager.', font=('misc/Inter-Black.ttf', 20,'bold'), background='#014976', foreground='white')    
    title_label.place(x=260, y=1)

    

    




    def function_dwnlmdi_btn():
        

        
        folder_media = "default_media/"
        dest_ml = "misc/"

        ftp = FTP(ip_picturall) 
        ftp.login(user='picmedia', passwd = 'aidemcip')
        ftp.cwd('picturall/media')

        print(ftp.getwelcome())

        notification.notify(title = 'Picurall Media Manager', message = 'You are connected to the Picturall.', app_icon = 'misc/logo.ico', timeout = 3)

        ftp.mkd('default_media')
        ftp.cwd('default_media')


        notification.notify(title = 'Picurall Media Manager', message = 'Medias are being uploaded!', app_icon = 'misc/logo.ico', timeout = 5)
        for x in range(1, 33):
            clearoutput()
            print("Installation des medias en cours ... ")

            

            print("\n Téléchargement de => " + "media_ ("+str(x)+").mp4 \n")

            file = open(folder_media + "media_ ("+str(x)+").mp4",'rb')                 
            ftp.storbinary('STOR media_ ('+str(x)+').mp4', file) 
            for i in progressbar.progressbar(range(100)):
                time.sleep(0.01)
        print("\nInstallation des médias terminés !")
        ftp.cwd('../../server/system')

        print("\nPlacement des médias dans la collection 252 à 255 'PMM' ")
        

          
        time.sleep(0.5)

        file = open(dest_ml + "media_library.xml",'rb')                  # file to send
        ftp.storbinary('STOR media_library.xml', file) 
        
   # send the file
        file.close()                                    # close file and FTP
        ftp.quit()

        

        secondwindows.wm_state('normal')

        notification.notify(title = 'Picurall Media Manager', message = 'Medias download is finished!', app_icon = 'misc/logo.ico', timeout = 3)

        messagebox.showinfo(title="Picturall Media Manager", message="The Picturall need to reboot! Press 'OK' for reboot!")

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip_picturall, username='root', password='picturall')
        stdin, stdout, stderr = client.exec_command("reboot")
        client.close()
        notification.notify(title = 'Picurall Media Manager', message = 'The Picturall reboot!', app_icon = 'misc/logo.ico', timeout = 2)


        




    def function_trashmdi_btn():   
        ftp = FTP(ip_picturall) 
        ftp.login(user='picmedia', passwd = 'aidemcip')
        ftp.cwd('picturall/media')

        print(ftp.getwelcome())
        notification.notify(title = 'Picurall Media Manager', message = 'You are connected to the Picturall.', app_icon = 'misc/logo.ico', timeout = 0.5)
        time.sleep(1)
        notification.notify(title = 'Picurall Media Manager', message = 'Medias are being deleted!', app_icon = 'misc/logo.ico', timeout = 0.5)

        telnet_trashmdi.telnet_trashmdi()

        for i in progressbar.progressbar(range(100)):
                time.sleep(0.01)
        ftp.cwd('default_media')
        for x in range(1, 33):
            ftp.delete("media_ ("+str(x)+").mp4")
        ftp.cwd('../') 
        time.sleep(1)
        ftp.rmd('default_media')  
        ftp.quit()



        print("Suppression terminés !")
        notification.notify(title = 'Picurall Media Manager', message = 'Deleting completed medias.', app_icon = 'misc/logo.ico', timeout = 1)

    def function_setupmdi_btn():
        print("setup media started!")
        notification.notify(title = 'Picurall Media Manager', message = 'The Picturall setup media has been started!', app_icon = 'misc/logo.ico', timeout = 1.5)
        telnet_setupmdi.telnet_setupmdi()



        #dest_ml = "misc/"

        #ftp = FTP(ip_picturall) 
        #ftp.login(user='picmedia', passwd = 'aidemcip')
        #ftp.cwd('picturall/server/system')



        #file = open(dest_ml + "exported.show", 'rb')
        #ftp.delete('exported.show')
        #time.sleep(0.5)
        #ftp.storbinary('STOR exported.show', file)    # send the file
        #file.close()                                    # close file and FTP
        #ftp.quit()
        notification.notify(title = 'Picurall Media Manager', message = 'The Picturall setup is done!', app_icon = 'misc/logo.ico', timeout = 3)




    def function_playmdi_btn():
        telnet_playmdi.telnet_playmdi()
        
    def function_stopmdi_btn():
        telnet_stopmdi.telnet_stopmdi()
        notification.notify(title = 'Picurall Media Manager', message = 'The medias playback has stopped.', app_icon = 'misc/logo.ico', timeout = 2)
    

    def function_pausemdi_btn():
        telnet_pausemdi.telnet_pausemdi()
        notification.notify(title = 'Picurall Media Manager', message = 'The medias playback has paused.', app_icon = 'misc/logo.ico', timeout = 2)
    

    def function_rebootpic_btn():
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip_picturall, username='root', password='picturall')
        stdin, stdout, stderr = client.exec_command("reboot")
        client.close()
        notification.notify(title = 'Picurall Media Manager', message = 'The Picturall reboot!', app_icon = 'misc/logo.ico', timeout = 2)



    dwnldmdi = PhotoImage(file='misc/download.png')
    dwnldmdi_btn = Button(secondwindows, image=dwnldmdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_dwnlmdi_btn)
    dwnldmdi_btn.place(x=285, y=100)

    download_label = Label(secondwindows, text="Install Media.", font=('misc/Inter-Black.ttf', 20,'bold'), background='#014976', foreground='white')
    download_label.place(x=340, y=110)

    trashmdi = PhotoImage(file='misc/trash.png')
    trashmdi_btn = Button(secondwindows, image=trashmdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_trashmdi_btn)
    trashmdi_btn.place(x=283, y=260)

    trash_label = Label(secondwindows, text="Delete Media.", font=('misc/Inter-Black.ttf', 20,'bold'), background='#014976', foreground='white')
    trash_label.place(x=340, y=270)

    playmdi = PhotoImage(file="misc/playmdi.png")
    playmdi_btn = Button(secondwindows, image=playmdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_playmdi_btn)
    playmdi_btn.place(x=10, y=340)

    setupmdi = PhotoImage(file="misc/setupmedia.png")
    setupmdi_btn = Button(secondwindows, image=setupmdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_setupmdi_btn)
    setupmdi_btn.place(x=290 ,y=175)

    setupmdi_label = Label(secondwindows, text="Setup Media.", font=('misc/Inter-Black.ttf', 20,'bold'), background='#014976', foreground='white')
    setupmdi_label.place(x=350, y=185)


    stopmdi = PhotoImage(file="misc/stopmdi.png")
    stopmdi_btn = Button(secondwindows, image=stopmdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_stopmdi_btn)
    stopmdi_btn.place(x=70, y=340)

    pausemdi = PhotoImage(file="misc/pausemdi.png")
    pausemdi_btn = Button(secondwindows, image=pausemdi, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_pausemdi_btn)
    pausemdi_btn.place(x=130, y=340)

    rebootpic = PhotoImage(file="misc/reboot.png")
    rebootpic_btn = Button(secondwindows, image=rebootpic, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=function_rebootpic_btn)
    rebootpic_btn.place(x=743, y=340)


    secondwindows.mainloop()

title_label = Label(root, text='Picturall Media Manager.', font=('misc/Inter-Black.ttf', 20,'bold'), background='#014976', foreground='white')    
title_label.place(x=260, y=1)


login_label = Label(root, text='login.', font=('misc/Inter-Black.ttf', 16,'bold'), background='#014976', foreground='white')
login_label.place(x=380, y=155)


cmd_login_btn = secondwindows
login_image_btn = PhotoImage(file='misc/login2.png')
login_btn = Button(root, image=login_image_btn, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=cmd_login_btn)
login_btn.place(x=380, y=90)

cmd_quit_btn = root.quit
quit_image_btn = PhotoImage(file='misc/quit2.png')
quit_btn = Button(root, image=quit_image_btn, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=cmd_quit_btn)
quit_btn.place(x=378, y=220)

quit_label = Label(root, text='quit.', font=('misc/Inter-Black.ttf', 16,'bold'), background='#014976', foreground='white')
quit_label.place(x=382, y=280)


def cmd_os_img():
    messagebox.showinfo(title="Picturall Media Manager", message="Version : Windows\nCredit : Cherchi Benjamin")
os_img = PhotoImage(file="misc/windows.png")
os_img_btn = Button(root, image=os_img, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=cmd_os_img)
os_img_btn.place(x=745, y=345)



mainloop()
