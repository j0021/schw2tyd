#!/usr/bin/python3

# This is free and unencumbered software released into the public domain.

# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# For more information, please refer to <https://unlicense.org>


import csv
import sys

schw_export_file = "schw_export.csv"
tyd_import_file = "tyd_import.csv"

with open(sys.argv[1], "r", newline="", encoding="utf-8") as raw_csv_file:
    raw_csv_data = raw_csv_file.readlines()
    with open(schw_export_file, "w", newline="", encoding="utf-8") as src_csv_file:
        src_csv_file.writelines(raw_csv_data[2:-2])

with open(schw_export_file, "r", newline="", encoding="utf-8") as src_csv_file:
    csv_reader = csv.DictReader(src_csv_file)
    src_csv_data = []
    for row in csv_reader:
        ticker, shares, cost = row["Symbol"], row["Quantity"], row["Cost/Share"][1:]
        src_csv_data.append([ticker, shares, cost])

with open(tyd_import_file, "w", newline="", encoding="utf-8") as dst_csv_file:
    csv_writer = csv.writer(dst_csv_file)
    csv_writer.writerows(src_csv_data)
