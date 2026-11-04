import pandas as pd

from functii import nan_replace_df, shannon

df_confesiuni = pd.read_csv('data_in/Religious.csv',index_col=0)
# print(df_confesiuni,type(df_confesiuni))
confesiuni = list(df_confesiuni)[1:]

nan_replace_df(df_confesiuni)

df_coduri_loc = pd.read_csv('data_in/Coduri_Localitati.csv',index_col=0)
df_confesiuni_loc = df_confesiuni[confesiuni].merge(df_coduri_loc,left_index=True,right_index=True)
df_confesiuni_jud = df_confesiuni_loc[confesiuni+["County"]].groupby(by=['County']).sum()
df_confesiuni_jud.to_csv('data_out/Confesiuni_jud.csv')

df_coduri_jud = pd.read_csv('data_in/Coduri_Judete.csv',index_col=0)
df_confesiuni_jud_reg = df_confesiuni_jud.merge(
    df_coduri_jud,
    left_index=True,
    right_on="IndicativJudet")
df_confesiuni_reg = (df_confesiuni_jud_reg[confesiuni+["Regiune"]]
                     .groupby(by=['Regiune']).sum())
df_confesiuni_reg.to_csv('data_out/Confesiuni_reg.csv')

# Tema: calcul pe macroregiuni
df_confesiuni_p = df_confesiuni[confesiuni].apply(
    func=lambda x:x*100/x.sum(),
    axis=1)
df_confesiuni_p.insert(0,"Localitate",df_confesiuni["City"])
df_confesiuni_p.to_csv('data_out/Confesiuni_p.csv')

df_confesiuni_jud_p = df_confesiuni_jud[confesiuni].apply(
    func=lambda x:x*100/x.sum(), axis=1)
df_confesiuni_jud_p.to_csv('data_out/Confesiuni_jud_p.csv')

df_shannon=df_confesiuni_loc[confesiuni+["County"]].groupby(by=['County']).apply(func=shannon,include_groups=False)
df_shannon.to_csv('data_out/Shannon.csv')

