# Industrie.csv - cerinte lucrate de student (NERULAT pe date reale)
import pandas as pd

df = pd.read_csv("data_in/Industrie.csv", index_col=0)
pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)

# 1 - cifra de afaceri totala pe localitate, in ordinea din fisier
s = df.iloc[:, 1:].sum(axis=1)
c1 = df[["Localitate"]].copy()
c1["Cifra de afaceri"] = s
c1.to_csv("data_out/Output1.csv")

# 2 - cifra de afaceri pe locuitor, descrescator
c2 = df[["Localitate"]].copy()
c2["CF/Loc"] = s / pop["Populatie"]                # aliniere dupa Siruta
c2 = c2.sort_values(by="CF/Loc", ascending=False)
c2.to_csv("data_out/Output2.csv")

# 3 - activitatea dominanta pe localitate (doar localitatile cu activitate)
filtrate = df.iloc[:, 1:].sum(axis=1) > 0
df_f = df[filtrate]
c3 = df_f[["Localitate"]].copy()
c3["Activitate"] = df_f.iloc[:, 1:].idxmax(axis=1)
c3.to_csv("data_out/Output3.csv")
