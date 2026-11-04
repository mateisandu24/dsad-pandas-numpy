# Seminar 2 - completari pentru Tema 2.1 (etnii) si Tema 2.2 (confesiuni):
#   - populatie pe judet / regiune / macroregiune
#   - procente pe localitate / judet / regiune / macroregiune
#   - Tema 2.1: indice de disimilaritate D si Shannon-Weaver H (log2) pe judet, per etnie
#   - Tema 2.2: Shannon-Weaver (log2), Simpson, Simpson invers pe judet si pe regiune
#               (n = numarul de confesiuni, p_i = ponderea confesiunii i in unitate)
# Rulare:  python completari/seminar2_diversitate_segregare.py
from pathlib import Path

import numpy as np
import pandas as pd

RAD = Path(__file__).resolve().parent
DATE = RAD.parent / "seminar2" / "grupa_1073" / "data_in"
DATE_REL = RAD.parent / "seminar2" / "grupa_1075" / "data_in"
IES = RAD / "data_out" / "seminar2"
IES.mkdir(parents=True, exist_ok=True)


def disimilaritate(df: pd.DataFrame):
    # D = 0.5 * sum_i |x_i/Tx - r_i/Tr|, pe fiecare coloana (grup etnic)
    x = df.values
    tx = np.sum(x, axis=0)
    tx[tx == 0] = 1
    sx = np.sum(x, axis=1)
    r = (sx - x.T).T
    tr = np.sum(r, axis=0)
    d = 0.5 * np.sum(np.abs(x / tx - r / tr), axis=0)
    return pd.Series(d, df.columns)


def shannon_segregare(df: pd.DataFrame):
    # H = - sum_i p_i log2 p_i, p_i = ponderea localitatii i in totalul grupului (pe coloana)
    x = df.values
    tx = np.sum(x, axis=0)
    tx[tx == 0] = 1
    p = x / tx
    with np.errstate(divide="ignore", invalid="ignore"):
        h = -np.nansum(np.where(p > 0, p * np.log2(p), 0.0), axis=0)
    return pd.Series(h, df.columns)


def indici_diversitate(df: pd.DataFrame):
    # df: o linie = o unitate (judet / regiune), coloanele = confesiuni (populatie)
    p = df.div(df.sum(axis=1), axis=0)
    with np.errstate(divide="ignore", invalid="ignore"):
        h = -(p * np.log2(p)).where(p > 0, 0.0).sum(axis=1)
    s1 = 1 - (p ** 2).sum(axis=1)
    s2 = 1 / (p ** 2).sum(axis=1)
    return pd.DataFrame({"Shannon": h, "Simpson": s1, "SimpsonInvers": s2})


def niveluri(df_loc: pd.DataFrame, coloane, coduri_judete, coduri_regiuni):
    # df_loc are deja coloana "County"; intoarce populatia pe judet, regiune, macroregiune
    jud = df_loc[coloane + ["County"]].groupby(by="County").sum()
    j = jud.merge(coduri_judete[["IndicativJudet", "Regiune"]], left_index=True, right_on="IndicativJudet")
    reg = j[coloane + ["Regiune"]].groupby(by="Regiune").sum()
    r = reg.merge(coduri_regiuni, left_index=True, right_on="Regiune")
    macro = r[coloane + ["MacroRegiune"]].groupby(by="MacroRegiune").sum()
    return jud, reg, macro


def procente(df, coloane):
    return df[coloane].apply(lambda x: x * 100 / x.sum(), axis=1)


coduri_loc = pd.read_csv(DATE / "Coduri_Localitati.csv", index_col=0)
coduri_jud = pd.read_csv(DATE / "Coduri_Judete.csv", index_col=0)
coduri_reg = pd.read_csv(DATE / "Coduri_Regiuni.csv")

# ---------------- Tema 2.1 - etnii ----------------
df = pd.read_csv(DATE / "Ethnicity.csv", index_col=0)
etnii = list(df.columns.values)[1:]
df_loc = df[etnii].merge(coduri_loc, left_index=True, right_index=True)
jud, reg, macro = niveluri(df_loc, etnii, coduri_jud, coduri_reg)
jud.to_csv(IES / "Etnii_Jud.csv")
reg.to_csv(IES / "Etnii_Reg.csv")
macro.to_csv(IES / "Etnii_Macro.csv")
p_loc = procente(df, etnii)
p_loc.insert(0, "Localitate", df["City"])
p_loc.to_csv(IES / "Etnii_P_Loc.csv")
procente(jud, etnii).to_csv(IES / "Etnii_P_Jud.csv")
procente(reg, etnii).to_csv(IES / "Etnii_P_Reg.csv")
procente(macro, etnii).to_csv(IES / "Etnii_P_Macro.csv")
df_loc[etnii + ["County"]].groupby(by="County").apply(
    disimilaritate, include_groups=False).to_csv(IES / "Etnii_Disimilaritate.csv")
df_loc[etnii + ["County"]].groupby(by="County").apply(
    shannon_segregare, include_groups=False).to_csv(IES / "Etnii_Shannon.csv")

# ---------------- Tema 2.2 - confesiuni ----------------
dr = pd.read_csv(DATE_REL / "Religious.csv", index_col=0)
confesiuni = list(dr.columns.values)[1:]
dr_loc = dr[confesiuni].merge(coduri_loc, left_index=True, right_index=True)
jud_r, reg_r, macro_r = niveluri(dr_loc, confesiuni, coduri_jud, coduri_reg)
jud_r.to_csv(IES / "Confesiuni_Jud.csv")
reg_r.to_csv(IES / "Confesiuni_Reg.csv")
macro_r.to_csv(IES / "Confesiuni_Macro.csv")
pr_loc = procente(dr, confesiuni)
pr_loc.insert(0, "Localitate", dr["City"])
pr_loc.to_csv(IES / "Confesiuni_P_Loc.csv")
procente(jud_r, confesiuni).to_csv(IES / "Confesiuni_P_Jud.csv")
procente(reg_r, confesiuni).to_csv(IES / "Confesiuni_P_Reg.csv")
procente(macro_r, confesiuni).to_csv(IES / "Confesiuni_P_Macro.csv")
indici_diversitate(jud_r).to_csv(IES / "Confesiuni_Diversitate_Jud.csv")
indici_diversitate(reg_r).to_csv(IES / "Confesiuni_Diversitate_Reg.csv")
print("Gata:", IES)
