import numpy as np
from scipy.stats import kstest,norm,shapiro,anderson,chi2

def nan_replace(x:np.ndarray):
    x = x.copy()
    k = np.where(np.isnan(x))
    x[k] = np.nanmean(x[:,k[1]], axis=0)
    return x

# Functie pentru aplicarea testelor de concordanta
# Primeste ca parametru matricea testata
def teste(x:np.ndarray,prag=0.05):
    # Preiau numarul de coloane
    m = x.shape[1]
    t = np.empty((m,4), dtype=bool)
    for i in range(m):
        print("Variabila",i)
        # Kolmogorov
        t_ks = kstest(x[:,i],norm.cdf,args=(np.mean(x[:,i]),np.std(x[:,i])))
        print(t_ks[0],t_ks[1])
        t[i,0] = t_ks[1]>prag
        # Shapiro
        t_sh = shapiro(x[:,i])
        print(t_sh[0],t_sh[1])
        t[i,1]=t_sh[1]>prag
        # Anderson
        t_an = anderson(x[:,i],dist="norm",method="interpolate")
        print(t_an[0],t_an[1])
        t[i,2]=t_an[1]>prag
        # Chi2
        p_value_chi2 = test_chi2(x[:,i])
        print(p_value_chi2)
        t[i,3] = p_value_chi2<prag
    return t

def test_chi2(x:np.ndarray):
    n = len(x)
    media = np.mean(x)
    std = np.std(x)
    f,l = np.histogram(x,bins="sturges")
    m = len(f)
    fe = n*(norm.cdf(l[1:],media,std)-norm.cdf(l[:m],media,std))
    k = fe!=0
    f_ = f[k]
    fe_ = fe[k]
    stts = np.sum((f_-fe_)**2/fe_)
    pvalue = chi2.cdf(stts,m-1)
    return pvalue
