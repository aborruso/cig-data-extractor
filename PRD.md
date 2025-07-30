# CIG Data Extractor - Product Requirements Document

## Versione

1.0

## Data

30 Luglio 2025

## Autore

Gemini CLI Agent

---

## 1. Introduzione

Questo documento definisce i requisiti per il "CIG Data Extractor", uno strumento progettato per automatizzare l'estrazione di dati dettagliati relativi ai CIG (Codice Identificativo Gara) dal portale `dati.anticorruzione.it` dell'Autorità Nazionale Anticorruzione (ANAC). L'obiettivo principale è fornire agli utenti un accesso programmatico e strutturato a queste informazioni.

## 2. Obiettivi

*   Automazione dell'Estrazione: Automatizzare il processo di recupero dei dati per specifici CIG, riducendo l'intervento manuale.
*   Formato Dati Strutturato: Fornire i dati estratti in un formato JSON facilmente parsificabile e utilizzabile.
*   Versioni Dati Flessibili: Offrire sia una versione "grezza" del JSON (direttamente dall'API) sia una versione "light" semplificata, con i dati annidati già parsificati per una maggiore usabilità.
*   Facilità d'Uso: Rendere lo strumento accessibile anche a utenti non tecnici tramite la creazione di un eseguibile autoconsistente.

## 3. Ambito

### In Ambito (In Scope)

*   Estrazione di dati CIG da `https://dati.anticorruzione.it` tramite chiamate API dirette.
*   Generazione di output JSON grezzo (`<CIG_NUMBER>_raw.json`).
*   Generazione di output JSON "light" con stringhe JSON annidate parsificate (`<CIG_NUMBER>.json`).
*   Interfaccia a riga di comando per la specifica del CIG.
*   Creazione di un eseguibile standalone per la distribuzione.

### Fuori Ambito (Out of Scope)

*   Gestione di interazioni complesse del browser (es. reCAPTCHA, navigazione UI), poichè si privilegia l'accesso diretto all'API.
*   Gestione dell'autenticazione utente (login, sessioni) se richiesta dall'API (attualmente non necessaria per l'endpoint target).
*   Estrazione massiva di più CIG in una singola esecuzione (sebbene lo script sia adattabile).
*   Validazione dei dati estratti oltre la parsificazione JSON di base.
*   Integrazione diretta con altri sistemi o database.

## 4. Funzionalità

*   Estrazione Dati CIG: Recupera i dati completi per un CIG fornito come argomento.
*   Output JSON Grezzo: Salva la risposta JSON originale dell'API in un file dedicato.
*   Output JSON Light: Salva una versione elaborata del JSON, dove i campi che contengono stringhe JSON annidate vengono automaticamente parsificati in oggetti Python (dizionari/liste).
*   Eseguibile Autoconsistente: Permette l'esecuzione dello strumento su sistemi senza un ambiente Python installato.

## 5. Considerazioni Tecniche

*   Stack Tecnologico: Python 3, libreria `requests`, PyInstaller.
*   Endpoint API: `https://dati.anticorruzione.it/api/v1/chart/data` (endpoint POST).
*   Gestione Errori: Gestione di base degli errori di rete e delle risposte API.
*   Verifica SSL: Attualmente disabilitata (`verify=False`) nella chiamata `requests` per aggirare potenziali problemi di certificato. Questo dovrebbe essere rivisto per ambienti di produzione.

## 6. Considerazioni Future (Opzionale)

*   Implementare una verifica più robusta dei certificati SSL.
*   Aggiungere il supporto per l'elaborazione di liste di CIG.
*   Migliorare la segnalazione degli errori e la gestione delle eccezioni.
*   Monitorare eventuali cambiamenti nell'API del sito ANAC per garantire la continuità del servizio.