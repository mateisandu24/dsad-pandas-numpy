# Industrie.csv - aceleasi 5 cerinte ca la seminarul 3 (cifra de afaceri pe industrii)
import pandas as pd
from numpy.ma.extras import average

pd.set_option("display.max_columns", None)
df_industrie = pd.read_csv("data_in/Industrie.csv", index_col=0)
activitati = list(df_industrie.columns.values)[1:]

# 1
s_total_loc = df_industrie[activitati].apply(func=lambda x: x.sum(), axis=1)
s_total_loc.name = "Total"
df_cerinta1 = df_industrie[s_total_loc != 0]
df_cerinta1.to_csv("data_out/Cerinta1.csv")

# 2
df_industrie["Total"] = s_total_loc
df_cerinta2 = df_industrie[activitati + ["Total"]].apply(
    func=lambda x: x[activitati] * 100 / x["Total"], axis=1)
df_cerinta2.insert(0, "Localitate", df_industrie["Localitate"])
df_cerinta2.to_csv("data_out/Cerinta2.csv")

# 3  (Judet cu MAJUSCULE in populatie -> litere mici, ca in Coduri_Judete)
df_populatie = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
df_populatie["Judet"] = df_populatie["Judet"].str.lower()
df_industrie_loc = df_industrie.merge(df_populatie, left_index=True, right_index=True)
df_industrie_jud = df_industrie_loc[activitati + ["Total", "Judet", "Populatie"]].groupby(by="Judet").sum()
s_cerinta3 = df_industrie_jud["Total"] / df_industrie_jud["Populatie"]
s_cerinta3.name = "Pondere"
s_cerinta3.sort_values(ascending=False).to_csv("data_out/Cerinta3.csv")

# 4
s_cerinta4 = df_industrie_jud[activitati].apply(func=lambda x: x.index[x.argmax()], axis=1)
s_cerinta4.name = "Activitate"
s_cerinta4.to_csv("data_out/Cerinta4.csv")


# 5
def calcul_medie(df: pd.DataFrame):
    x = df.values
    medii = average(x[:, :-1], axis=0, weights=x[:, -1])
    return pd.Series(medii, df.columns[:-1])


df_coduri = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
df_industrie_loc_reg = df_industrie_loc.merge(df_coduri, left_on="Judet", right_index=True)
df_cerinta5 = (df_industrie_loc_reg[activitati + ["Populatie", "Regiune"]]
               .groupby(by="Regiune")
               .apply(func=lambda x: calcul_medie(x), include_groups=False))
df_cerinta5.to_csv("data_out/Cerinta5.csv")

# Control: cerinta 1 = 2317 localitati; cerinta 5 = 8 regiuni
