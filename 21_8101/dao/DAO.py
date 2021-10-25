import pymysql
import dao.properties

database = dao.properties.kd_21

def chat(user_input):   
    db = pymysql.connect(host=database.get_host(), port= database.get_port(), user=database.get_user(), password=database.get_password(), db=database.get_db(), charset=database.get_charset())

    try:
        cursor = db.cursor()  
        read = " SELECT speakout FROM general_dialog WHERE reply = %s ;"
        cursor.execute(read, user_input)   
        data = cursor.fetchall()         
        return data
    except Exception as msg:
        print(msg)
    finally:
        cursor.close()  
        db.close()  

def memory(userspeak ,reply): 
    db = pymysql.connect(host=database.get_host(), port= database.get_port(), user=database.get_user(), password=database.get_password(), db=database.get_db(), charset=database.get_charset())

    try:
        cursor = db.cursor()         
        remember ="INSERT INTO general_dialog (reply, speakout) VALUES (%s, %s) ;"
        cursor.execute(remember, (userspeak, reply) )
        db.commit()
    except Exception as msg:
        print(msg)
    finally:
        cursor.close() 
        db.close() 

def schedule(weekDay, date):
    db = pymysql.connect(host=database.get_host(), port= database.get_port(), user=database.get_user(), password=database.get_password(), db=database.get_db(), charset=database.get_charset())

    try:
        cursor = db.cursor()  
        read = " SELECT topic FROM schedule WHERE date=%s or date=%s ;"
        cursor.execute(read, weekDay, date)   
        data = cursor.fetchall()       
        return data
    except Exception as msg:
        return(tuple('Error'))
    finally:
        cursor.close()  
        db.close()  