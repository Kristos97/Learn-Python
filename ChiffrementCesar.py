import numpy as np
import matplotlib.pyplot as plt

class Format():
    def __init__(self, phrase):
        phrase = phrase.lower()
        self.phrase = list(phrase)

    def formatage(self):
        for i in range(len(self.phrase)) :
            if (self.phrase[i] == "à" or
            self.phrase[i] == "â" or
            self.phrase[i] == "ä") :
                self.phrase.pop(i)
                self.phrase.insert(i, 'a')

            if (self.phrase[i] == "é" or 
            self.phrase[i]=='è' or 
            self.phrase[i] == "ê" or
            self.phrase[i] == "ë"):
                self.phrase.pop(i)
                self.phrase.insert(i, 'e')
             
            if (self.phrase[i] == "ï" or 
            self.phrase[i]=='î' or
            self.phrase[i] == "Î" or
            self.phrase[i] == "Ï"):
                self.phrase.pop(i)
                self.phrase.insert(i, 'i')

            if (self.phrase[i] == "û" or 
            self.phrase[i]=='ü' or 
            self.phrase[i]=='ù' or 
            self.phrase[i] == "Û"):
                self.phrase.pop(i)
                self.phrase.insert(i, 'u')

        return self.phrase


class Crypt():
    def __init__(self, phrase):
        self.phrase = Format(phrase).formatage()
        self.frq = np.zeros(26, int) #liste de differente frequence des alphabets

    
    def frequence(self):
        for i in self.phrase:
            j=0
            if 97 <= ord(i) <= 122:
                j = ord(i)-97
                self.frq[j]+=1
    
        self.key=0
        while max(self.frq)!=self.frq[self.key]:
            self.key+=1

    def freqGraph(self):
        self.frequence()
        y = self.frq
        x = [chr(i) for i in range(97, 123,1)]

        plt.bar(x, y, fc='blue', ec='black')
        plt.show()

    def cryptage(self):
        self.frequence()
        self.msgk = ""
        print(self.key)
        for i in self.phrase:
            if 97<= ord(i) <=122:
                self.msgk+= chr((ord(i)+self.key-97) % 26 + 97)
            else:
                self.msgk+=i

        return self.msgk       

class Decrypt():
    def __init__(self, phrase, key):
        self.phrase = phrase
        self.key = key
    
    def decryptage(self):
        self.msgk = ""
        print(self.key)
        for i in self.phrase:
            if 97<= ord(i) <=122:
                self.msgk+= chr((ord(i)-self.key-97) % 26 + 97)
            else:
                self.msgk+=i

        return self.msgk