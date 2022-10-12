import pandas as pd
import easygui


def read_xls_file(file_name):
    """Read xls file :return Excel table"""
    excel_table = pd.read_excel(file_name)
    return excel_table


def open_window():
    read = easygui.fileopenbox()
    return read
