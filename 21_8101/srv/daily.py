import property.Property
import dao.DAO
import random

def _init_():
    property.Property.user = input(property.Property.username+':    ')
    print('-------------------------------------------------')
    try:
        property.Property.reply = ''.join(random.choice(dao.DAO.chat(property.Property.user)))
        print(property.Property.name + ' : '+ property.Property.reply)
        print('-------------------------------------------------')
        
    except:
        print(property.Property.name + ' : '+'    ?    ')
        print('-------------------------------------------------')
        property.Property.reply = input(property.Property.username+':    '+'你要說')
        print('-------------------------------------------------')

    property.Property.user_ls = property.Property.user
    dao.DAO.memory(property.Property.user , property.Property.reply)

def dialog():
    property.Property.user = input(property.Property.username+':    ')
    print('-------------------------------------------------')
    if '你也可以回答' in property.Property.user :
        otherWords ()
    else:
        try:
            property.Property.reply = ''.join(random.choice(dao.DAO.chat(property.Property.user)))
            print(property.Property.name + ' : '+ property.Property.reply)
            print('-------------------------------------------------')

        except:
            print(property.Property.name + ' :'+'    ?    ')
            print('-------------------------------------------------')
            property.Property.reply = input(property.Property.username+':    '+'你要說')
            print('-------------------------------------------------')

        property.Property.user_ls = property.Property.user
        dao.DAO.memory(property.Property.user , property.Property.reply)

def otherWords ():
    start =  str(property.Property.user.find('你也可以回答'))
    end = len(property.Property.user)
    dao.DAO.memory(property.Property.user_ls , property.Property.user[int(start)+6:end])
    print(property.Property.name + ' : '+ '了解!')
    print('-------------------------------------------------')

