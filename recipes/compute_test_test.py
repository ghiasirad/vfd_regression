# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Features_topn = dataiku.Dataset("Features_topn")
Features_topn_df = Features_topn.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

test_test_df = Features_topn_df # For this sample code, simply copy input to output
test_test_df2 = test_test_df

# Write recipe outputs
test_test = dataiku.Dataset("test_test")
test_test.write_with_schema(test_test_df)

test_test2 = dataiku.Dataset("test_test2")
test_test2.write_with_schema(test_test_df2)