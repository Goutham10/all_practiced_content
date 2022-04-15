import great_expectations as ge
# import sys
# from great_expectations.checkpoint.types.checkpoint_result import CheckpointResult
# from great_expectations.data_context import DataContext
from ruamel import yaml

from great_expectations.core.batch import BatchRequest, RuntimeBatchRequest
# from .great_expectations.plugins.expectations.expect_column_values_to_be_specified_characters import ExpectColumnValuesToBeSpecifiedCharacters

from  .great_expectations.plugins.expectations.expect_column_values_max_to_be_between_custom import ExpectColumnMaxToBeBetweenCustom


context = ge.get_context()

datasource_config = {
    "name": "sample_datasource",
    "class_name": "Datasource",
    "module_name": "great_expectations.datasource",
    "execution_engine": {
        "module_name": "great_expectations.execution_engine",
        "class_name": "PandasExecutionEngine",
    },
    "data_connectors": {
        "default_runtime_data_connector_name": {
            "class_name": "RuntimeDataConnector",
            "module_name": "great_expectations.datasource.data_connector",
            "batch_identifiers": ["default_identifier_name"],
        },
        "default_inferred_data_connector_name": {
            "class_name": "InferredAssetFilesystemDataConnector",
            "base_directory": "/home/vy/sample.xls",
            "default_regex": {"group_names": ["data_asset_name"], "pattern": "(.*)"},
        },
    },
}

context.test_yaml_config(yaml.dump(datasource_config))
context.add_datasource(**datasource_config)

batch_request = RuntimeBatchRequest(
    datasource_name="sample_datasource",
    data_connector_name="default_runtime_data_connector_name",
    data_asset_name="tesingWithPandas",  # This can be anything that identifies this data_asset for you
    runtime_parameters={"path": "/home/vy/sample.xls"},  # Add your path here.
    batch_identifiers={"default_identifier_name": "default_identifier"},
)


context.create_expectation_suite(
    expectation_suite_name="test_suite", overwrite_existing=True
)
validator = context.get_validator(
    batch_request=batch_request, expectation_suite_name="test_suite"
)


# print(validator.head())


print(validator.expect_column_max_to_be_between_custom(column= "Age",min_value=1, max_value=10))