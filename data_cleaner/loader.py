import pandas as pd
import logging
from pathlib import Path


def load_csv(file_path: Path) -> pd.DataFrame:
    """
    Load a CSV file safely and return a DataFrame.
    """
    if not file_path.exists() or not file_path.is_file():
        logging.error("Invalid CSV file path provided.")
        raise FileNotFoundError("CSV file not found.")

    try:
        df = pd.read_csv(file_path)
        logging.info(f"Loaded data: {df.shape[0]} rows × {df.shape[1]} columns")
        return df
    except Exception as e:
        logging.error(f"Failed to load CSV file: {e}")
        raise

