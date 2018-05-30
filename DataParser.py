#import array as arr
import Speak
import os
import sys

class DataParser(object):

    def __init__(self, filePath, ignorable):
       
        self.globalList = []
        self.filePath = filePath
        # check file path
        if not os.path.isfile(filePath):
            print("File path {} does not exist. Exiting...".format(filePath))
            sys.exit()
        else:
            self.filePath = filePath
        # set ignorable list
        if len(ignorable)>0:
            self.ignorable = ignorable
            self.ignore = True
        else:
            self.ignore = False
        self.openFile()

    def openFile(self):
        self.dataFile = open(self.filePath, 'r')
        self.header_listMaker()
        for line in self.dataFile:
            self.createLists(line)
        self.dataFile.close()

    def header_listMaker(self):
        firstLine = self.dataFile.readline()
        firstLine = firstLine.rstrip()
        self.headers = firstLine.split(",") 
        # loop through headers
        for i in range(len(self.headers)):
            tempIgnore = False
            # if header was set to be ignored, then ignore
            if self.ignore:
                # check if column i should be ignored
                for j in range(len(self.ignorable)):
                    testValue = self.ignorable[j]
                    if i == (int(testValue)-1): # -1 to account for 0 index and user format input
                        tempIgnore = True
                if not tempIgnore:
                     # not match so don't ignore this column(i)
                    self.globalList.append([self.headers[i]])
            # if nothing to ignore
            else:
                self.globalList.append([self.headers[i]])
    
    def createLists(self, line):
        # clean up line string
        line = line.rstrip() # remove whitespaces
        line = line.replace("\'", "") # remove excess '
        line = line.replace("\"", "") # remove excess "
        # split line into columns
        lineData = line.split(",") 
        
        ignoreCount = 0
        # loop through headers [temp values used = {testValue,tempIgnore}]
        for i in range(len(self.headers)):
            tempIgnore = False
            # if header was set to be ignored, then ignore
            if self.ignore:
                # loop through our list of columns to ignore
                for j in range(len(self.ignorable)):
                    testValue = self.ignorable[j]
                    if i == (int(testValue)-1): # -1 to account for 0 index and user format input
                        tempIgnore = True
                        ignoreCount = ignoreCount + 1
                if not tempIgnore:
                     # not match so don't ignore this column(i)
                    self.globalList[i-ignoreCount].append(lineData[i])               
            # if nothing to ignore
            else:
                self.globalList[i].append(lineData[i])


    
                

    
        