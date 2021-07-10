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
                		'2iq', '2iq_short_interest_equity_curated_documentation.yaml')

AIRFLOW_CONF_DICT = {
    "dag": {
        "max_active_runs": 1,
        "owner": "CruxInformatics",
        "schedule_interval": '@daily',
        "priority_weight": 1,
        "dag_start_date": '2020-08-13',
        "dag_catchup": True,

    },
    "crux_api_conf": "${2IQ_SHORT_INTEREST_EQUITY_CURATED_DOCUMENTATION_API}",
    "endpoint": "${API_HOST}" 
}
dag = build_dag(WORKFLOW_FILE, AIRFLOW_CONF_DICT, PIPELINE_ENV)