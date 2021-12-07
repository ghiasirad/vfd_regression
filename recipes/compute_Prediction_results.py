# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
features_joined = dataiku.Dataset("Features_joined")
features_joined_df = features_joined.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

prediction_results_df = features_joined_df # For this sample code, simply copy input to output


# Write recipe outputs
prediction_results = dataiku.Dataset("Prediction_results")
prediction_results.write_with_schema(prediction_results_df)
