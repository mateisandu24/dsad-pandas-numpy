import numpy as np
import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype
from scipy.stats import entropy


def nan_replace_df(df: pd.DataFrame):
    for col in df.columns:
        if df[col].isna().any():
            if is_numeric_dtype(df[col]):
                df.fillna({col:df[col].mean()}, inplace=True)
            else:
                df.fillna({col:df[col].mode()[0]}, inplace=True)

def shannon(df: pd.DataFrame):
    x = df.values
    tx = np.sum(x,axis=0)
    tx[tx==0] = 1
    p = x/tx
    e = entropy(p,axis=0)
    return pd.Series(e,index=df.columns)

