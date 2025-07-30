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
    }
}
```

## Descrizione dei Campi

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
