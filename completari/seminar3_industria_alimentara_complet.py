# Seminar 3 - IndustriaAlimentara.csv: toate cele 6 cerinte, conform enuntului (Tema 2.4)
# Completeaza solutiile din seminar3/grupa_1073, grupa_1075, grupa_1086, unde:
#   - cerinta 2 trebuie sa dea procente (x100) si 0 (nu NaN) cand totalul e 0
#   - cerinta 3 trebuie sa fie pe JUDET, descrescator, cu antetul "Ponderi"
#   - cerinta 6 (indicii de localizare) lipseste
# Rulare:  python completari/seminar3_industria_alimentara_complet.py
from pathlib import Path

import numpy as np
import pandas as pd

RAD = Path(__file__).resolve().parent
DATE = RAD.parent / "seminar3" / "grupa_1086" / "data_in"
IES = RAD / "data_out" / "seminar3_industria_alimentara"
IES.mkdir(parents=True, exist_ok=True)

df_industrie = pd.read_csv(DATE / "IndustriaAlimentara.csv", index_col=0)
df_populatie = pd.read_csv(DATE / "PopulatieLocalitati.csv", index_col=0)
df_coduri = pd.read_csv(DATE / "Coduri_Judete.csv", index_col=0)   # index = IndicativJudet (3 coloane la Seminar 3)
activitati = list(df_industrie.columns.values)[1:]

# Cerinta 1 - localitati cu cel putin un angajat, aceleasi coloane ca fisierul initial
s_total = df_industrie[activitati].sum(axis=1)
df_industrie[s_total > 0].to_csv(IES / "Cerinta1.csv")

# Cerinta 2 - procent pe activitate in total pe localitate; total 0 -> procente 0
df_c2 = df_industrie[activitati].mul(100).div(s_total.replace(0, np.nan), axis=0).fillna(0)
df_c2.insert(0, "Localitate", df_industrie["Localitate"])
df_c2.to_csv(IES / "Cerinta2.csv")

# Cerinta 3 - judete sortate descrescator dupa (angajati industrie alimentara / populatie)
df_loc = df_industrie[activitati].merge(df_populatie[["Judet", "Populatie"]],
                                        left_index=True, right_index=True)
df_jud = df_loc.groupby(by="Judet").sum()
s_c3 = df_jud[activitati].sum(axis=1) / df_jud["Populatie"]
s_c3.name = "Ponderi"
s_c3.sort_values(ascending=False).to_csv(IES / "Cerinta3.csv")

# Cerinta 4 - activitatea dominanta pe judet
s_c4 = df_jud[activitati].idxmax(axis=1)
s_c4.name = "Activitate"
s_c4.to_csv(IES / "Cerinta4.csv")

# Cerinta 5 - media ponderata (pondere = populatia localitatii) pe regiune
df_loc_reg = df_loc.merge(df_coduri["Regiune"], left_on="Judet", right_index=True)
df_c5 = df_loc_reg[activitati + ["Populatie", "Regiune"]].groupby(by="Regiune").apply(
    lambda x: x[activitati].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
    include_groups=False)
df_c5.to_csv(IES / "Cerinta5.csv")

# Cerinta 6 - indice de localizare = (pondere judet in activitate la nivel national)
#                                    / (pondere populatie judet in populatia tarii)
pondere_activitate = df_jud[activitati] / df_jud[activitati].sum()
pondere_populatie = df_jud["Populatie"] / df_jud["Populatie"].sum()
df_c6 = pondere_activitate.div(pondere_populatie, axis=0)
df_c6.to_csv(IES / "Cerinta6.csv")
print("Gata:", IES)
