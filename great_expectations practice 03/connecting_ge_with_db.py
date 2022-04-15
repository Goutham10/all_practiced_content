from asyncio import FastChildWatcher
from ruamel import yaml

import great_expectations as ge
from great_expectations.core.batch import BatchRequest, RuntimeBatchRequest
from great_expectations.profile.user_configurable_profiler import (
    UserConfigurableProfiler,
)

from great_expectations.checkpoint import SimpleCheckpoint

# from .great_expectations.plugins.expectations.expect_column_values_to_be_specified_characters import ExpectColumnValuesToBeSpecifiedCharacters

context = ge.get_context()

datasource_config = {
    "name": "my_postgres_datasource",
    "class_name": "Datasource",
    "execution_engine": {
        "class_name": "SqlAlchemyExecutionEngine",
        "connection_string": "postgresql+psycopg2://postgres:sunny123@localhost:5432/postgre_flask",
    },
    "data_connectors": {
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "batch_identifiers": ["default_identifier_name"],
        },
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetSqlDataConnector",
            "include_schema_name": True,
        },
    },
}

context.test_yaml_config(yaml.dump(datasource_config))

context.add_datasource(**datasource_config)


batch_request = BatchRequest(
    datasource_name="my_postgres_datasource",
    data_connector_name="default_inferred_data_connector_name",
    data_asset_name="public.user_details",  # this is the name of the table you want to retrieve
)

expectation_suite_name="connecting_with_psql"

context.create_expectation_suite(
    expectation_suite_name="connecting_with_psql", overwrite_existing=True
)
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="connecting_with_psql"
)


ignored_columns = []

profiler = UserConfigurableProfiler(
    profile_dataset=validator,
    excluded_expectations=None,
    ignored_columns=ignored_columns,
    not_null_only=False,
    primary_or_compound_key=["id", "name"],
    semantic_types_dict=None,
    table_expectations_only=False,
    value_set_threshold="MANY",
)

suite = profiler.build_suite()
print(suite)

context.save_expectation_suite(suite) #creates the json file with expectation suite name in expectations folder 

checkpoint_config = {
    "class_name": "SimpleCheckpoint",
    "validations": [
        {
            "batch_request": batch_request,
            "expectation_suite_name": expectation_suite_name,
        }
    ],
}
checkpoint = SimpleCheckpoint(f"_tmp_checkpoint_{expectation_suite_name}",context,**checkpoint_config)
checkpoint_result = checkpoint.run()


# validation_result_identifier = (checkpoint_result.list_validation_result_identifiers()[0])

# print(validation_result_identifier)
context.build_data_docs()   #UI view of applied expectations in data docs/expectations/"suite_name".json


########################################################

# batch_request_1 = BatchRequest(
#     datasource_name="my_postgres_datasource",
#     data_connector_name="default_inferred_data_connector_name",
#     data_asset_name="public.car",  # this is the name of the table you want to retrieve
# )

# expectation_suite_name_1="connecting_with_psql_1"

# context.create_expectation_suite(
#     expectation_suite_name="connecting_with_psql_1", overwrite_existing=True
# )
# validator_1 = context.get_validator(
#     batch_request=batch_request, expectation_suite_name="connecting_with_psql_1"
# )


# ignored_columns_1 = []

# profiler_1 = UserConfigurableProfiler(
#     profile_dataset=validator_1,
#     excluded_expectations=None,
#     ignored_columns=ignored_columns_1,
#     not_null_only=False,
#     primary_or_compound_key=["id", "name"],
#     semantic_types_dict=None,
#     table_expectations_only=False,
#     value_set_threshold="MANY",
# )

# suite_1 = profiler_1.build_suite()
# print(suite_1)

# context.save_expectation_suite(suite_1) #creates the json file with expectation suite name in expectations folder 

# checkpoint_config_1 = {
#     "class_name": "SimpleCheckpoint",
#     "validations": [
#         {
#             "batch_request": batch_request_1,
#             "expectation_suite_name": expectation_suite_name_1,
#         }
#     ],
# }
# checkpoint_1 = SimpleCheckpoint(f"_tmp_checkpoint_{expectation_suite_name_1}",context,**checkpoint_config_1)
# checkpoint_result = checkpoint_1.run()


# # validation_result_identifier = (checkpoint_result.list_validation_result_identifiers()[0])

# # print(validation_result_identifier)
# context.build_data_docs()   #UI view of applied expectations in data docs/expectations/"suite_name".json
