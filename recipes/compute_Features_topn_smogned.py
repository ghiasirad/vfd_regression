# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Features_joined_Nanostring_topn = dataiku.Dataset("Features_joined_Nanostring_topn")
Features_joined_Nanostring_topn_df = Features_joined_Nanostring_topn.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

Features_topn_smogned_df = Features_joined_Nanostring_topn_df # For this sample code, simply copy input to output


# Write recipe outputs
Features_topn_smogned = dataiku.Dataset("Features_topn_smogned")
Features_topn_smogned.write_with_schema(Features_topn_smogned_df)
