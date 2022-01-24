# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Features_joined_Nanostring = dataiku.Dataset("Features_joined_Nanostring")
Features_joined_Nanostring_df = Features_joined_Nanostring.get_dataframe()
selectedFeatures = dataiku.Dataset("selectedFeatures")
selectedFeatures_df = selectedFeatures.get_dataframe()


Features_topn_df = Features_joined_Nanostring_df[selectedFeatures_df.Feature.values[:30]]
Features_topn_df['StudyID_Int'] = Features_joined_Nanostring_df.StudyID_Int


# Write recipe outputs
Features_topn = dataiku.Dataset("Features_topn")
Features_topn.write_with_schema(Features_topn_df)
