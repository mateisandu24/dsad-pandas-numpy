import pandas as pd

from functii import shannon

df_prezenta_vot = pd.read_csv("data_in/prezenta_vot.csv", index_col=0)
variabile_vot = list(df_prezenta_vot.columns.values)[2:]
categorii_varsta = variabile_vot[variabile_vot.index("Barbati_18-24"):]
# print(variabile_vot,categorii_varsta,sep="\n")

# Cerinta 1
# LT*100/(Votanti_LP+ Votanti_LS)
s_procent_prezenta = df_prezenta_vot["LT"]*100/(df_prezenta_vot["Votanti_LP"]+df_prezenta_vot["Votanti_LS"])
s_procent_prezenta.name="Procent"
df_procent_prezenta = pd.DataFrame(s_procent_prezenta)
df_procent_prezenta.insert(0,"Localitate",df_prezenta_vot["Localitate"])
df_procent_prezenta[df_procent_prezenta["Procent"]>50].to_csv("data_out/Prezenta50.csv")

# Cerinta 2
df_prezenta_sort = df_procent_prezenta.sort_values(by=["Procent"], ascending=False)
df_prezenta_sort.to_csv("data_out/PrezentaSort.csv")

# Cerinta 3
s_categorie_dominanta = df_prezenta_vot[categorii_varsta].apply(
    func=lambda x:x.index[x.argmax()],
    axis=1
)
s_categorie_dominanta.name = "Categorie"
df_categorie_dominanta = pd.DataFrame(s_categorie_dominanta)
df_categorie_dominanta.insert(0,"Localitate",df_prezenta_vot["Localitate"])
df_categorie_dominanta.to_csv("data_out/Varsta.csv")

# Cerinta 4
categorie_varsta="Barbati_35-44"
df_categorie = df_categorie_dominanta[df_categorie_dominanta["Categorie"]==categorie_varsta]
df_categorie.to_csv("data_out/"+categorie_varsta+".csv")

# Cerinta 5
df_coduri = pd.read_csv("data_in/Coduri_Localitati.csv", index_col=0)
df_prezenta_vot_loc = df_prezenta_vot.merge(df_coduri,left_index=True,right_index=True)
df_prezenta_vot_jud = df_prezenta_vot_loc[variabile_vot+["County"]].groupby(by="County").sum()
df_prezenta_vot_jud.to_csv("data_out/Prezenta_Judet.csv")

# Cerinta 6
df_disparitate = df_prezenta_vot_loc[categorii_varsta+["County"]].groupby(by="County").\
    apply(func=shannon,include_groups=False)
df_disparitate.to_csv("data_out/Disparitate.csv")
