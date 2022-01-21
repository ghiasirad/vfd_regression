# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Features_joined_Nanostring = dataiku.Dataset("Features_joined_Nanostring")
Features_joined_Nanostring_df = Features_joined_Nanostring.get_dataframe()
selectedFeatures_topn = dataiku.Dataset("selectedFeatures_topn")
selectedFeatures_topn_df = selectedFeatures_topn.get_dataframe()


# Filter the dataframe into a smaller dataset
Features_joined_Nanostring_topn_df = Features_joined_Nanostring_df[selectedFeatures_topn_df.line.values]
Features_joined_Nanostring_topn_df['StudyID_Int'] = Features_joined_Nanostring_df['StudyID_Int']
Features_joined_Nanostring_topn_df['VFD'] = Features_joined_Nanostring_df['VFD']

first_column = nanoString_normalized_df.pop('StudyID_Int')
nanoString_normalized_df.insert(0, 'StudyID_Int', first_column)


# Write recipe outputs
Features_joined_Nanostring_topn = dataiku.Dataset("Features_joined_Nanostring_topn")
Features_joined_Nanostring_topn.write_with_schema(Features_joined_Nanostring_topn_df)
