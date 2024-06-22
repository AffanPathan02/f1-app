from app.db_conn import get_db_connection
import time
from app.utils import fetch_utils
from app.route.query import GET_ALL_DRIVER,GET_DRIVER_BY_ID,GET_DRIVER_DETAIL_BY_POSITION_NUMBER,GET_DRIVER_DETAIL_BY_CIRCUIT

def get_all_driver():
    return fetch_utils.fetch_details(GET_ALL_DRIVER)

def get_driver_by_id(driver_id):
    return fetch_utils.fetch_details(GET_DRIVER_BY_ID,(f"%{driver_id}%",))

def get_driver_detail_by_position_number(driver_id, position_number):
    return fetch_utils.fetch_details(GET_DRIVER_DETAIL_BY_POSITION_NUMBER,(position_number, f"%{driver_id}%"))

def get_driver_details_by_circuit(driver_id,circuit_id):
    return fetch_utils.fetch_details(GET_DRIVER_DETAIL_BY_CIRCUIT,(f"%{driver_id}%",f"%{circuit_id}%"))
    
    