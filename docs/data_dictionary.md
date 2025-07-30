# Dizionario dei Dati

Questo documento descrive la struttura e il significato dei dati estratti dal portale `dati.anticorruzione.it`.

## Struttura Generale del JSON Light

Il JSON "light" (`<CIG_NUMBER>.json`) è la versione elaborata dei dati, con i campi annidati parsificati per una maggiore leggibilità.

```json
{
    "template": "string",
    "stazione_appaltante": {
        "CF_AMMINISTRAZIONE_APPALTANTE": "string",
        "CITTA": "string",
        "CODICE_AUSA": "string",
        "DENOMINAZIONE_AMMINISTRAZIONE_APPALTANTE": "string",
        "DENOMINAZIONE_CENTRO_COSTO": "string",
        "ID_CENTRO_COSTO": "string",
        "INDIRIZZO": "string",
        "ISTAT_COMUNE": "string",
        "REGIONE": "string",
        "SEZIONE_REGIONALE": "string"
    },
    "bando": {
        "CIG": "string",
        "COD_ESITO": "number",
        "COD_MODALITA_REALIZZAZIONE": "string",
        "COD_STRUMENTO_SVOLGIMENTO": "number",
        "COD_TIPO_SCELTA_CONTRAENTE": "string",
        "CPV": [
            {
                "COD_CPV": "string",
                "DESCRIZIONE_CPV": "string",
                "FLAG_PREVALENTE": "number"
            }
        ],
        "DATA_COMUNICAZIONE_ESITO": "string (YYYY-MM-DD)",
        "DATA_SCADENZA_OFFERTA": "string (YYYY-MM-DD)",
        "DETTAGLIO_STATO": {
            "DATA_ULTIMO_PERFEZIONAMENTO": "string (YYYY-MM-DD)"
        },
        "DURATA_PREVISTA": "number",
        "ESITO": "string",
        "FLAG_ESCLUSO": "number (0/1)",
        "FLAG_PREV_RIPETIZIONI": "number (0/1)",
        "FLAG_URGENZA": "number (0/1)",
        "IMPORTO_COMPLESSIVO_GARA": "number",
        "IMPORTO_LOTTO": "number",
        "IMPORTO_SICUREZZA": "number",
        "LUOGO_NUTS": "string",
        "MODALITA_REALIZZAZIONE": "string",
        "N_LOTTI_COMPONENTI": "string",
        "NUMERO_GARA": "string",
        "OGGETTO_GARA": "string",
        "OGGETTO_LOTTO": "string",
        "OGGETTO_PRINCIPALE_CONTRATTO": "string",
        "SETTORE": "string",
        "STATO": "string",
        "STRUMENTO_SVOLGIMENTO": "string",
        "TIPO_CIG": "string",
        "TIPO_SCELTA_CONTRAENTE": "string",
        "FLAG_PNRR_PNC": "number (0/1)",
        "FLAG_QUOTE": "string"
    },
    "pubblicazioni": {
        "DATA_CREAZIONE": "string (YYYY-MM-DD)",
        "DATA_PUBBLICAZIONE": "string (YYYY-MM-DD)"
    },
    "categorie_opera": [
        {
            "COD_TIPO_CATEGORIA": "string",
            "DESCRIZIONE": "string",
            "DESCRIZIONE_TIPO_CATEGORIA": "string",
            "ID_CATEGORIA": "string"
        }
    ],
    "categorie_dpcm_aggregazione": "null",
    "lavorazioni": "null",
    "incaricati": [
        {
            "COD_RUOLO": "string",
            "COGNOME": "string",
            "DESCRIZIONE_RUOLO": "string",
            "NOME": "string"
        }
    ],
    "partecipanti": [
        {
            "COD_GRUPPO": "string",
            "COD_RUOLO": "string",
            "CODICE_FISCALE": "string",
            "DENOMINAZIONE": "string",
            "FLAG_AGGIUDICATARIO": "number",
            "RUOLO": "string",
            "TIPO_SOGGETTO": "string"
        }
    ],
    "aggiudicazione": [
        {
            "ASTA_ELETTRONICA": "number (0/1)",
            "COD_ESITO": "string",
            "COD_PRESTAZIONI_COMPRESE": "number",
            "CRITERIO_AGGIUDICAZIONE": "string",
            "DATA_AGGIUDICAZIONE_DEFINITIVA": "string (YYYY-MM-DD)",
            "DATA_COMUNICAZIONE_ESITO": "string (YYYY-MM-DD)",
            "ESITO": "string",
            "FLAG_PROC_ACCELERATA": "number (0/1)",
            "FLAG_SCOMPUTO": "number (0/1)",
            "FLAG_SUBAPPALTO": "number (0/1)",
            "ID_AGGIUDICAZIONE": "number",
            "IMPORTO_AGGIUDICAZIONE": "number",
            "MASSIMO_RIBASSO": "number",
            "MINIMO_RIBASSO": "number",
            "N_MANIF_INTERESSE": "number",
            "NUM_IMPRESE_INVITATE": "number",
            "NUM_IMPRESE_OFFERENTI": "number",
            "NUM_IMPRESE_RICHIEDENTI": "number",
            "NUMERO_OFFERTE_AMMESSE": "number",
            "NUMERO_OFFERTE_ESCLUSE": "number",
            "PRESTAZIONI_COMPRESE": "string"
        }
    ],
    "quadro_economico": [
        {
            "DESCRIZIONE_EVENTO": "string",
            "DETTAGLIO_EVENTO": "number",
            "ID_AGGIUDICAZIONE": "number",
            "IMPORTO_FORNITURE": "number",
            "IMPORTO_LAVORI": "number",
            "IMPORTO_PROGETTAZIONE": "number",
            "IMPORTO_SERVIZI": "number",
            "IMPORTO_SICUREZZA": "number",
            "SOMME_A_DISPOSIZIONE": "number",
            "ULTERIORI_ONERI_NON_SOGGETTI_RIBASSO": "string"
        }
    ],
    "fonti_finanziamento": [
        {
            "ALTRO": "number",
            "APPORTO_DI_CAPITALI_PRIVATI": "number",
            "ENTRATE_CON_DEST_VINCOLATA_PRIVATI": "number",
            "ENTRATE_CON_DEST_VINCOLATA_PUBBLICA_COMUNITARIA": "number",
            "ENTRATE_CON_DEST_VINCOLATA_PUBBLICA_NAZIONALE_ALTRI": "number",
            "ENTRATE_CON_DEST_VINCOLATA_PUBBLICA_NAZIONALE_CENTRALE": "number",
            "ENTRATE_CON_DEST_VINCOLATA_PUBBLICA_NAZIONALE_LOCALE": "number",
            "ENTRATE_CON_DEST_VINCOLATA_PUBBLICA_NAZIONALE_REGIONALE": "number",
            "FONDI_DI_BILANCIO_DELLA_STAZIONE_APPALTANTE": "number",
            "FONDI_DI_BILANCIO_DELLAMMINISTRAZIONE_COMPETENTE": "number",
            "ID_AGGIUDICAZIONE": "number",
            "MUTUO": "number",
            "SFRUTTAMENTO_ECONOMICO_E_FUNZIONALE_DEL_BENE": "number",
            "TRASFERIMENTO_DI_IMMOBILI_EX_ART53_C6_DLGS_N163_06_ECONOMIA_SU_STANZIAMENTI_NON_VINCOLATI": "number"
        }
    ],
    "avvio_contratto": "null",
    "stati_avanzamento": "null",
    "collaudo": "null",
    "varianti": "null",
    "fine_contratto": "null",
    "subappalti": "null",
    "sospensioni": "null",
    "avvalimenti": "null"
}
```

## Descrizione dei Campi

> **Nota:** Lo schema dati e le descrizioni dei campi in questa sezione sono stati generati automaticamente da un'intelligenza artificiale basandosi su un campione di dati. Sebbene sia stato fatto ogni sforzo per garantirne l'accuratezza, potrebbero contenere imprecisioni o omissioni. Si raccomanda vivamente di verificare sempre le informazioni con la documentazione ufficiale dell'ANAC o con un'analisi diretta dei dati grezzi.

| Campo | Tipo | Descrizione | Note |
|---|---|---|---|
| `template` | string | Indica il template utilizzato per la gara. | Attualmente "N/A" per i dati estratti. |
| `stazione_appaltante` | object | Dettagli della stazione appaltante. | |
| `stazione_appaltante.CF_AMMINISTRAZIONE_APPALTANTE` | string | Codice Fiscale dell'amministrazione appaltante. | |
| `stazione_appaltante.CITTA` | string | Città della stazione appaltante. | |
| `stazione_appaltante.CODICE_AUSA` | string | Codice AUSA (Anagrafe Unica Stazioni Appaltanti). | |
| `stazione_appaltante.DENOMINAZIONE_AMMINISTRAZIONE_APPALTANTE` | string | Denominazione completa dell'amministrazione appaltante. | |
| `stazione_appaltante.DENOMINAZIONE_CENTRO_COSTO` | string | Denominazione del centro di costo. | |
| `stazione_appaltante.ID_CENTRO_COSTO` | string | Identificativo del centro di costo. | |
| `stazione_appaltante.INDIRIZZO` | string | Indirizzo della stazione appaltante. | |
| `stazione_appaltante.ISTAT_COMUNE` | string | Codice ISTAT del comune. | |
| `stazione_appaltante.REGIONE` | string | Regione della stazione appaltante. | |
| `stazione_appaltante.SEZIONE_REGIONALE` | string | Sezione regionale di appartenenza. | |
| `bando` | object | Dettagli specifici del bando di gara. | |
| `bando.CIG` | string | Codice Identificativo Gara. | Chiave primaria. |
| `bando.COD_ESITO` | number | Codice numerico dell'esito della gara. | |
| `bando.COD_MODALITA_REALIZZAZIONE` | string | Codice della modalità di realizzazione. | |
| `bando.COD_STRUMENTO_SVOLGIMENTO` | number | Codice dello strumento di svolgimento. | |
| `bando.COD_TIPO_SCELTA_CONTRAENTE` | string | Codice del tipo di scelta del contraente. | |
| `bando.CPV` | array of objects | Codici CPV (Common Procurement Vocabulary) associati alla gara. | Ogni oggetto contiene `COD_CPV`, `DESCRIZIONE_CPV`, `FLAG_PREVALENTE`. |
| `bando.DATA_COMUNICAZIONE_ESITO` | string | Data di comunicazione dell'esito. | Formato YYYY-MM-DD. |
| `bando.DATA_SCADENZA_OFFERTA` | string | Data di scadenza dell'offerta. | Formato YYYY-MM-DD. |
| `bando.DETTAGLIO_STATO` | object | Dettagli aggiuntivi sullo stato della gara. | |
| `bando.DETTAGLIO_STATO.DATA_ULTIMO_PERFEZIONAMENTO` | string | Data dell'ultimo perfezionamento. | Formato YYYY-MM-DD. |
| `bando.DURATA_PREVISTA` | number | Durata prevista della gara in giorni. | |
| `bando.ESITO` | string | Esito della gara (es. "AGGIUDICATA"). | |
| `bando.FLAG_ESCLUSO` | number | Flag che indica se la gara è esclusa (0 = No, 1 = Sì). | |
| `bando.FLAG_PREV_RIPETIZIONI` | number | Flag che indica se sono previste ripetizioni (0 = No, 1 = Sì). | |
| `bando.FLAG_URGENZA` | number | Flag che indica se la gara è urgente (0 = No, 1 = Sì). | |
| `bando.IMPORTO_COMPLESSIVO_GARA` | number | Importo complessivo della gara. | |
| `bando.IMPORTO_LOTTO` | number | Importo del lotto. | |
| `bando.IMPORTO_SICUREZZA` | number | Importo della sicurezza. | |
| `bando.LUOGO_NUTS` | string | Codice NUTS (Nomenclature of Territorial Units for Statistics) del luogo. | |
| `bando.MODALITA_REALIZZAZIONE` | string | Modalità di realizzazione della gara. | |
| `bando.N_LOTTI_COMPONENTI` | string | Numero di lotti componenti. | |
| `bando.NUMERO_GARA` | string | Numero identificativo della gara. | |
| `bando.OGGETTO_GARA` | string | Oggetto completo della gara. | |
| `bando.OGGETTO_LOTTO` | string | Oggetto specifico del lotto. | |
| `bando.OGGETTO_PRINCIPALE_CONTRATTO` | string | Oggetto principale del contratto. | |
| `bando.SETTORE` | string | Settore di appartenenza della gara. | |
| `bando.STATO` | string | Stato attuale della gara (es. "ATTIVO"). | |
| `bando.STRUMENTO_SVOLGIMENTO` | string | Strumento di svolgimento della gara. | |
| `bando.TIPO_CIG` | string | Tipo di CIG (es. "ORDINARIO"). | |
| `bando.TIPO_SCELTA_CONTRAENTE` | string | Tipo di scelta del contraente. | |
| `bando.FLAG_PNRR_PNC` | number | Flag PNRR/PNC (0 = No, 1 = Sì). | |
| `bando.FLAG_QUOTE` | string | Flag quote (es. "S"). | |
| `pubblicazioni` | object | Dettagli sulle date di creazione e pubblicazione. | |
| `pubblicazioni.DATA_CREAZIONE` | string | Data di creazione della pubblicazione. | Formato YYYY-MM-DD. |
| `pubblicazioni.DATA_PUBBLICAZIONE` | string | Data di pubblicazione. | Formato YYYY-MM-DD. |
| `categorie_opera` | array of objects | Categorie di opere o servizi. | Ogni oggetto contiene `COD_TIPO_CATEGORIA`, `DESCRIZIONE`, `DESCRIZIONE_TIPO_CATEGORIA`, `ID_CATEGORIA`. |
| `categorie_dpcm_aggregazione` | null | Categorie DPCM di aggregazione. | Attualmente `null`. |
| `lavorazioni` | null | Dettagli sulle lavorazioni. | Attualmente `null`. |
| `incaricati` | array of objects | Dettagli sugli incaricati (es. RUP). | Ogni oggetto contiene `COD_RUOLO`, `COGNOME`, `DESCRIZIONE_RUOLO`, `NOME`. |
| `partecipanti` | array of objects | Dettagli sui partecipanti alla gara. | Ogni oggetto contiene `COD_GRUPPO`, `COD_RUOLO`, `CODICE_FISCALE`, `DENOMINAZIONE`, `FLAG_AGGIUDICATARIO`, `RUOLO`, `TIPO_SOGGETTO`. |
| `aggiudicazione` | array of objects | Dettagli sull'aggiudicazione della gara. | Ogni oggetto contiene `ASTA_ELETTRONICA`, `COD_ESITO`, `COD_PRESTAZIONI_COMPRESE`, `CRITERIO_AGGIUDICAZIONE`, `DATA_AGGIUDICAZIONE_DEFINITIVA`, `DATA_COMUNICAZIONE_ESITO`, `ESITO`, `FLAG_PROC_ACCELERATA`, `FLAG_SCOMPUTO`, `FLAG_SUBAPPALTO`, `ID_AGGIUDICAZIONE`, `IMPORTO_AGGIUDICAZIONE`, `MASSIMO_RIBASSO`, `MINIMO_RIBASSO`, `N_MANIF_INTERESSE`, `NUM_IMPRESE_INVITATE`, `NUM_IMPRESE_OFFERENTI`, `NUM_IMPRESE_RICHIEDENTI`, `NUMERO_OFFERTE_AMMESSE`, `NUMERO_OFFERTE_ESCLUSE`, `PRESTAZIONI_COMPRESE`. |
| `quadro_economico` | array of objects | Dettagli sul quadro economico della gara. | Ogni oggetto contiene `DESCRIZIONE_EVENTO`, `DETTAGLIO_EVENTO`, `ID_AGGIUDICAZIONE`, `IMPORTO_FORNITURE`, `IMPORTO_LAVORI`, `IMPORTO_PROGETTAZIONE`, `IMPORTO_SERVIZI`, `IMPORTO_SICUREZZA`, `SOMME_A_DISPOSIZIONE`, `ULTERIORI_ONERI_NON_SOGGETTI_RIBASSO`. |
| `fonti_finanziamento` | array of objects | Dettagli sulle fonti di finanziamento. | Ogni oggetto contiene `ALTRO`, `APPORTO_DI_CAPITALI_PRIVATI`, `ENTRATE_CON_DEST_VINCOLATA_PRIVATI`, `ENTRATE_CON_DEST_VINCOLATA_PUBBLICA_COMUNITARIA`, `ENTRATE_CON_DEST_VINCOLATA_PUBBLICA_NAZIONALE_ALTRI`, `ENTRATE_CON_DEST_VINCOLATA_PUBBLICA_NAZIONALE_CENTRALE`, `ENTRATE_CON_DEST_VINCOLATA_PUBBLICA_NAZIONALE_LOCALE`, `ENTRATE_CON_DEST_VINCOLATA_PUBBLICA_NAZIONALE_REGIONALE`, `FONDI_DI_BILANCIO_DELLA_STAZIONE_APPALTANTE`, `FONDI_DI_BILANCIO_DELLAMMINISTRAZIONE_COMPETENTE`, `ID_AGGIUDICAZIONE`, `MUTUO`, `SFRUTTAMENTO_ECONOMICO_E_FUNZIONALE_DEL_BENE`, `TRASFERIMENTO_DI_IMMOBILI_EX_ART53_C6_DLGS_N163_06_ECONOMIA_SU_STANZIAMENTI_NON_VINCOLATI`. |
| `avvio_contratto` | null | Dettagli sull'avvio del contratto. | Attualmente `null`. |
| `stati_avanzamento` | null | Dettagli sugli stati di avanzamento. | Attualmente `null`. |
| `collaudo` | null | Dettagli sul collaudo. | Attualmente `null`. |
| `varianti` | null | Dettagli sulle varianti. | Attualmente `null`. |
| `fine_contratto` | null | Dettagli sulla fine del contratto. | Attualmente `null`. |
| `subappalti` | null | Dettagli sui subappalti. | Attualmente `null`. |
| `sospensioni` | null | Dettagli sulle sospensioni. | Attualmente `null`. |
| `avvalimenti` | null | Dettagli sugli avvalimenti. | Attualmente `null`. |## Mini-guida: Come distinguere partecipanti e vincitori in un file JSON di gara ANAC

Nei file JSON ANAC relativi alle gare pubbliche, per capire **chi ha partecipato** e **chi ha vinto**, bisogna analizzare principalmente due sezioni del file:

### 1. Sezione `partecipanti`
Contiene l'elenco di tutti i soggetti che hanno presentato un'offerta. Ogni partecipante ha queste informazioni chiave:

- `CODICE_FISCALE`: il codice fiscale del soggetto
- `DENOMINAZIONE`: nome dell'ente o azienda
- `RUOLO`: se è "MANDATARIA" o "MANDANTE" in un raggruppamento
- `COD_GRUPPO`: per identificare i membri di uno stesso ATI
- `FLAG_AGGIUDICATARIO`: **questo è il campo decisivo**

### 2. Campo `FLAG_AGGIUDICATARIO`
- Se **valorizzato** (cioè contiene un numero, ad es. `2542577`), il partecipante è parte di un gruppo **aggiudicatario** (ha vinto la gara).
- Se **assente o nullo**, significa che ha **partecipato ma non ha vinto**.
- Il valore corrisponde all'`ID_AGGIUDICAZIONE` nella sezione `aggiudicazione`.

### 3. Sezione `aggiudicazione`
Qui trovi l'elenco delle aggiudicazioni con:
- `ID_AGGIUDICAZIONE`: ID univoco dell'aggiudicazione
- `ESITO`: se è "AGGIUDICATA"
- `IMPORTO_AGGIUDICAZIONE`: importo totale del contratto

### 🔍 Esempio pratico
Supponiamo di avere questo partecipante:
```json
{
  "DENOMINAZIONE": "GAMI ENGINEERING SRL",
  "FLAG_AGGIUDICATARIO": 2542577,
  "RUOLO": "MANDANTE"
}
```
E nella sezione `aggiudicazione` troviamo:
```json
{
  "ID_AGGIUDICAZIONE": 2542577,
  "ESITO": "AGGIUDICATA"
}
```
Allora GAMI ENGINEERING SRL è tra i vincitori.

### ✅ In sintesi
- Cerca la sezione `partecipanti`
- Controlla chi ha il campo `FLAG_AGGIUDICATARIO` valorizzato
- Confronta con l'`ID_AGGIUDICAZIONE` nella sezione `aggiudicazione`
- Chi ha `FLAG_AGGIUDICATARIO` presente **ha vinto**
- Gli altri sono **solo partecipanti**

