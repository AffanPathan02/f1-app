from flask import jsonify, current_app,abort,request
from app import app
from app.route import get_all_driver,get_driver_by_id,get_all_constructor,get_constructor_by_id, get_driver_detail_by_position_number,get_race_details_by_circuit_id_and_year,get_race_winner_by_circuit

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
    
@app.route('/race/winner/<string:driver_id>')
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
