from app.db_conn import get_db_connection
from app.utils import fetch_utils
from app.query import GET_RACE_DETAILS_BY_CIRCUIT_ID_AND_YEAR,GET_QUALIFICATION_DETAILS_BY_CIRCUIT_BY_YEAR

def get_race_details_by_circuit_id_and_year(circuit_id,year):
    return fetch_utils.fetch_details(GET_RACE_DETAILS_BY_CIRCUIT_ID_AND_YEAR,(f"%{circuit_id}%",year))

def get_qualification_details_by_circuit_by_year(circuit_id,year):
    return fetch_utils.fetch_details(GET_QUALIFICATION_DETAILS_BY_CIRCUIT_BY_YEAR,(f"%{circuit_id}%",year))

