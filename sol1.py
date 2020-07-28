import urllib.request  


class my_dictionary(dict): 
 
    def _init_(self): 
        self = dict() 
          
    def add(self, key, value): 
        self[key] = value
        
def StpPunct(s):
    answ=""
    for c in s:
        if c.islower() or c.isupper():
            answ=answ+c.lower()
    return answ

def Rev(s):
    answ=""
    for c in s:
        answ=c+answ
    return answ

def IsPalindrome(s):
    s=StpPunct(s)
    if s==Rev(s):
        return True
    else:
        return False
    
def main():
    #url = "https://mettl-arq.s3-ap-southeast-1.amazonaws.com/questions/iit-kanpur/cyber-security-hackathon/round1/problem1/defaulttestcase.txt"
    url = input()
    count = 0
    now = 0
    dict_obj = my_dictionary()
    for line in urllib.request.urlopen(url):
        count = count + 1
        if IsPalindrome(line.decode('utf-8')):
            if line.decode('utf-8') != '\n':
                for line in line.decode('utf-8'):
                    line = line.strip("\n")
                    words = line.split()
                    now += len(words)
                
                dict_obj.add(count,now)
                now = 0
    print(dict_obj)
    print("file ok")
main()
