#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE todo(
        ID INT PRIMARY  KEY     NOT NULL,
        TITLE           TEXT    NOT NULL,
        BODY            TEXT    NOT NULL,
        CREATEDON       DATE    NOT NULL,
        DUEDATE         DATE,
        COMPLETEDON     DATE
    )
EOSQL