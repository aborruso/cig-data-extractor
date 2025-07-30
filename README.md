# CIG Data Extractor

Questo repository contiene uno script Python e un eseguibile standalone per l'estrazione automatizzata di dati relativi ai CIG (Codice Identificativo Gara) dal portale `dati.anticorruzione.it` dell'Autorità Nazionale Anticorruzione (ANAC).

Lo strumento è progettato per recuperare i dati dettagliati di un CIG specifico e fornirli in due formati JSON: una versione grezza (direttamente dall'API) e una versione "light" con i dati annidati già parsificati per una maggiore leggibilità e usabilità.

## Caratteristiche

* Estrazione Dati CIG: Recupera informazioni complete per un CIG fornito.
* Output JSON Grezzo: Salva la risposta JSON originale dell'API (`<CIG_NUMBER>_raw.json`).
* Output JSON Light: Salva una versione elaborata del JSON, con i campi JSON annidati parsificati (`<CIG_NUMBER>.json`).
* Eseguibile Autoconsistente: Permette l'esecuzione dello strumento su sistemi senza un ambiente Python installato.

## Requisiti

### Per l'Eseguibile Autoconsistente

Nessun requisito aggiuntivo. L'eseguibile include tutte le dipendenze necessarie.

### Per lo Script Python (se si esegue il `.py`)

* Python 3.x
* Libreria `requests`

Per installare la libreria `requests`:

```bash
pip install requests
```

## Utilizzo

### Utilizzo dell'Eseguibile Autoconsistente

1. Scarica l'eseguibile dalla directory `dist/` (o crealo seguendo le istruzioni di sviluppo).
2. Apri un terminale e naviga nella directory dove si trova l'eseguibile.
3. Esegui il comando, sostituendo `<CIG_NUMBER>` con il CIG desiderato:

    ```bash
    ./get_cig_data_requests <CIG_NUMBER>
    ```

    Esempio:

    ```bash
    ./get_cig_data_requests 918052266A
    ```

### Utilizzo dello Script Python

1. Assicurati di avere Python 3 e la libreria `requests` installati.
2. Apri un terminale e naviga nella directory dove si trova lo script `get_cig_data_requests.py`.
3. Esegui il comando, sostituendo `<CIG_NUMBER>` con il CIG desiderato:

    ```bash
    python3 get_cig_data_requests.py <CIG_NUMBER>
    ```

    Esempio:

    ```bash
    python3 get_cig_data_requests.py 918052266A
    ```

## Output

Dopo l'esecuzione, verranno creati due file JSON nella stessa directory:

* `<CIG_NUMBER>_raw.json`: Contiene la risposta JSON grezza dall'API.
* `<CIG_NUMBER>.json`: Contiene una versione elaborata del JSON, con i campi annidati parsificati per una maggiore leggibilità.

Esempio per CIG `918052266A`:

* `918052266A_raw.json`
* `918052266A.json`

Ecco un estratto del file `918052266A.json` (versione light):

```json
{
    "template": "N/A",
    "stazione_appaltante": {
        "CF_AMMINISTRAZIONE_APPALTANTE": "05678721001",
        "CITTA": "ROMA",
        "CODICE_AUSA": "0000225258",
        "DENOMINAZIONE_AMMINISTRAZIONE_APPALTANTE": "AGENZIA NAZIONALE PER L ATTRAZIONE DEGLI INVESTIMENTI E LO SVILUPPO D IMPRESA S.P.A.",
        "DENOMINAZIONE_CENTRO_COSTO": "CENTRALE DI COMMITTENZA",
        "ID_CENTRO_COSTO": "33986B12-6680-4F38-AE62-C734375E3060",
        "INDIRIZZO": "VIA CALABRIA 46",
        "ISTAT_COMUNE": "012058091",
        "REGIONE": "LAZIO",
        "SEZIONE_REGIONALE": "SEZIONE REGIONALE CENTRALE"
    },
    "bando": {
        "CIG": "918052266A",
        "COD_ESITO": 1.0,
        "COD_MODALITA_REALIZZAZIONE": "17",
        "COD_STRUMENTO_SVOLGIMENTO": 5.0,
        "COD_TIPO_SCELTA_CONTRAENTE": "1",
        "CPV": [
            {
                "COD_CPV": "71315400-3",
                "DESCRIZIONE_CPV": "SERVIZI DI COLLAUDO E VERIFICA DI EDIFICI",
                "FLAG_PREVALENTE": 1
            }
        ],
        "DATA_COMUNICAZIONE_ESITO": "2023-07-07",
        "DATA_SCADENZA_OFFERTA": "2022-05-26",
        "DETTAGLIO_STATO": {
            "DATA_ULTIMO_PERFEZIONAMENTO": "2022-05-24"
        },
        "DURATA_PREVISTA": 1220.0,
        "ESITO": "AGGIUDICATA",
        "FLAG_ESCLUSO": 0,
        "FLAG_PREV_RIPETIZIONI": 0,
        "FLAG_URGENZA": 0,
        "IMPORTO_COMPLESSIVO_GARA": 23569628.59,
        "IMPORTO_LOTTO": 3987864.4,
        "IMPORTO_SICUREZZA": 0.0,
        "LUOGO_NUTS": "ITF6",
        "MODALITA_REALIZZAZIONE": "ACCORDO QUADRO",
        "N_LOTTI_COMPONENTI": "7",
        "NUMERO_GARA": "8519126",
        "OGGETTO_GARA": "PROCEDURA DI GARA APERTA AI SENSI DEGLI ARTT. 54 E 60 DEL D.LGS. N. 50/2016, DA REALIZZARSI MEDIANTE PIATTAFORMA TELEMATICA, PER LA CONCLUSIONE DI ACCORDI QUADRO CON PIU’ OPERATORI ECONOMICI PER L’AFFIDAMENTO DI LAVORI (OG1 – OG11) E SERVIZI DI INGEGNERIA E ARCHITETTURA (E.21 – E.06 – S.03 – IA.02 – IA.04) PER LA NUOVA EDIFICAZIONE, RISTRUTTURAZIONE E RIQUALIFICAZIONE DI EDIFICI PUBBLICI RESIDENZIALI E NON.",
        "OGGETTO_LOTTO": "ACCORDO QUADRO OG1 - OG11 - SUB - LOTTO PRESTAZIONALE 1 – SERVIZI DI DI COLLAUDO - LOTTO GEOGRAFICO: CALABRIA - SICILIA",
        "OGGETTO_PRINCIPALE_CONTRATTO": "SERVIZI",
        "SETTORE": "SETTORI ORDINARI",
        "STATO": "ATTIVO",
        "STRUMENTO_SVOLGIMENTO": "PROCEDURE SVOLTE ATTRAVERSO PIATTAFORME TELEMATICHE DI NEGOZIAZIONE ART.58",
        "TIPO_CIG": "ORDINARIO",
        "TIPO_SCELTA_CONTRAENTE": "PROCEDURA APERTA",
        "FLAG_PNRR_PNC": 1,
        "FLAG_QUOTE": "S"
    }
}
```