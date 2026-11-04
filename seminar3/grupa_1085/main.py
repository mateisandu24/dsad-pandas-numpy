import pandas as pd
from numpy.ma.extras import average


def calcul_medie(df:pd.DataFrame):
    x = df.values
    medii = average(x[:,:-1],axis=0,weights=x[:,-1])
    return pd.Series(medii,df.columns[:-1])

pd.set_option('display.max_columns', None)

df_industrie = pd.read_csv("data_in/Industrie.csv", index_col=0)

# 1
activitati = list(df_industrie.columns.values)[1:]
df_cerinta1 = pd.DataFrame(df_industrie[activitati].sum(axis=1), columns=["Total CA"])
df_cerinta1.insert(0, "Localitate", df_industrie["Localitate"])
df_cerinta1.to_csv("data_out/Output1.csv")

# 2
df_populatie = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
df_industrie_loc = df_industrie.merge(
    df_populatie[["Judet", "Populatie"]],
    left_index=True,
    right_index=True
)
# print(df_industrie_loc.head(3))
df_cerinta2 = df_industrie_loc.apply(
    lambda x: pd.Series([x["Localitate"], x[activitati].sum() / x["Populatie"]], ["Localitate", "CA/Loc"]),
    axis=1
)
df_cerinta2.sort_values(by="CA/Loc", ascending=False).to_csv("data_out/Output2.csv")

# 3
df_industrie_ = df_industrie[df_cerinta1["Total CA"] > 0]
df_cerinta3 = pd.DataFrame(df_industrie_[activitati].apply(
    lambda x: x.index[x.argmax()],
    axis=1
),columns=["Activitate"]
)
df_cerinta3.insert(0,"Localitate",df_industrie_["Localitate"])
# print(df_cerinta3.head(3))
df_cerinta3.to_csv("data_out/Output3.csv")

# 4
df_industrie_jud = df_industrie_loc[activitati+["Judet", "Populatie"]].groupby(by="Judet").sum()
df_cerinta4 = df_industrie_jud[activitati]
df_cerinta4.round(2).to_csv("data_out/Output4.csv")

# 5
s_cerinta5 = df_industrie_jud[activitati].sum(axis=1)/df_industrie_jud["Populatie"]
s_cerinta5.name = "CA/Loc"
s_cerinta5.sort_values(ascending=False).to_csv("data_out/Output5.csv")

# 6
df_cerinta6 = df_industrie_loc[activitati+["Judet","Populatie"]].groupby(by="Judet").apply(
    func=calcul_medie,
    include_groups=False)
df_cerinta6.to_csv("data_out/Output6.csv")
