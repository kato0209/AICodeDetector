from airflow.backfill_job import BackfillJob from airflow.models.dagcode import DagCode from airflow.utils.db import create_session from airflow.utils.state import State from airflow.utils.dag_processing import SimpleDagBag, DagProcessing
from airflow.utils.state import State
import settings


class StateDBWrapper(object):
    def __init__(self, args): session = settings.Session() # create a session for the database use the session to clear out the dags that might be in the process of dags # currently running. Anything that was poorly written to the database for dag in session.query(DagBag).filter(DagBag.dag_id.in_(self.dags.values())):