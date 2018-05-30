import sys

class MainReader:
    
    def __init__(self,sysArg):
        # variables used in this class
        self.sysArg = sysArg
        self.searchTest = False
        self.ignoreTest = False
        self.searchable = []
        self.ignorable = []
        self.path = self.sysArg[1]
        self.cmdLineProcessing()
        
    def getPath(self):
        return self.path
    
    def getIgnorable(self):
        return self.ignorable
    
    def getSearchable(self):
        return self.searchable

    def cmdLineProcessing(self):
    # does not account for incorrect flag input instances in cmd line  
        # set file read path from cmd line
        self.path = self.sysArg[1]

        for i in range(2, len(self.sysArg)):
            # set search flag
            if "-s" == self.sysArg[i]:
                self.searchTest = True
            # set ignore flag
            elif "-i" == self.sysArg[i]:
                self.ignoreTest = True
            # storing column values
            else:
                if self.searchTest:
                    self.searchable = self.sysArg[i].split(",")
                    self.searchTest = False
                if self.ignoreTest:
                    self.ignorable = self.sysArg[i].split(",")
                    self.ignoreTest = False


