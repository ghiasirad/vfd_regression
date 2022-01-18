

# Read recipe inputs
DemographicData_prepared = dataiku.Dataset("DemographicData_prepared")
DemographicData_prepared_df = DemographicData_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

DemographicData_prepared_normal_df = DemographicData_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
DemographicData_prepared_normal = dataiku.Dataset("DemographicData_prepared_normal")
DemographicData_prepared_normal.write_with_schema(DemographicData_prepared_normal_df)




# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
# from sklearn.preprocessing import normalize
from sklearn import preprocessing

# Read recipe inputs
DemographicData_prepared = dataiku.Dataset("DemographicData_prepared")
DemographicData_prepared_df = DemographicData_prepared.get_dataframe()


# Normalize and return it as a dataframe
DemographicData_prepared_df = DemographicData_prepared_df.set_index('StudyID')

# Remove the empty cells and replace them with median of the column
DemographicData_prepared_df.fillna(DemographicData_prepared_df.median(), inplace=True)
# nanoString_normalized_values = normalize(nanoString_cleaned_df.values, axis=1, norm='l1')
min_max_scaler = preprocessing.MinMaxScaler()
nanoString_normalized_values = min_max_scaler.fit_transform(DemographicData_prepared_df.values)

nanoString_normalized_df = pd.DataFrame(data=nanoString_normalized_values, columns=nanoString_cleaned_df.columns)
nanoString_normalized_df['StudyIDUniversal'] = nanoString_cleaned_df.index

first_column = nanoString_normalized_df.pop('StudyIDUniversal')
nanoString_normalized_df.insert(0, 'StudyIDUniversal', first_column)


# Write recipe outputs
nanoStringDf_normalized = dataiku.Dataset("nanoStringDf_normalized")
nanoStringDf_normalized.write_with_schema(nanoString_normalized_df)



