"""
Author: Kunal Chavhan
Github username: techcraze
Email: techcraze5@gmail.com
Date: 9/12/14
Code description: It is an open source code which uses URLLIB module to download files from server(runs on console
                  NO UI is provided).OS module is used for directory related functions. Downloading videos from youtube
                  is NOT supported.
"""

import urllib.request
import os

hostAddress = input("enter address: ")
hostAddress = "https://" + hostAddress
print(hostAddress)

#os module function to get current working directory and list conents of directory
dir = os.getcwd()
FileList = []
FileList = os.listdir()

#change directory if necessary
print("\nFile will be saved in directory: "+dir)
opt = input("\nPress 'y' to save in the same directory or 'n' to change directory: ")
if(opt=="n"):
    path = input("\nenter the directory path: ")
    os.chdir(path)

#check if filename already exists
FileName = input("\nSave file as: ")
for i in range(len(FileList)):
    if(FileName==FileList[i]):
        print("\nfile name already exists")
        print("\nDo you want to replace file: "+FileList[i])
        ans=input("\nPress 'y' for YES and 'n' for NO: ")
        if(ans=="y"):
            break
        else:
            FileName=input("\nSave File as: ")
            i=0
        
#open url and start downloading
x = urllib.request.urlopen(hostAddress)
print("Downloading file: "+FileName)
print("Please wait...")
urllib.request.urlretrieve(hostAddress,FileName)
print("\nDownload complete!!!")
print("\nFile is downloaded to: "+os.getcwd())


#urllib.request.urlretrieve("https://www.tutorialspoint.com/java/java_tutorial.pdf","java.pdf")
