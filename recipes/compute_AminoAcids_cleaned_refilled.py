# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
amioAcids_cleaned = dataiku.Dataset("AmioAcids_cleaned")
amioAcids_cleaned_df = amioAcids_cleaned.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

aminoAcids_cleaned_refilled_df = amioAcids_cleaned_df # For this sample code, simply copy input to output


# Write recipe outputs
aminoAcids_cleaned_refilled = dataiku.Dataset("AminoAcids_cleaned_refilled")
aminoAcids_cleaned_refilled.write_with_schema(aminoAcids_cleaned_refilled_df)
