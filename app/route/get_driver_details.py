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

def get_driver_by_id(driver_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM driver WHERE id LIKE %s;', (f"%{driver_id}%",))
    columns = [desc[0] for desc in cur.description]
    driver = [dict(zip(columns, row)) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return driver

def get_driver_detail_by_position_number(driver_id, position_number):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
                SELECT r.official_name, d.name AS driver_name,
                       rd.position_number, rd.race_time, rd.race_grid_position_text
                FROM race_data rd
                JOIN race r ON r.id = rd.race_id
                JOIN driver d ON d.id = rd.driver_id
                WHERE rd.position_number = %s
                AND rd.type = 'RACE_RESULT'
                AND d.id LIKE %s
                """, (position_number, f"%{driver_id}%"))
    
    columns = [desc[0] for desc in cur.description]
    race_details = [dict(zip(columns, row)) for row in cur.fetchall()]
    print(len(race_details))
    cur.close()
    conn.close()
    
    return race_details
