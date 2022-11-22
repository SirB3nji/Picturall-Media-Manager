#Script Made by Benji

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
        

          
        time.sleep(0.5)

        file = open(dest_ml + "media_library.xml",'rb')                  # file to send
        ftp.storbinary('STOR media_library.xml', file)     # send the file
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

        

        os.system("start cmd")
        time.sleep(1)
        keyboard.write("telnet "+ip_picturall+" 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")
        time.sleep(1)

        keyboard.write("set source1 control play_state_req=6\nset source2 control play_state_req=6\nset source3 control play_state_req=6\nset source4 control play_state_req=6\nset source5 control play_state_req=6\nset source6 control play_state_req=6\nset source7 control play_state_req=6\nset source8 control play_state_req=6")
        keyboard.press("enter")
        time.sleep(1.5)
        keyboard.write("set source1 selection slot=0,collection=255\nset source2 selection slot=0,collection=255\nset source3 selection slot=0,collection=255\nset source4 selection slot=0,collection=255\nset source5 selection slot=0,collection=255\nset source6 selection slot=0,collection=255\nset source7 selection slot=0,collection=255\nset source8 selection slot=0,collection=255")
        keyboard.press("enter")
        print("source done !")
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
        notification.notify(title = 'Picurall Media Manager', message = 'Deleting completed medias.', app_icon = 'misc/logo.ico', timeout = 1)

    def function_setupmdi_btn():
        print("setup media started!")
        notification.notify(title = 'Picurall Media Manager', message = 'The Picturall setup media has been started!', app_icon = 'misc/logo.ico', timeout = 1.5)
        os.system("start cmd")
        time.sleep(1)
        keyboard.write("telnet "+ip_picturall+" 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")
        time.sleep(1)
        print("canva setup")
        keyboard.write("set canvas1 position8 x=0.0,y=0.5,w=0.25,h=0.15625,rotation=0.0,enabled=1\nset canvas1 position1 x=0.25,y=0.5,w=0.25,h=0.15625,rotation=0.0,enabled=1\nset canvas1 position2 x=0.5,y=0.5,w=0.25,h=0.15625,rotation=0.0,enabled=1\nset canvas1 position3 x=0.75,y=0.5,w=0.25,h=0.15625,rotation=0.0,enabled=1\nset canvas1 position4 x=0.0,y=0.34375,w=0.25,h=0.15625,rotation=0.0,enabled=1\nset canvas1 position5 x=0.25,y=0.359375,w=0.25,h=0.140625,rotation=0.0,enabled=1\nset canvas1 position6 x=0.5,y=0.34375,w=0.25,h=0.15625,rotation=0.0,enabled=1\nset canvas1 position7 x=0.75,y=0.34375,w=0.25,h=0.15625,rotation=0.0,enabled=1\ntransaction begin\nset canvas1 grouping8 column=0,row=0,group=1\nset canvas1 grouping1 column=1,row=0,group=1\nset canvas1 grouping2 column=2,row=0,group=1\nset canvas1 grouping3 column=3,row=0,group=1\nset canvas1 grouping4 column=0,row=1,group=1\nset canvas1 grouping5 column=1,row=1,group=1\nset canvas1 grouping6 column=2,row=1,group=1\nset canvas1 grouping7 column=3,row=1,group=1\ntransaction commit\nset canvas1 display_focus display=0\nset gpu1 pixel_space w=7680,h=2400,max_size=35.0\nset gpu2 pixel_space w=7680,h=2400,max_size=35.0")
        keyboard.press("enter")
        time.sleep(2.5)
        keyboard.write("set source1 selection slot=1,collection=255\nset source2 selection slot=2,collection=255\nset source3 selection slot=3,collection=255\nset source4 selection slot=4,collection=255\nset source5 selection slot=5,collection=255\nset source6 selection slot=6,collection=255\nset source7 selection slot=7,collection=255\nset source8 selection slot=8,collection=255")
        keyboard.press("enter")
        time.sleep(1.5)
        keyboard.write("set source1 control play_state_req=0\nset source2 control play_state_req=0\nset source3 control play_state_req=0\nset source4 control play_state_req=0\nset source5 control play_state_req=0\nset source6 control play_state_req=0\nset source7 control play_state_req=0\nset source8 control play_state_req=0")
        keyboard.press("enter")
        print("source done !")
        time.sleep(1.5)
        keyboard.write("fullscreen layer1 1 stretch\nfullscreen layer2 2 stretch\nfullscreen layer3 3 stretch\nfullscreen layer4 4 stretch\nfullscreen layer5 5 stretch\nfullscreen layer6 6 stretch\nfullscreen layer7 7 stretch\nfullscreen layer8 8 stretch")
        keyboard.press("enter")
        time.sleep(1.5)
        keyboard.write("set canvas1 test_system_info enabled=0")
        keyboard.press("enter")
        print("canva setup done!")
        time.sleep(1.5)
        print("full setup done! exit..")
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
        notification.notify(title = 'Picurall Media Manager', message = 'The Picturall setup is done!', app_icon = 'misc/logo.ico', timeout = 3)




    def function_playmdi_btn():
        os.system("start cmd")
        time.sleep(1)
        keyboard.write("telnet "+ip_picturall+" 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")
        time.sleep(1.5)
        keyboard.write("set source1 selection slot=1,collection=255\nset source2 selection slot=2,collection=255\nset source3 selection slot=3,collection=255\nset source4 selection slot=4,collection=255\nset source5 selection slot=5,collection=255\nset source6 selection slot=6,collection=255\nset source7 selection slot=7,collection=255\nset source8 selection slot=8,collection=255")
        keyboard.press("enter")
        time.sleep(1.5)
        keyboard.write("set source1 control play_state_req=0\nset source2 control play_state_req=0\nset source3 control play_state_req=0\nset source4 control play_state_req=0\nset source5 control play_state_req=0\nset source6 control play_state_req=0\nset source7 control play_state_req=0\nset source8 control play_state_req=0")
        keyboard.press("enter")
        print("source done !")
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
        notification.notify(title = 'Picurall Media Manager', message = 'The medias playback has started.', app_icon = 'misc/logo.ico', timeout = 2)

    def function_stopmdi_btn():
        os.system("start cmd")
        time.sleep(1)
        keyboard.write("telnet "+ip_picturall+" 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")  
        time.sleep(1.5)
        keyboard.write("set source1 control play_state_req=6\nset source2 control play_state_req=6\nset source3 control play_state_req=6\nset source4 control play_state_req=6\nset source5 control play_state_req=6\nset source6 control play_state_req=6\nset source7 control play_state_req=6\nset source8 control play_state_req=6")
        keyboard.press("enter")
        time.sleep(1.5)
        print("source done !")
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
        notification.notify(title = 'Picurall Media Manager', message = 'The medias playback has stopped.', app_icon = 'misc/logo.ico', timeout = 2)
    

    def function_pausemdi_btn():
        os.system("start cmd")
        time.sleep(1)
        keyboard.write("telnet "+ip_picturall+" 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")  
        time.sleep(1.5)
        keyboard.write("set source1 control play_state_req=5\nset source2 control play_state_req=5\nset source3 control play_state_req=5\nset source4 control play_state_req=5\nset source5 control play_state_req=5\nset source6 control play_state_req=5\nset source7 control play_state_req=5\nset source8 control play_state_req=5")
        keyboard.press("enter")
        time.sleep(1.5)
        print("source done !")
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




mainloop()
