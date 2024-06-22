GET_RACE_DETAILS_BY_CIRCUIT_ID_AND_YEAR="""
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
	                AND rd.type='RACE_RESULT'
                ORDER BY rd.position_number ASC
"""

GET_QUALIFICATION_DETAILS_BY_TYPE_BY_CIRCUIT_BY_YEAR="""
                SELECT * FROM get_qualifying_results(%s,%s,%s);
"""

GET_FREE_PRACTICE_DETAILS_BY_SESSION_BY_CIRCUIT_BY_YEAR="""
    SELECT * FROM get_free_practice_results(%s,%s,%s); 
"""

GET_SPRINT_RACE_DETAILS_BY_CIRCUIT_BY_YEAR="""
        SELECT 
            c.full_name,
            c.type AS circuit_type,
			c.place_name,
			r.year AS race_year,
	        r.date AS race_date,
	        r.distance AS race_distance,
			rd.race_time AS sprint_time,
			rd.race_gap AS sprint_gap,
			rd.race_interval AS sprint_interval,
            d.name AS driver_name,
            cons.name AS constructor_name,
	        rd.race_time
        FROM race_data rd
            JOIN race r ON r.id = rd.race_id
            JOIN circuit c ON c.id = r.circuit_id
            JOIN driver d ON d.id = rd.driver_id
            JOIN constructor cons on rd.constructor_id=cons.id
        WHERE c.id LIKE %s
            AND rd.type='SPRINT_RACE_RESULT'
            AND r.year=%s
		ORDER bY rd.position_number ASC
"""

GET_SPRINT_QUALIFICATION_DETAILS_BY_CIRCUIT_BY_YEAR="""
        SELECT 
            c.full_name,
            c.type AS circuit_type,
			c.place_name,
			r.year AS race_year,
	        r.date AS race_date,
	        r.distance AS race_distance,
            rd.position_number,
	 		rd.qualifying_laps,
			rd.qualifying_q1 AS sq1,
			rd.qualifying_q2 AS sq2,
	 		rd.qualifying_q3 AS sq3,
			rd.qualifying_gap AS sq3_gap,
	 		rd.qualifying_interval AS sq3_interval,
            d.name AS driver_name,
            cons.name AS constructor_name,
	        rd.race_time
        FROM race_data rd
            JOIN race r ON r.id = rd.race_id
            JOIN circuit c ON c.id = r.circuit_id
            JOIN driver d ON d.id = rd.driver_id
            JOIN constructor cons on rd.constructor_id=cons.id
        WHERE c.id LIKE %s
            AND rd.type='SPRINT_QUALIFYING_RESULT'
            AND r.year=%s
		ORDER bY rd.position_number ASC
                 
"""

GET_RACE_WINNER_BY_CIRCUIT="""
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
                """

GET_ALL_DRIVER="SELECT * FROM driver;"

GET_DRIVER_BY_ID="""SELECT * FROM driver WHERE id LIKE %s;"""

GET_DRIVER_DETAIL_BY_POSITION_NUMBER="""
                SELECT r.official_name, d.name AS driver_name,
                       rd.position_number, rd.race_time, rd.race_grid_position_text
                FROM race_data rd
                JOIN race r ON r.id = rd.race_id
                JOIN driver d ON d.id = rd.driver_id
                WHERE rd.position_number = %s
                AND rd.type = 'RACE_RESULT'
                AND d.id LIKE %s
                """

GET_DRIVER_DETAIL_BY_CIRCUIT="""
SELECT 
            c.full_name,
            c.type AS circuit_type,
			c.place_name,
			r.year AS race_year,
            d.name AS driver_name,
            cons.name AS constructor_name,
	        rd.race_time,
			rd.position_number,
			rd.race_grid_position_text 
            FROM race_data rd
                JOIN race r ON r.id = rd.race_id
                JOIN circuit c ON c.id = r.circuit_id
                JOIN driver d ON d.id = rd.driver_id
                JOIN constructor cons on rd.constructor_id=cons.id
                WHERE d.id LIKE %s
                AND c.id LIKE %s
                    
"""
                
GET_ALL_CONTRUCTOR="""select * from constructor;"""

GET_CONSTRUCTOR_BY_ID="""SELECT * FROM constructor WHERE id LIKE %s;"""

