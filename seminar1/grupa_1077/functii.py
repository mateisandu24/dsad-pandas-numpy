import numpy as np
import pandas as pd
from scipy.spatial import distance

def nan_replace(x:np.ndarray):
    x = x.copy()
    k = np.where(np.isnan(x))
    x[k] = np.nanmean(x[:,k[1]], axis=0)
    return x

def tabelare_salvare_matrice(
        x: np.ndarray,
        nume_linii,
        nume_coloane,
        nume_index,
        nume_fisier_output=None
):
    df = pd.DataFrame(x,nume_linii,nume_coloane)
    df.index.name = nume_index
    if nume_fisier_output is not None:
        df.to_csv("data_out/"+nume_fisier_output)
    return df

def calcul_inertii(x:np.ndarray,y:np.ndarray):
    m = x.shape[1]
    centru = np.mean(x,axis=0)
    distante = distance.cdist(x,centru.reshape(1,-1),metric='euclidean')
    inertia = np.sum(distante**2)
    inertii = {}
    grupe = np.unique(y)
    q = len(grupe)
    centrii = np.empty((q,m))
    for k in range(q):
        x_ = x[y==grupe[k],:]
        centru_k = np.mean(x_,axis=0)
        centrii[k,:] = centru_k
        distante_k = distance.cdist(x,centru_k.reshape(1,-1),metric='euclidean')
        inertii[grupe[k]] = (np.sum(distante_k**2),centru_k)
    distante_centrii = distance.cdist(centrii,centrii,metric='euclidean')
    return inertia,inertii,distante_centrii