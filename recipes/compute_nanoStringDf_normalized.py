# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
# from sklearn.preprocessing import normalize
from sklearn import preprocessing

# Read recipe inputs
nanoStringDf = dataiku.Dataset("nanoStringDf")
nanoStringDf_df = nanoStringDf.get_dataframe()


# Normalize and return it as a dataframe
nanoString_cleaned_df = nanoStringDf_df.set_index('StudyIDUniversal')

# Remove the empty cells and replace them with median of the column
nanoString_cleaned_df.fillna(nanoString_cleaned_df.median(), inplace=True)
# nanoString_normalized_values = normalize(nanoString_cleaned_df.values, axis=1, norm='l1')
min_max_scaler = preprocessing.MinMaxScaler()
nanoString_normalized_values = min_max_scaler.fit_transform(nanoString_cleaned_df.values)

nanoString_normalized_df = pd.DataFrame(data=nanoString_normalized_values, columns=nanoString_cleaned_df.columns)
nanoString_normalized_df['StudyIDUniversal'] = nanoString_cleaned_df.index

first_column = nanoString_normalized_df.pop('StudyIDUniversal')
nanoString_normalized_df.insert(0, 'StudyIDUniversal', first_column)


# Write recipe outputs
nanoStringDf_normalized = dataiku.Dataset("nanoStringDf_normalized")
nanoStringDf_normalized.write_with_schema(nanoString_normalized_df)


