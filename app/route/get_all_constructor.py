from app.db_conn import get_db_connection
import time

def get_all_constructor():
    conn=get_db_connection()
    cur=conn.cursor()
    
    start_time=time.time()
    cur.execute('select * from constructor;')  
    columns = [desc[0] for desc in cur.description]  # Fetch column names
    constructor_list = [dict(zip(columns, row)) for row in cur.fetchall()]
    end_time=time.time()
    
    cur.close()
    conn.close()
    
    return constructor_list