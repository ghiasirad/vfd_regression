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




# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from sklearn.preprocessing import normalize

# Read recipe inputs
nanoStringDf = dataiku.Dataset("nanoStringDf")
nanoStringDf_df = nanoStringDf.get_dataframe()


# Normalize and return it as a dataframe
nanoString_cleaned_df = nanoStringDf_df.set_index('StudyIDUniversal')

# Remove the empty cells and replace them with median of the column
nanoString_cleaned_df.fillna(nanoString_cleaned_df.median(), inplace=True)
amioAcids_normalized_values = normalize(amioAcids_cleaned_df.values, axis=1, norm='l1')

amioAcids_normalized_df = pd.DataFrame(data=amioAcids_normalized_values, columns=amioAcids_cleaned_df.columns)
amioAcids_normalized_df['StudyID_Int'] = amioAcids_cleaned_df.index

first_column = amioAcids_normalized_df.pop('StudyID_Int')
amioAcids_normalized_df.insert(0, 'StudyID_Int', first_column)


aminoacids_normalized_df = amioAcids_normalized_df # For this sample code, simply copy input to output


# Write recipe outputs
aminoacids_normalized = dataiku.Dataset("Aminoacids_normalized")
aminoacids_normalized.write_with_schema(aminoacids_normalized_df)


