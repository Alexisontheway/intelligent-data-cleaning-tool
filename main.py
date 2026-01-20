import logging
import argparse
from pathlib import Path

from data_cleaner.loader import load_csv
from data_cleaner.cleaner import (
    normalize_columns,
    handle_missing_values,
    remove_duplicates,
)
from data_cleaner.reporter import save_cleaned_data, log_summary


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
    force=True,
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description=(
            "Intelligent Data Cleaning Tool\n\n"
            "Cleans CSV files by normalizing columns, "
            "handling missing values, and removing duplicates."
        ),
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run the cleaning process without saving the output file",
    )

    parser.add_argument(
        "input",
        type=Path,
        help="Path to the input CSV file",
    )

    parser.add_argument(
        "output",
        type=Path,
        help="Path where the cleaned CSV will be saved",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    df = load_csv(args.input)
    df = normalize_columns(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)

    log_summary(df)

    if args.dry_run:
        logging.info("Dry-run mode enabled. No file was saved.")
        print("Dry run completed. No output file was written.")
    else:
        save_cleaned_data(df, args.output)
        print(f"Cleaning complete. Cleaned data saved to: {args.output}")


        
        
    


if __name__ == "__main__":
    main()
