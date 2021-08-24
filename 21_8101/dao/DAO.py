import pymysql

def chat(user_input):
    host = 'localhost'  
    port = 3306  
    user = 'root'  
    password = 'usaac130h41y799q'    
    db = 'kd21'    
    charset = 'utf8'  

    
    try:
        db = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset) 
        cursor = db.cursor()  

        read = " SELECT speakout FROM general_dialog WHERE reply = %s ;"
        line = cursor.execute(read, user_input)   
        data = cursor.fetchall()  
        
        return data

    except Exception as msg:
        return(tuple('你說什麼?',))
    finally:
        cursor.close()  
        db.close()  



def memory(userspeak ,reply):
    host = 'localhost'  
    port = 3306  
    user = 'root'  
    password = 'usaac130h41y799q'    
    db = 'kd21'    
    charset = 'utf8'  

    
    try:
        db = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset=charset) 
        cursor = db.cursor()  

        remember ="INSERT INTO general_dialog (reply, speakout) VALUES (%s, %s) ;"
        cursor.execute(remember, (userspeak, reply) )
        db.commit()
    except Exception as msg:
        print(msg)
    finally:
        cursor.close() 
        db.close() 