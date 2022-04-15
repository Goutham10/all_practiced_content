import great_expectations as ge
import pandas as pd
# from .great_expectations.plugins.expectations.custom_pandas_dataset import expect_column_values_to_be_even
from datetime import datetime
# context = ge.DataContext()
# context.create_expectation_suite("my_new_suite")
# my_batch = context.get_batch({
#     "path": "/home/vy/sample.xls",
#     "datasource": "my_data__dir"
# }, "my_new_suite")

# my_batch.expect_column_values_to_be_even("Age")


# my_pd_df = pd.read_excel("/home/vy/sample.xls")
# my_df = ge.from_pandas(my_pd_df)
# print(my_df)
# # print(my_df.expect_column_values_to_be_even("Age"))


print(datetime.now().strftime("%m-%d-%Y"))