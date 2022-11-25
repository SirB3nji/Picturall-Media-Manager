import telnetlib
import time
from tkinter import messagebox 

def telnet_playmdi():
    HOST = "192.168.2.140"
    PORT = "11000"

    tn=telnetlib.Telnet()
    tn.open(HOST, PORT)

    time.sleep(0.1)
    tn.write("wait_startup\n".encode('utf-8'))
    time.sleep(0.1) 

    tn.write("set source1 selection slot=1,collection=252\n".encode('utf-8'))
    time.sleep(0.5)
    tn.write("set source2 selection slot=2,collection=252\n".encode('utf-8'))
    time.sleep(0.5)
    tn.write("set source3 selection slot=3,collection=252\n".encode('utf-8'))
    time.sleep(0.5)
    tn.write("set source4 selection slot=4,collection=252\n".encode('utf-8'))
    time.sleep(0.5)
    tn.write("set source5 selection slot=5,collection=252\n".encode('utf-8'))
    time.sleep(0.5)
    tn.write("set source6 selection slot=6,collection=252\n".encode('utf-8'))
    time.sleep(0.5)
    tn.write("set source7 selection slot=7,collection=252\n".encode('utf-8'))
    time.sleep(0.5)
    tn.write("set source8 selection slot=8,collection=252\n".encode('utf-8'))
    time.sleep(0.5)

    tn.write("set source1 control play_state_req=0\n".encode('utf-8'))
    time.sleep(0.5)
    tn.write("set source2 control play_state_req=0\n".encode('utf-8')) 
    time.sleep(0.5)
    tn.write("set source3 control play_state_req=0\n".encode('utf-8')) 
    time.sleep(0.5)
    tn.write("set source4 control play_state_req=0\n".encode('utf-8')) 
    time.sleep(0.5)
    tn.write("set source5 control play_state_req=0\n".encode('utf-8')) 
    time.sleep(0.5)
    tn.write("set source6 control play_state_req=0\n".encode('utf-8')) 
    time.sleep(0.5)
    tn.write("set source7 control play_state_req=0\n".encode('utf-8')) 
    time.sleep(0.5)
    tn.write("set source8 control play_state_req=0\n".encode('utf-8'))  
    time.sleep(1)
    tn.write("logout\n".encode('utf-8')) 
    print(tn.read_all())
    tn.close()
    print("all medias are started!")
    messagebox.showinfo(title="Picturall Media Manager", message="The Picturall medias are started!")