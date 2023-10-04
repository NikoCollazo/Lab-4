import socket 
import sys
from datetime import datetime

def driver():
    server= input("Please input iteam to scan:    ")
    IP= socket.gethostbyname(server)

    start=datetime.now()

    for port in range (1,500):
        search= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        found= search.connect_ex((IP, port))
        if found==0:
            print ("Port {}:    Open".format(port))
        search.close

    end= datetime.now()

    timeTaken= end-start
    print("Your search took", {timeTaken})

if __name__ =="__main__":
    driver()

