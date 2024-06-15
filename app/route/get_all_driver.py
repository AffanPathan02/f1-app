from app.db_conn import get_db_connection
import time

def get_all_driver():
    conn = get_db_connection()
    cur = conn.cursor()
    start_time = time.time()  
    cur.execute('SELECT * FROM driver;')
    end_time = time.time()    
    
    columns = [desc[0] for desc in cur.description]  
    drivers = [dict(zip(columns, row)) for row in cur.fetchall()]  
    
    cur.close()
    conn.close()
    
    response_time = end_time - start_time 
    print(response_time)
    return drivers