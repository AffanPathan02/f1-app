from app.db_conn import get_db_connection

def get_constructor_by_id(constructor_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM constructor WHERE id = %s;', (constructor_id,))
    columns = [desc[0] for desc in cur.description]
    constructor = cur.fetchone()
    print(constructor)
    cur.close()
    conn.close()
    return dict(zip(columns, constructor))