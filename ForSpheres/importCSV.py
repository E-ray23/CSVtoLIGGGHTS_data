#importCSV.py

import pandas as pd


def csvReader(csv_path: str):

    list_of_values = []

    if isinstance(csv_path, str):
        df = pd.read_csv(csv_path, sep=",")  
        df.index = range(1, len(df)+1) # set the index directly to a range starting from 1 --> necessary for liggghts
        df_len = df.shape[0] #Number of rows

        list_of_values.append(df)
        list_of_values.append(df_len)
        return list_of_values
    else:
        print("[ERROR]:\tPlease insert a valid path for the .csv-file!")
        exit()
