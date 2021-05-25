# Scripto to convert the CSV from productboard html query to an excel suitable CSV
import tkinter as tk
from tkinter import filedialog
import re
import pandas as pd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # ask for CSV file
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Select CSV file form prodcutboard export",
                                           filetypes=(("CSV Files", "*.csv"), ("All", "*.*")))

    # load csv
    file = open(file_path, "r")
    raw_content = file.read()
    file.close()

    # write xlsx
    file = pd.read_csv(file_path)
    file_path = re.sub(r'\.csv', r'_real.xlsx', file_path)
    file.to_excel(file_path, index=None, header=True)
