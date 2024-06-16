from app.db_conn import get_db_connection

def get_race_winner_by_circuit(circuit_id):
    conn=get_db_connection();
    cur=conn.cursor()
    
    cur.execute("""
            SELECT 
            c.full_name,
            c.type AS circuit_type,
			c.place_name,
			r.year AS race_year,
	        r.date AS race_date,
	        r.distance AS race_distance,
	        r.laps,
	        r.scheduled_laps,
            d.name AS driver_name,
            cons.name AS constructor_name,
	        rd.race_time
            FROM race_data rd
                JOIN race r ON r.id = rd.race_id
                JOIN circuit c ON c.id = r.circuit_id
                JOIN driver d ON d.id = rd.driver_id
                JOIN constructor cons on rd.constructor_id=cons.id
                WHERE c.id LIKE %s
                    AND rd.type='RACE_RESULT'
                    AND rd.position_number=1
                """,(f"%{circuit_id}%",))  
    
    columns = [desc[0] for desc in cur.description]  # Fetch column names
    circuit_details = [dict(zip(columns, row)) for row in cur.fetchall()]
    
    cur.close()
    conn.close()
    return circuit_details