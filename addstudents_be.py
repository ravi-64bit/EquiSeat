"""Command-line helper to import a CSV or Excel student list."""
import argparse

import arrange_algo


def main():
    parser = argparse.ArgumentParser(description="Import students into EquiSeat.")
    parser.add_argument("file", help="CSV, XLSX or XLS file with regd_no, name and section columns")
    args = parser.parse_args()
    count = arrange_algo.import_students(args.file)
    print(f"Imported {count} student record(s).")


if __name__ == "__main__":
    main()
