# ======================================================================================
# TOATE FUNCTIILE SI METODELE FOLOSITE LA SEMINARII (stanga-dreapta, intr-un singur fisier)
# Partea 1: functiile scrise la seminar (def)        Partea 2: metode pandas
# Partea 3: numpy / scipy / sklearn / python         Partea 4: lista parametrilor (axis, by, ...)
# Exemplele ruleaza pe tabele mici definite aici; rezultatul asteptat e in comentariu.
# ======================================================================================
import io
import numpy as np
import pandas as pd
from numpy.ma.extras import average
from pandas.api.types import is_numeric_dtype
from scipy.spatial import distance
from scipy.stats import entropy, kstest, shapiro, anderson, norm, chi2
from sklearn.preprocessing import StandardScaler


# ======================================================================================
# PARTEA 1. FUNCTIILE SCRISE LA SEMINAR (functii.py + main.py)
# ======================================================================================

# --- NaN -> media coloanei, pe matrice numpy (Seminar 1) ---
def nan_replace(x: np.ndarray):
    y = x.copy()
    k = np.where(np.isnan(y))
    y[k] = np.nanmean(y[:, k[1]], axis=0)
    return y


# --- NaN pe DataFrame: numeric -> media, text -> valoarea cea mai frecventa (Seminar 2) ---
def nan_replace_df(df: pd.DataFrame):
    for c in df.columns:
        if df[c].isna().any():
            if is_numeric_dtype(df[c]):
                df.fillna({c: df[c].mean()}, inplace=True)
            else:
                df.fillna({c: df[c].mode()[0]}, inplace=True)


# --- centrare (scal=False) / standardizare; ddof=0 e implicit la np.std (Seminar 1) ---
def standardizare(x: np.ndarray, scal=True, ddof=0):
    x_ = x - np.mean(x, axis=0)
    if scal:
        x_ = x_ / np.std(x_, axis=0, ddof=ddof)
    return x_


# --- matrice numpy -> DataFrame cu indecsi, optional salvata in data_out/ (Seminar 1) ---
def tabelare_salvare_matrice(x: np.ndarray, index_linie, index_coloana, nume_index, nume_fisier=None):
    df = pd.DataFrame(x, index=index_linie, columns=index_coloana)
    df.index.name = nume_index
    if nume_fisier is not None:
        df.to_csv("data_out/" + nume_fisier)
    return df


# --- corelatii si covariante pe grupe: y = vector de etichete (Seminar 1, grupa 1075) ---
def calcul_corelatii_covariante(x: np.ndarray, y: np.ndarray):
    clase = np.unique(y)
    q = len(clase)
    m = x.shape[1]
    r = np.empty((q, m, m))
    v = np.empty((q, m, m))
    for i in range(q):
        z = x[y == clase[i], :]
        r[i] = np.corrcoef(z, rowvar=False)
        v[i] = np.cov(z, rowvar=False)
    return r, v, clase


# --- inertie generala, inertie fata de centrul fiecarei grupe, distante intre centri (Seminar 1, 1077) ---
def calcul_inertii(x: np.ndarray, y: np.ndarray):
    m = x.shape[1]
    centru = np.mean(x, axis=0)
    distante = distance.cdist(x, centru.reshape(1, -1), metric="euclidean")
    inertia = np.sum(distante ** 2)
    inertii = {}
    grupe = np.unique(y)
    q = len(grupe)
    centrii = np.empty((q, m))
    for k in range(q):
        x_ = x[y == grupe[k], :]
        centru_k = np.mean(x_, axis=0)
        centrii[k, :] = centru_k
        distante_k = distance.cdist(x, centru_k.reshape(1, -1), metric="euclidean")
        inertii[grupe[k]] = (np.sum(distante_k ** 2), centru_k)
    distante_centrii = distance.cdist(centrii, centrii, metric="euclidean")
    return inertia, inertii, distante_centrii


# --- test Chi2 pentru normalitate, implementat de mana (Seminar 1, 1085) ---
def test_chi2(x: np.ndarray):
    n = len(x)
    media = np.mean(x)
    std = np.std(x)
    f, l = np.histogram(x, bins="sturges")
    m = len(f)
    fe = n * (norm.cdf(l[1:], media, std) - norm.cdf(l[:m], media, std))
    k = fe != 0
    f_ = f[k]
    fe_ = fe[k]
    stts = np.sum((f_ - fe_) ** 2 / fe_)
    pvalue = chi2.cdf(stts, m - 1)
    return pvalue


# --- KS, Shapiro, Anderson, Chi2 pe fiecare coloana; True = nu se respinge normalitatea (Seminar 1, 1085) ---
def teste(x: np.ndarray, prag=0.05):
    m = x.shape[1]
    t = np.empty((m, 4), dtype=bool)
    for i in range(m):
        t_ks = kstest(x[:, i], norm.cdf, args=(np.mean(x[:, i]), np.std(x[:, i])))
        t[i, 0] = t_ks[1] > prag
        t_sh = shapiro(x[:, i])
        t[i, 1] = t_sh[1] > prag
        t_an = anderson(x[:, i], dist="norm", method="interpolate")
        t[i, 2] = t_an[1] > prag
        p_value_chi2 = test_chi2(x[:, i])
        t[i, 3] = p_value_chi2 < prag
    return t


# --- Shannon pe coloane, ca la seminar: logaritm NATURAL (nats) ---
def shannon(df: pd.DataFrame):
    x = df.values
    tx = np.sum(x, axis=0)
    tx[tx == 0] = 1
    p = x / tx
    e = entropy(p, axis=0)
    return pd.Series(e, index=df.columns)


# --- Shannon in BITI (log2), cum cer enunturile; total 0 -> 0 (nu NaN) ---
def shannon_biti(df: pd.DataFrame):
    x = df.values
    tx = np.sum(x, axis=0)
    tx[tx == 0] = 1
    p = x / tx
    e = entropy(p, axis=0, base=2)
    return pd.Series(np.nan_to_num(e), index=df.columns)


# --- indice de disimilaritate pe coloane (grupuri) (Seminar 2) ---
def disimilaritate(df: pd.DataFrame):
    x = df.values
    tx = np.sum(x, axis=0)
    tx[tx == 0] = 1
    sx = np.sum(x, axis=1)
    r = (sx - x.T).T
    tr = np.sum(r, axis=0)
    d = 0.5 * np.sum(np.abs(x / tx - r / tr), axis=0)
    return pd.Series(d, df.columns)


# --- Shannon / Simpson / Simpson invers pe RAND (rand = judet, coloane = confesiuni) ---
def indici_diversitate(df: pd.DataFrame):
    p = df.div(df.sum(axis=1), axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        h = -(p * np.log2(p)).where(p > 0, 0.0).sum(axis=1)
    s1 = 1 - (p ** 2).sum(axis=1)
    s2 = 1 / (p ** 2).sum(axis=1)
    return pd.DataFrame({"Shannon": h, "Simpson": s1, "SimpsonInvers": s2})


# --- media ponderata pe grup; pondera = ULTIMA coloana (Seminar 3). Folosita cu groupby().apply() ---
def calcul_medie(df: pd.DataFrame):
    x = df.values
    medii = average(x[:, :-1], axis=0, weights=x[:, -1])
    return pd.Series(medii, df.columns[:-1])


# --- procente pe rand (ponderea fiecarei coloane in totalul randului) ---
def procente(df: pd.DataFrame, coloane):
    return df[coloane].apply(lambda x: x * 100 / x.sum(), axis=1)


# ======================================================================================
# PARTEA 2. METODE PANDAS (stanga -> dreapta in ordinea in care le folosesti)
# ======================================================================================
df = pd.DataFrame(
    {"Localitate": ["A", "B", "C", "D"], "Carne": [0, 5, 3, 0], "Peste": [0, 2, 0, 0],
     "Judet": ["ab", "ab", "cj", "cj"], "Populatie": [100, 200, 300, 400]},
    index=pd.Index([1, 2, 3, 4], name="Siruta"))
pop = df[["Localitate", "Judet", "Populatie"]].copy()
reg = pd.DataFrame({"NumeJudet": ["Alba", "Cluj"], "Regiune": ["Centru", "Nord-Vest"]},
                   index=pd.Index(["ab", "cj"], name="IndicativJudet"))
activitati = list(df.columns.values)[1:3]                    # ["Carne", "Peste"]

# --- pd.read_csv / .to_csv (citire / scriere) ---
# df = pd.read_csv("data_in/X.csv", index_col=0)             # prima coloana devine index
# df = pd.read_csv("data_in/Innoptari.csv")                  # fara index_col (format lung, pentru pivot)
# df.to_csv("data_out/Cerinta1.csv")                         # indexul se salveaza ca prima coloana
# df.to_csv("f.csv", index_label="Siruta")                   # alt nume pentru prima coloana
# df.round(3).to_csv(...)                                    # rotunjire doar la salvare
buf = io.StringIO(); df.to_csv(buf); buf.seek(0)
df_citit = pd.read_csv(buf, index_col=0)                     # round-trip: aceleasi date

# --- pd.set_option (afisare) ---
pd.set_option("display.max_columns", None)                   # afiseaza toate coloanele in consola

# --- .head() .shape .columns .index .values .copy() ---
df.head(2); df.shape                                         # (4, 5)
list(df.columns.values)[1:]                                  # numele coloanelor, fara prima
df[["Carne"]].values                                         # matrice numpy (4, 1)
c = df[["Localitate"]].copy()                                # copie: evita SettingWithCopy

# --- [ ] [[ ]] .iloc .loc (selectie) ---
df["Carne"]                                                  # Series
df[["Localitate", "Carne"]]                                  # DataFrame (lista in paranteze)
df.iloc[:, 1:]                                               # dupa POZITIE: toate randurile, coloanele de la a doua
df.loc[1, "Localitate"]                                      # dupa ETICHETA -> "A"

# --- masca booleana + .sum(axis=1) .any() .all() .isin() .notna() .isna() ---
tot = df[activitati].sum(axis=1)                             # [0, 7, 3, 0]  un total pe RAND
df[tot != 0]                                                 # randurile B, C: suma tuturor coloanelor nenula
df[(df[activitati] != 0).any(axis=1)]                        # cel putin o coloana nenula -> B, C
df[(df[activitati] != 0).all(axis=1)]                        # toate coloanele nenule -> B
df[(df["Carne"] > 0) & (df["Peste"] > 0)]                    # & SI, | SAU, ~ NEGARE (paranteze obligatorii) -> B
df[df["Localitate"].isin(["A", "C"])]                        # apartenenta la lista
df[df[activitati].notna().all(axis=1)]                       # fara NaN
df.isna().sum()                                              # cate NaN pe coloana (diagnostic)

# --- .sum() .mean() .std() (agregari; axis=0 pe coloana, axis=1 pe rand) ---
df[activitati].sum()                                         # Carne 8, Peste 2  (pe coloana)
df[activitati].mean()                                        # 2.0, 0.5
df["Carne"].std()                                            # abatere standard cu ddof=1 (pandas)

# --- .idxmax(axis=1) .argmax() (maxim) ---
df[activitati].idxmax(axis=1)                                # NUMELE coloanei cu maximul pe rand (Carne, Carne, ...)
df[activitati].apply(lambda x: x.index[x.argmax()], axis=1)  # la fel; argmax = POZITIA maximului

# --- .apply(func=..., axis=...) ---
df[activitati].apply(lambda x: x * 100 / x.sum(), axis=1)    # axis=1: x = un RAND; randurile cu suma 0 -> NaN
df[activitati].apply(lambda x: x.sum(), axis=0)              # axis=0: x = o COLOANA

# --- .div() .mul() .multiply() (operatii pe tabel cu axis=0) ---
df[activitati].div(tot.replace(0, np.nan), axis=0)           # imparte fiecare RAND la totalul lui
df[activitati].mul(100)                                      # inmulteste tot tabelul
df[activitati].multiply(df["Populatie"], axis=0)             # inmulteste fiecare rand cu populatia lui

# --- .fillna() .mode() ---
df[activitati].div(tot.replace(0, np.nan), axis=0).fillna(0) # NaN (0/0) -> 0
df.fillna({"Carne": df["Carne"].mean()}, inplace=True)       # NaN -> media (inplace modifica pe loc)
df["Localitate"].mode()[0]                                   # valoarea cea mai frecventa (text)

# --- coloane noi: c["x"]= .insert() .drop() .rename() .astype() .round() ---
c["Total"] = tot                                             # se aliniaza dupa index
c.insert(0, "Cod", c.index)                                  # insert(pozitie, nume, valori); Series NU are insert
c = c.drop(columns="Cod")                                    # scoate coloana
c = c.rename(columns={"Total": "T"})                         # redenumire
df["Populatie"].astype(float)                                # schimba tipul
df[activitati].div(tot.replace(0, np.nan), axis=0).round(2)  # rotunjire

# --- .sort_values() (NU modifica pe loc: asigneaza) ---
c = c.sort_values(by="T", ascending=False)                   # descrescator
s = tot.copy(); s.name = "Total"; s.index.name = "Siruta"    # .name / .index.name = antetul la salvare

# --- .merge() (lipire dupa index sau dupa coloana) ---
m = df[activitati].merge(pop[["Judet", "Populatie"]], left_index=True, right_index=True)   # dupa index (Siruta)
m2 = m.merge(reg["Regiune"], left_on="Judet", right_index=True)    # coloana (stanga) cu indexul (dreapta)
# a.merge(b, left_on="Judet", right_on="IndicativJudet")           # coloana cu coloana
# a.merge(b, left_index=True, right_on="IndicativJudet")           # indexul din stanga cu coloana din dreapta
m.shape                                                      # verifica mereu numarul de randuri dupa merge

# --- .groupby(by=...) .sum() .size() .agg() .aggregate() .apply(..., include_groups=False) ---
jud = m[activitati + ["Judet", "Populatie"]].groupby(by="Judet").sum()    # ab: 5, 2, 300   cj: 3, 0, 700
rata = jud["Carne"] * 1000 / jud["Populatie"]                # aduni pe grup, apoi imparti
m.groupby("Judet").size()                                    # numar de randuri pe grup
m.groupby("Judet").agg({"Carne": "sum", "Populatie": "mean"})            # agregari diferite pe coloane
m2.groupby("Regiune")[activitati].aggregate(func=lambda x: x.sum())      # aggregate = agg
m[activitati + ["Populatie", "Judet"]].groupby(by="Judet").apply(calcul_medie, include_groups=False)
#   ab: Carne 3.3333   cj: Carne 1.2857  (media ponderata cu populatia)
m[["Carne", "Judet"]].groupby(by="Judet").apply(
    lambda g: g["Carne"].iloc[g["Carne"].argmax()], include_groups=False)  # valoarea maxima pe grup (iloc[pozitie])

# --- .pivot_table() .pivot() + .str.replace() (format lung -> lat) ---
lung = pd.DataFrame({"Siruta": [1, 1, 2], "Ani": ["Anul 2001", "Anul 2002", "Anul 2001"], "Valoare": [10, 20, 30]})
lung["Ani"] = lung["Ani"].str.replace("Anul ", "").astype(int)           # .str.* lucreaza pe coloane text
lat = lung.pivot_table(index="Siruta", columns="Ani", values="Valoare")  # Siruta = index, anii = coloane; lipsa -> NaN
lat2 = lung.pivot(index="Siruta", columns="Ani", values="Valoare")       # ca pivot_table, dar da eroare la duplicate
lat[lat.notna().all(axis=1)]                                 # localitati cu date in toti anii
lat.idxmax(axis=1)                                           # anul (numele coloanei) cu maximul
lat.sum()                                                    # total pe an
lat.fillna(0)

# --- sirurile de caractere ---
pop["Judet"].str.upper()                                     # ab -> AB  (pandas, pe coloana)
pop["Judet"].str.lower()                                     # AB -> ab
"Anul 2001".removeprefix("Anul ")                            # python pur, pe un singur sir -> "2001"
[v.removeprefix("Anul ") for v in ["Anul 2001", "Anul 2002"]]   # lista de sirurile taiate
reg.index.str.upper()                                        # indexul text cu majuscule

# --- coeficient de variatie, rata la 1000, indice de localizare (combinatii) ---
g = lat.groupby(lat.index % 2)[[2001, 2002]]                 # groupby pe o cheie, apoi selectie de coloane
g.std() / g.mean()                                           # CV pe grup: std (ddof=1) / media
jud.drop(columns="Populatie").mul(1000).div(jud["Populatie"], axis=0)    # rata la 1000, pe fiecare coloana
(jud[activitati] / jud[activitati].sum()).div(jud["Populatie"] / jud["Populatie"].sum(), axis=0)   # localizare


# ======================================================================================
# PARTEA 3. NUMPY / SCIPY / SKLEARN / PYTHON
# ======================================================================================
x = np.array([[1.0, 2.0, np.nan], [3.0, np.nan, 6.0], [5.0, 4.0, 9.0], [7.0, 8.0, 12.0]])
y = np.array(["a", "a", "b", "b"])

# --- np.set_printoptions ---
np.set_printoptions(precision=3, suppress=True)              # afisare numpy: 3 zecimale, fara notatie stiintifica

# --- np.isnan np.where np.nanmean np.nansum (valori lipsa) ---
np.isnan(x)                                                  # masca booleana (True unde lipseste)
np.isnan(x).sum()                                            # 2 valori lipsa
k = np.where(np.isnan(x))                                    # (indici de rand, indici de coloana)
np.nanmean(x, axis=0)                                        # media pe coloana, ignora NaN
np.nansum(x, axis=0)                                         # suma pe coloana, ignora NaN
np.where(x > 5, 1, 0)                                        # cu 3 argumente: conditie, daca True, daca False
xn = nan_replace(x)                                          # functia de la inceput (NaN -> media coloanei)

# --- np.mean np.std np.average (axis=0 pe coloana, axis=1 pe rand) ---
np.mean(xn, axis=0)                                          # o valoare PE COLOANA
np.mean(xn, axis=1)                                          # o valoare PE RAND
np.std(xn, axis=0)                                           # ddof=0 implicit (pandas .std() are ddof=1)
np.std(xn, axis=0, ddof=1)
average(xn, axis=0, weights=[1, 2, 3, 4])                    # media ponderata (np.average e echivalent)
xc = xn - np.mean(xn, axis=0)                                # centrare (broadcasting pe coloane)
xs = xc / np.std(xc, axis=0)                                 # standardizare

# --- np.cov np.corrcoef (rowvar=False: coloanele sunt variabilele) ---
V = np.cov(xn, rowvar=False)                                 # (3, 3); cu rowvar=True (implicit) ar iesi (4, 4)
R = np.corrcoef(xn, rowvar=False)                            # (3, 3)

# --- np.unique, masca pe randuri, np.empty, np.arange, len, range, zip ---
clase = np.unique(y)                                         # ["a", "b"] (sortate)
for clasa in clase:
    z = xn[y == clasa, :]                                    # doar randurile grupei
rr = np.empty((len(clase), 3, 3))                            # matrice goala (se umple dupa)
for i in range(len(clase)):
    rr[i] = np.corrcoef(xn[y == clase[i], :], rowvar=False)
w = np.arange(1, 5)                                          # [1, 2, 3, 4]
list(zip(["a", "b"], [1, 2]))                                # perechi: [("a", 1), ("b", 2)]

# --- np.abs np.log2 np.isfinite np.errstate np.histogram np.sum .reshape ---
np.abs(np.array([-1.0, 2.0]))
np.log2(8)                                                   # 3.0
np.isfinite(np.array([1.0, np.inf, np.nan]))                 # [True, False, False]  (filtru pentru inf / NaN)
with np.errstate(divide="ignore", invalid="ignore"):         # nu mai da avertisment la 0/0, log(0)
    np.log2(np.array([0.0, 1.0]))
f, l = np.histogram(xn[:, 0], bins="sturges")                # frecvente si limite de clase (regula Sturges)
np.sum(xn, axis=0)
centru = np.mean(xn, axis=0).reshape(1, -1)                  # vector -> matrice cu un rand si 3 coloane

# --- DataFrame din matrice ---
pd.DataFrame(R, index=["a", "b", "c"], columns=["a", "b", "c"])          # DataFrame(matrice, linii, coloane)
pd.Series([1, 2], index=["x", "y"], name="Valori")                       # Series (cum intoarce calcul_medie)

# --- scipy.spatial.distance.cdist ---
distance.cdist(xn, xn, metric="euclidean")                   # (4, 4) distante intre randuri
distance.cdist(xn, xn, metric="mahalanobis")                 # Mahalanobis (VI estimat din x duplicat)
distance.cdist(xn, centru, metric="euclidean")               # (4, 1) distanta fiecarui rand la centru

# --- scipy.stats: entropy, kstest, shapiro, anderson, norm.cdf, chi2.cdf ---
p = np.array([0.5, 0.25, 0.25])
entropy(p)                                                   # NATURAL (nats): 1.0397
entropy(p, base=2)                                           # BITI: 1.5
entropy(np.array([[0.5, 1.0], [0.5, 0.0]]), axis=0)          # pe coloane
kstest(xn[:, 0], norm.cdf, args=(np.mean(xn[:, 0]), np.std(xn[:, 0])))   # [statistic, pvalue]
shapiro(xn[:, 0])                                            # [statistic, pvalue]
anderson(xn[:, 0], dist="norm", method="interpolate")        # [statistic, pvalue]  (pvalue limitat la [0.01, 0.15])
norm.cdf(0.0, 0, 1)                                          # 0.5  (functia de repartitie normala)
chi2.cdf(3.84, 1)                                            # ~0.95; p-value-ul standard = 1 - cdf

# --- sklearn (apare doar in comentariu la Seminar 1, grupa 1075) ---
StandardScaler().fit_transform(xn)                           # standardizare cu ddof=0 = standardizare(xn)

# --- apelul functiilor din Partea 1 (cum apar in main.py) ---
tabelare_salvare_matrice(R, ["a", "b", "c"], ["a", "b", "c"], "Indicatori")              # fara nume_fisier = nu salveaza
calcul_corelatii_covariante(xn, y)                           # (r, v, clase)
calcul_inertii(xn, y)                                        # (inertia, {grupa: (inertie, centru)}, distante_centri)
teste(np.random.default_rng(0).normal(size=(50, 2)))         # matrice (2, 4) de True / False
standardizare(xn); standardizare(xn, scal=False)             # standardizat / doar centrat
shannon(pd.DataFrame({"u": [1, 1], "v": [3, 1]}))
shannon_biti(pd.DataFrame({"u": [1, 1], "v": [3, 1]}))
disimilaritate(pd.DataFrame({"u": [10, 0], "v": [0, 10]}))   # 1.0: segregare totala
indici_diversitate(pd.DataFrame({"p": [50, 25], "q": [50, 75]}, index=["x", "y"]))
procente(df, activitati)


# ======================================================================================
# PARTEA 4. PARAMETRI FOLOSITI (kwargs) - ce inseamna fiecare
# ======================================================================================
# axis=0 / axis=1        0 = in jos pe coloana (o valoare per coloana); 1 = de-a lungul randului (o valoare per rand)
# index_col=0            la read_csv: prima coloana devine index (codul Siruta)
# by="Judet"             la groupby / sort_values: cheia de grupare / de sortare
# ascending=False        la sort_values: descrescator
# func=...               la apply / aggregate: functia (nume sau lambda)
# include_groups=False   la groupby().apply(): coloana cheie NU intra in functie (pondere ramane ultima coloana)
# left_index=True        la merge: foloseste indexul tabelului din STANGA drept cheie
# right_index=True       la merge: foloseste indexul tabelului din DREAPTA drept cheie
# left_on="Judet"        la merge: coloana din stanga drept cheie
# right_on="IndicativJudet"   la merge: coloana din dreapta drept cheie
# index= / columns= / values=   la pivot / pivot_table: ce devine index, ce devine coloane, ce se pune in celule
# columns="Populatie"    la drop(columns=...): ce coloana se scoate;  la rename(columns={...}): redenumire
# inplace=True           modifica obiectul pe loc (fillna), nu intoarce unul nou
# index_label="Siruta"   la to_csv: numele primei coloane
# ddof=0 / ddof=1        la std: impartire la n (0) sau n-1 (1); numpy implicit 0, pandas implicit 1
# rowvar=False           la np.cov / np.corrcoef: coloanele sunt variabilele (randurile = observatii)
# weights=...            la average: ponderile
# metric="euclidean"     la cdist: tipul distantei ("mahalanobis" la fel)
# args=(medie, std)      la kstest: parametrii repartitiei teoretice
# dist="norm", method="interpolate"   la anderson: repartitia testata, p-value interpolat
# bins="sturges"         la histogram: numarul de clase dupa regula Sturges
# base=2                 la entropy: logaritm in baza 2 (implicit natural)
# precision=3, suppress=True   la set_printoptions: zecimale afisate, fara notatie 1e-05
# divide="ignore", invalid="ignore"   la errstate: ignora avertismentele la impartire la 0 / valori invalide
# scal=True / False      la standardizare (functia scrisa): True = standardizeaza, False = doar centreaza
