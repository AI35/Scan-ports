# -*- coding: utf-8 -*-
# SCAN PORTS
# DEV BY : ALI .B .OTH
# My ORG : LinePY ©
# Github account : https://github.com/alosh55
# My ORG on Github : https://github.com/orgs/LinePY
# version : 1.0.1

import socket
import sys,os,platform
from time import sleep
from multiprocessing import cpu_count

def compinfo():
    print '\nScan Ports v1.0.1'
    np = cpu_count()
    print '\nYou have {0:0} CPUs'.format(np)

    print
    print 'system   :', platform.system()
    print 'node     :', platform.node()
    print 'release  :', platform.release()
    print 'version  :', platform.version()
    print 'machine  :', platform.machine()
    print 'processor:', platform.processor()
    print'\nDEV BY : ALI .B .OTH - ORG : LinePY ©'
    for i in range(1, 6) :
        sleep(0.5)
        print '.',    

def starting():
    print '\nSTARTING ',
    for i in range(1, 6) :
        sleep(1)
        print '.',
    print 

if __name__ == "__main__":
    compinfo()
    if platform.system() != 'Windows' :
        print '\nNot Working on : ', platform.system() 
    else:
        if platform.python_version() < '2.7' or platform.python_version() >= '3.0':
            print'\nYour python version is ', platform.python_version()
            print '\nPlease install python 2.7'
            print '\nEXITING ',
            for i in range(1, 11) :
                sleep(1)
                print '.',
        else:        
            max_port=5000
            min_port=1
            check = True
            while check:    
                host=raw_input("\nEnter Host : ")
                try:
                    host_ip=socket.gethostbyname(host)
                except:
                    print "Invaild Host , Please Enter vaild Host..."
                else:
                    check = False
        
            starting()
        
            print "-" * 65
            print "Please wait.... Scanning this Host : ", host_ip ,'(',host,')'
            print "-" * 65
            try:
                for port in range(min_port,max_port):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.5)
            
                    result = sock.connect_ex((host_ip, port))
                    if result == 0:
                        print ("Port %d : \t Open "%(port))
                        sock.close()
            except KeyboardInterrupt:
                print "You pressed Ctrl+C"
                print "\n\n[*] User Requested An Interrupt."
                print "[*] Application Shutting Down."
                sleep(5)
                sys.exit()
            except socket.gaierror:
                print 'Hostname could not be resolved. Exiting..'
                sleep(5)
                sys.exit()
            except socket.error:
                print "Couldn't connect to server"
                sleep(5)
                sys.exit()
                
            
            print "[*] Finish.. "
            print'\nDEV BY : ALI .B .OTH - ORG : LinePY ©\nGithub account : https://github.com/alosh55\nMy ORG on Github : https://github.com/orgs/LinePY'
            pass

