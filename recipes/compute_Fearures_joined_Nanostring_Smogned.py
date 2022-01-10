# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import smogn

# Read recipe inputs
Features_joined_Nanostring = dataiku.Dataset("Features_joined_Nanostring")
Features_joined_Nanostring_df = Features_joined_Nanostring.get_dataframe()


## conduct smogn
features_smogn = smogn.smoter(
    
    data = Features_joined_Nanostring_df, 
    y = "VFD",
    k = 3,
    pert = 0.2
)

Fearures_joined_Nanostring_Smogned_df = features_smogn # For this sample code, simply copy input to output


# Write recipe outputs
Fearures_joined_Nanostring_Smogned = dataiku.Dataset("Fearures_joined_Nanostring_Smogned")
Fearures_joined_Nanostring_Smogned.write_with_schema(Fearures_joined_Nanostring_Smogned_df)

