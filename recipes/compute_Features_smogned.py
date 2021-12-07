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

features_smogned_df = features_joined_df # For this sample code, simply copy input to output


# Write recipe outputs
features_smogned = dataiku.Dataset("Features_smogned")
features_smogned.write_with_schema(features_smogned_df)
