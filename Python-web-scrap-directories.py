#Made By Blake McCullough
#Discord - Spoiled_Kitten#4911
#Github - https://github.com/Blake-McCullough/
#Email - privblakemccullough@protonmail.com


#BUILT TO SCRAP ALL DIRECTORYS AND FILES ON THE ARCHIVED LINUX SERVER
import requests
from bs4 import BeautifulSoup
import re
#setups
files = []
directorylist = []
def getfiles(baseurl):
    print("RUNNING NOW ")
    #Makes sure files are blank, so doesnt duplicate
    filesfile = open("archivefiles.txt", "w")
    filesfile.write("")
    filesfile.close()
    directoriesfile = open("archivedirectories.txt", "w")
    directoriesfile.write("")
    directoriesfile.close()


    #Makes blank directory list
    directorylist.append("")
    for directory in directorylist:
        #does requests
        URL = baseurl + directory
        bean = requests.get(URL,timeout=60)
        soop = BeautifulSoup(bean.text,"html.parser")
        for linkyboi in soop.find_all("a"):
            linkyboii=linkyboi.get("href")
            #Checks if it is the return directory, if it is then it goes and 
            if linkyboii == "../":
                continue
            else:
                #If it ends with / then it must be directory so adds it to list of things to be searched
                if linkyboii.endswith("/"):
                    directoriesfile = open("archivedirectories.txt", "a")
                    directoriesfile.write(URL+linkyboii+"\n")
                    directoriesfile.close()
                    #print(appending,"DIRECTORY")
                #Else it is a file so adds it to files list
                else:
                    #print(linkyboii, "NOT")
                    filesfile = open("archivefiles.txt", "a")
                    filesfile.write(URL+linkyboii+"\n")
                    filesfile.close()
             #adds to the files file



if __name__ == "__main__":
    getfiles("https://archive.archlinux.org/packages/")



