# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
Features_joined_Nanostring = dataiku.Dataset("Features_joined_Nanostring")
Features_joined_Nanostring_df = Features_joined_Nanostring.get_dataframe()


import matplotlib.pyplot as plt

# Apply ElasticNet
def applyLimitOnRemainedFeatures(totalDf, cutoff=0):
    
    ['Sex', 'Race', 'ECMO', 'Infection Status']
    
    tgt = totalDf.pop('VFD')
    
    sex = totalDf.pop('Sex')
    race = totalDf.pop('Race')
    ecmo = totalDf.pop('ECMO')
    infection = totalDf.pop('Infection Status')
    
    fDf = totalDf
    
    # Create correlation matrix
    corr_matrix = fDf.corr().abs()

    # Select upper triangle of correlation matrix
    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

    # print(upper)

    # Find index of feature columns with correlation greater than 0.95
    to_drop = [column for column in upper.columns if any(upper[column] > 0.8)]

#     print(to_drop)
    # print(len(to_drop))

    # Drop correlated features 
    featuresDf_nonCorr = fDf.drop(to_drop, axis=1)
#     featuresDf_nonCorr = fDf

#     print(featuresDf_nonCorr)
    print(featuresDf_nonCorr.shape)
#     print(featuresDf_nonCorr.columns)

    from sklearn.linear_model import ElasticNetCV

#     ElasticNetModel = ElasticNetCV(cv=10, random_state=42)
    ElasticNetModel = ElasticNetCV(random_state=42)
    ElasticNetModel.fit(featuresDf_nonCorr, tgt)

    # Assigns weight to each feature
    coefs = ElasticNetModel.coef_
#     print(coefs)
    # print(len(coefs))
#     print(fsDf.shape)

    # Make a dictionary of the metabolites and their weights
    remainedCols = {featuresDf_nonCorr.columns[i]:coefs[i] for i in range(featuresDf_nonCorr.shape[1]) if abs(coefs[i]) > cutoff}

    # Sort the dictionary of non zero values
    remainedColsSorted = sorted({x:y for x,y in remainedCols.items() if y!=0}.items(), key=lambda x: x[1])

#     print(remainedCols)
#     print(remainedColsSorted)


    # extrac    # extract keys and vals to plot in a bar chart
    # keys and vals to plot in a bar chart
    keys = []
    vals = []
    geneKeys = []
    geneVals = []
    for i in range(1,len(remainedCols)+1):
        keys.append(str(remainedColsSorted[-i][0]))
        vals.append(remainedColsSorted[-i][1])

#     print(len(keys))
#     print(keys)
#     print(vals)
    
    # Drop the low score columns
    featuresDfReduced = fDf[keys]
#     print(featuresDfReduced.shape)
    
    featuresDfReducedSmoteTotal = featuresDfReduced
    featuresDfReducedSmoteTotal['VFD'] = tgt
    
    featuresDfReducedSmoteTotal['Sex'] = sex
    featuresDfReducedSmoteTotal['Race'] = race
    featuresDfReducedSmoteTotal['ECMO'] = ecmo
    featuresDfReducedSmoteTotal['Infection Status'] = infection
    
    return keys, featuresDfReducedSmoteTotal

keysReturned, Features_joined_Nanostring_df = applyLimitOnRemainedFeatures(Features_joined_Nanostring_df, cutoff = 0.8)

Features_joined_Nanostring_Reduced_df = Features_joined_Nanostring_df # For this sample code, simply copy input to output


# Write recipe outputs
Features_joined_Nanostring_Reduced = dataiku.Dataset("Features_joined_Nanostring_Reduced")
Features_joined_Nanostring_Reduced.write_with_schema(Features_joined_Nanostring_Reduced_df)
