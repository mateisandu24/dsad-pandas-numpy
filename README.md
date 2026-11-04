# DSAD - pandas / numpy in stilul seminarului

Rezolvari pentru seminariile si subiectele de tip "date statistice pe localitati / judete / regiuni din Romania".
Cheia de legatura intre tabele este codul Siruta (`index_col=0`).

## Seminare
| Folder | Seminar | Ce acopera |
|---|---|---|
| `seminar1_natalitate/` | Seminar 1 | `pivot_table`, inlocuire NaN cu media coloanei, covarianta, corelatie, standardizare (numpy) |
| `seminar2_etnii/` | Seminar 2 | NaN in DataFrame (`functii.py`), `merge`, `groupby` pe judet si regiune, procente pe rand, indice de disimilaritate |
| `seminar3_industrie_alimentara/` | Seminar 3 | activitati pe localitate, pondere %, rata pe locuitor pe judet, activitate dominanta, media ponderata pe regiune |

## Subiecte
| Folder | Subiect | Nivel |
|---|---|---|
| `subiecte/s1_1085_firme_2014/` | S1_1085 (12014.csv), 4 cerinte | localitate, judet |
| `subiecte/industrie_cifra_afaceri/` | Industrie.csv: cele 5 cerinte de seminar + 3 cerinte lucrate | localitate, judet, regiune |
| `subiecte/innoptari/` | Innoptari.csv, format lung + pivot, 6 cerinte | localitate, judet, regiune |
| `subiecte/test_agricultura/` | Test generat Agricultura | localitate, judet, regiune |
| `subiecte/test_firme_pe_ani/` | Test generat Firme pe ani, 8 cerinte | localitate, judet, regiune |

## Cum rulezi
Pune fisierele CSV in `data_in/` (nu sunt incluse in repo), apoi din radacina:
`python seminar3_industrie_alimentara/main.py`

## Capcane
- `PopulatieLocalitati.csv` se citeste mereu cu `index_col=0`.
- Indicativele de judet pot fi cu majuscule intr-un fisier si cu litere mici in altul.
- `seminar2_etnii/main.py` foloseste caile `data_in/data_in/...` (asa a fost la seminar); ajusteaza-le dupa structura ta.
- `industrie_cifra_afaceri/main_cerinte_student.py` nu a fost rulat pe date reale.
