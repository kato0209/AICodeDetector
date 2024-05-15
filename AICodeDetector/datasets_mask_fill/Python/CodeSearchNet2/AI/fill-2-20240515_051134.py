from django.conf import settings
from django.utils.timezone import now

from airflow from airflow.operators.dummy_operator import DummyOperator from airflow.operators.subdag_operator import SubDagOperator import airflow.operators.subdag_operator dag = DAG( 'test_perm_vm_for_all_dag', start_date=DEFAULT_DATE, default_args={'owner': 'owner1'}) with dag: op1 = DummyOperator(task_id='A') op2 = DummyOperator(task_id='B')