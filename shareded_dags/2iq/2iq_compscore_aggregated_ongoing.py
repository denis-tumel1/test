import os
import logging
log = logging.getLogger(__name__)
"""Below comment is required for the DAG to load per: 
https://github.com/apache/incubator-airflow/blob/1.9.0/airflow/models.py#L270"""
# airflow DAG
from pipeline.airflow.dag_builder import build_dag

PIPELINE_ENV = os.environ.get('PIPELINE_ENVIRONMENT', 'dev')

CONFIG_DIRECTORY = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..', '..', '..', 'conf')
WORKFLOW_DIRECTORY = os.path.join(CONFIG_DIRECTORY, 'workflows')
WORKFLOW_FILE = os.path.join(WORKFLOW_DIRECTORY, 
                		'2iq', '2iq_compscore_aggregated_ongoing.yaml')

AIRFLOW_CONF_DICT = {
    "dag": {
        "max_active_runs": 10,
        "owner": "CruxInformatics",
        "schedule_interval": '20 15 * * 0',
        "priority_weight": 1,
        "dag_start_date": '2020-08-06',
        "dag_catchup": True

    },
    "crux_api_conf": "${2IQ_COMPSCORE_AGGREGATED_ONGOING_API}",
    "endpoint": "${API_HOST}" 
}
dag = build_dag(WORKFLOW_FILE, AIRFLOW_CONF_DICT, PIPELINE_ENV)