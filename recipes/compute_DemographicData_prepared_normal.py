# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

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
