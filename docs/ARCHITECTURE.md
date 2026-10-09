
```text
velib-analytics-pipeline/
├── README.md                  # schéma, choix, limites, captures du DAG
├── pyproject.toml / requirements.txt
├── .env.example
├── .gitignore                 # *.duckdb, .env, target/, logs/
├── docker-compose.yml         # optionnel, Airflow léger
├── .github/workflows/
│   ├── ci.yml                 # lint + pytest + dbt build
│   └── ingest.yml             # cron: ingestion planifiée
├── ingestion/
│   ├── extract.py             # appel API, retries, pagination
│   ├── load.py                # écriture brute (Parquet ou DuckDB), idempotente
│   └── config.py
├── tests/
│   └── test_extract.py        # pytest sur le parsing
├── dags/
│   └── velib_pipeline.py      # extract → load → dbt build → dbt test
├── dbt_project/
│   ├── dbt_project.yml
│   ├── profiles.yml           # profil duckdb
│   ├── models/
│   │   ├── sources.yml
│   │   ├── staging/           # stg_velib_stations, stg_velib_status
│   │   ├── intermediate/      # optionnel
│   │   └── marts/
│   │       ├── dim_station.sql
│   │       ├── fct_disponibilite.sql      # incrémental
│   │       └── mart_taux_remplissage.sql
│   ├── snapshots/             # snap_station (capacité, nom)
│   ├── tests/                 # tests SQL personnalisés
│   └── macros/
├── data/                      # ignoré par git
│   ├── raw/
│   └── velib.duckdb
├── dashboard/
│   └── app.py                 # Streamlit ou export pour Power BI
└── docs/
    └── architecture.png

```