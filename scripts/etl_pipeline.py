# etl_pipeline.py

import pandas as pd
import sqlite3
import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


RAW_PATH = BASE_DIR / "data" / "raw"

PROCESSED_PATH = BASE_DIR / "data" / "processed"

DB_PATH = BASE_DIR / "data" / "db" / "bluestock_mf.db"


PROCESSED_PATH.mkdir(parents=True, exist_ok=True)
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def clean_dataframe(df):

    df = df.drop_duplicates()

    df = df.dropna(how="all")


    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )


    numeric_columns = df.select_dtypes(
        include=["int64", "float64"]
    ).columns


    for col in numeric_columns:
        df[col] = df[col].fillna(
            df[col].median()
        )


    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns


    for col in categorical_columns:
        df[col] = df[col].fillna(
            "Unknown"
        )


    return df



def load_to_database(df, table_name, connection):

    df.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )


def run_etl():


    if not RAW_PATH.exists():

        logging.error(
            "Raw data folder does not exist"
        )

        return


    files = list(
        RAW_PATH.glob("*.csv")
    )


    if not files:

        logging.warning(
            "No CSV files found"
        )

        return



    connection = sqlite3.connect(
        DB_PATH
    )


    successful_files = 0


    try:


        logging.info(
            f"{len(files)} files detected"
        )


        for file in files:


            try:


                logging.info(
                    f"Reading {file.name}"
                )


                df = pd.read_csv(
                    file
                )


                if df.empty:

                    logging.warning(
                        f"{file.name} is empty"
                    )

                    continue



                logging.info(
                    f"Original rows: {len(df)}"
                )



                df = clean_dataframe(
                    df
                )



                output_file = (
                    PROCESSED_PATH /
                    file.name
                )


                df.to_csv(
                    output_file,
                    index=False
                )



                table_name = (
                    file.stem
                    .lower()
                    .replace(" ", "_")
                )


                load_to_database(
                    df,
                    table_name,
                    connection
                )


                successful_files += 1



                logging.info(
                    f"{file.name} loaded successfully"
                )



            except Exception as error:


                logging.exception(
                    f"Failed processing {file.name}: {error}"
                )



    finally:


        connection.close()



    logging.info(
        f"ETL completed. Successful files: {successful_files}/{len(files)}"
    )



if __name__ == "__main__":

    run_etl()