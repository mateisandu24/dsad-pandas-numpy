import sys

import numpy as np
import pandas as pd

from functii import nan_replace, teste

np.set_printoptions(suppress=True,precision=3,threshold=sys.maxsize)

df = pd.read_csv("data_in/Teritorial_2022.csv", index_col=0)
variabile = list(df)[3:]
# print(variabile)
x = df[variabile].values
# print(x)
# Inlocuire valori lipsa cu media
x = nan_replace(x)
# print(x)
# Aplicare teste de concordanta
t = teste(x)
print(t)
df_t = pd.DataFrame(t,variabile,["Kolmogorov-Smirnov","Shapiro","Anderson","Chi2"])
df_t.to_csv("data_out/Teste.csv")

