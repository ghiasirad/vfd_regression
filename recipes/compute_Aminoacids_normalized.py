# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from sklearn.preprocessing import normalize

# Read recipe inputs
amioAcids_cleaned = dataiku.Dataset("AmioAcids_cleaned")
amioAcids_cleaned_df = amioAcids_cleaned.get_dataframe()


# Normalize and return it as a dataframe
amioAcids_cleaned_df = amioAcids_cleaned_df.set_index('StudyID_Int')
amioAcids_cleaned_df = normalize(amioAcids_cleaned_df.values, axis=1, norm='l1')

aminoacids_normalized_df = amioAcids_cleaned_df # For this sample code, simply copy input to output


# Write recipe outputs
aminoacids_normalized = dataiku.Dataset("Aminoacids_normalized")
aminoacids_normalized.write_with_schema(aminoacids_normalized_df)
