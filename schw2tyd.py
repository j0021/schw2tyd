#!/usr/bin/python3

# SPDX-License-Identifier: Unlicense

import csv
import sys


def main():

    if len(sys.argv) != 2:
        print("Usage: \n\n schw2tyd.py <schwab csv export file>\n")
        sys.exit(0)

    schw_export_file = "schw_export.csv" # cleaned csv export file name, created by the script
    tyd_import_file = "tyd_import.csv" # file to use to bulk upload to Track Your Dividends

    # This is to clean up the first 2 and last 2 lines of the schwab csv export file
    with open(sys.argv[1], "r", newline="", encoding="utf-8") as raw_csv_file:
        raw_csv_data = raw_csv_file.readlines()
        with open(schw_export_file, "w", newline="", encoding="utf-8") as src_csv_file:
            src_csv_file.writelines(raw_csv_data[2:-2])

    with open(schw_export_file, "r", newline="", encoding="utf-8") as src_csv_file:
        csv_reader = csv.DictReader(src_csv_file)
        src_csv_data = []
        for row in csv_reader:
            # Positions settings must include the following columns
            try:
                ticker, shares, cost = row["Symbol"], row["Quantity"], row["Cost/Share"][1:]
            except KeyError as e:
                print("\nerror: the following column was not found: {}\n".format(e))
                sys.exit(1)
            src_csv_data.append([ticker, shares, cost])

    with open(tyd_import_file, "w", newline="", encoding="utf-8") as dst_csv_file:
        csv_writer = csv.writer(dst_csv_file)
        csv_writer.writerows(src_csv_data)

if __name__ == "__main__":
    main()
