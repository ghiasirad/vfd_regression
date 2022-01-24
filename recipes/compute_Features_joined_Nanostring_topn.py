# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Features_joined_Nanostring = dataiku.Dataset("Features_joined_Nanostring")
Features_joined_Nanostring_df = Features_joined_Nanostring.get_dataframe()
selectedFeatures_topn_stacked = dataiku.Dataset("selectedFeatures_topn_stacked")
selectedFeatures_topn_stacked_df = selectedFeatures_topn_stacked.get_dataframe()
selectedFeatures = dataiku.Dataset("selectedFeatures")
selectedFeatures_df = selectedFeatures.get_dataframe()


# Filter the dataframe into a smaller dataset
Features_joined_Nanostring_topn_df = Features_joined_Nanostring_df[selectedFeatures_df.line.values[:30]]
Features_joined_Nanostring_topn_df['StudyID_Int'] = Features_joined_Nanostring_df['StudyID_Int']
Features_joined_Nanostring_topn_df['VFD'] = Features_joined_Nanostring_df['VFD']

first_column = Features_joined_Nanostring_topn_df.pop('StudyID_Int')
Features_joined_Nanostring_topn_df.insert(0, 'StudyID_Int', first_column)


# Write recipe outputs
Features_joined_Nanostring_topn = dataiku.Dataset("Features_joined_Nanostring_topn")
Features_joined_Nanostring_topn.write_with_schema(Features_joined_Nanostring_topn_df)
