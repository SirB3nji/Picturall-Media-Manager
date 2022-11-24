# -*- coding: utf-8 -*-

#Script Made by Benji
#Version MACOS



from tkinter import *
from tkinter import messagebox
from ftplib import FTP
import os
import subprocess
import time
import pyautogui
import paramiko
import keyboard



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

        
        ftp.mkd('default_media')
        ftp.cwd('default_media')


        

        clearoutput()
        print("Installation des medias en cours ... ")

        
        print("\n Téléchargement de média")

        
        file = open(folder_media + "media_ (1).mp4",'rb')  
        ftp.storbinary('STOR media_ (1).mp4', file)

        file = open(folder_media + "media_ (2).mp4",'rb')  
        ftp.storbinary('STOR media_ (2).mp4', file)
        
        file = open(folder_media + "media_ (3).mp4",'rb')  
        ftp.storbinary('STOR media_ (3).mp4', file)
        
        file = open(folder_media + "media_ (4).mp4",'rb')  
        ftp.storbinary('STOR media_ (4).mp4', file)
        
        file = open(folder_media + "media_ (5).mp4",'rb')  
        ftp.storbinary('STOR media_ (5).mp4', file)
        
        file = open(folder_media + "media_ (6).mp4",'rb')  
        ftp.storbinary('STOR media_ (6).mp4', file)
        
        file = open(folder_media + "media_ (7).mp4",'rb')  
        ftp.storbinary('STOR media_ (7).mp4', file)
        
        file = open(folder_media + "media_ (8).mp4",'rb')  
        ftp.storbinary('STOR media_ (8).mp4', file)
        
        file = open(folder_media + "media_ (9).mp4",'rb')  
        ftp.storbinary('STOR media_ (9).mp4', file)
        
        file = open(folder_media + "media_ (10).mp4",'rb')  
        ftp.storbinary('STOR media_ (10).mp4', file)
        
        file = open(folder_media + "media_ (11).mp4",'rb')  
        ftp.storbinary('STOR media_ (11).mp4', file)
        
        file = open(folder_media + "media_ (12).mp4",'rb')  
        ftp.storbinary('STOR media_ (12).mp4', file)
        
        file = open(folder_media + "media_ (13).mp4",'rb')  
        ftp.storbinary('STOR media_ (13).mp4', file)
        
        file = open(folder_media + "media_ (14).mp4",'rb')  
        ftp.storbinary('STOR media_ (14).mp4', file)
        
        file = open(folder_media + "media_ (15).mp4",'rb')  
        ftp.storbinary('STOR media_ (15).mp4', file)
        
        file = open(folder_media + "media_ (16).mp4",'rb')  
        ftp.storbinary('STOR media_ (16).mp4', file)
        
        file = open(folder_media + "media_ (17).mp4",'rb')  
        ftp.storbinary('STOR media_ (17).mp4', file)
        
        file = open(folder_media + "media_ (18).mp4",'rb')  
        ftp.storbinary('STOR media_ (18).mp4', file)
        
        file = open(folder_media + "media_ (19).mp4",'rb')  
        ftp.storbinary('STOR media_ (19).mp4', file)
        
        file = open(folder_media + "media_ (20).mp4",'rb')  
        ftp.storbinary('STOR media_ (20).mp4', file)
        
        file = open(folder_media + "media_ (21).mp4",'rb')  
        ftp.storbinary('STOR media_ (21).mp4', file)
        
        file = open(folder_media + "media_ (22).mp4",'rb')  
        ftp.storbinary('STOR media_ (22).mp4', file)
        
        file = open(folder_media + "media_ (23).mp4",'rb')  
        ftp.storbinary('STOR media_ (23).mp4', file)
        
        file = open(folder_media + "media_ (24).mp4",'rb')  
        ftp.storbinary('STOR media_ (24).mp4', file)
        
        file = open(folder_media + "media_ (25).mp4",'rb')  
        ftp.storbinary('STOR media_ (25).mp4', file)
        
        file = open(folder_media + "media_ (26).mp4",'rb')  
        ftp.storbinary('STOR media_ (26).mp4', file)
        
        file = open(folder_media + "media_ (27).mp4",'rb')  
        ftp.storbinary('STOR media_ (27).mp4', file)
        
        file = open(folder_media + "media_ (28).mp4",'rb')  
        ftp.storbinary('STOR media_ (28).mp4', file)
        
        file = open(folder_media + "media_ (29).mp4",'rb')  
        ftp.storbinary('STOR media_ (29).mp4', file)
        
        file = open(folder_media + "media_ (30).mp4",'rb')  
        ftp.storbinary('STOR media_ (30).mp4', file)
        
        file = open(folder_media + "media_ (31).mp4",'rb')  
        ftp.storbinary('STOR media_ (31).mp4', file)
        
        file = open(folder_media + "media_ (32).mp4",'rb')  
        ftp.storbinary('STOR media_ (32).mp4', file)
        




























        print("media done!")
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

        
        messagebox.showinfo(title="Picturall Media Manager", message="The Picturall need to reboot! Press 'OK' for reboot!")

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip_picturall, username='root', password='picturall')
        stdin, stdout, stderr = client.exec_command("reboot")
        client.close()
        

        




    def function_trashmdi_btn():   
        ftp = FTP(ip_picturall) 
        ftp.login(user='picmedia', passwd = 'aidemcip')
        ftp.cwd('picturall/media')

        print(ftp.getwelcome())
        time.sleep(1)
        
        

        keyboard.press("cmd")
        keyboard.press("space")
        keyboard.release("cmd")
        keyboard.release("space")
        time.sleep(1)
        keyboard.write("terminal")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.press("cmd")
        keyboard.press("n")
        keyboard.release("cmd")
        keyboard.release("n")
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
        keyboard.write("set source1 selection slot=0,collection=252\nset source2 selection slot=0,collection=252\nset source3 selection slot=0,collection=252\nset source4 selection slot=0,collection=252\nset source5 selection slot=0,collection=252\nset source6 selection slot=0,collection=252\nset source7 selection slot=0,collection=252\nset source8 selection slot=0,collection=252")
        keyboard.press("enter")
        print("source done !")
        time.sleep(1.5)
        keyboard.press("ctrl")
        keyboard.press("§")
        keyboard.release("ctrl")
        keyboard.release("§")
        keyboard.write("close")
        keyboard.press("enter")
        keyboard.press("cmd")
        keyboard.press("w")
        keyboard.release("cmd")
        keyboard.release("w")
        time.sleep(1)
        keyboard.press("enter")


        
        ftp.cwd('default_media')
        
            
        ftp.delete("media_ (1).mp4")
        ftp.delete("media_ (2).mp4")
        ftp.delete("media_ (3).mp4")
        ftp.delete("media_ (4).mp4")
        ftp.delete("media_ (5).mp4")
        ftp.delete("media_ (6).mp4")
        ftp.delete("media_ (7).mp4")
        ftp.delete("media_ (8).mp4")
        ftp.delete("media_ (9).mp4")
        ftp.delete("media_ (10).mp4")
        ftp.delete("media_ (11).mp4")
        ftp.delete("media_ (12).mp4")
        ftp.delete("media_ (13).mp4")
        ftp.delete("media_ (14).mp4")
        ftp.delete("media_ (15).mp4")
        ftp.delete("media_ (16).mp4")
        ftp.delete("media_ (17).mp4")
        ftp.delete("media_ (18).mp4")
        ftp.delete("media_ (19).mp4")
        ftp.delete("media_ (20).mp4")
        ftp.delete("media_ (21).mp4")
        ftp.delete("media_ (22).mp4")
        ftp.delete("media_ (23).mp4")
        ftp.delete("media_ (24).mp4")
        ftp.delete("media_ (25).mp4")
        ftp.delete("media_ (26).mp4")
        ftp.delete("media_ (27).mp4")
        ftp.delete("media_ (28).mp4")
        ftp.delete("media_ (29).mp4")
        ftp.delete("media_ (30).mp4")
        ftp.delete("media_ (31).mp4")
        ftp.delete("media_ (32).mp4")
        print("media delete!")
        ftp.cwd('../') 
        time.sleep(1)
        ftp.rmd('default_media')  
        ftp.quit()



        print("Suppression terminés !")
        

    def function_setupmdi_btn():
        print("setup media started!")
        
        keyboard.press("cmd")
        keyboard.press("space")
        keyboard.release("cmd")
        keyboard.release("space")
        time.sleep(1)
        keyboard.write("terminal")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.press("cmd")
        keyboard.press("n")
        keyboard.release("cmd")
        keyboard.release("n")
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
        keyboard.write("set source1 selection slot=1,collection=252\nset source2 selection slot=2,collection=252\nset source3 selection slot=3,collection=252\nset source4 selection slot=4,collection=252\nset source5 selection slot=5,collection=252\nset source6 selection slot=6,collection=252\nset source7 selection slot=7,collection=252\nset source8 selection slot=8,collection=252")
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
        time.sleep(1.5)
        keyboard.write("set source1 control media_end_action=10\nset source2 control media_end_action=10\nset source3 control media_end_action=10\nset source4 control media_end_action=10\nset source5 control media_end_action=10\nset source5 control media_end_action=10\nset source6 control media_end_action=10\nset source7 control media_end_action=10\nset source8 control media_end_action=10\n")
        keyboard.press("enter")
        print("canva setup done!")
        time.sleep(1.5)
        print("full setup done! exit..")
        keyboard.press("ctrl")
        keyboard.press("§")
        keyboard.release("ctrl")
        keyboard.release("§")
        keyboard.write("close")
        keyboard.press("enter")
        keyboard.press("cmd")
        keyboard.press("w")
        keyboard.release("cmd")
        keyboard.release("w")
        time.sleep(1)
        keyboard.press("enter")



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
        



    def function_playmdi_btn():
        keyboard.press("cmd")
        keyboard.press("space")
        keyboard.release("cmd")
        keyboard.release("space")
        time.sleep(1)
        keyboard.write("terminal")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.press("cmd")
        keyboard.press("n")
        keyboard.release("cmd")
        keyboard.release("n")
        time.sleep(1)
        keyboard.write("telnet "+ip_picturall+" 11000")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.write("wait_startup")
        keyboard.press("enter")
        time.sleep(1.5)
        keyboard.write("set source1 selection slot=1,collection=252\nset source2 selection slot=2,collection=252\nset source3 selection slot=3,collection=252\nset source4 selection slot=4,collection=252\nset source5 selection slot=5,collection=252\nset source6 selection slot=6,collection=252\nset source7 selection slot=7,collection=252\nset source8 selection slot=8,collection=252")
        keyboard.press("enter")
        time.sleep(1.5)
        keyboard.write("set source1 control play_state_req=0\nset source2 control play_state_req=0\nset source3 control play_state_req=0\nset source4 control play_state_req=0\nset source5 control play_state_req=0\nset source6 control play_state_req=0\nset source7 control play_state_req=0\nset source8 control play_state_req=0")
        keyboard.press("enter")
        print("source done !")
        keyboard.press("ctrl")
        keyboard.press("§")
        keyboard.release("ctrl")
        keyboard.release("§")
        keyboard.write("close")
        keyboard.press("enter")
        keyboard.press("cmd")
        keyboard.press("w")
        keyboard.release("cmd")
        keyboard.release("w")
        time.sleep(1)
        keyboard.press("enter")
        print("the medias playback has started")
       

    def function_stopmdi_btn():
        keyboard.press("cmd")
        keyboard.press("space")
        keyboard.release("cmd")
        keyboard.release("space")
        time.sleep(1) # put everywhere
        keyboard.write("terminal")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.press("cmd")
        keyboard.press("n")
        keyboard.release("cmd")
        keyboard.release("n")
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
        keyboard.press("§")
        keyboard.release("ctrl")
        keyboard.release("§")
        keyboard.write("close")
        keyboard.press("enter")
        keyboard.press("cmd")
        keyboard.press("w")
        keyboard.release("cmd")
        keyboard.release("w")
        time.sleep(1)
        keyboard.press("enter")
        print("the medias playback has stopped")
            

    def function_pausemdi_btn():
        keyboard.press("cmd")
        keyboard.press("space")
        keyboard.release("cmd")
        keyboard.release("space")
        time.sleep(1)
        keyboard.write("terminal")
        keyboard.press("enter")
        time.sleep(1)
        keyboard.press("cmd")
        keyboard.press("n")
        keyboard.release("cmd")
        keyboard.release("n")
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
        keyboard.press("§")
        keyboard.release("ctrl")
        keyboard.release("§")
        keyboard.write("close")
        keyboard.press("enter")
        keyboard.press("cmd")
        keyboard.press("w")
        keyboard.release("cmd")
        keyboard.release("w")
        time.sleep(1)
        keyboard.press("enter")
        print("the medias playback has stopped")
            

    def function_rebootpic_btn():
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip_picturall, username='root', password='picturall')
        stdin, stdout, stderr = client.exec_command("reboot")
        client.close()
        


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
    messagebox.showinfo(title="Picturall Media Manager", message="Version : MacOS\nCredit : Cherchi Benjamin")
os_img = PhotoImage(file="misc/windows.png")
os_img_btn = Button(root, image=os_img, border=0, bg='#014976', fg='#014976', activebackground='#014976', activeforeground='#014976', command=cmd_os_img)
os_img_btn.place(x=745, y=345)



mainloop()
