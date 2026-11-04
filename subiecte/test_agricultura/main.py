# Test generat "Agricultura" (stil S1_1085)
import pandas as pd
import numpy as np

df_agri = pd.read_csv("data_in/Agricultura.csv", index_col=0)
df_pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
df_reg = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)

# Cerinta 1
df_ag = df_agri[df_agri["SuprafataHa"] > 0].copy()
df_ag["Randament"] = df_ag["ProductieTone"] / df_ag["SuprafataHa"]
df_c1 = df_ag[["DenLocalitate", "Randament"]].sort_values(by="Randament", ascending=False)
df_c1.round(3).to_csv("data_out/Output1.csv")

# Cerinta 2 (capcana: majuscule vs litere mici)
df_reg.index = df_reg.index.str.upper()
df_loc = df_agri.merge(df_pop[["Judet", "Populatie"]], left_index=True, right_index=True)
df_loc_reg = df_loc.merge(df_reg["Regiune"], left_on="Judet", right_index=True)
df_regiuni = df_loc_reg[["NrExploatatii", "Populatie", "Regiune"]].groupby(by="Regiune").sum()
s_c2 = df_regiuni["NrExploatatii"] * 1000 / df_regiuni["Populatie"]
s_c2.name = "Densitate"
s_c2.sort_values(ascending=False).to_csv("data_out/Output2.csv")

# Cerinta 3
df_loc["Productie/loc"] = df_loc["ProductieTone"] / df_loc["Populatie"]
s_c3 = (df_loc[["DenLocalitate", "Judet", "Productie/loc"]]
        .groupby(by="Judet")
        .apply(lambda g: g["DenLocalitate"].iloc[g["Productie/loc"].argmax()], include_groups=False))
s_c3.name = "Localitate"
s_c3.to_csv("data_out/Output3.csv")

# Cerinta 4
indicatori = ["NrExploatatii", "SuprafataHa", "ProductieTone", "Subventii", "Cheltuieli"]
df_c4 = (df_loc[indicatori + ["Judet", "Populatie"]]
         .groupby(by="Judet")
         .apply(lambda x: x[indicatori].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
                include_groups=False))
df_c4.round(3).to_csv("data_out/Output4.csv")

# Control: Output1 = 2972 randuri, Output2 = 8, Output3 = 42, Output4 = 42
