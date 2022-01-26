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
# DemographicData_prepared_df = DemographicData_prepared_df.set_index('Study ID')

# Remove the empty cells and replace them with median of the column
DemographicData_prepared_df.fillna(DemographicData_prepared_df.median(), inplace=True)
min_max_scaler = preprocessing.MinMaxScaler()
DemographicData_normalized_values = min_max_scaler.fit_transform(DemographicData_prepared_df[['Age_years', 'PRISM', 'PELOD']].values)

DemographicData_prepared_normal_df = DemographicData_prepared_df
DemographicData_prepared_normal_df['Age_years'] = DemographicData_normalized_values[:,0]
DemographicData_prepared_normal_df['PRISM'] = DemographicData_normalized_values[:,1]
DemographicData_prepared_normal_df['PELOD'] = DemographicData_normalized_values[:,2]


# Write recipe outputs
DemographicData_prepared_normal = dataiku.Dataset("DemographicData_prepared_normal")
DemographicData_prepared_normal.write_with_schema(DemographicData_prepared_normal_df)