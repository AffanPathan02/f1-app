from app.db_conn import get_db_connection
import time
from app.utils import fetch_utils
from app.route.query import GET_ALL_CONTRUCTOR,GET_CONSTRUCTOR_BY_ID

def get_all_constructor():
    return fetch_utils.fetch_details(GET_ALL_CONTRUCTOR)

def get_constructor_by_id(constructor_id):
    return fetch_utils.fetch_details(GET_CONSTRUCTOR_BY_ID, (f"%{constructor_id}%",))
