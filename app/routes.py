from flask import jsonify, current_app,abort
from app import app
from app.route import get_all_driver,get_driver_by_id

@app.route('/')
def get_all_driver_endpoint():
    drivers = getget_all_driver()
    return jsonify(drivers=drivers)

@app.route('/driver/<string:driver_id>')
def get_driver_id_endpoint(driver_id):
    driver=get_driver_by_id(driver_id)
    if driver is None:
        abort(404, description=f"Driver with id {driver_id} not found")
    return jsonify(driver=driver)
