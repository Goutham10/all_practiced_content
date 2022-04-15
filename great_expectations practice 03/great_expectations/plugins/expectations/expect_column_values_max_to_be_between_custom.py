"""
Example of custom expectation with renderer.

This custom expectation can be run as part of a checkpoint with the script run_checkpoint_with_custom_expectation.py
in the getting_started_tutorial_final_v3_api directory, e.g.

getting_started_tutorial_final_v3_api$ python run_checkpoint_with_custom_expectation.py

See corresponding documentation:
* https://docs.greatexpectations.io/en/latest/guides/how_to_guides/creating_and_editing_expectations/how_to_create_custom_expectations.html
* https://docs.greatexpectations.io/en/latest/guides/how_to_guides/configuring_data_docs/how_to_create_renderers_for_custom_expectations.html
"""

from great_expectations.core import ExpectationConfiguration, ExpectationValidationResult
from great_expectations.execution_engine import (
   ExecutionEngine,
   PandasExecutionEngine,
   SparkDFExecutionEngine,
   SqlAlchemyExecutionEngine,
)
from great_expectations.expectations.expectation import ColumnExpectation
from great_expectations.expectations.metrics import (
   ColumnAggregateMetricProvider,
   column_aggregate_value, column_aggregate_partial,
)
from great_expectations.expectations.metrics.import_manager import F, sa
#from great_expectations.expectations.util import render_evaluation_parameter_string
#from great_expectations.render.renderer.renderer import renderer
#from great_expectations.render.types import RenderedStringTemplateContent, RenderedTableContent, RenderedBulletListContent, RenderedGraphContent
#from great_expectations.render.util import substitute_none_for_missing 

from typing import Any, Dict, List, Optional, Union


class ColumnCustomMax(ColumnAggregateMetricProvider ):
    """MetricProvider Class for Custom Aggregate Max MetricProvider"""

    metric_name = "column.aggregate.custom.max"



    @column_aggregate_partial(engine=SqlAlchemyExecutionEngine)
    def _sqlalchemy(cls, column, **kwargs):
        """SqlAlchemy Max Implementation"""
        return sa.func.max(column)



class ExpectColumnMaxToBeBetweenCustom(ColumnExpectation):
    # Setting necessary computation metric dependencies and defining kwargs, as well as assigning kwargs default values
    metric_dependencies = ("column.aggregate.custom.max",)
    success_keys = ("min_value", "strict_min", "max_value", "strict_max")

    # Default values
    default_kwarg_values = {
        "row_condition": None,
        "condition_parser": None,
        "min_value": None,
        "max_value": None,
        "strict_min": None,
        "strict_max": None,
        "mostly": 1
    }

    def _validate(
        self,
        configuration: ExpectationConfiguration,
        metrics: Dict,
        runtime_configuration: dict = None,
        execution_engine: ExecutionEngine = None,
    ):
        """Validates the given data against the set minimum and maximum value thresholds for the column max"""
        column_max = metrics["column.aggregate.custom.max"]

        # Obtaining components needed for validation
        min_value = self.get_success_kwargs(configuration).get("min_value")
        strict_min = self.get_success_kwargs(configuration).get("strict_min")
        max_value = self.get_success_kwargs(configuration).get("max_value")
        strict_max = self.get_success_kwargs(configuration).get("strict_max")

        # Checking if mean lies between thresholds
        if min_value is not None:
            if strict_min:
                above_min = column_max > min_value
            else:
                above_min = column_max >= min_value
        else:
            above_min = True

        if max_value is not None:
            if strict_max:
                below_max = column_max < max_value
            else:
                below_max = column_max <= max_value
        else:
            below_max = True

        success = above_min and below_max

        return {"success": success, "result": {"observed_value": column_max}}

    def validate_configuration(self, configuration: Optional[ExpectationConfiguration]):
        """
        Validates that a configuration has been set, and sets a configuration if it has yet to be set. Ensures that
        necessary configuration arguments have been provided for the validation of the expectation.

        Args:
            configuration (OPTIONAL[ExpectationConfiguration]): \
                An optional Expectation Configuration entry that will be used to configure the expectation
        Returns:
            True if the configuration has been validated successfully. Otherwise, raises an exception
        """
        min_val = None
        max_val = None

        # Setting up a configuration
        super().validate_configuration(configuration)
        if configuration is None:
            configuration = self.configuration

        # Ensuring basic configuration parameters are properly set
        try:
            assert (
                "column" in configuration.kwargs
            ), "'column' parameter is required for column map expectations"
        except AssertionError as e:
            raise (str(e))

        # Validating that Minimum and Maximum values are of the proper format and type
        if "min_value" in configuration.kwargs:
            min_val = configuration.kwargs["min_value"]

        if "max_value" in configuration.kwargs:
            max_val = configuration.kwargs["max_value"]

        try:
            # Ensuring Proper interval has been provided
            assert (
                min_val is not None or max_val is not None
            ), "min_value and max_value cannot both be none"
            assert min_val is None or isinstance(
                min_val, (float, int)
            ), "Provided min threshold must be a number"
            assert max_val is None or isinstance(
                max_val, (float, int)
            ), "Provided max threshold must be a number"
        except AssertionError as e:
            raise (str(e))
