# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
nanoStringDf = dataiku.Dataset("nanoStringDf")
nanoStringDf_df = nanoStringDf.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

nanoStringDf_normalized_df = nanoStringDf_df # For this sample code, simply copy input to output


# Write recipe outputs
nanoStringDf_normalized = dataiku.Dataset("nanoStringDf_normalized")
nanoStringDf_normalized.write_with_schema(nanoStringDf_normalized_df)
