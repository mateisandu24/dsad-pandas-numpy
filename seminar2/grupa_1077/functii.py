import numpy as np
import pandas as pd
from scipy.stats import entropy


def shannon(df:pd.DataFrame):
    x = df.values
    tx = np.sum(x, axis=0)
    p = x/tx
    e = entropy(p,axis=0)
    return pd.Series(e,df.columns)

