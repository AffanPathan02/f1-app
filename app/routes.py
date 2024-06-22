from flask import jsonify, current_app,abort,request
from app import app
from app.route import get_all_driver,get_driver_by_id,get_all_constructor,get_constructor_by_id, get_driver_detail_by_position_number,get_race_details_by_circuit_id_and_year,get_race_winner_by_circuit,get_driver_details_by_circuit,get_qualification_details_by_circuit_by_year,get_free_practise_details_by_circuit_by_year

@app.route('/driver/')
def get_all_driver_endpoint():
    drivers_list = get_all_driver()
    if drivers_list is None:
        abort(404,descitpion="No driver list available")
    return jsonify(drivers=drivers_list)

@app.route('/driver/<string:driver_id>')
def get_driver_id_endpoint(driver_id):
    driver=get_driver_by_id(driver_id)
    if driver is None:
        abort(404, description=f"Driver with id {driver_id} not found")
    return jsonify(driver=driver)

@app.route('/driver/<string:driver_id>/<int:position_number>')
def get_driver_details_by_position_endpoint(driver_id,position_number):
    if position_number is None:
        return jsonify(message="position parameter is required"), 400
    if driver_id is None:
        return jsonify(message="driver_id parameter is required"), 400
    
    winners = get_driver_detail_by_position_number(driver_id, position_number)
    
    if winners:
        return jsonify(winners=winners)
    else:
        return jsonify(message=f"No race found for driver_id {driver_id} and position_number {position_number}"), 404

@app.route('/driver/<string:driver_id>/<string:circuit_id>')
def get_driver_details_by_circuit_endpoint(driver_id,circuit_id):
    if driver_id is None:
        return jsonify(message="driver_id parameter is required"), 400
    if circuit_id is None:
        return jsonify(message="circuit_id parameter is required"), 400
    
    driver_details = get_driver_details_by_circuit(driver_id,circuit_id)
    
    if driver_details:
        return jsonify(driver_details=driver_details)
    else:
        return jsonify(message=f"No race found for driver_id {driver_id} and circuit_id {circuit_id}"), 404
  
@app.route('/constructor/')
def get_constructor_endpoint():
    constructor_list=get_all_constructor()
    if constructor_list is None:
        abort(404,"No constructor list available")
    return jsonify(constructor_list=constructor_list)

@app.route('/constructor/<string:constructor_id>')
def get_constructor_id_endpoint(constructor_id):
    constructor=get_constructor_by_id(constructor_id)
    if constructor is None:
        abort(404, description=f"constructor with id {constructor_id} not found")
    return jsonify(constructor=constructor)
    
@app.route('/race/driver/<string:driver_id>')
def get_race_winners_by_driver_endpoint(driver_id):
    position_number=1
    
    winners = get_driver_detail_by_position_number(driver_id, position_number)
    
    if winners:
        return jsonify(winners=winners)
    else:
        return jsonify(message=f"No winners found for driver_id {driver_id} "), 404

@app.route('/race/circuit/<string:circuit_id>')    
def get_race_winner_by_circuit_endpoint(circuit_id):    
    circuit_detail=get_race_winner_by_circuit(circuit_id)
    
    if circuit_detail:
        return jsonify(circuit_detail=circuit_detail)
    else:
        return jsonify(message=f"No circuit detail for {circuit_id} for the year {year}"),404

@app.route('/race/circuit/<string:circuit_id>/<int:year>')    
def get_race_details_by_circuit_id_and_year_endpoint(circuit_id,year):    
    circuit_detail=get_race_details_by_circuit_id_and_year(circuit_id,year)
    
    if circuit_detail:
        return jsonify(race_detail=circuit_detail)
    else:
        return jsonify(message=f"No race detail for {circuit_id} for the year {year}"),404

@app.route('/race/q3/<string:circuit_id>/<int:year>')
def get_q3_details_by_circuit_by_year_endpoint(circuit_id,year):
    quali_session=3
    q3_details=get_qualification_details_by_circuit_by_year(quali_session,circuit_id,year)
    
    if q3_details:
        return jsonify(q3_details=q3_details)
    else:
        return jsonify(message=f"No q3 detail for {circuit_id} for the year {year}"),404

@app.route('/race/q2/<string:circuit_id>/<int:year>')
def get_q2_details_by_circuit_by_year_endpoint(circuit_id,year):
    quali_session=2
    q2_details=get_qualification_details_by_circuit_by_year(quali_session,circuit_id,year)
    
    if q2_details:
        return jsonify(q2_details=q2_details)
    else:
        return jsonify(message=f"No q2 detail for {circuit_id} for the year {year}"),404
    
@app.route('/race/q1/<string:circuit_id>/<int:year>')
def get_q1_details_by_circuit_by_year_endpoint(circuit_id,year):
    quali_session=1
    q1_details=get_qualification_details_by_circuit_by_year(quali_session,circuit_id,year)
    
    if q1_details:
        return jsonify(q1_details=q1_details)
    else:
        return jsonify(message=f"No q1 detail for {circuit_id} for the year {year}"),404

@app.route('/race/fp1/<string:circuit_id>/<int:year>')
def get_fp1_details_by_circuit_by_year_endpoint(circuit_id,year):
    practice_session=1
    fp1_details=get_free_practise_details_by_circuit_by_year(practice_session,circuit_id,year)
    
    if fp1_details:
        return jsonify(fp1_details=fp1_details)
    else:
        return jsonify(message=f"No free practice 1 detail for {circuit_id} for the year {year}"),404
    
@app.route('/race/fp2/<string:circuit_id>/<int:year>')
def get_fp2_details_by_circuit_by_year_endpoint(circuit_id,year):
    practice_session=2
    fp2_details=get_free_practise_details_by_circuit_by_year(practice_session,circuit_id,year)
    
    if fp2_details:
        return jsonify(fp2_details=fp2_details)
    else:
        return jsonify(message=f"No free practice 2 detail for {circuit_id} for the year {year}"),404
    
@app.route('/race/fp3/<string:circuit_id>/<int:year>')
def get_fp3_details_by_circuit_by_year_endpoint(circuit_id,year):
    practice_session=3
    fp3_details=get_free_practise_details_by_circuit_by_year(practice_session,circuit_id,year)
    
    if fp3_details:
        return jsonify(fp3_details=fp3_details)
    else:
        return jsonify(message=f"No free practice 3 detail for {circuit_id} for the year {year}"),404