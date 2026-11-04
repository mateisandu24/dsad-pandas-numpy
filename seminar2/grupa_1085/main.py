import pandas as pd

from functii import nan_replace_df, shannon

pd.set_option('display.max_columns', None)

df_etnii = pd.read_csv("data_in/Ethnicity.csv", index_col=0)
# print(df_etnii,type(df_etnii),sep="\n")

etnii = list(df_etnii.columns.values)[1:]

nan_replace_df(df_etnii)

df_coduri_loc = pd.read_csv("data_in/Coduri_Localitati.csv", index_col=0)
df_etnii_loc = df_etnii[etnii].merge(df_coduri_loc,left_index=True,right_index=True)
# print(df_etnii_loc.head())
df_etnii_jud = df_etnii_loc[etnii+["County"]].groupby(by="County").sum()
df_etnii_jud.to_csv("data_out/Ethnicity_Jud.csv")

df_coduri_jud = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
df_etnii_jud_reg = df_etnii_jud.merge(df_coduri_jud,left_index=True,right_on="IndicativJudet")
df_etnii_reg = df_etnii_jud_reg[etnii+["Regiune"]].groupby(by="Regiune").sum()
df_etnii_reg.to_csv("data_out/Ethnicity_Reg.csv")

#Tema: Calcul la nivel de macroregiune

# Calcul procente
df_etnii_p = df_etnii[etnii].apply(func=lambda x:x*100/x.sum(),axis=1)
df_etnii_p.insert(0,"Localitate",df_etnii["City"])
df_etnii_p.to_csv("data_out/Ethnicity_P.csv")

df_etnii_jud_p = df_etnii_jud[etnii].apply(func=lambda x:x*100/x.sum(),axis=1)
df_etnii_jud_p.to_csv("data_out/Ethnicity_P_Jud.csv")

#Tema: Calcul pentru regiune si macroregiune

df_shannon = df_etnii_loc[etnii+["County"]].groupby(by="County").apply(func=shannon,include_groups=False)
df_shannon.fillna(0,inplace=True)
df_shannon.to_csv("data_out/Ethnicity_Shannon.csv")

