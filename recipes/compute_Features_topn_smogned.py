# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import smogn

# Read recipe inputs
Features_joined_Nanostring_topn = dataiku.Dataset("Features_joined_Nanostring_topn")
Features_joined_Nanostring_topn_df = Features_joined_Nanostring_topn.get_dataframe()


## conduct smogn
features_smogn = smogn.smoter(
    
    data = Features_joined_Nanostring_topn_df, 
    y = "VFD",
    k = 3,
    pert = 0.2
)

Features_topn_smogned_df = features_smogn # For this sample code, simply copy input to output


# Write recipe outputs
Features_topn_smogned = dataiku.Dataset("Features_topn_smogned")
Features_topn_smogned.write_with_schema(Features_topn_smogned_df)

