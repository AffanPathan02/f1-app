from app.db_conn import get_db_connection

def get_driver_by_id(driver_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM driver WHERE id = %s;', (driver_id,))
    driver = cur.fetchone()
    cur.close()
    conn.close()
    return driver