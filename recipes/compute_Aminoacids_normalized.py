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

# Remove the empty cells and replace them with median of the column
amioAcids_cleaned_df.fillna(amioAcids_cleaned_df.median(), inplace=True)
amioAcids_normalized_values = normalize(amioAcids_cleaned_df.values, axis=1, norm='l1')

amioAcids_normalized_df = pd.DataFrame(data=amioAcids_normalized_values, columns=amioAcids_cleaned_df.columns)
amioAcids_normalized_df['StudyID_Int'] = amioAcids_cleaned_df.index

first_column = amioAcids_normalized_df.pop('StudyID_Int')
damioAcids_normalized_dff.insert(0, 'StudyID_Int', first_column)


aminoacids_normalized_df = amioAcids_normalized_df # For this sample code, simply copy input to output


# Write recipe outputs
aminoacids_normalized = dataiku.Dataset("Aminoacids_normalized")
aminoacids_normalized.write_with_schema(aminoacids_normalized_df)
