import great_expectations as ge
import re
import pandas as pd
from great_expectations.dataset import (
    PandasDataset,
    MetaPandasDataset,
)


class MyCustomPandasDataset(PandasDataset):

    _data_asset_type = "MyCustomPandasDataset"


    @MetaPandasDataset.column_map_expectation
    def expect_column_values_to_be_even(self, column):
        return column.map(lambda x: x%2==0)

    @MetaPandasDataset.column_map_expectation
    def expect_column_value_word_counts_to_be_between(self, column, min_value=None, max_value=None):
        def count_words(string):
            word_list = re.findall("(\S+)", string)
            return len(word_list)

        word_counts = column.map(lambda x: count_words(str(x)))

        if min_value is not None and max_value is not None:
            return word_counts.map(lambda x: min_value <= x <= max_value)
        elif min_value is not None and max_value is None:
            return word_counts.map(lambda x: min_value <= x)
        elif min_value is None and max_value is not None:
            return word_counts.map(lambda x: x <= max_value)
        else:
            return word_counts.map(lambda x: True)

        
my_pd_df = pd.read_excel("/home/vy/sample.xls")
my_df = ge.from_pandas(my_pd_df, dataset_class=MyCustomPandasDataset)

print(my_df.expect_column_values_to_be_even("Age"))

# print(my_df.expect_column_value_word_counts_to_be_between("Country"))

# a = my_df.expect_column_values_to_be_in_set("Gender", ["Male", "Female"])


# print(my_df)


