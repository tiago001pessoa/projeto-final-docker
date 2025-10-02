# MovieFlix Analytics — Projeto Final

Autor: Tiago Pessoa

## Visão geral

Plataforma simples para cadastro/avaliação de filmes e pipeline de dados simulando Data Lake → Data Warehouse → Data Mart.

## Estrutura

projeto-final-docker/
├── app/
│ ├── Dockerfile
│ ├── app.py
│ ├── requirements.txt
│ ├── models.py
│ ├── views.py
│ └── static/ (opcional)
│ └── ...
├── nginx/
│ └── default.conf
└── docker-compose.yml
├── etl/
│ ├── data_lake/ # CSVs brutos
│ │ ├── movies.csv
│ │ ├── users.csv
│ │ └── ratings.csv
│ ├── etl_load.py # script para carregar CSV → Postgres
│ └── create_tables.sql # DDL do DW
├── sql/
│ ├── datamart_views.sql # visões/queries do Data Mart
│ └── analytics_queries.sql
├── .github/
│ └── workflows/
│ └── ci-cd.yml
├── README.md
└── .env.example

## Rodando localmente (com Docker Compose)

1. Clone o repositório: https://github.com/tiago001pessoa/projeto-final-docker
