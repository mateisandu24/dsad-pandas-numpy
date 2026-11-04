# DSAD - pandas / numpy in stilul seminarului

```text
Repo (tinta de publicare, vezi sectiunea 15): github.com/mateisandu24/dsad-pandas-numpy
Autor: mateisandu24
Documentatie generata: 2026-11-04

Acest fisier contine documentatia COMPLETA a repo-ului: ce exista, cum se ruleaza, ce date se folosesc,
enuntul fiecarei teme, ce face fiecare solutie, formulele, rezultatele verificate, diferentele fata de enunt,
ghidul de retete si capcane, si codul sursa integral. Este scris fara diacritice si fara tabele markdown,
astfel incat sa poata fi citit identic ca README.md si ca README.txt.

Mediu in care a fost verificat tot codul (rulat efectiv, vezi sectiunea 12):
    Python 3.13, pandas 3.0.5, numpy 2.5.3, scipy 1.18.1, scikit-learn 1.9.1

CUPRINS
    1.  Ce contine repo-ul
    2.  Cum rulezi
    3.  Harta seminarelor si a grupelor
    4.  Datele (dictionar de fisiere)
    5.  Conventii de stil
    6.  Formule si definitii
    7.  Seminar 1 - statistica pe matrici (grupele 1075, 1077, 1085, 1086)
    8.  Seminar 2 - etnii, confesiuni, prezenta la vot (grupele 1073, 1075, 1077, 1085, 1086)
    9.  Seminar 3 - industrie, innoptari (grupele 1073, 1075, 1077, 1085, 1086)
    10. Completari verificate (cerinte lipsa sau neconforme cu enuntul)
    11. Subiecte si teste (S1_1085, Industrie, Innoptari, Agricultura, Firme pe ani)
    12. Rezultate verificate (rulare pe date reale)
    13. Diferente fata de enunt (lista consolidata)
    14. Capcane noi gasite la verificare
    15. Publicare pe GitHub
    Anexa A. Ghidul complet (retete B1-B15, capcane C, subiecte D1-D7, metode E, lista F)
    Anexa B. Codul sursa complet al fiecarui folder
```

# 1. Ce contine repo-ul

```text
    dsad-pandas-numpy/
      README.md                 aceasta documentatie
      README.txt                aceeasi documentatie, text simplu
      requirements.txt          pandas, numpy, scipy, scikit-learn
      seminar1/
        grupa_1075/  grupa_1077/  grupa_1085/  grupa_1086/
      seminar2/
        grupa_1073/  grupa_1075/  grupa_1077/  grupa_1085/  grupa_1086/
      seminar3/
        grupa_1073/  grupa_1075/  grupa_1077/  grupa_1085/  grupa_1086/
      completari/               cerintele lipsa / neconforme, rezolvate si verificate
        seminar2_diversitate_segregare.py
        seminar3_industria_alimentara_complet.py
        data_out/               rezultatele celor doua scripturi
      subiecte/                 subiecte de tip examen (S1_1085, Industrie, Innoptari, teste generate)
      referinta/                codul de referinta primit la inceput + ghidul GHID_pandas_numpy.txt

Fiecare folder grupa_XXXX este un proiect de sine statator, exact ca la seminar:
    main.py        solutia (puncte de intrare)
    functii.py     functii ajutatoare (doar la seminariile 1 si 2)
    data_in/       fisierele CSV de intrare
    data_out/      fisierele CSV rezultate (cele livrate de student, pastrate ca referinta)
    TemaN_M.pdf    enuntul temei (lipseste la Seminar 1 grupa 1086, care e pe natalitate)

Fiecare folder poate fi rulat izolat: nu depinde de alt folder.

Un commit git pentru fiecare exercitiu (14 foldere de grupa + completari + subiecte + referinta):
    git log --oneline
```

# 2. Cum rulezi

```text
Instalare dependente (o singura data):

    pip install -r requirements.txt

Rularea unei solutii: INTRI in folderul grupei si rulezi main.py. Caile din cod sunt relative
("data_in/..." si "data_out/..."), deci directorul curent trebuie sa fie folderul grupei:

    cd seminar3/grupa_1086
    python main.py

Rezultatele apar in data_out/ si suprascriu fisierele existente (sunt aceleasi daca nu ai schimbat codul).
Folderul data_out/ trebuie sa existe, altfel to_csv da eroare; in repo exista deja in toate folderele.

Rularea completarilor (din radacina repo-ului):

    python completari/seminar3_industria_alimentara_complet.py
    python completari/seminar2_diversitate_segregare.py

Versiuni de biblioteci:
    - Codul foloseste groupby(...).apply(..., include_groups=False). Parametrul include_groups
      exista din pandas 2.2 (de aceea requirements.txt cere pandas>=2.2). A fost rulat si pe pandas 3.0.5.
    - Seminar 1 grupa 1085 foloseste scipy.stats.anderson(..., method="interpolate"), disponibil
      doar in scipy recent (verificat pe 1.18.1).
    - Seminar 1 grupa 1075 are importul "from sklearn.preprocessing import StandardScaler"
      (folosit doar intr-un bloc comentat), deci scikit-learn trebuie instalat ca sa porneasca.

PyCharm: fiecare folder de grupa se deschide ca proiect separat (asa a fost lucrat), deoarece
functii.py se importa din main.py ("from functii import ...") si caile sunt relative la folderul proiectului.
```

# 3. Harta seminarelor si a grupelor

```text
Cele 14 foldere de grupa acopera 3 seminarii. Fiecare grupa are o tema diferita (PDF), dar aceleasi
tipare de lucru. Cheia de legatura intre tabele este codul Siruta (indexul tabelelor).

SEMINAR 1 - statistica pe matrici de date (numpy, scipy, standardizare, distante, teste)
    grupa 1075   Tema 1.1   standardizare si centrare; matrici de corelatie si covarianta, totale si pe grupe
    grupa 1077   Tema 1.3   distante euclidiene si Mahalanobis; inertii; centri de grupa; distante intre centri
    grupa 1085   Tema 1.2   teste de concordanta cu repartitia normala (Shapiro, KS, Anderson, Chi2)
    grupa 1086   (fara PDF) natalitate: pivot, inlocuire NaN, covarianta, corelatie, standardizare
    Date: Teritorial_2022.csv (grupele 1075, 1077, 1085), Natalitate_Ro.csv (grupa 1086)

SEMINAR 2 - populatie pe etnii/confesiuni/categorii, agregare pe judet-regiune, procente, indici
    grupa 1073   Tema 2.1   etnii: populatie pe judet/regiune/macroregiune, procente, indici de segregare
    grupa 1085   Tema 2.1   (aceeasi tema ca 1073)
    grupa 1086   Tema 2.1   (aceeasi tema ca 1073)
    grupa 1075   Tema 2.2   confesiuni: populatie, ponderi, indici de diversitate (Shannon, Simpson, Simpson invers)
    grupa 1077   Tema 2.3   prezenta la vot 2020: prezenta, categorii de varsta, Shannon pe judet
    Date: Ethnicity.csv, Religious.csv, prezenta_vot.csv + Coduri_Localitati / Coduri_Judete / Coduri_Regiuni

SEMINAR 3 - cerinte pe localitate / judet / regiune cu merge, groupby, medii ponderate, pivot
    grupa 1073   Tema 2.4   industria alimentara (6 cerinte)
    grupa 1075   Tema 2.4   (aceeasi tema ca 1073)
    grupa 1086   Tema 2.4   (aceeasi tema ca 1073)
    grupa 1085   Tema 2.5   industrie, cifra de afaceri (6 cerinte)
    grupa 1077   Tema 2.6   innoptari in structuri turistice, format lung -> pivot (6 cerinte)
    Date: IndustriaAlimentara.csv, Industrie.csv, Innoptari.csv + PopulatieLocalitati.csv, Coduri_Judete.csv

Nivelul unei cerinte decide pasii (regula centrala din ghid):
    "pentru fiecare localitate"  -> fara groupby, lucrezi pe randuri
    "pentru fiecare judet"       -> merge cu populatia, groupby("Judet")
    "pentru fiecare regiune"     -> merge cu populatia, merge cu Coduri_Judete, groupby("Regiune")
```

# 4. Datele (dictionar de fisiere)

```text
Toate fisierele sunt CSV cu antet si separator virgula. Unde exista, codul Siruta este prima coloana si devine
index la citirea cu index_col=0 (se numeste Siruta, sau Code in Ethnicity.csv, Religious.csv si
Coduri_Localitati.csv). Dimensiunile sunt masurate pe fisierele din repo.

    Coduri_Judete.csv (versiunea 1 din 2)
        folosit in:  S2/1073, S2/1075, S2/1085, S2/1086
        dimensiune:  42 randuri x 4 coloane
        coloane:     NrCrt, IndicativJudet, NumeJudet, Regiune
        primul rand: 1, ab, Alba, Centru

    Coduri_Judete.csv (versiunea 2 din 2)
        folosit in:  S3/1073, S3/1075, S3/1077, S3/1086
        dimensiune:  42 randuri x 3 coloane
        coloane:     IndicativJudet, NumeJudet, Regiune
        primul rand: ab, Alba, Centru

    Coduri_Localitati.csv
        folosit in:  S2/1073, S2/1075, S2/1077, S2/1085, S2/1086
        dimensiune:  3181 randuri x 3 coloane
        coloane:     Code, City, County
        primul rand: 1017, Municipiul Alba Iulia, ab

    Coduri_Regiuni.csv
        folosit in:  S2/1073, S2/1075, S2/1085, S2/1086
        dimensiune:  8 randuri x 2 coloane
        coloane:     Regiune, MacroRegiune
        primul rand: Centru, 1

    Ethnicity.csv
        folosit in:  S2/1073, S2/1085, S2/1086
        dimensiune:  3181 randuri x 24 coloane
        coloane:     Code, City, Romanian, Hungarians, Romany, Ukrainians, Germans, Turks, Russians_Lippovans,
                     Tatars, Serbs, Slovaks, Bulgarians, Croats, Greeks, Italians, Jews, Czechs, Poles, Chinese,
                     Armenians, Csango, Macedonians, Another
        primul rand: 1017, Municipiul Alba Iulia, 55671, 1010, 1119, 4, 115, 13, ...

    IndustriaAlimentara.csv
        folosit in:  S3/1073, S3/1075, S3/1086
        dimensiune:  3181 randuri x 9 coloane
        coloane:     Siruta, Localitate, Carne, Peste, LegumeFructe, Uleiuri, Lactate, Morarit, Panificatie
        primul rand: 32768, Budesti, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...

    Industrie.csv
        folosit in:  S3/1085
        dimensiune:  3181 randuri x 11 coloane
        coloane:     Siruta, Localitate, Alimentara, Textila, Lemnului, ChimicaFarmaceutica, Metalurgica,
                     ConstructiiMasini, CalculatoareElectronica, Mobila, Energetica
        primul rand: 32768, Budesti, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ...

    Innoptari.csv
        folosit in:  S3/1077
        dimensiune:  10923 randuri x 3 coloane
        coloane:     Siruta, Ani, Valoare
        primul rand: 1017, Anul 2001, 105792

    Natalitate_Ro.csv
        folosit in:  S1/1086
        dimensiune:  1512 randuri x 5 coloane
        coloane:     Judete, Localitati, Ani, UM: Numar persoane, Valoare
        primul rand: Alba,  TOTAL,  Anul 1990,  Numar persoane, 5762.0
        valori lipsa: {'Valoare': 2}

    PopulatieLocalitati.csv (versiunea 1 din 2)
        folosit in:  S3/1073, S3/1075, S3/1077, S3/1086
        dimensiune:  3181 randuri x 4 coloane
        coloane:     Siruta, Localitate, Judet, Populatie
        primul rand: 1017, Municipiul Alba Iulia, ab, 74283

    PopulatieLocalitati.csv (versiunea 2 din 2)
        folosit in:  S3/1085
        dimensiune:  3181 randuri x 4 coloane
        coloane:     Siruta, Localitate, Judet, Populatie
        primul rand: 1017, Municipiul Alba Iulia, AB, 74283

    Religious.csv
        folosit in:  S2/1075
        dimensiune:  3181 randuri x 23 coloane
        coloane:     Code, City, Orthodox, Roman_Catholic, Reformed, Pentecostal, Greek_Catholic, Baptist,
                     Seventh-day_Adventist, Islam, Unitarian, Jehova_Witnesses, Evangelical, Old_Calendarists,
                     Evangelical_Lutheran, Serbian_Orthodox, Romanian_Evangelical, Evangelical_Augustan, Judaism,
                     Armenian_Apostolic, Other_Religion, Without_religion, Atheists
        primul rand: 1017, Municipiul Alba Iulia, 51659, 1195, 582, 1368, 1226, 961, ...

    Teritorial_2022.csv
        folosit in:  S1/1075, S1/1077, S1/1085
        dimensiune:  42 randuri x 35 coloane
        coloane:     Indicativ, Judet, Regiunea, Macroregiunea, RN, RM, RMI, Emigranti, Imigranti, RS, Sal, CSom,
                     AjSoc, Pensie, PopScolara, PaturiUS, Medici, VolumeB, SpectatoriS, VizitatoriM, SportiviL,
                     PIB, SalariatiC, PAgrVeg, PAgrAnim, ServAgr, Silvicultura, SupLoc, DrumuriM, Innoptari,
                     BugetVenituri, BugetSubventii, Apa, Canal, Export
        primul rand: ab, Alba, c, 1, 7.2, 15.7, 5.9, 136.742, ...
        valori lipsa: {'SpectatoriS': 1, 'SalariatiC': 2, 'Silvicultura': 1}

    prezenta_vot.csv
        folosit in:  S2/1077
        dimensiune:  3181 randuri x 20 coloane
        coloane:     Siruta, Localitate, Mediu, Votanti_LP, Votanti_LS, LP, LS, LSC, UM, LT, Barbati_18-24,
                     Barbati_25-34, Barbati_35-44, Barbati_45-64, Barbati_65_, Femei_18-24, Femei_25-34,
                     Femei_35-44, Femei_45-64, Femei_65_
        primul rand: 1017, Municipiul Alba Iulia, U, 61753, 0, 20290, 1357, 0, ...

Particularitati care conteaza (toate verificate pe fisiere):

  1. Doua versiuni diferite de Coduri_Judete.csv:
        - Seminar 2 (grupele 1073, 1075, 1085, 1086): 4 coloane = NrCrt, IndicativJudet, NumeJudet, Regiune.
          La citirea cu index_col=0 indexul devine NrCrt, de aceea codul din Seminar 2 face merge cu
          right_on="IndicativJudet" (coloana), nu cu right_index=True.
        - Seminar 3 (grupele 1073, 1075, 1077, 1086): 3 coloane = IndicativJudet, NumeJudet, Regiune.
          Cu index_col=0 indexul este chiar IndicativJudet, deci merge-ul se face cu right_index=True.
  2. Doua versiuni de PopulatieLocalitati.csv:
        - Seminar 3 grupele 1073, 1075, 1077, 1086: coloanele Siruta, Localitate, Judet, Populatie,
          cu indicativele de judet cu LITERE MICI (ab, ag, b, if ...), la fel ca in Coduri_Judete.
        - Seminar 3 grupa 1085: aceleasi coloane, dar indicativele sunt cu MAJUSCULE (AB, AG, B, IF ...).
          De aceea in Output4/5/6 din 1085 judetele apar ca AB, AG, TM (la fel ca in exemplul din enunt).
          Grupa 1085 nu foloseste Coduri_Judete, deci nu apare problema majuscule/litere mici.
  3. Natalitate_Ro.csv: valorile text au spatiu in fata (" TOTAL", " Anul 1990", " Numar persoane").
     Dupa pivot, numele coloanelor sunt " Anul 1990", ..., " Anul 2025" (cu spatiu), vizibil in antetul
     fisierelor x_std.csv. Doua valori lipsa: Alba 1991 si Arad 1999.
  4. Teritorial_2022.csv: 42 de judete; indexul este Indicativ (ab, ar, ag, b, ...); coloanele Judet, Regiunea,
     Macroregiunea sunt text/cod, restul (31) sunt indicatori numerici -> list(df)[3:]. Valori lipsa:
     SpectatoriS (1), SalariatiC (2), Silvicultura (1) = 4 valori lipsa in total.
  5. Industrie.csv: 3181 de localitati; 2316 au cifra de afaceri totala > 0; 2317 au total != 0, pentru ca
     localitatea Vladila are total NEGATIV (-34611.0). Filtrul "> 0" da 2316 randuri
     (Output3 din grupa 1085), filtrul "!= 0" da 2317 (cifra din ghid, sectiunea D3).
  6. IndustriaAlimentara.csv: 3181 de localitati; 1372 au cel putin un angajat (Cerinta1 are 1372 randuri).
     Exista mai multe localitati cu acelasi nume (de exemplu trei "Budesti") cu coduri Siruta diferite:
     identifici o localitate dupa Siruta, nu dupa nume.
  7. Innoptari.csv este in format LUNG (Siruta, Ani, Valoare), 10923 randuri; dupa pivot: 1143 localitati x
     16 ani (2001-2016). Lipsesc 7365 de celule (combinatii localitate-an fara raportare);
     in datele brute nu exista nicio valoare 0.
  8. prezenta_vot.csv: LT este intotdeauna egal cu LP+LS+LSC+UM, iar suma celor 10 categorii de varsta/sex
     este intotdeauna egala cu LT (verificat pe toate cele 3181 de randuri). Procentul LT*100/(Votanti_LP+Votanti_LS)
     depaseste 100 la 6 localitati (maxim 147.12, localitatea Ciresu).
  9. Coduri_Localitati.csv (Code, City, County): 3181 de localitati; judetul "b" (Bucuresti) are o singura
     localitate, judetul "if" (Ilfov) 40.
```

# 5. Conventii de stil

```text
Conventiile complete (limba, importuri, prefixe, comentarii, citire cu index_col=0, rotunjire, nume de
coloane, verificare .shape) sunt in Anexa A, sectiunea A. Pe scurt:

    - comentarii si nume fara diacritice; fiecare cerinta incepe cu "# Cerinta N" (sau "# N")
    - import pandas as pd, import numpy as np (la seminar si: from numpy.ma.extras import average)
    - prefixe: df_ pentru DataFrame, s_ pentru Series (df_cerinta5, s_cerinta3)
    - fisiere citite cu index_col=0, lista coloanelor numerice: activitati = list(df.columns.values)[1:]
    - apply(...) cu lambda pentru functii scurte, def pentru cele lungi (calcul_medie)
    - rezultat salvat in data_out/ cu numele cerut de enunt; antetul identic cu exemplul din enunt
    - rotunjire doar daca o cere enuntul si doar la salvare; Series primeste .name inainte de salvare

Conventii observate in codul grupelor, in plus fata de ghid:
    - functii.py la Seminar 1 si 2 (nan_replace, nan_replace_df, standardizare, shannon, disimilaritate, ...);
      Seminar 3 are functiile in main.py (calcul_medie / calcul_medii).
    - tabelare_salvare_matrice(x, linii, coloane, nume_index, nume_fisier) transforma o matrice numpy in
      DataFrame cu indecsi si o salveaza in data_out/ (Seminar 1).
    - groupby(...).apply(func, include_groups=False): coloana de grupare nu mai intra in functie, deci
      ponderea (Populatie) ramane ultima coloana in calcul_medie (x[:, -1]).
    - max pe rand: x.index[x.argmax()] (pozitie) sau df.idxmax(axis=1) (eticheta).
```

# 6. Formule si definitii

```text
Notatii: x = valori, p = pondere, n = numar de observatii/unitati, i = indice de unitate (localitate/judet).

Suma si totaluri
    total pe localitate (rand)      df[activitati].sum(axis=1)          axis=1 = de-a lungul randului
    total pe coloana                df.sum()                            axis=0 (implicit)

Procent pe rand (ponderea unei activitati/etnii in total pe localitate sau judet)
    procent_j = x_j * 100 / sum_k x_k          (daca totalul e 0 rezulta NaN; enuntul poate cere 0 -> fillna(0))

Rata la 1000 de locuitori
    rata = valoare_agregata * 1000 / populatie_agregata
    Mai intai se aduna pe grup (groupby ... sum), apoi se imparte. Nu se face media rapoartelor.

Media ponderata pe grup (pondere = populatia)
    media = sum_i(x_i * pop_i) / sum_i(pop_i)          echivalent cu numpy.average(x, weights=pop)
    Enuntul Tema 2.4 o scrie ca suma x_i * p_i cu ponderi p_i normalizate (p_i = pop_i / suma pop).

Indice de localizare (Tema 2.4 cerinta 6)
    L(i, j) = [ angajati(i, j) / angajati_total(j) ]  /  [ populatie(i) / populatie_totala ]
    i = judet, j = activitate. L > 1 inseamna ca judetul e specializat in activitatea j.
    Exemplu din enunt: (3000/100000) / (200000/20000000) = 3.

Coeficient de variatie pe regiune, pe ani
    CV = std / medie, calculat pe valorile localitatilor din regiune; std este cel de selectie (ddof=1).

Standardizare si centrare (numpy)
    centrare:        x_c = x - medie(x, axis=0)
    standardizare:   x_std = (x - medie) / std(axis=0)
    np.std foloseste implicit ddof=0 (abatere standard a populatiei); np.cov foloseste ddof=1.
    De aceea functiile de standardizare au un parametru (ddof sau nlib), implicit 0.

Covarianta si corelatie
    V = np.cov(x, rowvar=False)        matrice (m x m); rowvar=False = coloanele sunt variabilele
    R = np.corrcoef(x, rowvar=False)

Distante
    euclidiana:   d(a, b) = sqrt( sum_k (a_k - b_k)^2 )
    Mahalanobis:  d(a, b) = sqrt( (a - b)^T V^-1 (a - b) ), V = matricea de covarianta
    Observatie verificata: scipy.spatial.distance.cdist(x, x, "mahalanobis") fara parametrul VI estimeaza
    V din np.vstack([x, x]) (datele duplicate), nu din x. Distantele livrate la grupa 1077 sunt de
    1.006079 = sqrt((2n-1)/(2(n-1))) ori mai mari decat cele cu VI = inv(np.cov(x, rowvar=False)), n = 42.

Inertie
    inertia generala         I = sum_i d^2(x_i, g)                    g = centrul de greutate (media pe coloane)
    inertia fata de centrul g_k al grupei k, calculata pe TOATE observatiile:  I_k = sum_i d^2(x_i, g_k)
    (asa face calcul_inertii din grupa 1077; inertia intra-grupa ar aduna doar observatiile grupei k)

Indice de disimilaritate (segregare), pe judet, pentru fiecare grup etnic
    D = 1/2 * sum_i | x_i / Tx - r_i / Tr |
    i = localitate din judet, x_i = populatia grupului in localitate, r_i = restul populatiei localitatii,
    Tx = totalul grupului in judet, Tr = totalul restului populatiei din judet. D este in [0, 1].

Shannon-Weaver
    H = - sum_i p_i * log2(p_i)          (baza 2 conform enuntului)
    Segregare (Tema 2.1 si 2.3): p_i = ponderea localitatii i in totalul grupului, calculat pe coloana.
    Diversitate (Tema 2.2): p_i = ponderea confesiunii i in unitate; n = numarul de confesiuni.
    ATENTIE: scipy.stats.entropy(p) foloseste logaritm NATURAL (nats) daca nu primeste base=2.
    Conversie: H_bits = H_nats / ln(2). Toate solutiile din seminar (grupele 1075, 1077, 1085) folosesc
    entropy fara base, deci valorile lor sunt in nats; completarile din completari/ sunt in biti
    si au fost verificate: H_nats / ln(2) == H_bits.

Simpson si Simpson invers (Tema 2.2)
    S1 = 1 - sum_i p_i^2            in [0, 1)
    S2 = 1 / sum_i p_i^2            >= 1 (numarul efectiv de confesiuni)

Teste de concordanta cu repartitia normala (Seminar 1, grupa 1085)
    Kolmogorov-Smirnov: scipy.stats.kstest(x, norm.cdf, args=(medie, std))
    Shapiro-Wilk:       scipy.stats.shapiro(x)
    Anderson-Darling:   scipy.stats.anderson(x, dist="norm", method="interpolate")  (p-value interpolat)
    Chi2 (implementat): clase prin histograma cu regula Sturges; frecvente asteptate fe = n * (F(sup) - F(inf))
                        cu F = functia de repartitie normala (medie, std); statistica = sum (f - fe)^2 / fe.
    Decizie: pentru KS, Shapiro, Anderson se compara p-value cu pragul 0.05 (True = nu se respinge normalitatea).
```

# 7. Seminar 1 - statistica pe matrici (numpy, scipy)

```text
Tiparul comun al celor 4 grupe:
    1. citesti tabelul, iei coloanele numerice:           x = df[variabile].values
    2. inlocuiesti valorile lipsa cu media coloanei:       x = nan_replace(x)
    3. calculezi ceva pe matricea numpy x (n x m) si salvezi cu tabelare_salvare_matrice / to_csv

nan_replace (identica in toate grupele):
    x = x.copy()                                  # nu modifica originalul
    k = np.where(np.isnan(x))                     # (linii, coloane) unde lipsesc valori
    x[k] = np.nanmean(x[:, k[1]], axis=0)         # in fiecare loc lipsa pune media coloanei respective
Atentie: np.nanmean(x[:, k[1]], axis=0) construieste o matrice cu coloanele din k[1] (cu repetari) si
ia media pe coloana, deci la pozitia (i, j) lipsa se pune exact media coloanei j.
```

## 7.1 Grupa 1075 - Tema 1.1: standardizare, corelatii, covariante totale si pe grupe

```text
Folder: seminar1/grupa_1075      Date: Teritorial_2022.csv      Enunt: Tema1_1.pdf

Enunt:
    In fisierul Teritorial_2022.csv sunt date privind indicatori statistici din diverse domenii si
    subdomenii economico-sociale. Sa se implementeze urmatoarele cerinte:
    - Inlocuirea valorilor lipsa cu media
    - Standardizarea si centrarea datelor
    - Calculul matricelor de corelatie si covarianta totale si pe grupe (daca exista criteriu de grupare)

Functii (functii.py):
    nan_replace(x)                                      inlocuire valori lipsa cu media coloanei
    standardizare(x, scal=True, nlib=0)                 centrare (scal=False) sau standardizare; nlib = ddof pentru np.std
    tabelare_salvare_matrice(x, index_linie, index_coloana, nume_index, nume_fisier=None)
                                                        DataFrame din matrice, salvat in data_out/ daca primeste nume
    calcul_corelatii_covariante(x, y)                   pentru fiecare clasa din y (valori unice): corcoef si cov pe
                                                        subtabelul x[y == clasa]; intoarce (r, v, clase), r si v au
                                                        forma (numar_clase, m, m)

Solutia (main.py):
    variabile = list(df)[3:]        cele 31 de coloane numerice (dupa Judet, Regiunea, Macroregiunea)
    x_std = standardizare(x)        -> x_std.csv   (42 x 31, cu index Indicativ)
    x_c = standardizare(x, scal=False) -> x_c.csv  (date doar centrate)
    V = np.cov(x, rowvar=False)     -> V.csv       (31 x 31)
    R = np.corrcoef(x, rowvar=False)-> R.csv       (31 x 31)
    pe grupe: calcul_corelatii_covariante(x, df["Regiunea"].values) cu grupele = codurile regiunilor
    (b, c, ne, nv, s, se, sv, v) -> pentru fiecare grupa R_<cod>.csv si V_<cod>.csv.
    Total: 4 fisiere + 16 fisiere pe grupe = 20 de fisiere in data_out/.
Rezultate:
    R.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.0,-0.5260947836217956,0.05207980262477511,0.002461226258092715,0.17537604479627375,... (+26)
    R_b.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.0,-1.0,1.0,-1.0,-1.0,... (+26)
    R_c.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.0,-0.3419450665389077,0.3882284515027672,-0.24616127999676823,-0.004235446637288167,... (+26)
    R_ne.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.0,-0.7408613022462871,-0.050291934590716215,0.0681483690384389,0.12296983034008621,... (+26)
    R_nv.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.0,0.46818421818730094,0.31163365993709286,-0.5305114184480066,-0.07458334281976918,... (+26)
    R_s.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,0.9999999999999999,-0.48388050779963787,0.8218306623097262,-0.7010465214592588,-0.08351102608055637...
    R_se.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.0,-0.29721630009430355,-0.04544793164137568,-0.2577163143853277,-0.04456479791239395,... (+26)
    R_sv.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.0,0.6165433234595302,0.9149449463499939,0.4474059793331585,0.4847146922054032,... (+26)
    R_v.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.0,-0.8147118868135433,-0.1984783377293041,-0.2719613892052282,0.8347535524932906,... (+26)
    V.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.2180255516840883,-1.3288037166085946,0.10578397212543549,0.2212465737514554,72.69757595818818,......
    V_b.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.125,-1.3500000000000005,0.5250000000000001,-150.279,-457.458,... (+26)
    V_c.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,0.49466666666666664,-0.27533333333333315,0.1620000000000001,-13.52141999999999,-0.11139333333333608...
    V_ne.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.7176666666666662,-1.7169999999999999,-0.13500000000000056,9.502646666666704,102.63741000000005,.....
    V_nv.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,0.6506666666666667,0.30533333333333346,0.4486666666666668,-11.941813333333327,-1.1064933333333333,....
    V_s.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,0.657666666666667,-0.8863333333333332,0.7183333333333333,-12.62117666666667,-0.5746833333333304,......
    V_se.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,0.4114285714285715,-0.37547619047618985,-0.06333333333333298,-11.092645238095246,-11.36458095238098...
    V_sv.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,0.24800000000000008,0.8860000000000009,0.7960000000000002,2.424255000000002,2.283775,... (+26)
    V_v.csv: 31 randuri x 32 coloane
        antet:       Indicatori,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: RN,1.5266666666666675,-1.8999999999999997,-0.3833333333333334,-11.887333333333334,23.268466666666672,....
    x_c.csv: 42 randuri x 32 coloane
        antet:       Indicativ,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: ab,-0.7952380952380977,0.054761904761905456,-0.0357142857142847,-23.608047619047596,-140.3595714285714...
    x_std.csv: 42 randuri x 32 coloane
        antet:       Indicativ,RN,RM,RMI,Emigranti,Imigranti,... (+26)
        primul rand: ab,-0.7292924100319669,0.024218242497613528,-0.019640491157317207,-0.29335667513410735,-0.378227664689...
Observatii:
    - Regiunea "b" (Bucuresti-Ilfov) are doar 2 judete in tabel (b si if), deci matricile ei se calculeaza pe
      2 observatii: corelatiile sunt +1/-1 (nu apar NaN).
    - Verificarea cu scikit-learn este lasata in comentariu (StandardScaler foloseste ddof=0, ca nlib=0).
```

## 7.2 Grupa 1077 - Tema 1.3: distante, inertii, centri de grupa

```text
Folder: seminar1/grupa_1077      Date: Teritorial_2022.csv      Enunt: Tema1_3.pdf

Enunt:
    In fisierul Teritorial_2022.csv sunt date privind indicatori statistici din diverse domenii si
    subdomenii economico-sociale. Sa se implementeze urmatoarele cerinte:
    - Inlocuirea valorilor lipsa cu media
    - Sa se calculeze si sa se salveze matricile de distanta in metrica euclidiana si mahalanobis
    - Sa se calculeze si sa se salveze inertia datelor in raport cu centrul de greutate general si cu centrii
    de greutate ai grupelor, folosind metrica euclidiana
    - Sa se calculeze si sa se salveze centrii de grupe
    - Sa se calculeze si sa se salveze distantele dintre centrii de grupa folosind metrica euclidiana

Functii (functii.py):
    nan_replace(x)
    tabelare_salvare_matrice(x, nume_linii, nume_coloane, nume_index, nume_fisier_output=None)
                                  ca la 1075, dar intoarce si DataFrame-ul
    calcul_inertii(x, y)          intoarce (inertia generala, dictionar {grupa: (inertie, centru)}, matricea
                                  distantelor dintre centrii de grupa)

Solutia (main.py):
    d_euclid = distance.cdist(x, x, metric="euclidean")          -> D_Euclid.csv        (42 x 42)
    d_mahalanobis = distance.cdist(x, x, metric="mahalanobis")   -> D_Mahalanobis.csv   (42 x 42)
    calcul_inertii(x, df["Regiunea"].values):
        centru = media pe coloane;  inertia = suma patratelor distantelor euclidiene fata de centru
        pentru fiecare grupa k: centrul grupei (media observatiilor grupei) si inertia fata de acel centru
        distante_centrii = cdist(centrii, centrii) -> DistanteRegiuni.csv (8 x 8, indexat dupa codul regiunii)
Rezultate:
    D_Euclid.csv: 42 randuri x 43 coloane
        antet:       Indicativ,ab,ar,ag,bc,bh,... (+37)
        primul rand: ab,0.0,3399.5575366526805,5441.94663740219,19385.693027690275,10466.785755893776,... (+37)
    D_Mahalanobis.csv: 42 randuri x 43 coloane
        antet:       Indicativ,ab,ar,ag,bc,bh,... (+37)
        primul rand: ab,0.0,7.531699811438134,7.943472009179095,7.529812084871717,7.750757982661261,... (+37)
    DistanteRegiuni.csv: 8 randuri x 9 coloane
        antet:       Regiuni,b,c,ne,nv,s,... (+3)
        primul rand: b,0.0,52742.11087088815,69771.92843715799,55400.45587932606,63098.530695673406,... (+3)
Valori afisate la rulare (nu sunt salvate in fisier): Inertia generala = 15936189794.361073;
pentru fiecare regiune se afiseaza inertia si centrul de grupa (31 de valori).
Observatii:
    - Enuntul cere SALVAREA inertiei si a centrilor de grupa; codul le afiseaza doar in consola
      (se salveaza numai matricile de distante si distantele dintre centri).
    - inertia pe grupa se calculeaza pe toate observatiile fata de centrul grupei (vezi sectiunea 6).
    - Mahalanobis: vezi nota din sectiunea 6 despre VI estimat din x duplicat (factor 1.006079).
```

## 7.3 Grupa 1085 - Tema 1.2: teste de concordanta cu repartitia normala

```text
Folder: seminar1/grupa_1085      Date: Teritorial_2022.csv      Enunt: Tema1_2.pdf

Enunt:
    In fisierul Teritorial_2022.csv sunt date privind indicatori statistici din diverse domenii si
    subdomenii economico-sociale. Sa se implementeze urmatoarele cerinte:
    - Inlocuirea valorilor lipsa cu media
    - Aplicarea testelor de concordanta pentru verificarea distributiei normal-gaussiene. Vor fi folosite
    testele Shapiro, Kolmogorov-Smirnov, Anderson si se va implementa testul Chi2.

Functii (functii.py):
    nan_replace(x)
    teste(x, prag=0.05)       pentru fiecare coloana: KS, Shapiro, Anderson, Chi2 -> matrice booleana (m x 4);
                              afiseaza statistica si p-value pentru fiecare test
    test_chi2(x)              testul Chi2 implementat de mana (vezi sectiunea 6); intoarce p-value-ul

Solutia (main.py): x = nan_replace(...); t = teste(x); DataFrame(t, variabile,
["Kolmogorov-Smirnov","Shapiro","Anderson","Chi2"]) -> Teste.csv (31 x 4 valori True/False).
Rezultate:
    Teste.csv: 31 randuri x 5 coloane
        antet:       ,Kolmogorov-Smirnov,Shapiro,Anderson,Chi2
        primul rand: RN,True,True,True,False
Rezumat al rezultatelor (numar de variabile din 31 pentru care e True): Kolmogorov-Smirnov 23,
Shapiro 12, Anderson 12, Chi2 1.
Observatii:
    - La Chi2 codul foloseste pvalue = chi2.cdf(statistica, m-1) si decide cu "pvalue < prag". Functia de
      repartitie (cdf) nu este p-value-ul standard, care este 1 - cdf (chi2.sf). Aceasta este o explicatie
      probabila pentru faptul ca Chi2 este True doar la 1 variabila din 31, cat timp celelalte teste sunt mult
      mai permisive. Gradele de libertate folosite sunt m-1 (nu se scad parametrii estimati, medie si std).
    - Anderson cu method="interpolate" intoarce un p-value limitat la intervalul [0.01, 0.15] (verificat:
      minimul este 0.01, iar 12 variabile din 31 au exact 0.15, plafonul). Cele 12 variabile cu 0.15 sunt
      exact cele pentru care Anderson este True.
    - Procedeul si fisierul Teste.csv sunt reproduse exact de codul din repo.
```

## 7.4 Grupa 1086 - natalitate (fara PDF)

```text
Folder: seminar1/grupa_1086      Date: Natalitate_Ro.csv (format lung)

Cerinte implementate (identice cu sectiunea E1 din ghid): pivot, inlocuire NaN, covarianta, corelatie,
standardizare.

Functii (functii.py):
    nan_replace(x)
    standardize(x, scal=True, ddof=0)       centrare/standardizare; ddof ales de utilizator

Solutia (main.py):
    t = pd.read_csv("data_in/Natalitate_Ro.csv")                       1512 randuri = 42 judete x 36 ani
    df = t.pivot_table(index="Judete", columns="Ani", values="Valoare")  42 x 36 (ani 1990-2025)
    x = nan_replace(df[variabile].values)                                 2 valori lipsa -> media coloanei
    V = np.cov(x, rowvar=False) -> V.csv      (36 x 36)
    R = np.corrcoef(x, rowvar=False) -> R.csv (36 x 36)
    x_std = standardize(x) -> x_std.csv       (42 x 36)
Rezultate:
    R.csv: 36 randuri x 37 coloane
        antet:       , Anul 1990, Anul 1991, Anul 1992, Anul 1993, Anul 1994,... (+31)
        primul rand:  Anul 1990,1.0,0.9917574239108856,0.9885046650835598,0.9878217250370788,0.987077380628865,... (+31)
    V.csv: 36 randuri x 37 coloane
        antet:       , Anul 1990, Anul 1991, Anul 1992, Anul 1993, Anul 1994,... (+31)
        primul rand:  Anul 1990,10849974.729384439,9272427.508030932,8521103.918699186,8168957.475029037,8120530.593495931,...
    x_std.csv: 42 randuri x 37 coloane
        antet:       Judete, Anul 1990, Anul 1991, Anul 1992, Anul 1993, Anul 1994,... (+31)
        primul rand: Alba,-0.5321747939372895,-3.243091986049646e-16,-0.5398380684276529,-0.6084386262152488,-0.59394890247...
Observatii: antetele anilor au spatiu in fata (" Anul 1990") pentru ca asa sunt valorile din fisierul sursa.
```

# 8. Seminar 2 - etnii, confesiuni, prezenta la vot

```text
Tiparul comun (populatie pe categorii la nivel de localitate -> judet -> regiune):
    1. nan_replace_df(df)                  inlocuire valori lipsa: media pentru coloane numerice, valoarea cea mai
                                           frecventa (mode) pentru coloane text; modifica DataFrame-ul pe loc
    2. df_loc = df.merge(Coduri_Localitati, left_index=True, right_index=True)     adauga coloana County
    3. df_jud = df_loc[categorii + ["County"]].groupby(by="County").sum()           populatie pe judet
    4. df_jud.merge(Coduri_Judete, left_index=True, right_on="IndicativJudet")      adauga Regiune
       df_reg = ...[categorii + ["Regiune"]].groupby(by="Regiune").sum()            populatie pe regiune
    5. procente pe rand:  df[categorii].apply(lambda x: x * 100 / x.sum(), axis=1)
    6. un indice calculat per judet:  df_loc[categorii + ["County"]].groupby("County").apply(functie, include_groups=False)

Coduri_Localitati.csv are coloanele Code (index), City, County (indicativ judet cu litere mici); Coduri_Judete.csv
are NrCrt, IndicativJudet, NumeJudet, Regiune; Coduri_Regiuni.csv are Regiune, MacroRegiune (4 macroregiuni).

Functii folosite in aceste grupe (functii.py):
    nan_replace_df(df)     in toate grupele, cu exceptia 1077
    disimilaritate(df)     grupele 1073, 1086: indice de disimilaritate D pe coloane (formula in sectiunea 6)
    shannon(df)            grupele 1075, 1077, 1085: p = x / total pe coloana; entropy(p, axis=0) (logaritm natural)
Detaliile functiei disimilaritate: x = matricea localitati x grupuri; tx = totalul pe grup (tx==0 -> 1);
sx = totalul pe localitate; r = (sx - x.T).T = restul populatiei din localitate; tr = totalul pe coloana al lui r;
d = 0.5 * sum(|x/tx - r/tr|, axis=0) -> Series cu un D pe grup.
```

## 8.1 Grupa 1073 - Tema 2.1 (etnii)

```text
Folder: seminar2/grupa_1073      Date: Ethnicity.csv, Coduri_Localitati, Coduri_Judete, Coduri_Regiuni
Enunt: Tema2_1.pdf

Enunt:
    Tema 2.1

    In fisierul Etnicity.csv se afla date privind populatia pe etnii la nivelul localitatilor conform
    Recensamantului Populatiei si Locuintelor din 2011. In fisierele Coduri_Localitati.csv,
    Coduri_Judete.csv si Coduri_Regiuni.csv sunt codificarile localitatilor, judetelor, regiunilor si
    macroregiunilor Romaniei.
    1. Sa se calculeze si sa se salveze populatia pe etnii la nivelul judetelor, regiunilor si
    macroregiunilor
    2. Sa se calculeze si sa se salveze procentele pe etnii la nivelul localitatilor, judetelor, regiunilor si
    macroregiunilor
    3. Sa se calculeze si sa se salveze indicii de segregare etnica la nivelul judetelor. Vor fi utilizati
    urmatorii indici:
    Indicele de disimilaritate:  D = 1/2 * SUM(i=1..n) | x_i/Tx - r_i/Tr |
    Shannon-Weaver:  H = - SUM(i=1..n) p_i * log2(p_i)
    unde i este unitatea administrativ-teritoriala (UAT), n este numarul de unitati administrativ-
    teritoriale, xi este populatia de o anumita etnie, ri este restul populatiei, Tx este totalul populatiei de
    etnia respectiva, Tr este totalul restului populatiei, pi este ponderea etniei la nivelul unitatii
    administrativ-teritoriale i fata de totalul etniei.

Nota: enuntul scrie "Etnicity.csv"; fisierul real este Ethnicity.csv.

Solutia (main.py): populatia pe etnii la nivel de judet (Ethnicity_Jud.csv) si regiune (Ethnicity_Reg.csv) si procentele
pe localitate (Ethnicity_P.csv, cu coloana Localitate). In cod, linia "# De calculat la nivel de judet si regiune"
marcheaza partea ramasa ca tema.
Rezultate:
    Ethnicity_Jud.csv: 42 randuri x 23 coloane
        antet:       County,Romanian,Hungarians,Romany,Ukrainians,Germans,... (+17)
        primul rand: ab,291850,14831,14287,10,711,... (+17)
    Ethnicity_P.csv: 3181 randuri x 24 coloane
        antet:       Code,Localitate,Romanian,Hungarians,Romany,Ukrainians,... (+18)
        primul rand: 1017,Municipiul Alba Iulia,95.91667958856671,1.7401492048724179,1.927947485398253,0.006891680019296704...
    Ethnicity_Reg.csv: 8 randuri x 24 coloane
        antet:       Regiune,Romanian,Hungarians,Romany,Ukrainians,Germans,... (+18)
        primul rand: Bucuresti-Ilfov,1960778,3592,39607,307,1301,... (+18)
Observatii:
    - Ethnicity_Reg.csv are o coloana in plus, IndicativJudet, cu indicativele judetelor concatenate (de exemplu "bif"
      pentru Bucuresti-Ilfov): merge-ul pastreaza coloana text si groupby(...).sum() o concateneaza. Corect este sa
      selectezi doar etnii + ["Regiune"] dupa merge (asa fac grupele 1075, 1085, 1086).
    - Nu sunt implementate: macroregiuni, procente pe judet/regiune/macroregiune, indicii de segregare (cerinta 3).
      Toate sunt rezolvate in completari/seminar2_diversitate_segregare.py.
```

## 8.2 Grupa 1085 - Tema 2.1 (etnii)

```text
Folder: seminar2/grupa_1085      Date: ca la 1073      Enunt: Tema2_1.pdf (aceeasi tema)

Solutia (main.py): Ethnicity_Jud.csv, Ethnicity_Reg.csv (curat, 22 de etnii + Regiune), Ethnicity_P.csv (procente pe localitate),
Ethnicity_P_Jud.csv (procente pe judet), Ethnicity_Shannon.csv (Shannon pe judet, per etnie, cu fillna(0)).
Comentariile din cod lasa ca tema: macroregiunea, procentele pe regiune/macroregiune, indicii pe regiune/macroregiune.
Rezultate:
    Ethnicity_Jud.csv: 42 randuri x 23 coloane
        antet:       County,Romanian,Hungarians,Romany,Ukrainians,Germans,... (+17)
        primul rand: ab,291850,14831,14287,10,711,... (+17)
    Ethnicity_P.csv: 3181 randuri x 24 coloane
        antet:       Code,Localitate,Romanian,Hungarians,Romany,Ukrainians,... (+18)
        primul rand: 1017,Municipiul Alba Iulia,95.91667958856671,1.7401492048724179,1.927947485398253,0.006891680019296704...
    Ethnicity_P_Jud.csv: 42 randuri x 23 coloane
        antet:       County,Romanian,Hungarians,Romany,Ukrainians,Germans,... (+17)
        primul rand: ab,90.67916942417096,4.608061544388828,4.439038182501732,0.0031070470935127964,0.22091104834875983,......
    Ethnicity_Reg.csv: 8 randuri x 23 coloane
        antet:       Regiune,Romanian,Hungarians,Romany,Ukrainians,Germans,... (+17)
        primul rand: Bucuresti-Ilfov,1960778,3592,39607,307,1301,... (+17)
    Ethnicity_Shannon.csv: 42 randuri x 23 coloane
        antet:       County,Romanian,Hungarians,Romany,Ukrainians,Germans,... (+17)
        primul rand: ab,3.582844763739844,2.748810061549076,3.2500217022899824,1.0888999753452238,2.2442277671272226,... (+17)
Observatii:
    - shannon din functii.py foloseste scipy entropy fara base=2 -> valori in nats, enuntul cere log2.
      (H_nats / ln 2 coincide cu valorile din completari, verificat.)
    - Lipseste indicele de disimilaritate (cerinta 3 prima formula).
```

## 8.3 Grupa 1086 - Tema 2.1 (etnii)

```text
Folder: seminar2/grupa_1086      Date: ca la 1073      Enunt: Tema2_1.pdf (aceeasi tema)

Solutia (main.py): Etnii_jud.csv, Etnii_reg.csv, Etnii_p.csv (procente pe localitate, FARA coloana Localitate),
Etnii_jud_p.csv (procente pe judet). Indicele de disimilaritate se calculeaza si se AFISEAZA (print), nu se salveaza.
Rezultate:
    Etnii_jud.csv: 42 randuri x 23 coloane
        antet:       County,Romanian,Hungarians,Romany,Ukrainians,Germans,... (+17)
        primul rand: ab,291850,14831,14287,10,711,... (+17)
    Etnii_jud_p.csv: 42 randuri x 23 coloane
        antet:       County,Romanian,Hungarians,Romany,Ukrainians,Germans,... (+17)
        primul rand: ab,90.67916942417096,4.608061544388828,4.439038182501732,0.0031070470935127964,0.22091104834875983,......
    Etnii_p.csv: 3181 randuri x 23 coloane
        antet:       Code,Romanian,Hungarians,Romany,Ukrainians,Germans,... (+17)
        primul rand: 1017,95.91667958856671,1.7401492048724179,1.927947485398253,0.006891680019296704,0.19813580055478025,....
    Etnii_reg.csv: 8 randuri x 23 coloane
        antet:       Regiune,Romanian,Hungarians,Romany,Ukrainians,Germans,... (+17)
        primul rand: Bucuresti-Ilfov,1960778,3592,39607,307,1301,... (+17)
Observatii:
    - Valorile D sunt in [0, 1]; pentru judetul "b" (o singura localitate) toate valorile D sunt 0.
    - Lipsesc salvarea disimilaritatii, macroregiunea, procentele pe regiune/macroregiune si Shannon-Weaver.
```

## 8.4 Grupa 1075 - Tema 2.2 (confesiuni)

```text
Folder: seminar2/grupa_1075      Date: Religious.csv, Coduri_Localitati, Coduri_Judete, Coduri_Regiuni
Enunt: Tema2_2.pdf

Enunt:
    In fisierul Religious.csv se afla date privind populatia pe confesiuni la nivelul localitatilor conform
    Recensamantului Populatiei si Locuintelor din 2011. In fisierele Coduri_Localitati.csv,
    Coduri_Judete.csv si Coduri_Regiuni.csv sunt codificarile localitatilor, judetelor, regiunilor si
    macroregiunilor Romaniei.

    1. Sa se calculeze populatia pe confesiuni la nivelul judetelor, regiunilor si macroregiunilor
    2. Sa se calculeze si sa se salveze ponderile pe confesiuni la nivelul localitatilor, judetelor,
    regiunilor si macroregiunilor
    3. Sa se calculeze si sa se salveze indicii de diversitate confesionala la nivel de judet si regiune.
    Vor fi folosite urmatoarele relatii de calcul pentru diversitate:
    Shannon-Weaver:  H = - SUM(i=1..n) p_i * log2(p_i)
    Simpson:  S1 = 1 - SUM(i=1..n) p_i^2
    Inverse Simpson:  S2 = 1 / SUM(i=1..n) p_i^2
    unde n este numarul de confesiuni, pi este ponderea confesiunii i la nivelul unitatii administrativ-
    teritoriale fata de totalul etniei.

Solutia (main.py): Confesiuni_jud.csv, Confesiuni_reg.csv, Confesiuni_p.csv (procente pe localitate, cu Localitate),
Confesiuni_jud_p.csv, Shannon.csv. Comentariu in cod: "# Tema: calcul pe macroregiuni".
Rezultate:
    Confesiuni_jud.csv: 42 randuri x 22 coloane
        antet:       County,Orthodox,Roman_Catholic,Reformed,Pentecostal,Greek_Catholic,... (+16)
        primul rand: ab,281888,3345,11057,6411,9282,... (+16)
    Confesiuni_jud_p.csv: 42 randuri x 22 coloane
        antet:       County,Orthodox,Roman_Catholic,Reformed,Pentecostal,Greek_Catholic,... (+16)
        primul rand: ab,87.73385538081351,1.0410863401380024,3.441342799075005,1.9953376761209964,2.8888978801676943,... (+16)
    Confesiuni_p.csv: 3181 randuri x 23 coloane
        antet:       Code,Localitate,Orthodox,Roman_Catholic,Reformed,Pentecostal,... (+17)
        primul rand: 1017,Municipiul Alba Iulia,89.19642240486222,2.063333103114856,1.0049036535672353,2.3620415774570067,....
    Confesiuni_reg.csv: 8 randuri x 22 coloane
        antet:       Regiune,Orthodox,Roman_Catholic,Reformed,Pentecostal,Greek_Catholic,... (+16)
        primul rand: Bucuresti-Ilfov,1934155,28768,1370,6463,4220,... (+16)
    Shannon.csv: 42 randuri x 22 coloane
        antet:       County,Orthodox,Roman_Catholic,Reformed,Pentecostal,Greek_Catholic,... (+16)
        primul rand: ab,3.6131566845023264,2.2903917001164507,2.664672103521116,3.126219606861913,2.6412605399935773,... (+16)
Observatii:
    - Shannon.csv contine 75 de valori NaN: la perechile judet x confesiune cu total 0 (functia pune tx=1 dar
      entropy normalizeaza vectorul de zerouri). Grupa 1085 repara asta cu fillna(0).
    - Valorile sunt in nats (entropy fara base=2).
    - Enuntul 2.2 defineste indicii de diversitate cu n = numarul de confesiuni, deci o valoare per judet (si per
      regiune). Codul calculeaza Shannon pe judet x confesiune (distributia unei confesiuni intre localitati),
      adica formula de segregare din Tema 2.1. Diversitatea conform textului enuntului (Shannon in biti, Simpson,
      Simpson invers pe judet si regiune) este in completari/seminar2_diversitate_segregare.py.
    - Lipsesc macroregiunile, ponderile pe regiune/macroregiune, Simpson, Simpson invers si indicii pe regiune.
```

## 8.5 Grupa 1077 - Tema 2.3 (prezenta la vot)

```text
Folder: seminar2/grupa_1077      Date: prezenta_vot.csv, Coduri_Localitati.csv      Enunt: Tema2_3.pdf

Enunt:
    In fisierul prezenta_vot.csv sunt prezentate date privind prezenta la vot la nivelul localitatilor la
    alegerile parlamentare din 2020. Campurile sunt urmatoarele:
    Siruta - Cod siruta, Localitate - Nume localitate, Mediu - Mediul urban sau rural, Nr_sectie -
    Numar sectie, Votanti_LP - Numar votanti inscrisi lista permanenta, Votanti_LS - Votanti inscrisi
    pe lista suplimentara, LP - Voturi pe lista permanenta, LS - Voturi pe lista suplimentara, LSC -
    Voturi prin corespondenta, UM - Voturi cu urna mobila, LT - Total voturi,
    Barbati_18-24, Barbati_25-34, ..., Femei_65_ - Voturi pe categorii de varsta si sexe.
    In fisierul Coduri_Localiatati.csv sunt codurile Siruta ale localitatilor si indicativul de judet.
    Sa se scrie o aplicatie care sa efectueze urmatoarele operatiuni:
    1. Salvarea in fisierul Prezenta50.csv a localitatilor in care prezenta la vot a fost mai mare decat
    50%. Va fi salvat codul, numele si procentul prezentei la vot.
    2. Salvarea in fisierul PrezentaSort.csv a localitatilor sortate descrescator dupa procentul de
    participare la vot.
    3. Determinarea si salvarea in fisierul Varsta.csv pentru fiecare localitate a categoriei de varsta cu
    cea mai mare prezenta la vot.
    4. Sa se salveze in fisierul categorie_varsta.csv, localitatile in care categorie_varsta a avut cea
    mai mare prezenta la vot.
    5. Salvarea in fisierul Judete.csv a prezentei la vot la nivelul judetelor.
    6. Sa se calculeze si sa se salveze indicele de disparitate a votului pentru fiecare categorie de votanti
    la nivelul judetelor. Va fi utilizat indicele Shannon-Weaver, H = - SUM(i=1..n) p_i * log2(p_i), unde n este
    numarul de unitati administrativ-teritoriale, pi este ponderea categoriei de votanti la nivelul unitatii
    administrativ-teritoriale i fata de totalul categoriei.

    Indicatie
    Relatia de calcul pentru procentul participarii la vot este: LT*100/(Votanti_LP+ Votanti_LS)

Functii (functii.py): shannon(df) = p = x / total pe coloana, entropy(p, axis=0) (fara protectie la total 0, fara base=2).

Solutia (main.py): variabile_vot = list(coloane)[2:] (de la Votanti_LP incolo); categorii_varsta = din "Barbati_18-24" incolo (10 coloane).
    Cerinta 1  prezenta % = LT*100/(Votanti_LP+Votanti_LS); filtru > 50      -> Prezenta50.csv (Siruta, Localitate, Procent)
    Cerinta 2  aceeasi tabela sortata descrescator                         -> PrezentaSort.csv
    Cerinta 3  categoria de varsta cu prezenta maxima pe localitate         -> Varsta.csv (x.index[x.argmax()])
    Cerinta 4  localitatile unde categoria dominanta este "Barbati_35-44"   -> Barbati_35-44.csv
    Cerinta 5  suma tuturor variabilelor de vot pe judet                    -> Prezenta_Judet.csv
    Cerinta 6  Shannon pe judet pentru fiecare categorie de varsta          -> Disparitate.csv
Rezultate:
    Barbati_35-44.csv: 7 randuri x 3 coloane
        antet:       Siruta,Localitate,Categorie
        primul rand: 57706,Floresti,Barbati_35-44
    Disparitate.csv: 42 randuri x 11 coloane
        antet:       County,Barbati_18-24,Barbati_25-34,Barbati_35-44,Barbati_45-64,Barbati_65_,... (+5)
        primul rand: ab,3.76193406174579,3.646789239324488,3.502341114302794,3.65663294324748,3.623899372381438,... (+5)
    Femei_65_.csv: 73 randuri x 3 coloane
        antet:       Siruta,Localitate,Categorie
        primul rand: 6164,Ohaba,Femei_65_
    Prezenta50.csv: 359 randuri x 3 coloane
        antet:       Siruta,Localitate,Procent
        primul rand: 1071,Ciugud,53.765060240963855
    PrezentaSort.csv: 3181 randuri x 3 coloane
        antet:       Siruta,Localitate,Procent
        primul rand: 111220,Ciresu,147.12041884816753
    Prezenta_Judet.csv: 42 randuri x 18 coloane
        antet:       County,Votanti_LP,Votanti_LS,LP,LS,LSC,... (+12)
        primul rand: ab,308520,0,97670,8514,0,... (+12)
    Varsta.csv: 3181 randuri x 3 coloane
        antet:       Siruta,Localitate,Categorie
        primul rand: 1017,Municipiul Alba Iulia,Femei_45-64
Distributia categoriei dominante (Varsta.csv): Barbati_45-64 2798, Femei_45-64 283, Femei_65_ 73, Barbati_65_ 19,
Barbati_35-44 7, Barbati_25-34 1 (total 3181).
Observatii:
    - Cerinta 4: categoria este fixata in cod ("Barbati_35-44") si fisierul se numeste dupa categorie; enuntul
      vorbeste de categorie_varsta.csv. Fisierul Femei_65_.csv din arhiva este ramas dintr-o rulare anterioara cu
      alta categorie (nu mai e regenerat de main.py).
    - Cerinta 5: enuntul cere fisierul Judete.csv cu PREZENTA la nivel de judet; codul salveaza Prezenta_Judet.csv cu
      sumele variabilelor (42 x 17), nu procentul. Procentul pe judet = LT*100/(Votanti_LP+Votanti_LS) pe sume.
    - Cerinta 6: valori in nats (entropy fara base=2). Nu apar NaN in Disparitate.csv.
    - Procentul depaseste 100 la 6 localitati (maxim 147.12), vezi sectiunea 4. PrezentaSort.csv are valori egale
      (egalitati) a caror ordine poate diferi intre rulari; continutul este acelasi.
```

# 9. Seminar 3 - industrie si innoptari

```text
Tiparul comun: citesti tabelul pe localitati (index_col=0), faci merge cu PopulatieLocalitati.csv dupa Siruta,
apoi alegi nivelul (localitate / judet / regiune) conform sectiunii 3. Functia pentru media ponderata este definita
in main.py (nu exista functii.py la Seminar 3):

    def calcul_medie(df):                 # numit calcul_medii in grupa 1073
        x = df.values
        medii = average(x[:, :-1], axis=0, weights=x[:, -1])      # pondere = ULTIMA coloana (Populatie)
        return pd.Series(medii, df.columns[:-1])
```

## 9.1 Tema 2.4 - industria alimentara (grupele 1073, 1075, 1086)

```text
Folderele: seminar3/grupa_1073, seminar3/grupa_1075, seminar3/grupa_1086
Date: IndustriaAlimentara.csv, PopulatieLocalitati.csv, Coduri_Judete.csv (versiunea cu 3 coloane)
Enunt (Tema2_4.pdf, identic in cele trei grupe):

    In fisierul IndustriaAlimentara.csv se afla informatii privind numarul de angajati in industria
    alimentara la nivel de localitate. Informatiile sunt urmatoarele:
    Siruta - Codul Siruta al localitatii;
    Localitate - Denumirea localitatii;
    Carne, Peste, LegumeFructe, Uleiuri, Lactate, Morarit, Panificatie - Valorile reprezentand
    numarul de angajati pe principalele activitati din industria alimentara.
    In fisierul PopulatieLocalitati.csv se afla populatia pe localitati si indicativele de judet pentru
    fiecare localitate. In fisierul Coduri_Judete.csv este specificata apartenenta la regiune pentru
    fiecare judet.

    Cerinte:
    1. Sa se salveze in fisierul Cerinta1.csv datele privind numarul de angajati pe activitatile din
    industria alimentara, pentru localitatile in care numarul de angajati este mai mare decat 0. Fisierul
    Cerinta1.csv va avea aceleasi coloane ca fisierul IndustriaAlimentara.csv.
    Exemplu
    Siruta,Localitate,Carne,Peste,LegumeFructe,Uleiuri,Lactate,Morarit,Panificatie
    57350,Cojocna,0.0,0.0,0.0,0.0,1.0,0.0,0.0
    ...
    2. Sa se calculeze si sa se salveze in fisierul Cerinta2.csv, procentul de angajati pe fiecare activitate
    la nivel de localitate. Daca numarul total de angajati este 0, procentele vor fi 0. Vor fi salvate
    codul Siruta, numele localitatii si procentele pentru fiecare localitate.
    Exemplu
    Siruta,Localitate,Carne,Peste,LegumeFructe,Uleiuri,Lactate,Morarit,Panificatie
    32768,Budesti,0.0,0.0,0.0,0.0,0.0,0.0,0.0
    ...
    3. Sa se salveze in fisierul Cerinta3.csv judetele sortate descrescator dupa ponderea angajatilor din
    industria alimentara in populatia totala. Se va salva pentru fiecare judet, indicativul si ponderea
    industriei alimentare.
    Exemplu
    Judet,Ponderi
    if,0.017788851398883143
    ...
    4. Sa se salveze in fisierul Cerinta4.csv, activitatea cu cei mai multi angajati la nivel de judet. Se
    va afisa indicativul de judet si activitatea dominanta.
    Exemplu
    Judet,Activitate
    ab,Carne
    ...
    5. Sa se salveze in fisierul Cerinta5.csv numarul mediu de angajati pe fiecare activitate la nivel de
    regiune. Se va calcula media ponderata, folosind ca pondere populatia localitatilor.
    Exemplu
    Regiune,Carne,Peste,LegumeFructe,Uleiuri,Lactate,Morarit,Panificatie
    Bucuresti-Ilfov,
    2516.507241672197,330.4067432568632,1283.9654215356093,387.2487577642238,532.082127655
    4866,760.203802718469,5413.520212398902
    ...
    6. Sa se calculeze si sa se afiseze in fisierul Cerinta6.csv indicii de localizare la nivel de judet
    pentru fiecare activitate. Un indice de localizare se calculeaza ca raport intre ponderea judetului i
    in activitatea j la nivel national si ponderea populatiei din judetul i in totalul populatiei.
    De exemplu daca pentru judetul x numarul de angajati in industria carnii este de 3000 de persoane
    si populatia este de 200000 de locuitori, iar la nivel national numarul de angajati in industria carnii
    este de 100000 de persoane iar populatia tarii este de 20000000 locuitori, indicele de localizare
    pentru industria carnii in judetul x este: (3000/100000)/(200000/20000000) = 3.
    Exemplu
    Judet,Carne,Peste,LegumeFructe,Uleiuri,Lactate,Morarit,Panificatie
    ab,3.188383891910333,4.891793337941724,0.1324839720970428,0.01758474402299803,5.354642
    2246082175,0.513386058398296,0.8566490275582636
    ...

    Observatie
    Media ponderata pentru o serie de observatii x_i, i = 1..n si ponderi p_i, i = 1..n se calculeaza dupa
    relatia: media = SUM(i=1..n) x_i * p_i .

Ce face fiecare cerinta in cod (activitati = list(df.columns.values)[1:], cele 7 activitati):
    Cerinta 1  total pe localitate (sum axis=1), filtru total > 0 sau != 0      -> Cerinta1.csv, 1372 randuri, 9 coloane
    Cerinta 2  procent pe activitate in total pe localitate                      -> Cerinta2.csv, 3181 randuri
               df[activitati + [Total]].apply(lambda x: x[activitati] * 100 / x["Total"], axis=1)
    Cerinta 3  merge cu populatia, groupby("Judet").sum(), Total / Populatie      -> Cerinta3.csv, 42 randuri, descrescator
    Cerinta 4  activitatea dominanta pe judet: x.index[x.argmax()] cu axis=1      -> Cerinta4.csv, 42 randuri
    Cerinta 5  merge cu Coduri_Judete (left_on="Judet", right_index=True),
               groupby("Regiune") + calcul_medie                                  -> Cerinta5.csv, 8 randuri x 7 activitati
    Cerinta 6  indice de localizare pe judet, pe activitate (formula in sectiunea 6)

Diferente intre cele trei grupe (acelasi enunt, scrisori usor diferite):
    GRUPA 1086  cerintele 1-5 conforme (antet "Pondere" la Cerinta3 in loc de "Ponderi"); Cerinta 6 lipseste.
    GRUPA 1073  cerintele 1, 3, 4, 5 conforme (antet "Totaluri" la Cerinta3); Cerinta 2 da NaN la totaluri zero
                (enuntul cere 0); la Cerinta 6 codul doar afiseaza totalurile nationale pe activitate si populatia
                (Carne 44783, Peste 1158, LegumeFructe 4408, Uleiuri 3321, Lactate 13840, Morarit 11489,
                Panificatie 62854, Populatie 22260798) - primul pas, necompletat.
    GRUPA 1075  Cerinta 2 imparte la total fara x100 (valori intre 0 si 1, nu procente) si da NaN la total 0;
                Cerinta 3 este facuta pe LOCALITATE (3181 de randuri, nesortat, antet "Siruta,Pondere", round(5)),
                nu pe judet; Cerinta 4 si 5 conforme; Cerinta 6 lipseste.

Rezultate (grupa 1086; 1073 si 1075 au aceleasi forme, cu exceptia Cerinta3 la 1075 = 3181 x 2):
    Cerinta1.csv: 1372 randuri x 9 coloane
        antet:       Siruta,Localitate,Carne,Peste,LegumeFructe,Uleiuri,... (+3)
        primul rand: 57350,Cojocna,0.0,0.0,0.0,0.0,... (+3)
    Cerinta2.csv: 3181 randuri x 9 coloane
        antet:       Siruta,Localitate,Carne,Peste,LegumeFructe,Uleiuri,... (+3)
        primul rand: 32768,Budesti,,,,,... (+3)
    Cerinta3.csv: 42 randuri x 2 coloane
        antet:       Judet,Pondere
        primul rand: if,0.017788851398883143
    Cerinta4.csv: 42 randuri x 2 coloane
        antet:       Judet,Activitate
        primul rand: ab,Carne
    Cerinta5.csv: 8 randuri x 8 coloane
        antet:       Regiune,Carne,Peste,LegumeFructe,Uleiuri,Lactate,... (+2)
        primul rand: Bucuresti-Ilfov,2256.5629831750803,297.5996138201782,1180.1593840335777,364.7251342703371,529.96320124...
Rezultate grupa 1073:
    Cerinta1.csv: 1372 randuri x 9 coloane
        antet:       Siruta,Localitate,Carne,Peste,LegumeFructe,Uleiuri,... (+3)
        primul rand: 57350,Cojocna,0.0,0.0,0.0,0.0,... (+3)
    Cerinta2.csv: 3181 randuri x 9 coloane
        antet:       Siruta,Localitate,Carne,Peste,LegumeFructe,Uleiuri,... (+3)
        primul rand: 32768,Budesti,,,,,... (+3)
    Cerinta3.csv: 42 randuri x 2 coloane
        antet:       Judet,Totaluri
        primul rand: if,0.017788851398883143
    Cerinta4.csv: 42 randuri x 2 coloane
        antet:       Judet,Activitate
        primul rand: ab,Carne
    Cerinta5.csv: 8 randuri x 8 coloane
        antet:       Regiune,Carne,Peste,LegumeFructe,Uleiuri,Lactate,... (+2)
        primul rand: Bucuresti-Ilfov,2256.5629831750803,297.5996138201782,1180.1593840335777,364.7251342703371,529.96320124...
Rezultate grupa 1075:
    Cerinta1.csv: 1372 randuri x 9 coloane
        antet:       Siruta,Localitate,Carne,Peste,LegumeFructe,Uleiuri,... (+3)
        primul rand: 57350,Cojocna,0.0,0.0,0.0,0.0,... (+3)
    Cerinta2.csv: 3181 randuri x 9 coloane
        antet:       Siruta,Localitate,Carne,Peste,LegumeFructe,Uleiuri,... (+3)
        primul rand: 32768,Budesti,,,,,... (+3)
    Cerinta3.csv: 3181 randuri x 2 coloane
        antet:       Siruta,Pondere
        primul rand: 32768,0.0
    Cerinta4.csv: 42 randuri x 2 coloane
        antet:       Judet,Activitate
        primul rand: ab,Carne
    Cerinta5.csv: 8 randuri x 8 coloane
        antet:       Regiune,Carne,Peste,LegumeFructe,Uleiuri,Lactate,... (+2)
        primul rand: Bucuresti-Ilfov,2256.5629831750803,297.5996138201782,1180.1593840335777,364.7251342703371,529.96320124...

Verificari fata de exemplele din enunt (facute pe date reale):
    - Cerinta 3: judetul "if" are ponderea 0.017788851398883143 - EXACT valoarea din exemplul enuntului.
    - Cerinta 2: Siruta 32768 (Budesti) are toate procentele 0.0 in exemplul enuntului; codul din grupele 1073/1075/1086
      produce NaN pentru acest rand (fillna(0) il aduce la exemplu - vezi completari).
    - Cerinta 5: exemplul din enunt pentru Bucuresti-Ilfov este Carne 2516.507241672197; media ponderata cu
      populatia din fisierele livrate este 2256.5629831750803 (aceeasi in cele trei grupe si cu np.average).
      Raportul dintre exemplu si calcul difera de la o activitate la alta (de la 1.004 la 1.333), deci exemplul
      nu provine din aceleasi date; formula Sum(x*pop)/Sum(pop) este cea standard si este cea din cod.
    - Cerinta 6: indicele de localizare calculat in completari/ reproduce exact exemplul pentru judetul "ab"
      (Carne 3.188383891910333, Peste 4.891793337941724, LegumeFructe 0.1324839720970428, Uleiuri
      0.01758474402299803, Lactate 5.3546422246082175, Morarit 0.513386058398296, Panificatie 0.8566490275582636).
```

## 9.2 Grupa 1085 - Tema 2.5 (industrie, cifra de afaceri)

```text
Folder: seminar3/grupa_1085      Date: Industrie.csv, PopulatieLocalitati.csv (Judet cu MAJUSCULE)      Enunt: Tema2_5.pdf

Enunt:
    In fisierul Industrie.csv se afla informatii privind cifra de afaceri pentru activitati industriale la
    nivel de localitate. Informatiile sunt urmatoarele:
    Siruta - Codul Siruta al localitatii;
    Localitate - Denumirea localitatii;
    Alimentara, Textila, Lemnului, ChimicaFarmaceutica, Metalurgica, ConstructiiMasini,
    CalculatoareElectronica, Mobila, Energetica - Activitatile industriale cu cifra de afaceri.
    In fisierul PopulatieLocalitati.csv se afla populatia pe localitati si indicativele de judet pentru
    fiecare localitate.

    Cerinte si barem:
    1. Sa se salveze in fisierul Output1.csv cifra de afaceri totala, pe toate activitatile industriale, la
    nivel de localitate. Pentru fiecare localitate se va salva codul Siruta, numele localitatii si cifra de
    afaceri.
    Exemplu
    Siruta,Localitate,Cifra de afaceri
    32768,Budesti,0.0
    49153,Sahateni,0.0
    57350,Cojocna,1685412.0
    ...

    2. Sa se salveze in fisierul Output2.csv cifra de afaceri pe locuitor la nivel de localitate (suma cifrei
    de afaceri pentru toate activitatile raportata la numarul de locuitori). Pentru fiecare localitate se va
    salva codul Siruta, numele localitatii si cifra de afaceri pe locuitor, in ordinea descrescatoare a
    cifrei de afaceri pe locuitor.
    Exemplu
    Siruta,Localitate,CF/Loc
    13301,Oras Mioveni,586069.3455250441
    40214,Oras Ghimbav,437357.6605888257
    40900,Cristian,360546.91625124624
    ...

    3. Sa se salveze in fisierul Output3.csv activitatea cu cifra de afaceri cea mai mare la nivel de
    localitate. Vor fi omise localitatile in care nu exista activitate industriala (cifra de afaceri totala
    este 0). Pentru fiecare localitate se va salva codul Siruta, denumirea localitatii si activitatea cu cifra
    de afaceri cea mai mare.
    Exemplu
    Siruta,Localitate,Activitate
    57350,Cojocna,Alimentara
    90119,Lunca Cernii De Jos,Lemnului
    73736,Poiana Mare,Alimentara
    ...

    4. Sa se calculeze si sa se salveze in fisierul Output4.csv cifra de afaceri pe fiecare activitate la
    nivel de judet. Pentru fiecare judet se va afisa indicativul de judet si cifra de afaceri pentru fiecare
    activitate.
    Exemplu
    Judet,Alimentara,Textila,Lemnului,ChimicaFarmaceutica,Metalurgica,ConstructiiMasini,Ca
    lculatoareElectronica,Mobila,Energetica
    AB,1426022767.0,404955702.0,3749416915.0,17056044.0,145210335.0,856776187.0,13967917.0
    ,210749628.0,296201076.0
    ...
    5. Sa se calculeze si sa se salveze in fisierul Output5.csv cifra de afaceri totala (pentru toate
    activitatile) pe locuitor la nivel de judet. Pentru fiecare judet se va afisa indicativul de judet si cifra
    de afaceri pe locuitor. Datele vor fi salvate in ordinea descrescatoare a cifrei de afaceri pe locuitor.
    Exemplu
    Judet,CA/Loc
    AG,42819.77
    B,27433.928
    TM,23958.813
    ...

    6. Sa se calculeze valorile medii ponderate (media localitatilor) pentru cifra de afaceri pe activitati,
    la nivel de judet, folosind ca pondere populatia. Se vor salva pentru fiecare judet valorile medii.
    Exemplu
    Judet,Alimentara,Textila,Lemnului,ChimicaFarmaceutica,Metalurgica,ConstructiiMasini,Ca
    lculatoareElectronica,Mobila,Energetica
    AB,102110054.27338956,52549931.08201529,314725866.3491664,821854.4863360311,20324411.7
    1006729,57935018.930676706,840925.3542085864,15095941.809551792,56235401.50840143
    ...

Solutia (main.py), activitati = cele 9 industrii:
    Output1  suma pe activitati pe localitate (axis=1)                 -> 3181 randuri, antet "Siruta,Localitate,Total CA"
    Output2  merge cu populatia; (suma activitati / Populatie) pe localitate, descrescator
                                                                       -> 3181 randuri, antet "Siruta,Localitate,CA/Loc"
    Output3  doar localitatile cu cifra de afaceri totala > 0, activitatea dominanta (idxmax prin x.index[x.argmax()])
                                                                       -> 2316 randuri
    Output4  cifra de afaceri pe activitate pe judet (groupby Judet, sum), round(2)  -> 42 randuri
    Output5  (suma activitati pe judet) / Populatie, descrescator                    -> 42 randuri, "Judet,CA/Loc"
    Output6  media ponderata (pondere populatia) pe judet cu calcul_medie           -> 42 randuri
Rezultate:
    Output1.csv: 3181 randuri x 3 coloane
        antet:       Siruta,Localitate,Total CA
        primul rand: 32768,Budesti,0.0
    Output2.csv: 3181 randuri x 3 coloane
        antet:       Siruta,Localitate,CA/Loc
        primul rand: 13301,Oras Mioveni,586069.3455250441
    Output3.csv: 2316 randuri x 3 coloane
        antet:       Siruta,Localitate,Activitate
        primul rand: 57350,Cojocna,Alimentara
    Output4.csv: 42 randuri x 10 coloane
        antet:       Judet,Alimentara,Textila,Lemnului,ChimicaFarmaceutica,Metalurgica,... (+4)
        primul rand: AB,1426022767.0,404955702.0,3749416915.0,17056044.0,145210335.0,... (+4)
    Output5.csv: 42 randuri x 2 coloane
        antet:       Judet,CA/Loc
        primul rand: AG,42819.77016843766
    Output6.csv: 42 randuri x 10 coloane
        antet:       Judet,Alimentara,Textila,Lemnului,ChimicaFarmaceutica,Metalurgica,... (+4)
        primul rand: AB,102110054.27338956,52549931.08201529,314725866.3491664,821854.4863360311,20324411.71006729,... (+4)
Verificari fata de exemplele din enunt: primele randuri din Output1, Output2 (Oras Mioveni 586069.3455250441), Output3 (Cojocna, Lunca Cernii De Jos, ...),
Output4 (AB), Output5 (AG, B) si Output6 (AB: 102110054.27338956 ...) coincid cu exemplele din enunt
(Output5 este rotunjit la 2 zecimale in enunt, in cod nu).
Observatii: antetul Output1 este "Total CA" (enunt: "Cifra de afaceri"); antetul Output2 este "CA/Loc" (enunt: "CF/Loc",
iar la Output5 enuntul foloseste "CA/Loc"); Output4 este rotunjit la 2 zecimale fara sa se ceara.
```

## 9.3 Grupa 1077 - Tema 2.6 (innoptari)

```text
Folder: seminar3/grupa_1077      Date: Innoptari.csv (format lung), PopulatieLocalitati.csv, Coduri_Judete.csv      Enunt: Tema2_6.pdf

Enunt:
    In fisierul Innoptari.csv se afla informatii privind numarul de innoptari in structuri de primire
    turistica la nivel de localitati conform INSSE. Informatiile sunt urmatoarele:
    Siruta - Codul Siruta al localitatii;
    Ani - Anul la care s-a facut raportarea;
    Valoare - Numar de innoptari.
    In fisierul PopulatieLocalitati.csv se afla populatia pe localitati si indicativele de judet pentru
    fiecare localitate. In fisierul Coduri_Judete.csv este specificata apartenenta la regiune pentru
    fiecare judet.

    1. Sa se salveze in fisierul Cerinta1.csv valorile privind innoptarile la nivel de localitate. Fiecare
    an va fi o coloana distincta. In denumirea coloanei va aparea doar anul in cifre.
    Exemplu
    Siruta,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016
    1017,105792.0,94378.0,110498.0,110104.0,117024.0,129430.0,135886.0,125616.0,80876.0,84
    312.0,119020.0,144498.0,162756.0,156672.0,222892.0,232864.0
    ...
    2. Sa se salveze in fisierul Cerinta2.csv localitatile in care s-au inregistrat innoptari in toti anii
    analizati. Fisierul va avea aceesi structura ca a fisierului Cerinta1.csv.
    3. Sa se determine pentru fiecare localitate anul in care s-au inregistrat cele mai multe innoptari.
    Rezultatul va fi salvat in fisierul Cerinta3.csv. Pentru fiecare localitate va fi salvat codul Siruta,
    denumirea localitatii si anul cu cele mai multe innoptari.
    Exemplu
    Siruta,Localitate,Anul
    1017,Municipiul Alba Iulia,2016
    ...
    4. Sa se determine si sa se salveze in fisierul Cerinta4.csv, numarul total de innoptari la 1000 de
    locuitori la nivel de localitate. Pentru fiecare localitate va fi salvat codul Siruta, denumirea
    localitatii si numarul de innoptari la 1000 de locuitori.
    Exemplu
    Siruta,Localitate,Innoptari_1000
    1017,Municipiul Alba Iulia,28709.368226915984
    ...
    5. Sa se determine si sa se salveze in fisierul Cerinta5.csv, numarul de innoptari la 1000 de
    locuitori, pe fiecare an, la nivel de judet. Pentru fiecare judet se va salva indicativul de judet si
    innoptarile la 1000 de locuitori pentru fiecare an.
    Exemplu
    Judet,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016
    ab,617.19,614.72,635.08,581.33,610.33,665.32,758.8,716.38,650.3,651.91,1004.22,1330.74
    ,1373.67,1404.95,2016.93,2021.15
    ...
    6. Sa se determine si sa se salveze in fisierul Cerinta6.csv, coeficientii de variatie la nivel de
    regiune, pe ani, pornind de la innoptarile la nivel de localitate. Pentru fiecare regiune se va salva
    codul regiunii si coeficientii de variatie.
    Exemplu
    Regiune,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,201
    6
    Bucuresti-
    Ilfov,4.371155276592813,4.265532731344076,4.2595498588592395,4.167267062112512,4.11045
    4430850232,4.142376702522658,4.109437203478815,4.053052719831163,4.156056266756756,4.1
    658235801056795,4.220830284346206,4.164693996873714,4.182696674963091,4.18785244450342
    9,4.211252704015913,4.1880655581010515
    ...

Solutia (main.py):
    Cerinta 1  df.pivot(index="Siruta", columns="Ani", values="Valoare"); fillna(0); numele coloanelor taiate cu
               removeprefix("Anul ") -> ani ca text ("2001", ...)             -> Cerinta1.csv (1143 x 17)
    Cerinta 2  localitati cu valori > 0 in toti anii: apply(lambda x: (x > 0).all(), axis=1)  -> Cerinta2.csv (306 randuri)
    Cerinta 3  anul cu cele mai multe innoptari: x.index[x.argmax()] pe randuri, plus Localitate  -> Cerinta3.csv (1143)
    Cerinta 4  innoptari totale la 1000 de locuitori pe localitate                -> Cerinta4.csv (1143) si Cerinta4_sort.csv (sortat)
    Cerinta 5  groupby Judet sum; x[ani] * 1000 / x["Populatie"]; round(1)         -> Cerinta5.csv (42 x 17)
    Cerinta 6  groupby Regiune cu aggregate(lambda x: x.std() / x.mean()); round(2) -> Cerinta6.csv (8 x 17)
Rezultate:
    Cerinta1.csv: 1143 randuri x 17 coloane
        antet:       Siruta,2001,2002,2003,2004,2005,... (+11)
        primul rand: 1017,105792.0,94378.0,110498.0,110104.0,117024.0,... (+11)
    Cerinta2.csv: 306 randuri x 17 coloane
        antet:       Siruta,2001,2002,2003,2004,2005,... (+11)
        primul rand: 1017,105792.0,94378.0,110498.0,110104.0,117024.0,... (+11)
    Cerinta3.csv: 1143 randuri x 3 coloane
        antet:       Siruta,Localitate,Anul
        primul rand: 1017,Municipiul Alba Iulia,2016
    Cerinta4.csv: 1143 randuri x 3 coloane
        antet:       Siruta,Localitate,Innoptari/1000
        primul rand: 1017,Municipiul Alba Iulia,28709.368226915984
    Cerinta4_sort.csv: 1143 randuri x 3 coloane
        antet:       Siruta,Localitate,Innoptari/1000
        primul rand: 11478,Moneasa,3611291.304347826
    Cerinta5.csv: 42 randuri x 17 coloane
        antet:       Judet,2001,2002,2003,2004,2005,... (+11)
        primul rand: ab,617.2,614.7,635.1,581.3,610.3,... (+11)
    Cerinta6.csv: 8 randuri x 17 coloane
        antet:       Regiune,2001,2002,2003,2004,2005,... (+11)
        primul rand: Bucuresti-Ilfov,4.37,4.27,4.26,4.17,4.11,... (+11)
Verificari: primul rand din Cerinta1 (Siruta 1017) coincide cu exemplul; Cerinta3 si Cerinta4 (Alba Iulia: 2016, 28709.368226915984)
coincid cu exemplele; CV-ul regiunii Bucuresti-Ilfov pentru 2001 este 4.37 (exemplul: 4.371155276592813).
Observatii (diferente fata de enunt):
    - Cerinta 4: antet "Innoptari/1000" (enunt: "Innoptari_1000"); Cerinta4_sort.csv este un fisier in plus.
    - Cerinta 5: rotunjit la 1 zecimala (exemplul din enunt are 2 zecimale: ab 617.19; codul da 617.2).
    - Cerinta 6: rotunjit la 2 zecimale (exemplul din enunt este cu precizie completa, 4.371155276592813).
    - Valorile lipsa din pivot se inlocuiesc cu 0 (fillna(0)): Cerinta1 contine 0.0 pentru anii fara innoptari, iar
      CV-ul din Cerinta6 include acesti 0 (std si medie calculate cu zerouri), la fel ca exemplul din enunt.
    - Cerinta 2: "innoptari in toti anii" = fara valori lipsa; in date nu exista zerouri brute, deci filtrul ">0"
      si filtrul "fara NaN" dau acelasi rezultat (306 localitati).
```

# 10. Completari verificate

```text
Folderul completari/ contine doua scripturi care rezolva cerintele lipsa sau neconforme cu enuntul. Nu modifica
solutiile din seminar; sunt scrise in acelasi stil si verificate pe datele din repo. Scripturile citesc datele din
folderele seminar2/grupa_1073, seminar2/grupa_1075 si seminar3/grupa_1086 si scriu in completari/data_out/.
```

## 10.1 seminar3_industria_alimentara_complet.py   (Tema 2.4, cerintele 1-6)

```text
    Cerinta 1  localitati cu cel putin un angajat, aceleasi coloane ca fisierul initial
    Cerinta 2  procente (x100), cu 0 in loc de NaN cand totalul e 0
    Cerinta 3  judete descrescator dupa angajati/populatie, antet "Ponderi"
    Cerinta 4  activitatea dominanta pe judet (idxmax axis=1)
    Cerinta 5  media ponderata pe regiune: x[activitati].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum()
    Cerinta 6  indice de localizare = (angajati judet / angajati national) / (populatie judet / populatie nationala)
Verificari efectuate:
    - Cerinta 1, 4, 5 identice cu fisierele din seminar3/grupa_1086/data_out
    - Cerinta 2: randul Siruta 32768 are toate valorile 0.0, fara NaN in tot fisierul
    - Cerinta 3: judetul if = 0.0177888513988831 (exemplul enuntului), 42 de randuri, ordonat descrescator
    - Cerinta 6: judetul ab coincide cu exemplul enuntului la toate cele 7 activitati (toleranta 1e-12), forma 42 x 7
```

## 10.2 seminar2_diversitate_segregare.py   (Tema 2.1 si Tema 2.2)

```text
    Etnii (Tema 2.1):
        populatie pe judet / regiune / macroregiune                -> Etnii_Jud, Etnii_Reg, Etnii_Macro
        procente pe localitate / judet / regiune / macroregiune    -> Etnii_P_Loc, Etnii_P_Jud, Etnii_P_Reg, Etnii_P_Macro
        indice de disimilaritate pe judet                          -> Etnii_Disimilaritate
        Shannon-Weaver (log2) pe judet, per etnie                  -> Etnii_Shannon
    Confesiuni (Tema 2.2):
        populatie si ponderi pe judet / regiune / macroregiune     -> Confesiuni_Jud/Reg/Macro, Confesiuni_P_Loc/Jud/Reg/Macro
        diversitate pe judet si pe regiune: Shannon (log2), Simpson, Simpson invers
                                                                    -> Confesiuni_Diversitate_Jud, Confesiuni_Diversitate_Reg
Verificari efectuate:
    - totalurile pe judet, regiune si macroregiune sunt egale (18879221 de persoane la etnii)
    - procentele pe macroregiune insumeaza 100 pe fiecare rand; 4 macroregiuni
    - Shannon in biti = Shannon in nats din solutia grupei 1085 / ln(2), la toate cele 42 x 22 de valori
    - disimilaritatea este in [0, 0.9929]; Simpson in [0, 1); Simpson invers >= 1; Shannon (confesiuni) maxim 2.065 <= log2(21)
    - diversitatea pe regiune (Shannon bits / Simpson / Simpson invers): Bucuresti-Ilfov 0.403/0.084/1.092,
      Centru 1.806/0.559/2.268, Nord-Est 0.695/0.195/1.243, Nord-Vest 1.704/0.509/2.037, Sud 0.226/0.046/1.048,
      Sud-Est 0.387/0.090/1.098, Sud-Vest 0.132/0.024/1.025, Vest 1.238/0.342/1.520
Nu sunt acoperite prin completari: Seminar 1 (observatiile despre Chi2, inertii) si Seminar 2 grupa 1077
(Judete.csv cu procentul pe judet, categorie_varsta.csv); pentru ele sunt notate diferentele in sectiunea 13.
```

# 11. Subiecte si teste (folderul subiecte/)

```text
Acestea sunt subiecte de tip examen, din ghid (Anexa A, sectiunea D). Fiecare are un main.py in folderul lui, cu
data_in/ si data_out/ goale: fisierele CSV ale acestor subiecte (12014.csv, Agricultura.csv, Firme.csv etc.)
NU au fost primite, deci codul din aceste foldere nu a fost rulat aici.

    subiecte/s1_1085_firme_2014/            S1_1085 (12014.csv), 4 cerinte: raport CA/NrSal pe localitate, rata ocuparii pe judet,
                                             localitatea cu profit/locuitor maxim, media ponderata pe judet.
                                             Marcat [RULAT] in ghid; control: Output1 = 2749 randuri, Output2/3/4 = 42 randuri.
    subiecte/industrie_cifra_afaceri/        main_cerinte_seminar.py: aceleasi 5 cerinte ca la seminarul 3 pe Industrie.csv
                                             ([RULAT] in ghid: cerinta 1 = 2317 localitati, 8 regiuni la cerinta 5);
                                             main_cerinte_student.py: 3 cerinte (total pe localitate, CA pe locuitor, activitate
                                             dominanta) - [NERULAT] in ghid.
    subiecte/innoptari/                      Innoptari.csv, 6 cerinte cu pivot (cerintele 1-4 lucrate de student; 5 si 6 rulate pe
                                             un set cu aceeasi structura). Acelasi tip de cerinte ca grupa 1077 de la Seminar 3.
    subiecte/test_agricultura/               test generat Agricultura (stil S1_1085), [RULAT]: control Output1 = 2972, Output2 = 8,
                                             Output3 = 42, Output4 = 42 randuri.
    subiecte/test_firme_pe_ani/              test generat Firme pe ani (format lung, 8 cerinte), [RULAT].

Verificat acum (doar sintaxa): toate fisierele .py din subiecte/ compileaza. Pentru rulare, pune fisierele CSV in
data_in/ din folderul subiectului. Industrie.csv exista in repo (seminar3/grupa_1085/data_in/), deci
main_cerinte_seminar.py si main_cerinte_student.py pot fi rulate copiind Industrie.csv, PopulatieLocalitati.csv
(si Coduri_Judete.csv de la Seminar 3) in subiecte/industrie_cifra_afaceri/data_in/. ATENTIE: PopulatieLocalitati.csv de la
grupa 1085 are judetele cu MAJUSCULE, iar main_cerinte_seminar.py converteste populatia la litere mici inainte de merge cu Coduri_Judete.
Enunturile complete ale acestor subiecte sunt in Anexa A (sectiunea D).
```

# 12. Rezultate verificate (rulare pe date reale)

```text
Metoda: pentru fiecare dintre cele 14 foldere de grupa, am copiat arhiva primita, am sters data_out/, am rulat main.py
(Python 3.13, pandas 3.0.5, numpy 2.5.3, scipy 1.18.1) si am comparat fisierele regenerate cu cele livrate in data_out/
(aceeasi forma, aceleasi antete, aceleasi valori la toleranta 1e-9). Toate cele 14 rulari s-au incheiat fara eroare (exit 0).

    Seminar 1, grupa 1075   20 din 20 de fisiere identice
    Seminar 1, grupa 1077    3 din 3 fisiere identice
    Seminar 1, grupa 1085    1 din 1 fisiere identice
    Seminar 1, grupa 1086    3 din 3 fisiere identice
    Seminar 2, grupa 1073    3 din 3 fisiere identice
    Seminar 2, grupa 1075    5 din 5 fisiere identice
    Seminar 2, grupa 1077    5 identice; PrezentaSort.csv are aceleasi randuri, cu ordine diferita doar intre
                             localitati cu procent egal (14 pozitii); Femei_65_.csv din arhiva nu mai este regenerat
                             (ramas dintr-o rulare anterioara cu alta categorie)
    Seminar 2, grupa 1085    5 din 5 fisiere identice
    Seminar 2, grupa 1086    4 din 4 fisiere identice
    Seminar 3, grupa 1073    5 din 5 fisiere identice
    Seminar 3, grupa 1075    5 din 5 fisiere identice
    Seminar 3, grupa 1077    7 din 7 fisiere identice
    Seminar 3, grupa 1085    5 identice; Output2.csv are aceleasi randuri, ordine diferita doar intre localitatile cu
                             valoare 0 (sortarea nu e stabila la egalitate)
    Seminar 3, grupa 1086    5 din 5 fisiere identice

Concluzie: codul din repo reproduce rezultatele livrate si pe pandas 3 (cele livrate au fost produse cu o versiune mai veche).

Verificari suplimentare (pe langa compararea cu fisierele livrate):
    - exemple numerice din enunturi reproduse exact (vezi sectiunile 9.1, 9.2, 9.3 si 10);
    - completarile din completari/ rulate si verificate (sectiunea 10);
    - toate fisierele .py din repo compileaza.

Ce NU a fost verificat: subiectele din subiecte/ (lipsesc fisierele CSV ale lor); exemplul Cerinta 5 din Tema 2.4
nu se reproduce din datele livrate (sectiunea 9.1).
```

# 13. Diferente fata de enunt (lista consolidata)

```text
Aceasta lista nu modifica solutiile; arata unde fisierele produse difera de ce cere enuntul sau de exemplul din enunt,
ca sa stii ce trebuie corectat inainte de predare. Cele marcate COMPLETAT au rezolvare verificata in completari/.

SEMINAR 1
    1077  Inertia si centrii de grupa sunt doar afisati, nu salvati (enuntul cere salvarea).
    1077  Inertia pe grupa se calculeaza pe toate observatiile fata de centrul grupei (nu intra-grupa).
    1085  Chi2: p-value calculat ca cdf (nu 1 - cdf), comparat cu "<" prag; grade de libertate m-1.

SEMINAR 2
    1073  Ethnicity_Reg.csv are coloana in plus IndicativJudet (siruri concatenate).
    1073  Lipsesc macroregiunile, procentele pe judet/regiune/macroregiune si indicii de segregare.   COMPLETAT
    1075  Shannon in nats (nu log2); 75 NaN; calculat per judet x confesiune, nu o valoare de diversitate per judet.
    1075  Lipsesc Simpson, Simpson invers, indicii pe regiune, macroregiunile, ponderile pe regiune/macroregiune.   COMPLETAT
    1077  Cerinta 4: categorie fixata in cod, fisierul se numeste dupa categorie (enunt: categorie_varsta.csv).
    1077  Cerinta 5: fisierul se numeste Prezenta_Judet.csv si contine sume, nu procentul (enunt: Judete.csv cu prezenta).
    1077  Cerinta 6: Shannon in nats.
    1085  Shannon in nats; lipsesc disimilaritatea, macroregiunea, procentele pe regiune/macroregiune.   COMPLETAT
    1086  Disimilaritatea este doar afisata, nu salvata; lipsesc macroregiunea, procentele pe regiune/macroregiune, Shannon.   COMPLETAT

SEMINAR 3
    1073  Cerinta 2: NaN la total 0 (enunt: 0); Cerinta 3: antet "Totaluri" (enunt: "Ponderi"); Cerinta 6 doar schitata.   COMPLETAT
    1075  Cerinta 2: fractii in loc de procente si NaN la total 0; Cerinta 3 pe localitati si nesortata (enunt: pe judet,
          descrescator, antet "Judet,Ponderi"); Cerinta 6 lipseste.   COMPLETAT
    1086  Cerinta 2: NaN la total 0 (enunt: 0); Cerinta 3: antet "Pondere" (enunt: "Ponderi"); Cerinta 6 lipseste.   COMPLETAT
    1077  Cerinta 4: antet "Innoptari/1000" (enunt: "Innoptari_1000"), fisier in plus Cerinta4_sort.csv;
          Cerinta 5: round(1) (exemplu cu 2 zecimale); Cerinta 6: round(2) (exemplu cu precizie completa).
    1085  Antetele "Total CA" (enunt: "Cifra de afaceri") si "CA/Loc" la Output2 (enunt: "CF/Loc"); Output4 rotunjit la 2 zecimale.
    toate (1073, 1075, 1086)  Exemplul Cerinta 5 din enunt (Bucuresti-Ilfov, Carne 2516.507...) nu se reproduce din datele
          livrate: media ponderata corecta este 2256.563.
```

# 14. Capcane noi gasite la verificare

```text
Se adauga celor 14 capcane din Anexa A, sectiunea C.

  15. Coduri_Judete.csv are DOUA formate (3 coloane la Seminar 3, 4 coloane cu NrCrt la Seminar 2). Cu index_col=0,
      la formatul cu 4 coloane indexul devine NrCrt, nu indicativul. Cu index_col=1 pe formatul cu 3 coloane
      indexul devine NumeJudet si merge-ul pierde TOATE randurile (0 randuri, fara eroare). Verifica mereu
      print(df_coduri.head()) si .shape dupa merge.
  16. groupby(...).sum() peste coloane text le CONCATENEAZA (apare "bif" in loc de un total). Selecteaza explicit
      coloanele numerice + cheia: df[etnii + ["Regiune"]] (cazul Ethnicity_Reg.csv din grupa 1073).
  17. scipy.stats.entropy foloseste logaritm natural. Pentru Shannon-Weaver in biti: entropy(p, base=2) sau
      impartire la ln(2).
  18. entropy pe un vector de zerouri da NaN (nu 0). tx[tx == 0] = 1 NU repara asta, pentru ca p = x / tx ramane
      vector de zerouri. Solutie: .fillna(0) pe rezultat.
  19. cdist(x, x, "mahalanobis") fara VI estimeaza covarianta din x duplicat (vstack([x, x])), deci distantele
      difera cu un factor constant 1.006079 (n = 42) fata de VI = inv(np.cov(x, rowvar=False)). Daca enuntul cere
      inversa matricei de covarianta a datelor, paseaza VI explicit.
  20. np.std (ddof=0) nu este pandas std (ddof=1). Standardizarea cu numpy imparte la std cu ddof=0; coeficientul de
      variatie din pandas (x.std() / x.mean()) foloseste ddof=1.
  21. sort_values nu este stabil la egalitate: localitatile cu aceeasi valoare (de exemplu 0.0 sau procente egale) pot
      aparea in alta ordine la rulari diferite. Continutul fisierului ramane acelasi; daca ordinea conteaza, adauga
      kind="stable" sau o cheie secundara.
  22. Un total negativ exista in date (Industrie.csv, localitatea Vladila): filtrul "total > 0" (2316) difera de
      "total != 0" (2317). Citeste enuntul: "mai mare decat 0" sau "diferit de 0".
  23. In Natalitate_Ro.csv valorile text au spatiu in fata (" TOTAL", " Anul 1990"); pivot-ul pastreaza spatiul in
      numele coloanelor. Nu face comparatii exacte pe aceste siruri fara .str.strip().
  24. pivot_table(...) agrega valorile duplicate (media), pe cand pivot(...) da eroare la duplicate; ambele lasa NaN
      pentru combinatiile lipsa. fillna(0) dupa pivot schimba semantica: un an lipsa devine "0 innoptari", ceea ce
      intra in coeficientul de variatie (grupa 1077 de la Seminar 3, unde si exemplul din enunt include acei 0).
```

# 15. Publicare pe GitHub

```text
Repo-ul local are deja istoricul git (un commit per exercitiu). Pentru a-l publica pe contul mateisandu24:

  1. Pe github.com creeaza un repository NOU, public, numit dsad-pandas-numpy. NU bifa "Add a README" si nu adauga
     .gitignore sau licenta (repo-ul local le are deja).
  2. Dezarhiveaza dsad-pandas-numpy.zip, intra in folder si ruleaza:

         git remote add origin https://github.com/mateisandu24/dsad-pandas-numpy.git
         git push -u origin main

     (daca ai SSH configurat: git@github.com:mateisandu24/dsad-pandas-numpy.git)
  3. La prima trimitere GitHub cere autentificare: parola contului nu mai merge, foloseste un Personal Access Token
     (Settings > Developer settings > Personal access tokens) sau GitHub CLI: gh auth login.

Verificari utile inainte de push:
    git log --oneline            istoricul complet, cate un commit per exercitiu
    git status                   trebuie sa fie curat
    git config user.name         numele din commit-uri; schimba-l daca vrei altul:
                                 git config user.name "Numele Tau" (pentru commit-uri noi)

Continutul este public odata publicat. Atentie la:
    - fisierele PDF cu enunturile (TemaN_M.pdf) sunt materiale ale cursului; sterge-le daca nu vrei sa le redistribui:
          git rm seminar*/grupa_*/Tema*.pdf && git commit -m "Scot enunturile PDF"
      (enunturile sunt oricum transcrise in aceasta documentatie).
    - fisierele CSV de date sunt statistici publice, dar sunt incluse in mai multe copii (cate una pe folder de grupa,
      ca fiecare folder sa ruleze izolat); repo-ul are aproximativ 11 MB.
```

# Anexa A. Ghidul complet (retete B1-B15, capcane C, subiecte D1-D7, metode E, lista F)

```text
Aceasta anexa reproduce INTEGRAL fisierul referinta/GHID_pandas_numpy.txt, primit ca ghid.
Marcaje: [RULAT] = cod rulat si comparat cu rezultatele corecte; [NERULAT] = scris dupa acelasi tipar, nerulat pe date reale.

--- INCEPUT GHID ---

================================================================================
GHID: PANDAS / NUMPY IN STILUL SEMINARULUI (DSAD) - PENTRU UN AI CARE TREBUIE SA INVETE
================================================================================

CUM SA FOLOSESTI ACEST FISIER (instructiune pentru AI)
-------------------------------------------------------
Studentul rezolva subiecte de tip "date statistice pe localitati/judete/regiuni din
Romania" in Python, cu pandas si numpy. Fisierul contine:
  A. Stilul de scris si conventiile (de respectat cand scrii cod pentru acest student)
  B. Retetele (tiparele) care se repeta in toate subiectele
  C. Capcanele frecvente (greseli reale facute de student, cu corectura)
  D. Subiecte rezolvate complet, cu enunt scurt, cod si note
  E. Metode suplimentare din seminar (NaN, standardizare, corelatii etc.)

Cand studentul iti da un enunt nou:
  1. Identifica nivelul fiecarei cerinte: localitate, judet sau regiune.
  2. Alege reteta din sectiunea B care se potriveste.
  3. Scrie codul in stilul din sectiunea A, cerinta cu cerinta, cu comentariu "# Cerinta N".
  4. Explica pe scurt ce face fiecare linie (studentul invata, nu doar copiaza).
  5. Spune la final ce rezultat trebuie sa vada (numar de randuri, primul rand) ca sa se poata verifica.

Date reale folosite: ~3181 de localitati, 42 de judete (incl. Bucuresti), 8 regiuni.
Cheia de legatura intre tabele: codul Siruta (indexul tabelelor).

Marcaje: [RULAT] = codul a fost rulat si comparat cu rezultatele corecte.
         [NERULAT] = scris dupa acelasi tipar, dar nerulat pe datele reale.


================================================================================
A. STILUL DE SCRIS (seminar)
================================================================================
- Limba: comentarii si nume in romana, fara diacritice ("Cerinta", "Judet", "Populatie").
- Importuri standard:
      import pandas as pd
      import numpy as np
  (in seminar se foloseste si:  from numpy.ma.extras import average )
- Prefixe de nume: df_ pentru DataFrame, s_ pentru Series. Exemple: df_industrie, s_cerinta3,
  df_cerinta5. In rezolvari scurte: c1, c2, ... pentru rezultatele cerintelor.
- Fiecare cerinta incepe cu un comentariu:  # Cerinta 1   (sau  # 1 )
- Fisierele se citesc cu  index_col=0  (codul Siruta devine index):
      df = pd.read_csv("data_in/Industrie.csv", index_col=0)
- Lista coloanelor numerice:
      activitati = list(df.columns.values)[1:]      # toate coloanele fara prima (text)
- Se prefera  apply(...)  cu  lambda  pentru functii scurte, si  def  pentru functii mai lungi
  (de ex. calcul_medie).
- Rezultatele se salveaza in  data_out/  cu  .to_csv("data_out/CerintaN.csv")  sau
  OutputN.csv, exact cum cere enuntul.
- Antetul coloanelor trebuie sa fie IDENTIC cu exemplul din enunt (majuscule, spatii, "/").
- La salvare se rotunjeste doar daca enuntul cere:  .round(3).to_csv(...)
- Se da nume coloanei unui Series inainte de salvare:  s.name = "Rata Ocuparii"
- Dupa fiecare merge se verifica  .shape  (3181 randuri pentru localitati).


================================================================================
B. RETETELE (tiparele care se repeta)
================================================================================
Regula centrala: NIVELUL cerintei decide pasii.
  "pentru fiecare localitate" -> fara groupby, lucrezi pe randuri
  "pentru fiecare judet"      -> merge populatie, groupby("Judet")
  "pentru fiecare regiune"    -> merge populatie, merge Coduri_Judete, groupby("Regiune")

--- B1. Incarcare ---------------------------------------------------------------
    df  = pd.read_csv("data_in/X.csv", index_col=0)
    pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)   # coloane: Localitate, Judet, Populatie
    reg = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)         # index = indicativ judet, coloana Regiune
  ATENTIE: pop trebuie citit mereu cu index_col=0, altfel merge-urile se lipesc dupa pozitie.

--- B2. Filtru cu masca booleana, coloana noua, sortare --------------------------
    df_f = df[df["NrSal"] > 0]                         # pastreaza randurile unde conditia e True
    c1 = df_f[["DenLocalitate"]].copy()
    c1["Raport"] = df_f["TotalCifraAfaceri"] / df_f["NrSal"]
    c1 = c1.sort_values(by="Raport", ascending=False)  # descrescator
  - df["c"] da Series; df[["c"]] da DataFrame (doar DataFrame-ul are merge).
  - .copy() evita avertismentul SettingWithCopy.
  - sort_values NU modifica pe loc: trebuie asignat  c1 = c1.sort_values(...).

--- B3. Suma pe rand si pe coloana ------------------------------------------------
    df.iloc[:, 1:].sum(axis=1)     # un total pe localitate (rand), coloane de la a doua incolo
    df.sum()                       # un total pe coloana
  - iloc[:, 1:] = toate randurile, coloanele de la pozitia 1 incolo (numerotarea incepe de la 0).
  - df[1:] taie RANDURI, nu coloane.
  - axis=1: de-a lungul randului (o valoare per rand). axis=0 (implicit): in jos pe coloana.

--- B4. Merge (join dupa index) ---------------------------------------------------
    m = df.merge(pop[["Judet", "Populatie"]], left_index=True, right_index=True)
  - Lipeste tabelele dupa Siruta (indexul). Inner join implicit.
  - Dupa un merge ordinea randurilor este cea a tabelului din STANGA.
  - Daca coloana de legatura nu e index: left_on="Judet", right_index=True. Exemplu regiune:
        m = m.merge(reg["Regiune"], left_on="Judet", right_index=True)
  - Daca ai deja Localitate in df nu mai ai nevoie de pop pentru nume:
        c = df[["Localitate"]].copy(); c["Valoare"] = s      # aliniere automata dupa index

--- B5. Groupby + sum, apoi raport (judet / regiune) ------------------------------
    jud = m[["NrSal", "Judet", "Populatie"]].groupby(by="Judet").sum()
    rata = jud["NrSal"] * 1000 / jud["Populatie"]
    rata.name = "Rata Ocuparii"
    rata.sort_values(ascending=False).to_csv("data_out/Output2.csv")
  - Selectezi inainte DOAR coloanele numerice + cheia de grupare.
  - Mai intai ADUNI pe grup, apoi IMPARTI. Nu faci media rapoartelor pe localitati.

--- B6. Maximul pe grup (numele localitatii) -------------------------------------
    s = (m[["DenLocalitate", "Judet", "Profit/loc"]]
         .groupby(by="Judet")
         .apply(lambda g: g["DenLocalitate"].iloc[g["Profit/loc"].argmax()],
                include_groups=False))
    s.name = "Localitate"
  - argmax() = POZITIA maximului; .iloc[pozitie] aduce valoarea de la acea pozitie.
  - idxmax() = ETICHETA (indexul) maximului. Pe un tabel pe judete, dominanta se obtine cu
        x.index[x.argmax()]   sau   df.idxmax(axis=1)     (numele coloanei)
  - include_groups=False scoate coloana de grupare din tabelul primit de functie.

--- B7. Coloana dominanta pe rand ---------------------------------------------------
    df.iloc[:, 1:].idxmax(axis=1)       # numele coloanei cu valoarea maxima pe fiecare rand
  - NU include coloana text (Localitate) in idxmax.
  - Randurile cu toate valorile 0 returneaza prima coloana: filtreaza-le inainte
        df_f = df[df.iloc[:, 1:].sum(axis=1) > 0]

--- B8. Media ponderata pe grup ---------------------------------------------------
  Varianta cu numpy (stilul seminarului). Ponderea (Populatie) trebuie sa fie ULTIMA coloana:
    def calcul_medie(df):
        x = df.values
        medii = average(x[:, :-1], axis=0, weights=x[:, -1])      # np.average e echivalent
        return pd.Series(medii, df.columns[:-1])

    res = (m[indicatori + ["Judet", "Populatie"]]
           .groupby(by="Judet")
           .apply(calcul_medie, include_groups=False))
  Varianta cu lambda (fara def, nu conteaza ordinea coloanelor):
    res = (m[indicatori + ["Judet", "Populatie"]]
           .groupby(by="Judet")
           .apply(lambda x: x[indicatori].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
                  include_groups=False))
  Formula: suma(valoare * pondere) / suma(pondere). Ambele variante dau acelasi rezultat.
  Returnand un pd.Series din functie, pandas construieste un rand pe grup.

--- B9. Procente pe rand (ponderea unei activitati in total pe localitate) -------
    s_total = df[activitati].apply(lambda x: x.sum(), axis=1)
    df["Total"] = s_total
    c2 = df[activitati + ["Total"]].apply(lambda x: x[activitati] * 100 / x["Total"], axis=1)
    c2.insert(0, "Localitate", df["Localitate"])
  - Randurile cu total 0 dau NaN (0/0). Pentru 0 in loc de NaN: .fillna(0).
  - axis=1 = pe rand (ponderea in interiorul localitatii). axis=0 ar da ponderea din totalul national.

--- B10. Format lung -> lat (pivot) -------------------------------------------------
    df = pd.read_csv("data_in/Innoptari.csv")                      # Siruta, Ani ("Anul 2001"), Valoare
    df["Ani"] = df["Ani"].str.replace("Anul ", "").astype(int)
    c1 = df.pivot_table(index="Siruta", columns="Ani", values="Valoare")
  Ani devin coloane (int), Siruta devine index.

--- B11. Filtru "fara lipsuri" / "doar nenule" -----------------------------------
    c1.notna().all(axis=1)                 # True pe randurile fara NaN
    c2 = c1[c1.notna().all(axis=1)]
    df.iloc[:, 1:].sum(axis=1) > 0         # localitati cu cel putin o valoare nenula
    df.isna().sum()                        # cate NaN pe coloana (diagnostic)
  all() = "toate valorile", any() = "cel putin una".

--- B12. Rata la 1000 de locuitori pe grup si pe ani ------------------------------
    m   = c1.merge(pop[["Judet", "Populatie"]], left_index=True, right_index=True)
    jud = m.groupby("Judet").sum()
    c5  = jud.drop(columns="Populatie").mul(1000).div(jud["Populatie"], axis=0)
  - drop(columns="Populatie") scoate populatia din tabelul cu ani.
  - div(..., axis=0) imparte fiecare RAND la populatia lui (axis=0 = potrivire dupa rand).

--- B13. Coeficient de variatie pe regiune, pe ani --------------------------------
    anii = list(c1.columns)
    g  = mr.groupby("Regiune")[anii]
    c6 = g.std() / g.mean()                # abaterea standard de selectie (ddof=1) / media

--- B14. Total pe an --------------------------------------------------------------
    s7 = c1.sum()                          # suma pe coloane = un total pe an
    s7.name = "Total"; s7.index.name = "Anul"

--- B15. Numele primei coloane la salvare ---------------------------------------
    c.index.name = "Siruta"
    c.to_csv("f.csv")                      # sau: c.to_csv("f.csv", index_label="Siruta")


================================================================================
C. CAPCANE FRECVENTE (greseli reale, cu corectura)
================================================================================
1. merge care da rezultate gresite fara eroare: pop citit FARA index_col=0 -> pandas leaga
   dupa pozitie (0,1,2,..) si numele localitatilor se amesteca (ex. 1017 apare ca "Brates"
   in loc de "Municipiul Alba Iulia"). Verificare: print(pop.head()); un rand cunoscut:
   1017 = Municipiul Alba Iulia.
2. KeyError: None of [Index(['Judet,Populatie'])]: s-a scris  pop[["Judet,Populatie"]]  (un
   singur sir). Corect:  pop[["Judet", "Populatie"]].
3. AttributeError: 'Series' object has no attribute 'merge': s-a scris pop["Localitate"]
   (Series). Corect: pop[["Localitate"]] (DataFrame).
4. Paranteza lipsa la o expresie pe mai multe randuri (PyCharm: "Unexpected expression syntax").
   Daca expresia incepe cu  x = (  trebuie inchisa si ea.
5. df[1:] in loc de df.iloc[:, 1:]: primul taie randuri, al doilea coloane.
6. df.iloc[mask]: iloc vrea pozitii. Pentru masca booleana:  df[mask]  sau  df.loc[mask].
7. sum() fara axis=1 cand vrei total pe localitate: da total pe coloana.
8. idxmax pe un tabel care contine si coloana text: foloseste df.iloc[:, 1:].idxmax(axis=1).
9. sort_values fara asignare: c = c.sort_values(...), apoi to_csv(c).
10. inf / NaN prin impartire la 0 apar primele la sortarea descrescatoare. Filtru:
        c = c[np.isfinite(c["Coloana"])]
11. Ordinea randurilor din rezultat: dupa merge, ordinea e cea a tabelului din stanga. Daca
    exemplul din enunt pastreaza ordinea fisierului initial, pornesti de la df, nu de la pop.
12. Indicativele de judet pot fi cu majuscule intr-un fisier (PopulatieLocalitati: AB) si
    cu litere mici in altul (Coduri_Judete: ab). Un merge direct pierde toate randurile:
        reg.index = reg.index.str.upper()      # sau  pop["Judet"].str.lower()
13. Antet diferit de enunt: "Rata ocuparii" in loc de "Rata Ocuparii".
14. Calea fisierelor: "data_in/12014.csv" (nu doar "12014.csv") daca fisierele sunt in data_in/.
    Folderul data_out/ trebuie sa existe, altfel to_csv da eroare.


================================================================================
D. SUBIECTE REZOLVATE
================================================================================

--------------------------------------------------------------------------------
D1. SUBIECTUL S1_1085  (fisier 12014.csv)  [RULAT, comparat cu rezultatele corecte]
--------------------------------------------------------------------------------
Date: 12014.csv = Siruta, DenLocalitate, NrFirme, NrSal, TotalCifraAfaceri, TotalProfit,
      TotalPierdere (firme in 2014, pe localitate).
      PopulatieLocalitati.csv = Siruta, Localitate, Judet, Populatie.
Cerinte:
 1. (2p) Output1.csv: raport cifra de afaceri / numar salariati pe localitate unde exista
    salariati, descrescator. Coloane: Siruta, DenLocalitate, Raport CA/NrSal.
 2. (2p) Output2.csv: rata ocuparii = salariati la 1000 de locuitori, pe judet, descrescator.
    Coloane: Judet, Rata Ocuparii.
 3. (2p) Output3.csv: pentru fiecare judet, localitatea cu cel mai mare profit pe locuitor.
    Coloane: Judet, Localitate.
 4. (3p) Output4.csv: media ponderata (pondere = populatia) a celor 5 indicatori pe judet.
    Coloane: Judet, NrFirme, NrSal, TotalCifraAfaceri, TotalProfit, TotalPierdere.
 (+1 punct din oficiu)

Solutie:

    import pandas as pd
    import numpy as np

    df_firme = pd.read_csv("data_in/12014.csv", index_col=0)
    df_pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)

    # Cerinta 1
    df_sal = df_firme[df_firme["NrSal"] > 0]
    c1 = df_sal[["DenLocalitate"]].copy()
    c1["Raport CA/NrSal"] = df_sal["TotalCifraAfaceri"] / df_sal["NrSal"]
    c1 = c1.sort_values(by="Raport CA/NrSal", ascending=False)
    c1.round(3).to_csv("data_out/Output1.csv")

    # Cerinta 2
    df_loc = df_firme.merge(df_pop[["Judet", "Populatie"]], left_index=True, right_index=True)
    df_jud = df_loc[["NrSal", "Judet", "Populatie"]].groupby(by="Judet").sum()
    s2 = df_jud["NrSal"] * 1000 / df_jud["Populatie"]
    s2.name = "Rata Ocuparii"
    s2.sort_values(ascending=False).to_csv("data_out/Output2.csv")

    # Cerinta 3
    df_loc["Profit/loc"] = df_loc["TotalProfit"] / df_loc["Populatie"]
    s3 = (df_loc[["DenLocalitate", "Judet", "Profit/loc"]]
          .groupby(by="Judet")
          .apply(lambda g: g["DenLocalitate"].iloc[g["Profit/loc"].argmax()], include_groups=False))
    s3.name = "Localitate"
    s3.to_csv("data_out/Output3.csv")

    # Cerinta 4
    indicatori = ["NrFirme", "NrSal", "TotalCifraAfaceri", "TotalProfit", "TotalPierdere"]
    c4 = (df_loc[indicatori + ["Judet", "Populatie"]]
          .groupby(by="Judet")
          .apply(lambda x: x[indicatori].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
                 include_groups=False))
    c4.round(3).to_csv("data_out/Output4.csv")

Rezultate de control (set de date de practica): Output1 are 2749 de randuri, Output2/3/4 au
cate 42 de randuri (cate unul per judet).


--------------------------------------------------------------------------------
D2. SEMINAR 3 - IndustriaAlimentara.csv (5 cerinte)  [RULAT pe date, acelasi cod]
--------------------------------------------------------------------------------
Date: IndustriaAlimentara.csv = Siruta, Localitate, Carne, Peste, LegumeFructe, Uleiuri,
      Lactate, Morarit, Panificatie. PopulatieLocalitati.csv, Coduri_Judete.csv
      (IndicativJudet, NumeJudet, Regiune).
Cerinte:
 1. Localitatile cu cel putin o firma.
 2. Ponderea (%) fiecarei activitati in total pe localitate.
 3. Numarul de firme / locuitor pe judet, descrescator.
 4. Activitatea dominanta pe judet.
 5. Media ponderata (pondere = populatia) a activitatilor pe regiune.

Solutie:

    import pandas as pd
    from numpy.ma.extras import average

    pd.set_option("display.max_columns", None)
    df_industria_a = pd.read_csv("data_in/IndustriaAlimentara.csv", index_col=0)
    activitati = list(df_industria_a.columns.values)[1:]

    # 1
    s_total_loc = df_industria_a[activitati].apply(func=lambda x: x.sum(), axis=1)
    s_total_loc.name = "Total"
    df_cerinta1 = df_industria_a[s_total_loc != 0]
    df_cerinta1.to_csv("data_out/Cerinta1.csv")

    # 2
    df_industria_a["Total"] = s_total_loc
    df_cerinta2 = df_industria_a[activitati + ["Total"]].apply(
        func=lambda x: x[activitati] * 100 / x["Total"], axis=1)
    df_cerinta2.insert(0, "Localitate", df_industria_a["Localitate"])
    df_cerinta2.to_csv("data_out/Cerinta2.csv")

    # 3
    df_populatie = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
    df_industria_a_loc = df_industria_a.merge(df_populatie, left_index=True, right_index=True)
    df_industria_a_jud = df_industria_a_loc[activitati + ["Total", "Judet", "Populatie"]].groupby(by="Judet").sum()
    s_cerinta3 = df_industria_a_jud["Total"] / df_industria_a_jud["Populatie"]
    s_cerinta3.name = "Pondere"
    s_cerinta3.sort_values(ascending=False).to_csv("data_out/Cerinta3.csv")

    # 4
    s_cerinta4 = df_industria_a_jud[activitati].apply(
        func=lambda x: x.index[x.argmax()], axis=1)
    s_cerinta4.name = "Activitate"
    s_cerinta4.to_csv("data_out/Cerinta4.csv")

    # 5
    def calcul_medie(df: pd.DataFrame):
        x = df.values
        medii = average(x[:, :-1], axis=0, weights=x[:, -1])
        return pd.Series(medii, df.columns[:-1])

    df_coduri = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
    df_industria_a_loc_reg = df_industria_a_loc.merge(
        df_coduri, left_on="Judet", right_index=True)
    df_cerinta5 = df_industria_a_loc_reg[activitati + ["Populatie", "Regiune"]].groupby(by="Regiune").apply(
        func=lambda x: calcul_medie(x), include_groups=False)
    df_cerinta5.to_csv("data_out/Cerinta5.csv")

Note: localitatile cu total 0 dau NaN la cerinta 2 (0/0). Daca Judet din populatie e cu
majuscule si Coduri_Judete cu litere mici: df_industria_a_loc["Judet"] =
df_industria_a_loc["Judet"].str.lower() inainte de ultimul merge.


--------------------------------------------------------------------------------
D3. Industrie.csv (9 industrii) - aceleasi 5 cerinte  [RULAT]
--------------------------------------------------------------------------------
Date: Industrie.csv = Siruta, Localitate, Alimentara, Textila, Lemnului, ChimicaFarmaceutica,
      Metalurgica, ConstructiiMasini, CalculatoareElectronica, Mobila, Energetica.
      (valorile sunt sume de bani - cifra de afaceri, nu numar de firme).
Codul este cel de la D2 cu "Industrie.csv" in loc de "IndustriaAlimentara.csv" si cu linia:
      df_populatie["Judet"] = df_populatie["Judet"].str.lower()     # AB -> ab
(PopulatieLocalitati are aici judetele cu majuscule, Coduri_Judete cu litere mici.)
Rezultate: cerinta 1 = 2317 localitati; cerinta 3: ag, b, tm in frunte; 8 regiuni la cerinta 5.


--------------------------------------------------------------------------------
D4. Industrie.csv - cerinte lucrate de student (cifra de afaceri)
--------------------------------------------------------------------------------
Cerinte (extrase):
 1. Output1.csv: cifra de afaceri totala pe localitate (suma pe toate activitatile), in ordinea
    din fisier.
 2. Output2.csv: cifra de afaceri pe locuitor, descrescator.
    Coloane: Siruta, Localitate, CF/Loc.
 3. Output3.csv: activitatea dominanta pe localitate (doar localitatile cu activitate).

Solutie [partea cu iloc / sum(axis=1) / merge: RULATA conceptual; codul exact: NERULAT]:

    df = pd.read_csv("data_in/Industrie.csv", index_col=0)
    pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)

    # 1
    s = df.iloc[:, 1:].sum(axis=1)                     # coloanele numerice, suma pe rand
    c1 = df[["Localitate"]].copy()
    c1["Cifra de afaceri"] = s
    c1.to_csv("Output1.csv")

    # 2
    c2 = df[["Localitate"]].copy()
    c2["CF/Loc"] = s / pop["Populatie"]                # aliniere dupa Siruta
    c2 = c2.sort_values(by="CF/Loc", ascending=False)
    c2.to_csv("Output2.csv")

    # 3
    filtrate = df.iloc[:, 1:].sum(axis=1) > 0
    df_f = df[filtrate]
    c3 = df_f[["Localitate"]].copy()
    c3["Activitate"] = df_f.iloc[:, 1:].idxmax(axis=1)
    c3.to_csv("Output3.csv")


--------------------------------------------------------------------------------
D5. INNOPTARI.csv (6 cerinte, cu pivot)  [cerintele 1-4: cod lucrat de student;
    5 si 6 rulate pe un set cu aceeasi structura (Firme.csv)]
--------------------------------------------------------------------------------
Date: Innoptari.csv (format lung) = Siruta, Ani ("Anul 2001"...), Valoare (nr. innoptari).
      PopulatieLocalitati.csv, Coduri_Judete.csv.
Cerinte:
 1. Cerinta1.csv: innoptarile pe localitate, fiecare an o coloana, antetul = anul in cifre.
 2. Cerinta2.csv: localitatile cu innoptari in toti anii (aceeasi structura ca la 1).
 3. Cerinta3.csv: pentru fiecare localitate, anul cu cele mai multe innoptari
    (Siruta, Localitate, Anul).
 4. Cerinta4.csv: totalul innoptarilor la 1000 de locuitori pe localitate
    (Siruta, Localitate, Innoptari_1000).
 5. Cerinta5.csv: innoptari la 1000 de locuitori, pe fiecare an, pe judet (rotunjit 2 zecimale).
 6. Cerinta6.csv: coeficientii de variatie pe regiune, pe ani, pornind de la valorile pe localitate.

Solutie:

    import pandas as pd
    import numpy as np

    # Cerinta 1
    df = pd.read_csv("data_in/Innoptari.csv")
    df["Ani"] = df["Ani"].str.replace("Anul ", "").astype(int)
    c1 = df.pivot_table(index="Siruta", columns="Ani", values="Valoare")
    c1.to_csv("Cerinta1.csv")
    anii = list(c1.columns)

    # Cerinta 2
    c2 = c1[c1.notna().all(axis=1)]
    c2.to_csv("Cerinta2.csv")

    # Cerinta 3
    pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)     # index_col=0 OBLIGATORIU
    s3 = c1.idxmax(axis=1)                                                # anul = numele coloanei
    s3.name = "Anul"
    c3 = pop[["Localitate"]].merge(s3, left_index=True, right_index=True)
    c3.index.name = "Siruta"
    c3.to_csv("Cerinta3.csv")

    # Cerinta 4
    suma = c1.sum(axis=1) * 1000 / pop["Populatie"]
    suma.name = "Innoptari_1000"
    c4 = pop[["Localitate"]].merge(suma, left_index=True, right_index=True)
    c4 = c4[c4.notna().all(axis=1)]
    c4.to_csv("Cerinta4.csv")

    # Cerinta 5
    m = c1.merge(pop[["Judet", "Populatie"]], left_index=True, right_index=True)
    jud = m.groupby("Judet").sum()
    c5 = jud.drop(columns="Populatie").mul(1000).div(jud["Populatie"], axis=0)
    c5.round(2).to_csv("Cerinta5.csv")

    # Cerinta 6
    reg = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
    pop_l = pop.copy()
    pop_l["Judet"] = pop_l["Judet"].str.lower()
    mr = c1.merge(pop_l[["Judet"]], left_index=True, right_index=True)
    mr = mr.merge(reg["Regiune"], left_on="Judet", right_index=True)
    g = mr.groupby("Regiune")[anii]
    c6 = g.std() / g.mean()
    c6.to_csv("Cerinta6.csv")

Cerinta 2: "date in toti anii" = fara NaN. Daca enuntul cere si > 0:
    c1[(c1.notna() & (c1 > 0)).all(axis=1)]


--------------------------------------------------------------------------------
D6. TEST GENERAT "AGRICULTURA" (stil S1_1085)  [RULAT]
--------------------------------------------------------------------------------
Date: Agricultura.csv = Siruta, DenLocalitate, NrExploatatii, SuprafataHa, ProductieTone,
      Subventii, Cheltuieli. PopulatieLocalitati.csv (Judet cu MAJUSCULE),
      Coduri_Judete.csv (indicativ cu litere MICI).
Cerinte:
 1. (2p) Output1.csv: randament = productie / suprafata, doar unde suprafata > 0,
    descrescator, 3 zecimale. Coloane: Siruta, DenLocalitate, Randament.
 2. (2p) Output2.csv: exploatatii la 1000 de locuitori pe REGIUNE, descrescator.
    Coloane: Regiune, Densitate.
 3. (2p) Output3.csv: pe judet, localitatea cu cea mai mare productie pe locuitor.
 4. (3p) Output4.csv: media ponderata (pondere populatia) a celor 5 indicatori pe judet,
    3 zecimale.

Solutie:

    import pandas as pd
    import numpy as np

    df_agri = pd.read_csv("data_in/Agricultura.csv", index_col=0)
    df_pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
    df_reg = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)

    # Cerinta 1
    df_ag = df_agri[df_agri["SuprafataHa"] > 0].copy()
    df_ag["Randament"] = df_ag["ProductieTone"] / df_ag["SuprafataHa"]
    df_c1 = df_ag[["DenLocalitate", "Randament"]].sort_values(by="Randament", ascending=False)
    df_c1.round(3).to_csv("data_out/Output1.csv")

    # Cerinta 2 (capcana: majuscule vs litere mici)
    df_reg.index = df_reg.index.str.upper()
    df_loc = df_agri.merge(df_pop[["Judet", "Populatie"]], left_index=True, right_index=True)
    df_loc_reg = df_loc.merge(df_reg["Regiune"], left_on="Judet", right_index=True)
    df_regiuni = df_loc_reg[["NrExploatatii", "Populatie", "Regiune"]].groupby(by="Regiune").sum()
    s_c2 = df_regiuni["NrExploatatii"] * 1000 / df_regiuni["Populatie"]
    s_c2.name = "Densitate"
    s_c2.sort_values(ascending=False).to_csv("data_out/Output2.csv")

    # Cerinta 3
    df_loc["Productie/loc"] = df_loc["ProductieTone"] / df_loc["Populatie"]
    s_c3 = (df_loc[["DenLocalitate", "Judet", "Productie/loc"]]
            .groupby(by="Judet")
            .apply(lambda g: g["DenLocalitate"].iloc[g["Productie/loc"].argmax()], include_groups=False))
    s_c3.name = "Localitate"
    s_c3.to_csv("data_out/Output3.csv")

    # Cerinta 4
    indicatori = ["NrExploatatii", "SuprafataHa", "ProductieTone", "Subventii", "Cheltuieli"]
    df_c4 = (df_loc[indicatori + ["Judet", "Populatie"]]
             .groupby(by="Judet")
             .apply(lambda x: x[indicatori].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
                    include_groups=False))
    df_c4.round(3).to_csv("data_out/Output4.csv")

Rezultate de control: Output1 = 2972 randuri, Output2 = 8, Output3 = 42, Output4 = 42.


--------------------------------------------------------------------------------
D7. TEST GENERAT "FIRME PE ANI" (format lung, 8 cerinte)  [RULAT]
--------------------------------------------------------------------------------
Date: Firme.csv = Siruta, Ani ("Anul 2010".."Anul 2017"), Valoare (nr. firme active;
      pentru unele localitati lipsesc ani). Populatie (Judet MAJUSCULE), Coduri_Judete (litere mici).
Cerinte: 1 pivot; 2 localitati fara ani lipsa; 3 anul cu maximul; 4 firme la 1000 locuitori
 pe localitate; 5 firme la 1000 locuitori pe an, pe judet (2 zecimale); 6 coeficient de variatie
 pe regiune si an; 7 total firme pe an; 8 media ponderata (populatie) pe regiune si an, doar
 pentru localitatile din cerinta 2 (3 zecimale).
Cerintele 1-6 sunt ca la D5. Restul:

    # Cerinta 7
    s7 = c1.sum()                      # suma pe coloane = total pe an
    s7.name = "Total"
    s7.index.name = "Anul"
    s7.to_csv("Cerinta7.csv")

    # Cerinta 8
    m2 = c2.merge(pop_l[["Judet", "Populatie"]], left_index=True, right_index=True)
    m2 = m2.merge(reg["Regiune"], left_on="Judet", right_index=True)
    c8 = m2[anii + ["Populatie", "Regiune"]].groupby(by="Regiune").apply(
        lambda x: x[anii].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
        include_groups=False)
    c8.round(3).to_csv("Cerinta8.csv")


================================================================================
E. METODE SUPLIMENTARE DIN SEMINAR
================================================================================

--- E1. Seminar 1: natalitate (pivot, NaN, covarianta, corelatie, standardizare) ---
    import sys
    import pandas as pd
    import numpy as np

    t = pd.read_csv("data_in/Natalitate_Ro.csv")     # Judete, Localitati, Ani, UM, Valoare
    df = t.pivot_table(index="Judete", columns="Ani", values="Valoare")
    variabile = list(df)
    x = df[variabile].values

    def nan_replace(x):
        y = x.copy()
        k = np.where(np.isnan(y))
        y[k] = np.nanmean(y[:, k[1]], axis=0)        # NaN -> media coloanei
        return y

    def standardize(x, scal=True, ddof=0):
        x_ = x - np.mean(x, axis=0)
        if scal:
            x_ = x_ / np.std(x_, axis=0, ddof=ddof)
        return x_

    x = nan_replace(x)
    v = np.cov(x, rowvar=False)                      # covarianta intre coloane (ani)
    r = np.corrcoef(x, rowvar=False)                 # corelatii intre coloane
    pd.DataFrame(v, variabile, variabile).to_csv("data_out/V.csv")
    pd.DataFrame(r, variabile, variabile).to_csv("data_out/R.csv")
    pd.DataFrame(standardize(x), df.index, variabile).to_csv("data_out/x_std.csv")
  - rowvar=False: coloanele sunt variabilele.
  - np.std are ddof=0 implicit; np.cov are ddof=1. De aceea standardize are parametrul ddof.

--- E2. Seminar 2: etnii (NaN in DataFrame, sume pe judet/regiune, procente, indice) ---
    from pandas.api.types import is_numeric_dtype

    def nan_replace_df(df):
        for c in df.columns:
            if df[c].isna().any():
                if is_numeric_dtype(df[c]):
                    df.fillna({c: df[c].mean()}, inplace=True)       # numeric: media
                else:
                    df.fillna({c: df[c].mode()[0]}, inplace=True)    # text: valoarea cea mai frecventa

    df = pd.read_csv("data_in/Ethnicity.csv", index_col=0)           # Code, City, Romanian, Hungarians, ...
    nan_replace_df(df)
    etnii = list(df)[1:]
    df_coduri_loc = pd.read_csv("data_in/Coduri_Localitati.csv", index_col=0)    # City, County
    df_etnii_loc = df.merge(df_coduri_loc, left_index=True, right_index=True)
    df_etnii_jud = df_etnii_loc[etnii + ["County"]].groupby(by="County").sum()   # pe judet
    df_coduri_jud = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
    df_etnii_jud_ = df_etnii_jud.merge(df_coduri_jud, left_index=True, right_on="IndicativJudet")
    df_etnii_reg = df_etnii_jud_[etnii + ["Regiune"]].groupby(by="Regiune").sum()  # pe regiune

    # procente pe rand (fiecare etnie in total pe localitate / judet)
    df_etnii_loc_p = df[etnii].apply(func=lambda x: x * 100 / x.sum(), axis=1)
    df_etnii_jud_p = df_etnii_jud[etnii].apply(func=lambda x: x * 100 / x.sum(), axis=1)

    # indicele de disimilaritate pe judet (calcul numpy)
    def disimilaritate(df):
        x = df.values
        tx = np.sum(x, axis=0)             # total pe etnie
        tx[tx == 0] = 1                    # evita impartirea la 0
        sx = np.sum(x, axis=1)             # total pe localitate
        r = (sx - x.T).T                   # restul populatiei din fiecare localitate
        tr = np.sum(r, axis=0)
        d = 0.5 * np.sum(np.abs(x / tx - r / tr), axis=0)
        return pd.Series(d, df.columns)

    df_dis = df_etnii_loc[etnii + ["County"]].groupby(by="County").apply(
        func=disimilaritate, include_groups=False)

--- E3. Alte fisiere de date disponibile (pentru exercitii noi) ---------------------
  Religious.csv      : Code, City, Orthodox, Roman_Catholic, Reformed, ... (22 religii pe localitate)
  Ethnicity.csv      : Code, City, Romanian, Hungarians, Romany, ... (22 etnii pe localitate)
  prezenta_vot.csv   : Siruta, Localitate, Mediu (U/R), Votanti_LP, Votanti_LS, LP, LS, LSC, UM, LT,
                       Barbati_18-24 ... Barbati_65_, Femei_18-24 ... Femei_65_
  Teritorial_2022.csv: 42 judete x 35 indicatori (RN, RM, Emigranti, PIB, Export, ...), cu cateva
                       valori lipsa (VolumeB - Calarasi, SalariatiC - Caras-Severin, PIB - Mehedinti).
  Coduri_Regiuni.csv : Regiune, MacroRegiune (8 regiuni).


================================================================================
F. LISTA DE VERIFICARE INAINTE SA PREDAI UN SUBIECT
================================================================================
[ ] Fisierele sunt citite cu index_col=0 (inclusiv PopulatieLocalitati.csv).
[ ] Calea e corecta ("data_in/..."), iar folderul data_out/ exista.
[ ] Dupa fiecare merge: .shape are 3181 randuri (sau numarul asteptat).
[ ] Un rand cunoscut e corect: Siruta 1017 = Municipiul Alba Iulia.
[ ] Antetul fiecarei coloane e identic cu exemplul din enunt.
[ ] Sortarea e asignata (c = c.sort_values(...)) si e cea ceruta (descrescator).
[ ] Rotunjirea e facuta doar cand e ceruta, doar la salvare.
[ ] Indicativele de judet au aceeasi forma (majuscule/litere mici) in ambele tabele.
[ ] Randurile cu 0 / NaN / inf au fost tratate cum cere enuntul.
[ ] Fiecare cerinta scrie in fisierul cu numele cerut (Output1.csv, Cerinta1.csv, ...).

--- SFARSIT GHID ---
```

# Anexa B. Codul sursa complet

Fiecare fisier .py din repo, in ordinea: seminar1, seminar2, seminar3, completari, subiecte, referinta.
Fisierele sunt reproduse exact asa cum sunt in repo.

## B.1 seminar1/grupa_1075/functii.py

```python
import numpy as np
import pandas as pd


# Inlocuire valori lipsa cu media pe coloana
def nan_replace(x:np.ndarray):
    x = x.copy()
    k = np.where(np.isnan(x))
    x[k] = np.nanmean(x[:,k[1]], axis=0)
    return x

# Centrare/Standardizare
def standardizare(x:np.ndarray,scal=True,nlib=0):
    x_ = x - np.mean(x,axis=0)
    if scal:
        x_ = x_ / np.std(x_,axis=0,ddof=nlib)
    return x_

def tabelare_salvare_matrice(
        x:np.ndarray,
        index_linie,
        index_coloana,
        nume_index,
        nume_fisier=None
        ):
    df = pd.DataFrame(x,
                      index=index_linie,
                      columns=index_coloana)
    df.index.name=nume_index
    if nume_fisier is not None:
        df.to_csv("data_out/"+nume_fisier)

def calcul_corelatii_covariante(x:np.ndarray,y:np.ndarray):
    clase = np.unique(y)
    q = len(clase)
    m = x.shape[1]
    r = np.empty((q,m,m))
    v = np.empty((q,m,m))
    for i in range(q):
        z = x[y==clase[i],:]
        r[i] = np.corrcoef(z,rowvar=False)
        v[i] = np.cov(z,rowvar=False)
    return r,v,clase
```

## B.2 seminar1/grupa_1075/main.py

```python
import sys

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from functii import nan_replace, standardizare, tabelare_salvare_matrice, calcul_corelatii_covariante

np.set_printoptions(precision=3, suppress=True,threshold=sys.maxsize)

df = pd.read_csv("data_in/Teritorial_2022.csv", index_col=0)
variabile = list(df)[3:]
x = df[variabile].values
# print(x,type(x),sep="\n")
# Inlocuire valori lipsa
x = nan_replace(x)
# print(x)

x_std = standardizare(x)
x_c = standardizare(x,scal=False)
tabelare_salvare_matrice(x_std,df.index,variabile,df.index.name,"x_std.csv")
tabelare_salvare_matrice(x_c,df.index,variabile,df.index.name,"x_c.csv")

# std = StandardScaler()
# x_std_ = std.fit_transform(x)
# print(x_std-x_std_)

V = np.cov(x,rowvar=False)
tabelare_salvare_matrice(V,variabile,variabile,"Indicatori","V.csv")
R = np.corrcoef(x,rowvar=False)
tabelare_salvare_matrice(R,variabile,variabile,"Indicatori","R.csv")
r,v,clase = calcul_corelatii_covariante(x,df["Regiunea"].values)
for i in zip(clase,r,v):
    tabelare_salvare_matrice(i[1],variabile,variabile,"Indicatori","R_"+i[0]+".csv")
    tabelare_salvare_matrice(i[2],variabile,variabile,"Indicatori","V_"+i[0]+".csv")
```

## B.3 seminar1/grupa_1077/functii.py

```python
import numpy as np
import pandas as pd
from scipy.spatial import distance

def nan_replace(x:np.ndarray):
    x = x.copy()
    k = np.where(np.isnan(x))
    x[k] = np.nanmean(x[:,k[1]], axis=0)
    return x

def tabelare_salvare_matrice(
        x: np.ndarray,
        nume_linii,
        nume_coloane,
        nume_index,
        nume_fisier_output=None
):
    df = pd.DataFrame(x,nume_linii,nume_coloane)
    df.index.name = nume_index
    if nume_fisier_output is not None:
        df.to_csv("data_out/"+nume_fisier_output)
    return df

def calcul_inertii(x:np.ndarray,y:np.ndarray):
    m = x.shape[1]
    centru = np.mean(x,axis=0)
    distante = distance.cdist(x,centru.reshape(1,-1),metric='euclidean')
    inertia = np.sum(distante**2)
    inertii = {}
    grupe = np.unique(y)
    q = len(grupe)
    centrii = np.empty((q,m))
    for k in range(q):
        x_ = x[y==grupe[k],:]
        centru_k = np.mean(x_,axis=0)
        centrii[k,:] = centru_k
        distante_k = distance.cdist(x,centru_k.reshape(1,-1),metric='euclidean')
        inertii[grupe[k]] = (np.sum(distante_k**2),centru_k)
    distante_centrii = distance.cdist(centrii,centrii,metric='euclidean')
    return inertia,inertii,distante_centrii
```

## B.4 seminar1/grupa_1077/main.py

```python
import sys

import numpy as np
import pandas as pd

from functii import nan_replace, tabelare_salvare_matrice, calcul_inertii
from scipy.spatial import distance

np.set_printoptions(precision=3, suppress=True, threshold=sys.maxsize)

df = pd.read_csv("data_in/Teritorial_2022.csv", index_col=0)
variabile_observate = list(df)[3:]
x = df[variabile_observate].values

# print(x,type(x),sep="\n")
x = nan_replace(x)
# print(x)
d_euclid = distance.cdist(x, x, metric='euclidean')
d_mahalanobis = distance.cdist(x, x, metric='mahalanobis')

df_d_euclid=tabelare_salvare_matrice(
    d_euclid,
    df.index,
    df.index,
    df.index.name,
    "D_Euclid.csv"
)
df_d_mahalanobis=tabelare_salvare_matrice(
    d_mahalanobis,
    df.index,
    df.index,
    df.index.name,
    "D_Mahalanobis.csv"
)
inertia,inertii,distante_centrii = calcul_inertii(
    x,df["Regiunea"].values
)
print("Inertia generala:",inertia)
for ch in inertii:
    print("Regiunea",ch)
    print("Inertie:",inertii[ch][0])
    print("Centru de grupa:")
    print(inertii[ch][1])
print("Distante intre grupe:")
print(distante_centrii)
tabelare_salvare_matrice(
    distante_centrii,
    list(inertii),
    list(inertii),
    "Regiuni",
    "DistanteRegiuni.csv"
)
```

## B.5 seminar1/grupa_1085/functii.py

```python
import numpy as np
from scipy.stats import kstest,norm,shapiro,anderson,chi2

def nan_replace(x:np.ndarray):
    x = x.copy()
    k = np.where(np.isnan(x))
    x[k] = np.nanmean(x[:,k[1]], axis=0)
    return x

# Functie pentru aplicarea testelor de concordanta
# Primeste ca parametru matricea testata
def teste(x:np.ndarray,prag=0.05):
    # Preiau numarul de coloane
    m = x.shape[1]
    t = np.empty((m,4), dtype=bool)
    for i in range(m):
        print("Variabila",i)
        # Kolmogorov
        t_ks = kstest(x[:,i],norm.cdf,args=(np.mean(x[:,i]),np.std(x[:,i])))
        print(t_ks[0],t_ks[1])
        t[i,0] = t_ks[1]>prag
        # Shapiro
        t_sh = shapiro(x[:,i])
        print(t_sh[0],t_sh[1])
        t[i,1]=t_sh[1]>prag
        # Anderson
        t_an = anderson(x[:,i],dist="norm",method="interpolate")
        print(t_an[0],t_an[1])
        t[i,2]=t_an[1]>prag
        # Chi2
        p_value_chi2 = test_chi2(x[:,i])
        print(p_value_chi2)
        t[i,3] = p_value_chi2<prag
    return t

def test_chi2(x:np.ndarray):
    n = len(x)
    media = np.mean(x)
    std = np.std(x)
    f,l = np.histogram(x,bins="sturges")
    m = len(f)
    fe = n*(norm.cdf(l[1:],media,std)-norm.cdf(l[:m],media,std))
    k = fe!=0
    f_ = f[k]
    fe_ = fe[k]
    stts = np.sum((f_-fe_)**2/fe_)
    pvalue = chi2.cdf(stts,m-1)
    return pvalue
```

## B.6 seminar1/grupa_1085/main.py

```python
import sys

import numpy as np
import pandas as pd

from functii import nan_replace, teste

np.set_printoptions(suppress=True,precision=3,threshold=sys.maxsize)

df = pd.read_csv("data_in/Teritorial_2022.csv", index_col=0)
variabile = list(df)[3:]
# print(variabile)
x = df[variabile].values
# print(x)
# Inlocuire valori lipsa cu media
x = nan_replace(x)
# print(x)
# Aplicare teste de concordanta
t = teste(x)
print(t)
df_t = pd.DataFrame(t,variabile,["Kolmogorov-Smirnov","Shapiro","Anderson","Chi2"])
df_t.to_csv("data_out/Teste.csv")
```

## B.7 seminar1/grupa_1086/functii.py

```python
import numpy as np


def nan_replace(x:np.ndarray):
    y = x.copy()
    k = np.where(np.isnan(y))
    y[k] = np.nanmean(y[:, k[1]], axis=0)
    return y



def standardize(x:np.ndarray,scal=True,ddof=0):
    x_ = x - np.mean(x,axis=0)
    if scal:
        x_ = x_ / np.std(x_,axis=0,ddof=ddof)
    return x_
```

## B.8 seminar1/grupa_1086/main.py

```python
import sys

import pandas as pd
import numpy as np

from functii import nan_replace, standardize

np.set_printoptions(suppress=True,precision=3, threshold=sys.maxsize)

t = pd.read_csv("data_in/Natalitate_Ro.csv")
# print(type(t))
df = t.pivot_table(index="Judete", columns="Ani", values="Valoare")
variabile = list(df)
# Inlocuire valori lipsa
x = df[variabile].values
x = nan_replace(x)
# Calcul corelatii/covariante
v = np.cov(x, rowvar=False)
# print(v)
df_cov = pd.DataFrame(v,variabile,variabile)
df_cov.to_csv("data_out/V.csv")
r = np.corrcoef(x, rowvar=False)
df_r = pd.DataFrame(r,variabile,variabile)
df_r.to_csv("data_out/R.csv")

# Standardizare date
x_std = standardize(x)
df_x_std = pd.DataFrame(x_std,df.index,variabile)
df_x_std.to_csv("data_out/x_std.csv")
```

## B.9 seminar2/grupa_1073/functii.py

```python
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

def nan_replace_df(df: pd.DataFrame):
    for col in df.columns:
        if df[col].isna().any():
            if is_numeric_dtype(df[col]):
                df.fillna({col:df[col].mean()}, inplace=True)
            else:
                df.fillna({col:df[col].mode()[0]}, inplace=True)

def disimilaritate(df: pd.DataFrame):
    x = df.values
    tx = np.sum(x, axis=0)
    tx[tx==0]=1
    sx = np.sum(x,axis=1)
    r = (sx - x.T).T
    tr = np.sum(r,axis=0)
    d = 0.5*np.sum(np.abs(x/tx-r/tr),axis=0)
    return pd.Series(d,df.columns)
```

## B.10 seminar2/grupa_1073/main.py

```python
import pandas as pd

from functii import nan_replace_df

pd.set_option('display.max_columns', None)

df_etnii = pd.read_csv("data_in/Ethnicity.csv", index_col=0)
# print(df_etnii,type(df_etnii),sep="\n")
etnii = list(df_etnii.columns.values[1:])
# print(etnii)

nan_replace_df(df_etnii)

df_coduri_loc = pd.read_csv("data_in/Coduri_Localitati.csv", index_col=0)
df_etnii_loc = df_etnii.merge(df_coduri_loc, left_index=True, right_index=True)
# print(df_etnii_loc)
df_etnii_jud = df_etnii_loc[etnii+["County"]].groupby("County").sum()
df_etnii_jud.to_csv("data_out/Ethnicity_Jud.csv")

df_coduri_jud = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
df_etnii_jud_reg = df_etnii_jud[etnii].merge(
    df_coduri_jud[["IndicativJudet","Regiune"]],
    left_index=True, right_on="IndicativJudet")
df_etnii_reg = df_etnii_jud_reg.groupby(by="Regiune").sum()
df_etnii_reg.to_csv("data_out/Ethnicity_Reg.csv")

df_etnii_p = df_etnii[etnii].apply(func=lambda x:x*100/x.sum(), axis=1)
df_etnii_p.insert(0, "Localitate", df_etnii["City"])
df_etnii_p.to_csv("data_out/Ethnicity_P.csv")

# De calculat la nivel de judet si regiune
```

## B.11 seminar2/grupa_1075/functii.py

```python
import numpy as np
import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype
from scipy.stats import entropy


def nan_replace_df(df: pd.DataFrame):
    for col in df.columns:
        if df[col].isna().any():
            if is_numeric_dtype(df[col]):
                df.fillna({col:df[col].mean()}, inplace=True)
            else:
                df.fillna({col:df[col].mode()[0]}, inplace=True)

def shannon(df: pd.DataFrame):
    x = df.values
    tx = np.sum(x,axis=0)
    tx[tx==0] = 1
    p = x/tx
    e = entropy(p,axis=0)
    return pd.Series(e,index=df.columns)
```

## B.12 seminar2/grupa_1075/main.py

```python
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
```

## B.13 seminar2/grupa_1077/functii.py

```python
import numpy as np
import pandas as pd
from scipy.stats import entropy


def shannon(df:pd.DataFrame):
    x = df.values
    tx = np.sum(x, axis=0)
    p = x/tx
    e = entropy(p,axis=0)
    return pd.Series(e,df.columns)
```

## B.14 seminar2/grupa_1077/main.py

```python
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
```

## B.15 seminar2/grupa_1085/functii.py

```python
import numpy as np
import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype
from scipy.stats import entropy


def nan_replace_df(df: pd.DataFrame):
    for col in df.columns:
        if df[col].isna().any():
            if is_numeric_dtype(df[col]):
                df.fillna({col:df[col].mean()}, inplace=True)
            else:
                df.fillna({col:df[col].mode()[0]}, inplace=True)


def shannon(df: pd.DataFrame):
    x = df.values
    tx = np.sum(x, axis=0)
    tx[tx==0] = 1
    p = x/tx
    e = entropy(p,axis=0)
    return pd.Series(e,index=df.columns)
```

## B.16 seminar2/grupa_1085/main.py

```python
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
```

## B.17 seminar2/grupa_1086/functii.py

```python
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

def nan_replace_df(df: pd.DataFrame):
    for c in df.columns:
        if df[c].isna().any():
            if is_numeric_dtype(df[c]):
                df.fillna({c:df[c].mean()}, inplace=True)
            else:
                df.fillna({c:df[c].mode()[0]}, inplace=True)


def disimilaritate(df: pd.DataFrame):
    x = df.values
    tx = np.sum(x,axis=0)
    tx[tx==0] = 1
    sx = np.sum(x,axis=1)
    r = (sx - x.T).T
    tr = np.sum(r,axis=0)
    d = 0.5*np.sum( np.abs(x/tx-r/tr) ,axis=0)
    return pd.Series(d,df.columns)
```

## B.18 seminar2/grupa_1086/main.py

```python
import pandas as pd
pd.set_option('display.max_columns', None)

from functii import nan_replace_df, disimilaritate

df = pd.read_csv("data_in/Ethnicity.csv", index_col=0)
nan_replace_df(df)
# print(df)

etnii = list(df)[1:]

df_coduri_loc = pd.read_csv("data_in/Coduri_Localitati.csv", index_col=0)
df_etnii_loc = df.merge(df_coduri_loc,left_index=True,right_index=True)
# print(df_etnii_loc)

df_etnii_jud = df_etnii_loc[etnii+["County"]].groupby(by="County").sum()
# print(df_etnii_jud)
df_etnii_jud.to_csv("data_out/Etnii_jud.csv")

df_coduri_jud = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
df_etnii_jud_ = df_etnii_jud.merge(df_coduri_jud, left_index=True,right_on="IndicativJudet")
# print(df_etnii_jud_)
df_etnii_reg = df_etnii_jud_[etnii+["Regiune"]].groupby(by="Regiune").sum()
df_etnii_reg.to_csv("data_out/Etnii_reg.csv")

# Calcul procente
df_etnii_loc_p = df[etnii].apply(func=lambda x:x*100/x.sum(),axis=1)
df_etnii_loc_p.to_csv("data_out/Etnii_p.csv")

df_etnii_jud_p = df_etnii_jud[etnii].apply(func=lambda x:x*100/x.sum(),axis=1)
df_etnii_jud_p.to_csv("data_out/Etnii_jud_p.csv")

df_disimilaritate = df_etnii_loc[etnii+["County"]].groupby(by="County").apply(func=disimilaritate,include_groups=False)
print(df_disimilaritate)
```

## B.19 seminar3/grupa_1073/main.py

```python
import pandas as pd
from numpy.ma.extras import average


def calcul_medii(df:pd.DataFrame):
    x = df.values
    medii = average(x[:,:-1],axis=0,weights=x[:,-1])
    return pd.Series(medii,df.columns[:-1])

pd.set_option('display.max_columns', None)

df_industrie_alim = pd.read_csv("data_in/IndustriaAlimentara.csv", index_col=0)
activitati = list(df_industrie_alim.columns.values)[1:]

# 1
s_totaluri = df_industrie_alim[activitati].sum(axis=1)
# print(s_totaluri)
df_cerinta1 = df_industrie_alim[s_totaluri > 0]
df_cerinta1.to_csv("data_out/Cerinta1.csv")

# 2
df_industrie_alim["Totaluri"] = s_totaluri
df_cerinta2 = df_industrie_alim[activitati+["Totaluri"]].apply(
    func=lambda x:x[activitati]*100/x["Totaluri"],
    axis=1
)
df_cerinta2.insert(0,"Localitate",df_industrie_alim["Localitate"])
df_cerinta2.to_csv("data_out/Cerinta2.csv")

# 3
df_populatie = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
df_industrie_alim_loc = df_industrie_alim.merge(df_populatie,left_index=True,right_index=True)
# print(df_industrie_alim_loc.head())
df_industrie_alim_jud = df_industrie_alim_loc[activitati+["Totaluri","Judet","Populatie"]]\
    .groupby(by=["Judet"]).sum()
s_cerinta3 = df_industrie_alim_jud["Totaluri"]/df_industrie_alim_jud["Populatie"]
s_cerinta3.name="Totaluri"
s_cerinta3.sort_values(ascending=False).to_csv("data_out/Cerinta3.csv")

# 4
s_cerinta4 = df_industrie_alim_jud[activitati].apply(
    func=lambda x:x.index[x.argmax()],
    axis=1
)
s_cerinta4.name="Activitate"
s_cerinta4.to_csv("data_out/Cerinta4.csv")

# 5
df_coduri = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
df_industrie_alim_loc_reg = df_industrie_alim_loc.merge(
    df_coduri,
    left_on="Judet",
    right_index=True
)
# print(df_industrie_alim_loc_reg.head())
df_cerinta5 = df_industrie_alim_loc_reg[activitati+["Populatie","Regiune"]].groupby(by="Regiune").apply(
    func=calcul_medii,
    include_groups=False
)
# print(df_cerinta5)
df_cerinta5.to_csv("data_out/Cerinta5.csv")

# 6
s_totaluri_national = df_industrie_alim_jud[activitati+["Populatie"]].sum(axis=0)
print(s_totaluri_national)
```

## B.20 seminar3/grupa_1075/main.py

```python
import pandas as pd
from numpy.ma.extras import average


def calcul_medie(df:pd.DataFrame):
    x = df.values
    medii = average(x[:,:-1],axis=0,weights=x[:,-1])
    return pd.Series(medii,df.columns[:-1])


pd.set_option('display.max_columns', None)

df_industrie_alim = pd.read_csv("data_in/IndustriaAlimentara.csv", index_col=0)
activitati = list(df_industrie_alim.columns.values)[1:]


# 1
s_totaluri = df_industrie_alim[activitati].sum(axis=1)
# print(s_totaluri)
df_cerinta1 = df_industrie_alim[s_totaluri > 0]
df_cerinta1.to_csv("data_out/Cerinta1.csv")

# 2
df_industrie_alim["Total"] = s_totaluri
df_cerinta2 = df_industrie_alim[activitati].apply(
    func = lambda x: x/x.sum() ,
    axis = 1
)
df_cerinta2.insert(0,"Localitate",df_industrie_alim["Localitate"])
# print(df_cerinta2.head(3))
df_cerinta2.to_csv("data_out/Cerinta2.csv")

# 3
df_populatie = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
df_industrie_alim_loc = df_industrie_alim.merge(
    df_populatie[["Judet","Populatie"]],
    left_index=True,
    right_index=True)
s_cerinta3 = df_industrie_alim_loc["Total"]/df_industrie_alim_loc["Populatie"]
s_cerinta3.name = "Pondere"
s_cerinta3.round(5).to_csv("data_out/Cerinta3.csv")

# 4
df_industrie_alim_jud = df_industrie_alim_loc[activitati+["Judet","Populatie"]].groupby(by="Judet").sum()
# print(df_industrie_alim_jud.head(3))
s_cerinta4 = df_industrie_alim_jud[activitati].apply(
    lambda x:x.index[x.argmax()],
    axis = 1
)
s_cerinta4.name="Activitate"
s_cerinta4.to_csv("data_out/Cerinta4.csv")

# 5
df_coduri = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
df_industrie_alim_loc_reg = df_industrie_alim_loc.merge(
    df_coduri,
    left_on="Judet",
    right_index=True
)
# print(df_industrie_alim_loc_reg.head(3))
df_cerinta5 = df_industrie_alim_loc_reg[activitati+["Regiune","Populatie"]].groupby(by="Regiune").apply(
    func=calcul_medie,
    include_groups=False
)
df_cerinta5.to_csv("data_out/Cerinta5.csv")
```

## B.21 seminar3/grupa_1077/main.py

```python
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
```

## B.22 seminar3/grupa_1085/main.py

```python
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
```

## B.23 seminar3/grupa_1086/main.py

```python
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
```

## B.24 completari/seminar2_diversitate_segregare.py

```python
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
```

## B.25 completari/seminar3_industria_alimentara_complet.py

```python
# Seminar 3 - IndustriaAlimentara.csv: toate cele 6 cerinte, conform enuntului (Tema 2.4)
# Completeaza solutiile din seminar3/grupa_1073, grupa_1075, grupa_1086, unde:
#   - cerinta 2 trebuie sa dea procente (x100) si 0 (nu NaN) cand totalul e 0
#   - cerinta 3 trebuie sa fie pe JUDET, descrescator, cu antetul "Ponderi"
#   - cerinta 6 (indicii de localizare) lipseste
# Rulare:  python completari/seminar3_industria_alimentara_complet.py
from pathlib import Path

import numpy as np
import pandas as pd

RAD = Path(__file__).resolve().parent
DATE = RAD.parent / "seminar3" / "grupa_1086" / "data_in"
IES = RAD / "data_out" / "seminar3_industria_alimentara"
IES.mkdir(parents=True, exist_ok=True)

df_industrie = pd.read_csv(DATE / "IndustriaAlimentara.csv", index_col=0)
df_populatie = pd.read_csv(DATE / "PopulatieLocalitati.csv", index_col=0)
df_coduri = pd.read_csv(DATE / "Coduri_Judete.csv", index_col=0)   # index = IndicativJudet (3 coloane la Seminar 3)
activitati = list(df_industrie.columns.values)[1:]

# Cerinta 1 - localitati cu cel putin un angajat, aceleasi coloane ca fisierul initial
s_total = df_industrie[activitati].sum(axis=1)
df_industrie[s_total > 0].to_csv(IES / "Cerinta1.csv")

# Cerinta 2 - procent pe activitate in total pe localitate; total 0 -> procente 0
df_c2 = df_industrie[activitati].mul(100).div(s_total.replace(0, np.nan), axis=0).fillna(0)
df_c2.insert(0, "Localitate", df_industrie["Localitate"])
df_c2.to_csv(IES / "Cerinta2.csv")

# Cerinta 3 - judete sortate descrescator dupa (angajati industrie alimentara / populatie)
df_loc = df_industrie[activitati].merge(df_populatie[["Judet", "Populatie"]],
                                        left_index=True, right_index=True)
df_jud = df_loc.groupby(by="Judet").sum()
s_c3 = df_jud[activitati].sum(axis=1) / df_jud["Populatie"]
s_c3.name = "Ponderi"
s_c3.sort_values(ascending=False).to_csv(IES / "Cerinta3.csv")

# Cerinta 4 - activitatea dominanta pe judet
s_c4 = df_jud[activitati].idxmax(axis=1)
s_c4.name = "Activitate"
s_c4.to_csv(IES / "Cerinta4.csv")

# Cerinta 5 - media ponderata (pondere = populatia localitatii) pe regiune
df_loc_reg = df_loc.merge(df_coduri["Regiune"], left_on="Judet", right_index=True)
df_c5 = df_loc_reg[activitati + ["Populatie", "Regiune"]].groupby(by="Regiune").apply(
    lambda x: x[activitati].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
    include_groups=False)
df_c5.to_csv(IES / "Cerinta5.csv")

# Cerinta 6 - indice de localizare = (pondere judet in activitate la nivel national)
#                                    / (pondere populatie judet in populatia tarii)
pondere_activitate = df_jud[activitati] / df_jud[activitati].sum()
pondere_populatie = df_jud["Populatie"] / df_jud["Populatie"].sum()
df_c6 = pondere_activitate.div(pondere_populatie, axis=0)
df_c6.to_csv(IES / "Cerinta6.csv")
print("Gata:", IES)
```

## B.26 subiecte/industrie_cifra_afaceri/main_cerinte_seminar.py

```python
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
```

## B.27 subiecte/industrie_cifra_afaceri/main_cerinte_student.py

```python
# Industrie.csv - cerinte lucrate de student (NERULAT pe date reale)
import pandas as pd

df = pd.read_csv("data_in/Industrie.csv", index_col=0)
pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)

# 1 - cifra de afaceri totala pe localitate, in ordinea din fisier
s = df.iloc[:, 1:].sum(axis=1)
c1 = df[["Localitate"]].copy()
c1["Cifra de afaceri"] = s
c1.to_csv("data_out/Output1.csv")

# 2 - cifra de afaceri pe locuitor, descrescator
c2 = df[["Localitate"]].copy()
c2["CF/Loc"] = s / pop["Populatie"]                # aliniere dupa Siruta
c2 = c2.sort_values(by="CF/Loc", ascending=False)
c2.to_csv("data_out/Output2.csv")

# 3 - activitatea dominanta pe localitate (doar localitatile cu activitate)
filtrate = df.iloc[:, 1:].sum(axis=1) > 0
df_f = df[filtrate]
c3 = df_f[["Localitate"]].copy()
c3["Activitate"] = df_f.iloc[:, 1:].idxmax(axis=1)
c3.to_csv("data_out/Output3.csv")
```

## B.28 subiecte/innoptari/main.py

```python
# Innoptari.csv - format lung -> pivot (6 cerinte)
import pandas as pd
import numpy as np

# Cerinta 1
df = pd.read_csv("data_in/Innoptari.csv")
df["Ani"] = df["Ani"].str.replace("Anul ", "").astype(int)
c1 = df.pivot_table(index="Siruta", columns="Ani", values="Valoare")
c1.to_csv("data_out/Cerinta1.csv")
anii = list(c1.columns)

# Cerinta 2 - localitati cu date in toti anii (fara NaN)
c2 = c1[c1.notna().all(axis=1)]
c2.to_csv("data_out/Cerinta2.csv")

# Cerinta 3 - anul cu cele mai multe innoptari
pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)     # index_col=0 OBLIGATORIU
s3 = c1.idxmax(axis=1)
s3.name = "Anul"
c3 = pop[["Localitate"]].merge(s3, left_index=True, right_index=True)
c3.index.name = "Siruta"
c3.to_csv("data_out/Cerinta3.csv")

# Cerinta 4 - innoptari la 1000 de locuitori
suma = c1.sum(axis=1) * 1000 / pop["Populatie"]
suma.name = "Innoptari_1000"
c4 = pop[["Localitate"]].merge(suma, left_index=True, right_index=True)
c4 = c4[c4.notna().all(axis=1)]
c4.to_csv("data_out/Cerinta4.csv")

# Cerinta 5 - la 1000 de locuitori, pe ani, pe judet
m = c1.merge(pop[["Judet", "Populatie"]], left_index=True, right_index=True)
jud = m.groupby("Judet").sum()
c5 = jud.drop(columns="Populatie").mul(1000).div(jud["Populatie"], axis=0)
c5.round(2).to_csv("data_out/Cerinta5.csv")

# Cerinta 6 - coeficient de variatie pe regiune, pe ani
reg = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
pop_l = pop.copy()
pop_l["Judet"] = pop_l["Judet"].str.lower()
mr = c1.merge(pop_l[["Judet"]], left_index=True, right_index=True)
mr = mr.merge(reg["Regiune"], left_on="Judet", right_index=True)
g = mr.groupby("Regiune")[anii]
c6 = g.std() / g.mean()
c6.to_csv("data_out/Cerinta6.csv")
```

## B.29 subiecte/s1_1085_firme_2014/main.py

```python
# Subiect S1_1085 - firme 2014 (12014.csv)
import pandas as pd
import numpy as np

df_firme = pd.read_csv("data_in/12014.csv", index_col=0)
df_pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)

# Cerinta 1
df_sal = df_firme[df_firme["NrSal"] > 0]
c1 = df_sal[["DenLocalitate"]].copy()
c1["Raport CA/NrSal"] = df_sal["TotalCifraAfaceri"] / df_sal["NrSal"]
c1 = c1.sort_values(by="Raport CA/NrSal", ascending=False)
c1.round(3).to_csv("data_out/Output1.csv")

# Cerinta 2
df_loc = df_firme.merge(df_pop[["Judet", "Populatie"]], left_index=True, right_index=True)
df_jud = df_loc[["NrSal", "Judet", "Populatie"]].groupby(by="Judet").sum()
s2 = df_jud["NrSal"] * 1000 / df_jud["Populatie"]
s2.name = "Rata Ocuparii"
s2.sort_values(ascending=False).to_csv("data_out/Output2.csv")

# Cerinta 3
df_loc["Profit/loc"] = df_loc["TotalProfit"] / df_loc["Populatie"]
s3 = (df_loc[["DenLocalitate", "Judet", "Profit/loc"]]
      .groupby(by="Judet")
      .apply(lambda g: g["DenLocalitate"].iloc[g["Profit/loc"].argmax()], include_groups=False))
s3.name = "Localitate"
s3.to_csv("data_out/Output3.csv")

# Cerinta 4
indicatori = ["NrFirme", "NrSal", "TotalCifraAfaceri", "TotalProfit", "TotalPierdere"]
c4 = (df_loc[indicatori + ["Judet", "Populatie"]]
      .groupby(by="Judet")
      .apply(lambda x: x[indicatori].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
             include_groups=False))
c4.round(3).to_csv("data_out/Output4.csv")

# Control: Output1 = 2749 randuri; Output2/3/4 = 42 randuri
```

## B.30 subiecte/test_agricultura/main.py

```python
# Test generat "Agricultura" (stil S1_1085)
import pandas as pd
import numpy as np

df_agri = pd.read_csv("data_in/Agricultura.csv", index_col=0)
df_pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
df_reg = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)

# Cerinta 1
df_ag = df_agri[df_agri["SuprafataHa"] > 0].copy()
df_ag["Randament"] = df_ag["ProductieTone"] / df_ag["SuprafataHa"]
df_c1 = df_ag[["DenLocalitate", "Randament"]].sort_values(by="Randament", ascending=False)
df_c1.round(3).to_csv("data_out/Output1.csv")

# Cerinta 2 (capcana: majuscule vs litere mici)
df_reg.index = df_reg.index.str.upper()
df_loc = df_agri.merge(df_pop[["Judet", "Populatie"]], left_index=True, right_index=True)
df_loc_reg = df_loc.merge(df_reg["Regiune"], left_on="Judet", right_index=True)
df_regiuni = df_loc_reg[["NrExploatatii", "Populatie", "Regiune"]].groupby(by="Regiune").sum()
s_c2 = df_regiuni["NrExploatatii"] * 1000 / df_regiuni["Populatie"]
s_c2.name = "Densitate"
s_c2.sort_values(ascending=False).to_csv("data_out/Output2.csv")

# Cerinta 3
df_loc["Productie/loc"] = df_loc["ProductieTone"] / df_loc["Populatie"]
s_c3 = (df_loc[["DenLocalitate", "Judet", "Productie/loc"]]
        .groupby(by="Judet")
        .apply(lambda g: g["DenLocalitate"].iloc[g["Productie/loc"].argmax()], include_groups=False))
s_c3.name = "Localitate"
s_c3.to_csv("data_out/Output3.csv")

# Cerinta 4
indicatori = ["NrExploatatii", "SuprafataHa", "ProductieTone", "Subventii", "Cheltuieli"]
df_c4 = (df_loc[indicatori + ["Judet", "Populatie"]]
         .groupby(by="Judet")
         .apply(lambda x: x[indicatori].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
                include_groups=False))
df_c4.round(3).to_csv("data_out/Output4.csv")

# Control: Output1 = 2972 randuri, Output2 = 8, Output3 = 42, Output4 = 42
```

## B.31 subiecte/test_firme_pe_ani/main.py

```python
# Test generat "Firme pe ani" (format lung, 8 cerinte)
import pandas as pd
import numpy as np

# Cerinta 1
df = pd.read_csv("data_in/Firme.csv")
df["Ani"] = df["Ani"].str.replace("Anul ", "").astype(int)
c1 = df.pivot_table(index="Siruta", columns="Ani", values="Valoare")
c1.to_csv("data_out/Cerinta1.csv")
anii = list(c1.columns)

# Cerinta 2
c2 = c1[c1.notna().all(axis=1)]
c2.to_csv("data_out/Cerinta2.csv")

# Cerinta 3
pop = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)
s3 = c1.idxmax(axis=1)
s3.name = "Anul"
c3 = pop[["Localitate"]].merge(s3, left_index=True, right_index=True)
c3.index.name = "Siruta"
c3.to_csv("data_out/Cerinta3.csv")

# Cerinta 4
suma = c1.sum(axis=1) * 1000 / pop["Populatie"]
suma.name = "Firme_1000"
c4 = pop[["Localitate"]].merge(suma, left_index=True, right_index=True)
c4 = c4[c4.notna().all(axis=1)]
c4.to_csv("data_out/Cerinta4.csv")

# Cerinta 5
m = c1.merge(pop[["Judet", "Populatie"]], left_index=True, right_index=True)
jud = m.groupby("Judet").sum()
c5 = jud.drop(columns="Populatie").mul(1000).div(jud["Populatie"], axis=0)
c5.round(2).to_csv("data_out/Cerinta5.csv")

# Cerinta 6
reg = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
pop_l = pop.copy()
pop_l["Judet"] = pop_l["Judet"].str.lower()
mr = c1.merge(pop_l[["Judet"]], left_index=True, right_index=True)
mr = mr.merge(reg["Regiune"], left_on="Judet", right_index=True)
g = mr.groupby("Regiune")[anii]
c6 = g.std() / g.mean()
c6.to_csv("data_out/Cerinta6.csv")

# Cerinta 7 - total pe an
s7 = c1.sum()
s7.name = "Total"
s7.index.name = "Anul"
s7.to_csv("data_out/Cerinta7.csv")

# Cerinta 8 - media ponderata pe regiune si an, doar localitatile din cerinta 2
m2 = c2.merge(pop_l[["Judet", "Populatie"]], left_index=True, right_index=True)
m2 = m2.merge(reg["Regiune"], left_on="Judet", right_index=True)
c8 = m2[anii + ["Populatie", "Regiune"]].groupby(by="Regiune").apply(
    lambda x: x[anii].multiply(x["Populatie"], axis=0).sum() / x["Populatie"].sum(),
    include_groups=False)
c8.round(3).to_csv("data_out/Cerinta8.csv")
```

## B.32 referinta/seminar1_natalitate_ghid/main.py

```python
# Seminar 1 - Natalitate: pivot, NaN, covarianta, corelatie, standardizare
import pandas as pd
import numpy as np

t = pd.read_csv("data_in/Natalitate_Ro.csv")     # Judete, Localitati, Ani, UM, Valoare
df = t.pivot_table(index="Judete", columns="Ani", values="Valoare")
variabile = list(df)
x = df[variabile].values


def nan_replace(x):
    y = x.copy()
    k = np.where(np.isnan(y))
    y[k] = np.nanmean(y[:, k[1]], axis=0)        # NaN -> media coloanei
    return y


def standardize(x, scal=True, ddof=0):
    x_ = x - np.mean(x, axis=0)
    if scal:
        x_ = x_ / np.std(x_, axis=0, ddof=ddof)
    return x_


x = nan_replace(x)
v = np.cov(x, rowvar=False)                      # covarianta intre coloane (ani)
r = np.corrcoef(x, rowvar=False)                 # corelatii intre coloane
pd.DataFrame(v, variabile, variabile).to_csv("data_out/V.csv")
pd.DataFrame(r, variabile, variabile).to_csv("data_out/R.csv")
pd.DataFrame(standardize(x), df.index, variabile).to_csv("data_out/x_std.csv")
```

## B.33 referinta/seminar2_etnii_ghid/functii.py

```python
import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype

def nan_replace_df(df: pd.DataFrame):
    for c in df.columns:
        if df[c].isna().any():
            if is_numeric_dtype(df[c]):
                df.fillna({c:df[c].mean()}, inplace=True)
            else:
                df.fillna({c:df[c].mode()[0]},inplace=True)

def disimilaritate(df: pd.DataFrame):
    x = df.values
    tx = np.sum(x,axis=0)

    tx[tx==0] = 1
    sx = np.sum(x,axis=1)

    r = (sx - x.T).T
    tr = np.sum(r,axis=0)

    d = 0.5 * np.sum(np.abs(x/tx-r/tr),axis=0)
    return pd.Series(d,df.columns)
```

## B.34 referinta/seminar2_etnii_ghid/main.py

```python
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
```

## B.35 referinta/seminar3_industrie_alimentara_ghid/main.py

```python
import pandas as pd
from numpy.ma.extras import average
from pandas import DataFrame

pd.set_option("display.max_columns", None)
df_industria_a = pd.read_csv("data_in/IndustriaAlimentara.csv",index_col=0)


activitati = list(df_industria_a.columns.values)[1:]

s_total_loc = df_industria_a[activitati].apply(func=lambda x: x.sum(), axis=1)
s_total_loc.name = "Total"

df_cerinta1 = df_industria_a[s_total_loc!=0]
#print(df_cerinta1)
df_cerinta1.to_csv("data_out/Cerinta1.csv")

# Cerinta 2
df_industria_a["total"] = s_total_loc


df_cerinta2 = df_industria_a[activitati+["total"]].apply(func=lambda x: x[activitati]*100/ x["total"], axis=1)


df_cerinta2.insert(0, "Localitate", df_industria_a["Localitate"])

df_cerinta2.to_csv("data_out/Cerinta2.csv")

# Cerinta 3
df_populatie = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)

# Cerinta 3
df_populatie = pd.read_csv("data_in/PopulatieLocalitati.csv", index_col=0)

df_industria_a_loc = df_industria_a.merge(
    df_populatie, left_index=True, right_index= True
)

df_industria_a_jud = df_industria_a_loc[activitati+["total", "Judet", "Populatie"]].groupby(by="Judet").sum()

s_cerinta3 = df_industria_a_jud["total"]/ df_industria_a_jud["Populatie"]
s_cerinta3.name = "Pondere"
s_cerinta3.sort_values(ascending=False).to_csv("data_out/Cerinta3.csv")

print(df_industria_a_jud[activitati])
#cerinta 4
s_cerinta4 = df_industria_a_jud[activitati].apply(
    func = lambda x: x.index[x.argmax()],
    axis=1
)

s_cerinta4.name ="Activitate"

s_cerinta4.to_csv("data_out/Cerinta4.csv")

def calcul_medie(df:DataFrame):
    x = df.values
    medii = average(x[:,:-1],axis=0,weights=x[:,-1])
    return pd.Series(medii,df.columns[:-1])

df_coduri = pd.read_csv("data_in/Coduri_Judete.csv", index_col=0)
df_industria_a_loc_reg = df_industria_a_loc.merge(
    df_coduri, left_on="Judet", right_index = True
)

df_cerinta5 = df_industria_a_loc_reg[activitati+["Populatie","Regiune"]].groupby(by="Regiune").apply(func=lambda x: calcul_medie(x),include_groups=False)
df_cerinta5.to_csv("data_out/Cerinta5.csv")
```
