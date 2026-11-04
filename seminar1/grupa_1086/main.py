import sys

import pandas as pd
import numpy as np

from functii import nan_replace, standardize

np.set_printoptions(suppress=True,precision=3, threshold=sys.maxsize)

t = pd.read_csv("data_in/Natalitate_Ro.csv")
# print(type(t))
df = t.pivot_table(index="Judete", columns="Ani", values="Valoare")
variabile = list(df)
# Inlocuire valori lipsa
x = df[variabile].values
x = nan_replace(x)
# Calcul corelatii/covariante
v = np.cov(x, rowvar=False)
# print(v)
df_cov = pd.DataFrame(v,variabile,variabile)
df_cov.to_csv("data_out/V.csv")
r = np.corrcoef(x, rowvar=False)
df_r = pd.DataFrame(r,variabile,variabile)
df_r.to_csv("data_out/R.csv")

# Standardizare date
x_std = standardize(x)
df_x_std = pd.DataFrame(x_std,df.index,variabile)
df_x_std.to_csv("data_out/x_std.csv")
