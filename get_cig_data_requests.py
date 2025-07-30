import requests
import json
import sys
import os
import argparse

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

def get_cig_data_direct(cig_number, output_file_path=None):
    url = "https://dati.anticorruzione.it/api/v1/chart/data?form_data=%7B%22slice_id%22%3A372%7D&dashboard_id=26&force"

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'origin': 'https://dati.anticorruzione.it',
        'referer': f'https://dati.anticorruzione.it/superset/dashboard/dettaglio_cig/?UUID=some_uuid&cig={cig_number}', # UUID è un placeholder
        'user-agent': 'Mozilla/5.5 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    # Il payload JSON della richiesta POST
    payload = {
        "datasource": {"id": 66, "type": "table"},
        "force": False,
        "queries": [
            {
                "time_range": "No filter",
                "granularity": "ts",
                "filters": [],
                "extras": {"time_grain_sqla": "P1D", "time_range_endpoints": ["inclusive", "exclusive"], "having": "", "having_druid": [], "where": ""},
                "applied_time_extras": {},
                "columns": ["template", "stazione_appaltante", "bando", "pubblicazioni", "categorie_opera", "categorie_dpcm_aggregazione", "lavorazioni", "incaricati", "partecipanti", "aggiudicazione", "quadro_economico", "fonti_finanziamento", "avvio_contratto", "stati_avanzamento", "collaudo", "varianti", "fine_contratto", "subappalti", "sospensioni", "avvalimenti"],
                "orderby": [["template", True]],
                "annotation_layers": [],
                "row_limit": None,  # Nessun limite di righe
                "timeseries_limit": 0,
                "order_desc": True,
                "url_params": {"UUID": "some_uuid", "cig": cig_number}, # UUID è un placeholder
                "custom_params": {},
                "custom_form_data": {},
                "post_processing": []
            }
        ],
        "form_data": {
            "datasource": "66__table",
            "viz_type": "table",
            "slice_id": 372,
            "url_params": {"UUID": "some_uuid", "cig": cig_number},
            "time_range_endpoints": ["inclusive", "exclusive"],
            "granularity_sqla": "ts",
            "time_grain_sqla": "P1D",
            "time_range": "No filter",
            "query_mode": "raw",
            "groupby": [],
            "all_columns": ["template", "stazione_appaltante", "bando", "pubblicazioni", "categorie_opera", "categorie_dpcm_aggregazione", "lavorazioni", "incaricati", "partecipanti", "aggiudicazione", "quadro_economico", "fonti_finanziamento", "avvio_contratto", "stati_avanzamento", "collaudo", "varianti", "fine_contratto", "subappalti", "sospensioni", "avvalimenti"],
            "percent_metrics": [],
            "adhoc_filters": [],
            "order_by_cols": ["[\"template\", true]"],
            "row_limit": None,
            "server_page_length": 10,
            "include_time": False,
            "order_desc": True,
            "table_timestamp_format": "smart_date",
            "show_cell_bars": True,
            "color_pn": True,
            "database_name": "Dremio",
            "datasource_name": "DETTAGLIO_CIG",
            "extra_form_data": {},
            "import_time": 1737979700,
            "remote_id": 745,
            "schema": "appalti",
            "label_colors": {},
            "shared_label_colors": {},
            "extra_filters": [],
            "dashboardId": 26,
            "force": None,
            "result_format": "json",
            "result_type": "full"
        },
        "result_format": "json",
        "result_type": "full"
    }

    print(f"Tentativo di recuperare i dati per CIG: {cig_number} direttamente tramite API...")
    try:
        response = requests.post(url, headers=headers, json=payload, verify=False) # verify=False per ignorare errori SSL
        response.raise_for_status()  # Solleva un'eccezione per codici di stato HTTP di errore (4xx o 5xx)
        
        raw_json_data = response.json()
        print("Dati JSON grezzi ricevuti.")

        # Controlla se sono stati trovati dati per il CIG
        if not raw_json_data.get('result') or not raw_json_data['result'][0].get('data') or \
           raw_json_data['result'][0].get('rowcount') == 0 or \
           (raw_json_data['result'][0].get('rowcount') == 1 and \
            raw_json_data['result'][0]['data'][0].get('stazione_appaltante') == 'N/A'):
            print(f"Nessun dato trovato per il CIG: {cig_number}")
            return None, None

        # Processa per la versione light
        light_data = {}
        main_data_entry = raw_json_data['result'][0]['data'][0]
        for key, value in main_data_entry.items():
            if isinstance(value, str) and is_json(value):
                light_data[key] = json.loads(value)
            else:
                light_data[key] = value

        # Gestione del percorso di output
        if output_file_path:
            # Verifica se il file esiste già
            if os.path.exists(output_file_path):
                print(f"Errore: Il file di output specificato esiste già: {output_file_path}")
                return None, None
            
            # Crea la directory se non esiste
            output_dir = os.path.dirname(output_file_path)
            if output_dir and not os.path.exists(output_dir):
                os.makedirs(output_dir)

            with open(output_file_path, 'w', encoding='utf-8') as f:
                json.dump(light_data, f, ensure_ascii=False, indent=4)
            print(f"Dati light salvati in: {output_file_path}")
            return None, output_file_path # Non salviamo il raw se specificato output_path
        else:
            # Salva il JSON grezzo con il suffisso _raw
            raw_output_filename = f"{cig_number}_raw.json"
            with open(raw_output_filename, 'w', encoding='utf-8') as f:
                json.dump(raw_json_data, f, ensure_ascii=False, indent=4)
            print(f"Dati grezzi salvati in: {raw_output_filename}")

            # Salva la versione light senza suffisso
            light_output_filename = f"{cig_number}.json"
            with open(light_output_filename, 'w', encoding='utf-8') as f:
                json.dump(light_data, f, ensure_ascii=False, indent=4)
            print(f"Dati light salvati in: {light_output_filename}")
            return raw_output_filename, light_output_filename

    except requests.exceptions.RequestException as e:
        print(f"Errore durante la richiesta API: {e}")
        if response.status_code:
            print(f"Codice di stato HTTP: {response.status_code}")
            print(f"Contenuto della risposta: {response.text}")
        return None, None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estrae dati CIG dal portale ANAC.")
    parser.add_argument("cig_number", help="Il Codice Identificativo Gara (CIG) da estrarre.")
    parser.add_argument("-o", "--output-path", help="Percorso completo del file JSON light di output. Se specificato, solo il file light verrà salvato a questo percorso. Se il file esiste già, l'operazione verrà bloccata.")
    
    args = parser.parse_args()

    raw_file, light_file = get_cig_data_direct(args.cig_number, args.output_path)
    if raw_file or light_file:
        if args.output_path:
            print(f"Processo completato per CIG {args.cig_number}. Dati light salvati in {light_file}")
        else:
            print(f"Processo completato per CIG {args.cig_number}. Dati grezzi in {raw_file}, dati light in {light_file}")
    else:
        print(f"Impossibile recuperare i dati per CIG {args.cig_number}.")
