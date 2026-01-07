import pandas as pd
import logging


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize column names: lowercase, underscores, strip spaces.
    """
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    logging.info("Normalized column names.")
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values conservatively.
    """
    for column in df.columns:
        missing_count = df[column].isna().sum()

        if missing_count == 0:
            continue

        if df[column].dtype == "object":
            df[column].fillna("unknown", inplace=True)
        else:
            # Leave numeric NaNs untouched
            pass

        logging.info(f"Handled {missing_count} missing values in column '{column}'")

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove exact duplicate rows.
    """
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    removed = before - after
    if removed > 0:
        logging.info(f"Removed {removed} duplicate rows.")
    else:
        logging.info("No duplicate rows found.")

    return df
