from app.db_conn import get_db_connection

def get_race_details_by_circuit_id_and_year(circuit_id,year):
    conn=get_db_connection()
    cur=conn.cursor()
    cur.execute("""
                SELECT 
                    c.name AS circuit_name, 
                    r.year, 
                    d.name AS driver_name, 
                    rd.position_number,
                    cons.name AS constructor_name,
                    rd.race_time,
                    rd.race_gap,
                    rd.race_interval,
                    rd.race_points,
                    rd.race_grid_position_number AS starting_grid_position,
                    rd.race_pit_stops as pit_stops
                FROM race_data rd
                JOIN race r ON r.id = rd.race_id
                JOIN circuit c ON c.id = r.circuit_id
                JOIN driver d ON d.id = rd.driver_id
                JOIN constructor cons on rd.constructor_id=cons.id
                WHERE c.id LIKE %s
                    AND r.year = %s
	                AND rd.type='RACE_RESULT';
                 """,(f"%{circuit_id}%", year))
    columns = [desc[0] for desc in cur.description]
    circuit_details = [dict(zip(columns, row)) for row in cur.fetchall()]
    cur.close()
    conn.close()
    return circuit_details

