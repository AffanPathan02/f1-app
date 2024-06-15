from flask import jsonify, current_app,abort
from app import app
from app.route import get_all_driver,get_driver_by_id,get_all_constructor,get_constructor_by_id

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
