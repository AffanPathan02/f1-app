from app.db_conn import get_db_connection

def get_all_driver():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM driver;')
    drivers = cur.fetchall()
    cur.close()
    conn.close()
    return drivers