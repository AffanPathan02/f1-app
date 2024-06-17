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
	                AND rd.type='RACE_RESULT';
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
                
GET_ALL_CONTRUCTOR="""select * from constructor;"""

GET_CONSTRUCTOR_BY_ID="""SELECT * FROM constructor WHERE id LIKE %s;"""

