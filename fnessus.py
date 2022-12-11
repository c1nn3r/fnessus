from colorama import Fore,Back,Style
import click
import os
import ftpbasic
import sshbasic



@click.command()
@click.option("-t", help="Target Host", required=True)
@click.option("-m", default=("ftp","ssh","telnet",), help="Modules to use (default=ftp,ssh,telnet)")
@click.option("-s", default=1, help="Scan depth level(1/2) (default=1)")



def main(t,m,s):

    if "ftp" in m: 
            if ftpbasic.checkconn(f"{t}",21)==False: print(Back.RED+"--|! Error when connecting to "+f"{t}"+" on port "+str(21)+Back.RESET)
            else:
                ftpbasic.ftpc(f"{t}",21,s)
                
    if "ssh" in m: sshbasic.sshc(f"{t}",22,s)
    print("HIII")

if __name__ == '__main__':
    main()
