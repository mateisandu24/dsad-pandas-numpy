import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv("data_in/Innoptari.csv")

# 1
df_innoptari = df.pivot(index="Siruta",columns="Ani",values="Valoare")
df_innoptari.fillna(0, inplace=True)
coloane = [v.removeprefix("Anul ") for v in df_innoptari.columns.values]
df_innoptari.columns = coloane
df_innoptari.to_csv("data_out/Cerinta1.csv")

# 2
s_fltru_activitate = df_innoptari.apply(
    lambda x: (x>0).all() ,
    axis=1
)
# print(s_fltru_activitate)
df_cerinta2 = df_innoptari[s_fltru_activitate]
df_cerinta2.to_csv("data_out/Cerinta2.csv")

# 3
df_populatie = pd.read_csv("data_in/PopulatieLocalitati.csv",index_col=0)
df_innoptari_loc = df_innoptari.merge(df_populatie,left_index=True,right_index=True)
# print(df_innoptari_loc.head(3))
df_cerinta3 = pd.DataFrame(df_innoptari_loc[coloane].apply(
    lambda x:x.index[x.argmax()] ,
    axis=1
), columns=["Anul"]
)
df_cerinta3.insert(0,"Localitate",df_innoptari_loc["Localitate"])
# print(df_cerinta3)
df_cerinta3.to_csv("data_out/Cerinta3.csv")

# 4
df_cerinta4 = df_innoptari_loc.apply(
    lambda x: pd.Series([x["Localitate"],x[coloane].sum()*1000/x["Populatie"]],["Localitate","Innoptari/1000"]),
    axis=1
)
df_cerinta4.to_csv("data_out/Cerinta4.csv")
df_cerinta4.sort_values(by="Innoptari/1000",ascending=False).to_csv("data_out/Cerinta4_sort.csv")

# 5
df_innoptari_jud = df_innoptari_loc[coloane+["Judet","Populatie"]].groupby(by="Judet").sum()
# print(df_innoptari_jud.head(3))
df_cerinta5 = df_innoptari_jud.apply(
    lambda x: x[coloane]*1000/x["Populatie"],
    axis=1
)
df_cerinta5.round(1).to_csv("data_out/Cerinta5.csv")

# 6
df_coduri = pd.read_csv("data_in/Coduri_Judete.csv",index_col=0)
df_innoptari_loc_reg = df_innoptari_loc.merge(
    df_coduri,
    left_on="Judet",
    right_index=True)
# print(df_innoptari_loc_reg.head(3))
df_cerinta6 = df_innoptari_loc_reg[coloane+["Regiune"]].groupby("Regiune").aggregate(func=lambda x:x.std()/x.mean())
# print(df_cerinta6)
df_cerinta6.round(2).to_csv("data_out/Cerinta6.csv")
