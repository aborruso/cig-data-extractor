# CIG Data Extractor

Questo repository contiene uno script Python e un eseguibile standalone per l'estrazione automatizzata di dati relativi ai CIG (Codice Identificativo Gara) dal portale `dati.anticorruzione.it` dell'Autorità Nazionale Anticorruzione (ANAC).

Lo strumento è progettato per recuperare i dati dettagliati di un CIG specifico e fornirli in due formati JSON: una versione grezza (direttamente dall'API) e una versione "light" con i dati annidati già parsificati per una maggiore leggibilità e usabilità.

## Caratteristiche

*   Estrazione Dati CIG: Recupera informazioni complete per un CIG fornito.
*   Output JSON Grezzo: Salva la risposta JSON originale dell'API (`<CIG_NUMBER>_raw.json`).
*   Output JSON Light: Salva una versione elaborata del JSON, con i campi JSON annidati parsificati (`<CIG_NUMBER>.json`).
*   Eseguibile Autoconsistente: Permette l'esecuzione dello strumento su sistemi senza un ambiente Python installato.

## Requisiti

### Per l'Eseguibile Autoconsistente

Nessun requisito aggiuntivo. L'eseguibile include tutte le dipendenze necessarie.

### Per lo Script Python (se si esegue il `.py`)

*   Python 3.x
*   Libreria `requests`

Per installare la libreria `requests`:

```bash
pip install requests
```

## Utilizzo

### Utilizzo dell'Eseguibile Autoconsistente

1.  Scarica l'eseguibile dalla directory `dist/` (o crealo seguendo le istruzioni di sviluppo).
2.  Apri un terminale e naviga nella directory dove si trova l'eseguibile.
3.  Esegui il comando, sostituendo `<CIG_NUMBER>` con il CIG desiderato:

    ```bash
    ./get_cig_data_requests <CIG_NUMBER>
    ```

    Esempio:

    ```bash
    ./get_cig_data_requests 918052266A
    ```

### Utilizzo dello Script Python

1.  Assicurati di avere Python 3 e la libreria `requests` installati.
2.  Apri un terminale e naviga nella directory dove si trova lo script `get_cig_data_requests.py`.
3.  Esegui il comando, sostituendo `<CIG_NUMBER>` con il CIG desiderato:

    ```bash
    python3 get_cig_data_requests.py <CIG_NUMBER>
    ```

    Esempio:

    ```bash
    python3 get_cig_data_requests.py 918052266A
    ```

## Output

Dopo l'esecuzione, verranno creati due file JSON nella stessa directory:

*   `<CIG_NUMBER>_raw.json`: Contiene la risposta JSON grezza dall'API.
*   `<CIG_NUMBER>.json`: Contiene una versione elaborata del JSON, con i campi annidati parsificati per una maggiore leggibilità.

Esempio per CIG `918052266A`:

*   `918052266A_raw.json`
*   `918052266A.json`

## Sviluppo

### Creazione dell'Eseguibile Autoconsistente

Per creare l'eseguibile standalone, assicurati di avere [PyInstaller](https://pyinstaller.org/) installato:

```bash
pip install pyinstaller
```

Quindi, esegui il seguente comando nella directory principale del progetto:

```bash
pyinstaller --onefile get_cig_data_requests.py
```

Questo creerà l'eseguibile nella directory `dist/`.

### Pulizia dei File di Build

PyInstaller crea delle directory temporanee (`build/`) e un file `.spec`. Puoi rimuoverli con:

```bash
rm -rf build/ get_cig_data_requests.spec
```

## Licenza

Questo progetto è rilasciato sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli. (Nota: il file LICENSE non è incluso in questo esempio, ma è una buona pratica aggiungerlo).