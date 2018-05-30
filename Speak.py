class  Speak(object):
    
    def __init__(self):
        self.talking = False
        self.test = True
    
    def talk(self,*msg):
        if self.talking:
            print(msg)

    def testTalk(self, *msg):
        if self.test:
            print(msg)

