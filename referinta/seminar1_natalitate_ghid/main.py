# Seminar 1 - Natalitate: pivot, NaN, covarianta, corelatie, standardizare
import pandas as pd
import numpy as np

t = pd.read_csv("data_in/Natalitate_Ro.csv")     # Judete, Localitati, Ani, UM, Valoare
df = t.pivot_table(index="Judete", columns="Ani", values="Valoare")
variabile = list(df)
x = df[variabile].values


def nan_replace(x):
    y = x.copy()
    k = np.where(np.isnan(y))
    y[k] = np.nanmean(y[:, k[1]], axis=0)        # NaN -> media coloanei
    return y


def standardize(x, scal=True, ddof=0):
    x_ = x - np.mean(x, axis=0)
    if scal:
        x_ = x_ / np.std(x_, axis=0, ddof=ddof)
    return x_


x = nan_replace(x)
v = np.cov(x, rowvar=False)                      # covarianta intre coloane (ani)
r = np.corrcoef(x, rowvar=False)                 # corelatii intre coloane
pd.DataFrame(v, variabile, variabile).to_csv("data_out/V.csv")
pd.DataFrame(r, variabile, variabile).to_csv("data_out/R.csv")
pd.DataFrame(standardize(x), df.index, variabile).to_csv("data_out/x_std.csv")
