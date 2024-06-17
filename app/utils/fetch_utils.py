from app.db_conn import get_db_connection

def fetch_details(query,params=None):
    conn = get_db_connection()
    cur = conn.cursor()
    
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)
    
    columns = [desc[0] for desc in cur.description]
    details = [dict(zip(columns, row)) for row in cur.fetchall()]
    
    cur.close()
    conn.close()
    
    return details