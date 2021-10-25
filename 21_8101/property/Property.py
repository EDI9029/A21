import dao.DAO
import random
import srv.time.getTime
import srv.search.google

class homo_sapiens:
    def __init__(self, name, height, weight, least_sentence):
        self.name = name
        self.height = height
        self.weight = weight
        self.least_sentence = least_sentence
    def speak(self):
        self.least_sentence = input(self.name+' : ')                 
        print('-------------------------------------------------')   

class A21_8000:
    def __init__(self, name, id, model, country, mfd, least_sentence, user_ls, reply):
        self.name = name
        self.id = id
        self.model = model
        self.country = country
        self.mfd = mfd
        self.least_sentence = least_sentence
        self.user_ls = user_ls
        self.reply = reply

    def speak(self):
        if '你也可以回答' in User.least_sentence :   #文句部分要獨立出來
            otherWords()
        elif '現在幾點' in User.least_sentence :     #文句部分要獨立出來
            time()
        elif '幫我查' in User.least_sentence :       #文句部分要獨立出來
            search()    
        elif '你先下線一下' in User.least_sentence : #文句部分要獨立出來
            exit()
        else:
            try:
                self.reply = ''.join(random.choice(dao.DAO.chat(User.least_sentence)))
                print(self.name + ' : '+ self.reply)
                print('-------------------------------------------------')                   
                self.user_ls = User.least_sentence
        
            except:
                print(self.name + ' : '+'    ?    ')
                print('-------------------------------------------------')                   
                self.reply = input(User.name+' : '+'你要說')    
                print('-------------------------------------------------')                    
                self.user_ls = User.least_sentence
                dao.DAO.memory(User.least_sentence , self.reply)

def otherWords ():    
    start =  str(User.least_sentence.find('你也可以回答'))                                                   #文句部分要獨立出來
    end = len(User.least_sentence)
    dao.DAO.memory(local_system.user_ls , User.least_sentence[int(start)+6:end])
    print(local_system.name + ' : '+ '了解!')                                                               #文句部分要獨立出來
    print('-------------------------------------------------')                                             #文句部分要獨立出來

def time():
    print(local_system.name + ' : '+ srv.time.getTime.getTime())
    print('-------------------------------------------------')

def search():
    start = 0
    end = len(User.least_sentence)
    print(local_system.name + ' : '+'這些是你要的資料!')
    srv.search.google.google_search(User.least_sentence[int(start)+3:end])
    print('-------------------------------------------------')

User = homo_sapiens('Edward', 165, 45, 'sententce')
local_system = A21_8000('Agnes ', 'A21_8101', 'A21_8100', 'Republic Of China', '2021-10-18', 'sententce', 'init', 'init')   #定型化參數待加密
