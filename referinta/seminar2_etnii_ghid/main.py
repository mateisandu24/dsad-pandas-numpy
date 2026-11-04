from itertools import groupby
import pandas as pd
from functii import nan_replace_df, disimilaritate

df = pd.read_csv('data_in/data_in/Ethnicity.csv',index_col=0)
nan_replace_df(df)

etnii = list(df)[1:]

df_coduri_loc = pd.read_csv('data_in/data_in/Coduri_Localitati.csv',index_col=0)
df_etnii_loc = df.merge(df_coduri_loc,left_index=True,right_index=True)

#print(df_etnii_loc)

df_etnii_jud = (df_etnii_loc[etnii+["County"]]
                .groupby(by="County").sum())
df_etnii_jud.to_csv("data_out/Etnii_jud.csv")


df_coduri_judete = pd.read_csv('data_in/data_in/Coduri_Judete.csv',index_col=0)
df_etnii_jud_ = (df_etnii_jud
                 .merge(df_coduri_judete,left_index=True,right_on="IndicativJudet"))

df_etnii_reg = (df_etnii_jud_[etnii+["Regiune"]]
                .groupby(by="Regiune")
                .sum())
df_etnii_reg.to_csv("data_out/Etnii_reg.csv")


df_etnii_loc_p = df[etnii].apply(func=lambda x: x*100/x.sum(), axis=1)
df_etnii_loc_p.to_csv("data_out/Etnii_loc_procente.csv")

df_etnii_jud_p = df_etnii_jud[etnii].apply(func=lambda x: x*100/x.sum(), axis=1)
df_etnii_jud_p.to_csv("data_out/Etnii_jud_proc.csv")

df_disimilaritate = (df_etnii_loc[etnii+["County"]]
                     .groupby(by="County")
                     .apply(func=disimilaritate,include_groups=False))
print(df_disimilaritate)

