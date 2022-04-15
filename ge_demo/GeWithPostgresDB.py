from logging.config import valid_ident
import pandas as pd
from sqlalchemy import create_engine
import great_expectations as ge
from great_expectations.cli.datasource import (
    sanitize_yaml_and_save_datasource,
    check_if_datasource_name_exists,
)
import yaml

from great_expectations.core.batch import BatchRequest, RuntimeBatchRequest

import psycopg2
from psycopg2 import pool
from ruamel import yaml



connection_string = "postgresql+psycopg2://postgres:sunny123@localhost:5432/postgre_flask"

# DB_HOST = "localhost"
# DB_NAME = "postgres"
# DB_USER = "postgre_flask"
# DB_PASS = "sunny123"

# connection_string = psycopg2.connect(host = DB_HOST, database = DB_NAME, user = DB_USER, password = DB_PASS)

datasource_config = {
    "name": 'my_datasource',
    "class_name": "Datasource",
    "execution_engine": {
        "class_name": "SqlAlchemyExecutionEngine",
        "connection_string": connection_string,
    },
    "data_connectors": {
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "batch_identifiers": ["default_identifier_name"],
        },
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetSqlDataConnector",
            "name": "whole_table",
        },
    },
}

context = ge.get_context()
context.test_yaml_config(yaml.dump(datasource_config))
context.add_datasource(**datasource_config)

batch_request = BatchRequest(
    datasource_name="my_datasource",
    data_connector_name="default_inferred_data_connector_name",
    # this is the name of the table you want to retrieve
    data_asset_name="public.user_details",
)

context.create_expectation_suite(
    expectation_suite_name="test_suite", overwrite_existing=True
)

validator = context.get_validator(
    batch_request=batch_request,
    expectation_suite_name="test_suite"
)



# print("validator: ", validator.head(20))
# print("Context: ", context)
# print(validator.expect_column_values_to_not_be_null("id"))

# print(validator.expect_column_min_to_be_between(column="id", min_value=50, max_value=60))
# print(validator.expect_table_row_count_to_be_between())

a = (validator.expect_column_mean_to_be_between(column="id", min_value=1, max_value=None))

# print(validator.expect_column_value_lengths_to_equal(column="name", value=4))
b= validator.head(20)
lst = []
for i in b.columns:
    lst+=[i]


print(sum(b[lst[0]]))

# print(validator.expect_column_values_to_be_alphabetical("name"))

