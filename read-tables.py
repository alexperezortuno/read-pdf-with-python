from dataclasses import make_dataclass
from typing import List

import pandas.core.frame
import tabula


df: List = tabula.read_pdf("tables.pdf", multiple_tables=True, pages=1)
Point = make_dataclass("Point", [("x", int), ("y", int)])
first_table: pandas.core.frame.DataFrame = df[0]
print(first_table.head())
tabula.convert_into("tables.pdf", "tables-output.csv", output_format="csv", pages='all')
