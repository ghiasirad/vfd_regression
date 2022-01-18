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
DemographicData_prepared_df = DemographicData_prepared_df.set_index('Study ID')

# Remove the empty cells and replace them with median of the column
DemographicData_prepared_df.fillna(DemographicData_prepared_df.median(), inplace=True)
# nanoString_normalized_values = normalize(nanoString_cleaned_df.values, axis=1, norm='l1')
min_max_scaler = preprocessing.MinMaxScaler()
DemographicData_normalized_values = min_max_scaler.fit_transform(DemographicData_prepared_df.values)

DemographicData_prepared_normal_df = pd.DataFrame(data=DemographicData_normalized_values, columns=DemographicData_prepared_df.columns)
DemographicData_prepared_normal_df['Study ID'] = DemographicData_prepared_df.index

first_column = nanoString_normalized_df.pop('Study ID')
DemographicData_prepared_normal_df.insert(0, 'Study ID', first_column)


# Write recipe outputs
DemographicData_prepared_normal = dataiku.Dataset("DemographicData_prepared_normal")
DemographicData_prepared_normal.write_with_schema(DemographicData_prepared_normal_df)



