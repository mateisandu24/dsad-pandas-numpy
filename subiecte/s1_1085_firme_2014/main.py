# Subiect S1_1085 - firme 2014 (12014.csv)
import pandas as pd
import numpy as np

df_firme = pd.read_csv("data_in/12014.csv", index_col=0)
df_pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)

# Cerinta 1
df_sal = df_firme[df_firme["NrSal"] > 0]
c1 = df_sal[["DenLocalitate"]].copy()
c1["Raport CA/NrSal"] = df_sal["TotalCifraAfaceri"] / df_sal["NrSal"]
c1 = c1.sort_values(by="Raport CA/NrSal", ascending=False)
c1.round(3).to_csv("data_out/Output1.csv")

# Cerinta 2
df_loc = df_firme.merge(df_pop[["Judet", "Populatie"]], left_index=True, right_index=True)
df_jud = df_loc[["NrSal", "Judet", "Populatie"]].groupby(by="Judet").sum()
s2 = df_jud["NrSal"] * 1000 / df_jud["Populatie"]
s2.name = "Rata Ocuparii"
s2.sort_values(ascending=False).to_csv("data_out/Output2.csv")

# Cerinta 3
df_loc["Profit/loc"] = df_loc["TotalProfit"] / df_loc["Populatie"]
s3 = (df_loc[["DenLocalitate", "Judet", "Profit/loc"]]
      .groupby(by="Judet")
      .apply(lambda g: g["DenLocalitate"].iloc[g["Profit/loc"].argmax()], include_groups=False))
s3.name = "Localitate"
s3.to_csv("data_out/Output3.csv")

# Cerinta 4
indicatori = ["NrFirme", "NrSal", "TotalCifraAfaceri", "TotalProfit", "TotalPierdere"]
c4 = (df_loc[indicatori + ["Judet", "Populatie"]]
      .groupby(by="Judet")
      .apply(lambda x: x[indicatori].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
             include_groups=False))
c4.round(3).to_csv("data_out/Output4.csv")

# Control: Output1 = 2749 randuri; Output2/3/4 = 42 randuri
