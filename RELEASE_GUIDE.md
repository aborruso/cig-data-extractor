# Guida alla Release del Pacchetto Python e dell'Eseguibile

Questa guida descrive i passaggi per rilasciare una nuova versione del pacchetto Python su PyPI e creare una nuova release su GitHub con l'eseguibile compilato.

## Prerequisiti

Assicurati di aver configurato correttamente i "Trusted Publishers" su PyPI per il progetto `cig-data-extractor`. Questo è un metodo di pubblicazione sicuro che non richiede l'uso di token API di lunga durata direttamente nel workflow.

## Procedura di Rilascio

Segui questi passaggi ogni volta che desideri rilasciare una nuova versione:

1.  **Aggiorna il numero di versione nel `pyproject.toml`:**
    Apri il file `pyproject.toml` nella root del tuo progetto. Trova la sezione `[project]` e aggiorna il valore di `version` al nuovo numero di versione (es. `0.2.5`).

    ```toml
    [project]
    name = "cig-data-extractor"
    version = "0.2.5" # <-- Aggiorna qui
    description = "A tool to extract CIG data."
    # ... altre configurazioni
    ```

2.  **Crea un nuovo tag Git:**
    Apri il terminale nella root del tuo progetto e crea un nuovo tag Git. Il nome del tag **deve corrispondere** al nuovo numero di versione che hai impostato in `pyproject.toml`, preceduto da una `v` (es. `v0.2.5`). Aggiungi un messaggio descrittivo per il tag.

    ```bash
    git tag -a v0.2.5 -m "Release della versione 0.2.5 con nuove funzionalità/correzioni"
    ```

    Sostituisci `v0.2.5` con il tuo nuovo numero di versione e il messaggio con una descrizione appropriata.

3.  **Esegui il push del tag al repository remoto:**
    Invia il nuovo tag al tuo repository GitHub. Questo azione triggererà automaticamente il workflow di GitHub Actions configurato (`.github/workflows/release.yml`).

    ```bash
    git push origin v0.2.5
    ```

## Cosa succede dopo il push del tag?

Una volta che il tag viene inviato a GitHub, il workflow `release.yml` si attiverà automaticamente ed eseguirà i seguenti passaggi:

-   **Build del pacchetto Python:** Verrà costruito il pacchetto di distribuzione (`.tar.gz` e `.whl`) del tuo progetto.
-   **Pubblicazione su PyPI:** Il pacchetto verrà pubblicato automaticamente su PyPI utilizzando la configurazione di "Trusted Publishers".
-   **Compilazione dell'eseguibile:** Verrà compilato un eseguibile (tramite PyInstaller) per le piattaforme supportate.
-   **Creazione della Release su GitHub:** Verrà creata una nuova release su GitHub associata al tag, e l'eseguibile compilato verrà allegato a questa release.

Puoi monitorare l'avanzamento del workflow nella sezione "Actions" del tuo repository GitHub.

## Post-Pubblicazione (Importante per la Sicurezza)

Dopo la prima pubblicazione riuscita su PyPI tramite "Trusted Publishers", se in precedenza avevi configurato un token API PyPI con ambito "All projects" (come suggerito inizialmente per i test), **è fondamentale che tu lo sostituisca con un token specifico per il progetto `cig-data-extractor`**. Questo riduce il rischio in caso di compromissione del token.

Per fare ciò:
1.  Vai su PyPI, nella sezione dei tuoi token API.
2.  Elimina il token con ambito "All projects".
3.  Crea un nuovo token API specificamente per il progetto `cig-data-extractor`.
4.  Aggiorna il segreto `PYPI_API_TOKEN` nel tuo repository GitHub con il nuovo token specifico per il progetto.



