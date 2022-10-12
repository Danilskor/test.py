import pandas as pd


def read_xls_file(file_name):
    """Read xls file :return Excel table"""
    excel_table = pd.read_excel(file_name)
    return excel_table


