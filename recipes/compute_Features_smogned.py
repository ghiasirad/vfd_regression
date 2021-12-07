# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import smogn

# Read recipe inputs
features_joined = dataiku.Dataset("Features_joined")
features_joined_df = features_joined.get_dataframe()


## conduct smogn
features_smogn = smogn.smoter(
    
    data = features_joined_df, 
    y = "VFD",
    k = 3,
    pert = 0.2
)

features_smogned_df = features_smogn # For this sample code, simply copy input to output


# Write recipe outputs
features_smogned = dataiku.Dataset("Features_smogned")
features_smogned.write_with_schema(features_smogned_df)
