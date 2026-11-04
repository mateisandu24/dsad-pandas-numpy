# Test generat "Firme pe ani" (format lung, 8 cerinte)
import pandas as pd
import numpy as np

# Cerinta 1
df = pd.read_csv("data_in/Firme.csv")
df["Ani"] = df["Ani"].str.replace("Anul ", "").astype(int)
c1 = df.pivot_table(index="Siruta", columns="Ani", values="Valoare")
c1.to_csv("data_out/Cerinta1.csv")
anii = list(c1.columns)

# Cerinta 2
c2 = c1[c1.notna().all(axis=1)]
c2.to_csv("data_out/Cerinta2.csv")

# Cerinta 3
pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
s3 = c1.idxmax(axis=1)
s3.name = "Anul"
c3 = pop[["Localitate"]].merge(s3, left_index=True, right_index=True)
c3.index.name = "Siruta"
c3.to_csv("data_out/Cerinta3.csv")

# Cerinta 4
suma = c1.sum(axis=1) * 1000 / pop["Populatie"]
suma.name = "Firme_1000"
c4 = pop[["Localitate"]].merge(suma, left_index=True, right_index=True)
c4 = c4[c4.notna().all(axis=1)]
c4.to_csv("data_out/Cerinta4.csv")

# Cerinta 5
m = c1.merge(pop[["Judet", "Populatie"]], left_index=True, right_index=True)
jud = m.groupby("Judet").sum()
c5 = jud.drop(columns="Populatie").mul(1000).div(jud["Populatie"], axis=0)
c5.round(2).to_csv("data_out/Cerinta5.csv")

# Cerinta 6
reg = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
pop_l = pop.copy()
pop_l["Judet"] = pop_l["Judet"].str.lower()
mr = c1.merge(pop_l[["Judet"]], left_index=True, right_index=True)
mr = mr.merge(reg["Regiune"], left_on="Judet", right_index=True)
g = mr.groupby("Regiune")[anii]
c6 = g.std() / g.mean()
c6.to_csv("data_out/Cerinta6.csv")

# Cerinta 7 - total pe an
s7 = c1.sum()
s7.name = "Total"
s7.index.name = "Anul"
s7.to_csv("data_out/Cerinta7.csv")

# Cerinta 8 - media ponderata pe regiune si an, doar localitatile din cerinta 2
m2 = c2.merge(pop_l[["Judet", "Populatie"]], left_index=True, right_index=True)
m2 = m2.merge(reg["Regiune"], left_on="Judet", right_index=True)
c8 = m2[anii + ["Populatie", "Regiune"]].groupby(by="Regiune").apply(
    lambda x: x[anii].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
    include_groups=False)
c8.round(3).to_csv("data_out/Cerinta8.csv")
