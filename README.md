# DSAD - sintaxa pandas / numpy (fisa de scris)

Fiecare exemplu a fost rulat pe datele din repo; rezultatul este in comentariu. Acelasi cod este in `sintaxa.py`.

Solutiile pe seminar si grupa sunt in `seminar1/`, `seminar2/`, `seminar3/`; documentatia lunga este in `docs/`.

## Importuri

```python
import pandas as pd
import numpy as np
from numpy.ma.extras import average
from scipy.spatial import distance
```

## 0. CITIRE

```python
df = pd.read_csv("data_in/IndustriaAlimentara.csv", index_col=0)    # coloana 0 (Siruta) devine INDEX
pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)   # Localitate, Judet, Populatie
reg = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)         # index = indicativ judet; NumeJudet, Regiune
activitati = list(df.columns.values)[1:]    # toate coloanele fara prima (Localitate) = cele numerice
# df.shape = (3181, 8)     df.head()     df.columns     df.index
```

## 1. SELECTIE DE COLOANE: [ ] vs [[ ]]

```python
s = df["Carne"]                  # O coloana intre [ ]   -> Series (nu are .merge, nu are .insert)
d = df[["Carne"]]                # O coloana intre [[ ]] -> DataFrame
d2 = df[["Localitate", "Carne"]] # mai multe coloane = lista in [ ] -> [[ ]]
d3 = df[activitati]              # lista pregatita (variabila) -> doar [ ]
d4 = df.iloc[:, 1:]              # iloc[randuri, coloane] dupa POZITIE: toate randurile, coloanele de la a 2-a
d5 = df.iloc[:5, 1:3]            # primele 5 randuri, coloanele 1 si 2
cell = df.loc[32768, "Localitate"]  # loc[eticheta_index, nume_coloana]  -> "Budesti"
# df[1:] taie RANDURI, nu coloane.  df["Carne", "Peste"] este GRESIT (KeyError): lipsesc parantezele duble.
```

## 2. FILTRARE DE RANDURI (masca booleana)

```python
f1 = df[df["Carne"] > 0]                                  # randuri cu Carne > 0
tot = df[activitati].sum(axis=1)                          # suma pe fiecare RAND (vezi sectiunea 3)
f2 = df[tot != 0]                                         # randuri unde SUMA tuturor coloanelor e nenula  -> 1372
f3 = df[tot > 0]                                          # randuri unde suma e pozitiva                   -> 1372
f4 = df[df[activitati].sum(axis=1) > 0]                   # la fel, fara variabila intermediara
f5 = df[(df[activitati] != 0).any(axis=1)]                # cel putin O coloana nenula                     -> 1372
f6 = df[(df[activitati] != 0).all(axis=1)]                # TOATE coloanele nenule                         -> 3
f7 = df[(df["Carne"] > 0) & (df["Lactate"] > 0)]          # SI = &   SAU = |   NEGARE = ~   (paranteze obligatorii)
f8 = df[df["Localitate"] == "Budesti"]                    # egalitate pe text                              -> 3
f9 = df[df["Localitate"].isin(["Budesti", "Sahateni"])]   # apartenenta la o lista
f10 = df[df[activitati].notna().all(axis=1)]              # randuri FARA valori lipsa (NaN)                -> 3181
# df.isna().sum() = cate NaN pe coloana.   df.iloc[masca] este GRESIT: iloc vrea pozitii; foloseste df[masca] sau df.loc[masca].
```

## 3. AXIS: 0 = in jos pe coloana, 1 = de-a lungul randului

```python
tot_rand = df[activitati].sum(axis=1)       # un numar PE RAND   (Series cu 3181 valori)
tot_coloana = df[activitati].sum()          # un numar PE COLOANA (axis=0 e implicit)    (7 valori)
dom = df[activitati].idxmax(axis=1)         # NUMELE coloanei cu maximul, pe fiecare rand
dom2 = df[activitati].apply(lambda x: x.index[x.argmax()], axis=1)   # la fel; in lambda x = un rand
# idxmax = eticheta (numele coloanei/indexului);  argmax = pozitia.  Rand cu toate 0 -> intoarce prima coloana (filtreaza-l inainte).
proc = df[activitati].apply(lambda x: x * 100 / x.sum(), axis=1)     # procent pe rand; suma 0 -> NaN
proc2 = df[activitati].mul(100).div(tot_rand, axis=0)                # acelasi lucru; div(..., axis=0) = impartire RAND cu RAND
proc3 = proc2.fillna(0)                                              # NaN (0/0) -> 0
# x * 100 / x.sum() cu axis=1 -> procentul in interiorul randului;  axis=0 ar da procentul din totalul coloanei.
```

## 4. COLOANE NOI, SORTARE, SALVARE

```python
c = df[["Localitate"]].copy()               # .copy() evita avertismentul SettingWithCopy
c["Total"] = tot_rand                       # coloana noua; se aliniaza automat dupa index (Siruta)
c.insert(1, "Total2", tot_rand)             # insert(pozitie, nume, valori) - Series nu are insert
c = c.sort_values(by="Total", ascending=False)    # sort_values NU modifica pe loc: ASIGNEAZA rezultatul
c = c.rename(columns={"Total2": "T2"})      # redenumire coloana
c.index.name = "Siruta"                     # numele primei coloane la salvare
s_tot = tot_rand.copy(); s_tot.name = "Total"    # un Series isi primeste numele inainte de salvare
c.round(3).to_csv("data_out/exemplu.csv")        # rotunjire doar la salvare, daca o cere enuntul
c.to_csv("data_out/exemplu2.csv", index_label="Siruta")   # alta varianta pentru numele index-ului
c = c[np.isfinite(c["Total"])]              # scoate NaN / inf (apar primele la sortare descrescatoare)
```

## 5. MERGE (lipirea tabelelor)

```python
m = df.merge(pop[["Judet", "Populatie"]], left_index=True, right_index=True)   # dupa Siruta (ambele au indexul Siruta)
# -> (3181, 10): ordinea randurilor = cea a tabelului din STANGA; implicit INNER join
m2 = m.merge(reg["Regiune"], left_on="Judet", right_index=True)
# left_on = coloana din stanga (Judet), right_index=True = indexul din dreapta (indicativ judet) -> (3181, 11)
# Coloana de legatura in ambele ca COLOANE:  a.merge(b, left_on="Judet", right_on="IndicativJudet")
# Seminar 2 (Coduri_Judete cu 4 coloane, index NrCrt):  jud.merge(cj, left_index=True, right_on="IndicativJudet")
# Dupa fiecare merge verifica m.shape (3181 randuri). pop["Localitate"] e Series (nu are merge) -> pop[["Localitate"]].
# Indicativele de judet trebuie sa aiba aceeasi forma (mici/MAJUSCULE) in ambele: reg.index.str.upper() / pop["Judet"].str.lower()
# PopulatieLocalitati.csv se citeste MEREU cu index_col=0, altfel merge-ul leaga dupa pozitie si amesteca localitatile.
```

## 6. GROUPBY

```python
jud = m[activitati + ["Judet", "Populatie"]].groupby(by="Judet").sum()
# 1) selectezi DOAR coloanele numerice + cheia de grupare (text in plus se concateneaza!)  2) groupby(by=cheie)  3) agregare
# -> (42, 8), indexul = Judet
rata = jud[activitati].sum(axis=1) * 1000 / jud["Populatie"]      # ADUNI pe grup, apoi IMPARTI (nu media rapoartelor)
rata.name = "Rata"
dom_jud = jud[activitati].idxmax(axis=1)                          # activitatea dominanta pe judet
regiuni = m2[activitati + ["Populatie", "Regiune"]].groupby("Regiune").sum()    # -> (8, 8)
nr = m.groupby("Judet").size()                                    # numar de randuri pe grup
medie = m.groupby("Judet")["Carne"].mean()                        # o singura coloana: groupby(...)["col"].mean()
mai_multe = m.groupby("Judet").agg({"Carne": "sum", "Populatie": "mean"})    # agregari diferite pe coloane

def calcul_medie(df):                       # media ponderata: ponderea = ULTIMA coloana
    x = df.values
    medii = average(x[:, :-1], axis=0, weights=x[:, -1])      # np.average(...) e echivalent
    return pd.Series(medii, df.columns[:-1])

pond = m2[activitati + ["Populatie", "Regiune"]].groupby("Regiune").apply(calcul_medie, include_groups=False)   # (8, 7)
pond2 = m2[activitati + ["Populatie", "Regiune"]].groupby("Regiune").apply(
    lambda x: x[activitati].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
    include_groups=False)                   # aceeasi medie ponderata, fara def; include_groups=False scoate cheia din tabelul primit
# apply returneaza un pd.Series -> pandas construieste un RAND pe grup.

nume_max = m.groupby("Judet").apply(lambda g: g["Localitate"].iloc[g["Carne"].argmax()], include_groups=False)
# numele localitatii cu maximul pe grup: argmax = pozitie in grup, .iloc[pozitie] = valoarea de la acea pozitie (42 valori)

# indice de localizare (judet i, activitate j) = (angajati_ij / angajati_j) / (populatie_i / populatie_tara)
loc = (jud[activitati] / jud[activitati].sum()).div(jud["Populatie"] / jud["Populatie"].sum(), axis=0)    # (42, 7)
```

## 7. FORMAT LUNG -> LAT (pivot)

```python
lung = pd.read_csv("data_in/Innoptari.csv")                       # Siruta, Ani ("Anul 2001"), Valoare - FARA index_col
lung["Ani"] = lung["Ani"].str.replace("Anul ", "").astype(int)    # .str.* pe coloane text; astype(int) -> anii devin cifre
lat = lung.pivot_table(index="Siruta", columns="Ani", values="Valoare")    # Siruta = index, anii = coloane   (1143, 16)
anii = list(lat.columns)
toti_anii = lat[lat.notna().all(axis=1)]                          # localitati cu date in TOTI anii                 -> 306
an_max = lat.idxmax(axis=1)                                       # anul (numele coloanei) cu maximul, pe localitate
total_an = lat.sum()                                              # total pe an (axis=0)
total_an.name = "Total"; total_an.index.name = "Anul"
la_mie = lat.merge(pop[["Judet", "Populatie"]], left_index=True, right_index=True).groupby("Judet").sum()
la_mie = la_mie.drop(columns="Populatie").mul(1000).div(la_mie["Populatie"], axis=0)    # rata la 1000, pe an, pe judet (42, 16)
lat_reg = lat.merge(pop[["Judet"]], left_index=True, right_index=True).merge(reg["Regiune"], left_on="Judet", right_index=True)
g = lat_reg.groupby("Regiune")[anii]
cv = g.std() / g.mean()                                           # coeficient de variatie pe regiune, pe ani (8, 16); std = ddof 1
```

## 8. NUMPY

```python
t = pd.read_csv("data_in/Teritorial_2022.csv", index_col=0)
variabile = list(t)[3:]                     # 31 de coloane numerice (dupa Judet, Regiunea, Macroregiunea)
x = t[variabile].values                     # .values = matrice numpy (42, 31); x[i, j] = randul i, coloana j

def nan_replace(x):                         # NaN -> media coloanei
    y = x.copy()
    k = np.where(np.isnan(y))               # (indici de rand, indici de coloana) ale valorilor lipsa
    y[k] = np.nanmean(y[:, k[1]], axis=0)
    return y

x = nan_replace(x)                          # np.isnan(x).sum() = 0 dupa inlocuire (inainte: 4)
medie_col = np.mean(x, axis=0)              # axis=0: o valoare PE COLOANA (31);  axis=1: pe rand (42)
std0 = np.std(x, axis=0)                    # ddof=0 implicit;  pandas .std() foloseste ddof=1
std1 = np.std(x, axis=0, ddof=1)
x_c = x - np.mean(x, axis=0)                # centrare
x_std = x_c / np.std(x_c, axis=0)           # standardizare

V = np.cov(x, rowvar=False)                 # covarianta (31, 31); rowvar=False = COLOANELE sunt variabilele
R = np.corrcoef(x, rowvar=False)            # corelatii (31, 31); cu rowvar=True (implicit) ar iesi (42, 42) = greseala
pd.DataFrame(R, variabile, variabile).to_csv("data_out/R.csv")     # DataFrame(matrice, nume_linii, nume_coloane)
pd.DataFrame(x_std, t.index, variabile).to_csv("data_out/x_std.csv")

y = t["Regiunea"].values                    # vector de etichete (grupe)
for clasa in np.unique(y):                  # valorile distincte, sortate
    z = x[y == clasa, :]                    # masca pe randuri: doar observatiile grupei
    r_grupa = np.corrcoef(z, rowvar=False)

D = distance.cdist(x, x, metric="euclidean")      # (42, 42); metric="mahalanobis" pentru Mahalanobis
centru = np.mean(x, axis=0)
inertie = np.sum(distance.cdist(x, centru.reshape(1, -1), metric="euclidean") ** 2)   # reshape(1, -1) = un rand cu 31 valori
w = np.arange(1, x.shape[0] + 1)
medie_pond = average(x, axis=0, weights=w)        # media ponderata pe coloane
```

## 9. ERORI FRECVENTE

```python
# KeyError ['Judet,Populatie']        -> pop[["Judet", "Populatie"]]   (doua nume = doua stringuri)
# 'Series' has no attribute 'merge'   -> pop[["Localitate"]], nu pop["Localitate"]
# sum() fara axis=1                   -> da total pe coloana, nu pe localitate
# idxmax pe tabel cu coloana text     -> df.iloc[:, 1:].idxmax(axis=1) sau df[activitati].idxmax(axis=1)
# sort_values fara asignare           -> c = c.sort_values(...)  apoi c.to_csv(...)
# merge care pierde toate randurile   -> majuscule vs litere mici la Judet, sau index_col gresit (verifica .shape)
# groupby(...).sum() cu coloane text  -> le concateneaza; selecteaza explicit coloanele numerice + cheia
# antet diferit de enunt              -> "Rata Ocuparii" != "Rata ocuparii"; copiaza exact din exemplul enuntului
# folderul data_out/ lipseste         -> to_csv da eroare; calea e "data_out/Cerinta1.csv"
```
