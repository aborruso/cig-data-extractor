# LOG

## 2025-07-30

* Inizializzazione del progetto "CIG Data Extractor".
* Sviluppo dello script `get_cig_data_requests.py` per l'estrazione dati CIG tramite API diretta.
* Implementazione della generazione di JSON grezzo (`<CIG>_raw.json`) e versione light (`<CIG>.json`).
* Gestione dei CIG non esistenti e dei casi di input non valido.
* Creazione del Product Requirements Document (`PRD.md`).
* Creazione del README del progetto (`README.md`).
* Configurazione del controllo versione con Git e `.gitignore`.
* Correzione della formattazione Markdown per `PRD.md` e `README.md`.
* Creazione dell'eseguibile autoconsistente tramite PyInstaller.
* **Aggiornamento dello script `get_cig_data_requests.py` per supportare l'opzione `-o` (o `--output-path`) come percorso completo del file di output per il JSON light, con verifica dell'esistenza del file.**
* **Aggiornamento del `README.md` per documentare la nuova funzionalità dell'opzione `-o`.**