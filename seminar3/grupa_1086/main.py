import pandas as pd
from numpy.ma.extras import average

pd.set_option('display.max_columns', None)

def calcul_medie(df:pd.DataFrame):
    # print(df)
    x = df.values
    medii = average(x[:,:-1],axis=0,weights=x[:,-1])
    return pd.Series(medii,df.columns[:-1])

df_industria_a = pd.read_csv("data_in/IndustriaAlimentara.csv", index_col=0)
activitati = list(df_industria_a.columns.values)[1:]

# 1
s_total_loc = df_industria_a[activitati].apply(
    func=lambda x:x.sum(),
    axis=1)
s_total_loc.name="Total"
# print(s_total_loc)
df_cerinta1 = df_industria_a[s_total_loc!=0]
# print(df_cerinta1)
df_cerinta1.to_csv("data_out/Cerinta1.csv")

# 2
df_industria_a["Total"]=s_total_loc
# print(df_industria_a)
df_cerinta2 = df_industria_a[activitati+["Total"]].apply(
    func=lambda x:x[activitati]*100/x["Total"],
    axis=1)
df_cerinta2.insert(0,"Localitate",df_industria_a["Localitate"])
df_cerinta2.to_csv("data_out/Cerinta2.csv")

# 3
df_populatie = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
df_industria_a_loc = df_industria_a.merge(
    df_populatie,left_index=True,right_index=True
)
df_industria_a_jud = df_industria_a_loc[activitati+["Total","Judet","Populatie"]].groupby(by="Judet").sum()
# print(df_industria_a_jud)
s_cerinta3 = df_industria_a_jud["Total"]/df_industria_a_jud["Populatie"]
s_cerinta3.name="Pondere"
s_cerinta3.sort_values(ascending=False).to_csv("data_out/Cerinta3.csv")

# 4
s_cerinta4 = df_industria_a_jud[activitati].apply(
    func=lambda x:x.index[x.argmax()],
    axis=1
)
s_cerinta4.name = "Activitate"
s_cerinta4.to_csv("data_out/Cerinta4.csv")

# 5
df_coduri = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
df_industria_a_loc_reg = df_industria_a_loc.merge(
    df_coduri,left_on="Judet",right_index=True
)
# print(df_industria_a_loc_reg.head())
df_cerinta5 = df_industria_a_loc_reg[activitati+["Populatie","Regiune"]].groupby(by="Regiune").apply(func=calcul_medie,include_groups=False)
df_cerinta5.to_csv("data_out/Cerinta5.csv")

