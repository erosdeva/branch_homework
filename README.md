# Branch Homework

## Installation

```
mkdir -p ./venv && \
>   virtualenv --python python3 ./venv && \
>   . venv/bin/activate && \
>   pip install --requirement requirements.txt && \
>   pip install --requirement dev_requirements.txt
```

## Part 1: DB Diagrams

DB diagrams can be found under /app/results

The precise link to the DB diagrams page can be found in https://dbdiagram.io/d/61ec30ae7cf3fc0e7c55788a


## Part 2: CSV Generation

To generate the CSV you must run the main file from the root directory

```bash
sudo python main.py
```

Afterwards you will find the CSV results in the /app/results directory

CSV will be generated from the data that is present in /app/data/api_output.json


## Part 3: ETL Concept Diagram

The concept diagram for how this process can be turned into an ETL job can be found under /app/etl_concept

The overall concept for this ETL job is pretty straight forward. First we would convert our code into an APP
that runs in a serverless environment (Appengine, CloudRun, CloudFunction). A cron would be set to batch fetch 
data on a periodic basis. Then, based on the code that we have in this app we would convert the data into CSVs
that would then be stored in Google Cloud Storage. From this point forward, we can import the data
directly into Google's best Data warehouse solution which is BigQuery. For more information on this 
one can refer the official Google Docs: https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-csv

As mentioned, the concept diagrams highlight this process. If the data is meant to be used in other ways
(other than analysis work) then a new workflow would need to be constructed. 
