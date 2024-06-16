from flask import jsonify, current_app,abort,request
from app import app
from app.route import get_all_driver,get_driver_by_id,get_all_constructor,get_constructor_by_id, get_driver_race_detail_by_position_number,get_circuit_details_by_year

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

@app.route('/race/')
def get_driver_race_position_by_position_endpoint():
    position_number = request.args.get('position_number')
    driver_id=request.args.get('driver_id')
    if position_number is None:
        return jsonify(message="Position number parameter is required"), 400
    
    winners = get_driver_race_detail_by_position_number(driver_id, position_number)
    
    if winners:
        return jsonify(winners=winners)
    else:
        return jsonify(message=f"No race found for driver_id {driver_id} and position_number {position_number}"), 404
    
@app.route('/race/winner')
def get_race_winners_by_driver_endpoint():
    driver_id=request.args.get('driver_id')
    position_number=1
    
    winners = get_driver_race_detail_by_position_number(driver_id, position_number)
    
    if winners:
        return jsonify(winners=winners)
    else:
        return jsonify(message=f"No winners found for driver_id {driver_id} "), 404

@app.route('/race/circuit')    
def get_circuit_details_by_year_endpoint():
    circuit_id=request.args.get('circuit_id')
    year=request.args.get('year')
    
    circuit_detail=get_circuit_details_by_year(circuit_id,year)
    
    if circuit_detail:
        return jsonify(circuit_detail=circuit_detail)
    else:
        return jsonify(message=f"No circuit detail for {circuit_id} for the year {year}"),404
