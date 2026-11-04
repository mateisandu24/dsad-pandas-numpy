import sys

import numpy as np
import pandas as pd

from functii import nan_replace, tabelare_salvare_matrice, calcul_inertii
from scipy.spatial import distance

np.set_printoptions(precision=3, suppress=True, threshold=sys.maxsize)

df = pd.read_csv("data_in/Teritorial_2022.csv", index_col=0)
variabile_observate = list(df)[3:]
x = df[variabile_observate].values

# print(x,type(x),sep="\n")
x = nan_replace(x)
# print(x)
d_euclid = distance.cdist(x, x, metric='euclidean')
d_mahalanobis = distance.cdist(x, x, metric='mahalanobis')

df_d_euclid=tabelare_salvare_matrice(
    d_euclid,
    df.index,
    df.index,
    df.index.name,
    "D_Euclid.csv"
)
df_d_mahalanobis=tabelare_salvare_matrice(
    d_mahalanobis,
    df.index,
    df.index,
    df.index.name,
    "D_Mahalanobis.csv"
)
inertia,inertii,distante_centrii = calcul_inertii(
    x,df["Regiunea"].values
)
print("Inertia generala:",inertia)
for ch in inertii:
    print("Regiunea",ch)
    print("Inertie:",inertii[ch][0])
    print("Centru de grupa:")
    print(inertii[ch][1])
print("Distante intre grupe:")
print(distante_centrii)
tabelare_salvare_matrice(
    distante_centrii,
    list(inertii),
    list(inertii),
    "Regiuni",
    "DistanteRegiuni.csv"
)