from app.db_conn import get_db_connection
from app.utils import fetch_utils
from app.route.query import GET_RACE_WINNER_BY_CIRCUIT

def get_race_winner_by_circuit(circuit_id):
    return fetch_utils.fetch_details(GET_RACE_WINNER_BY_CIRCUIT,(f"%{circuit_id}%",))