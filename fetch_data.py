# read the .xlsx file holding the hospital data of (date, number of inpatients)

import pandas as pd


def pull_dataset(hospital: str):
    filename = 'hospital_' + hospital + '_data.xlsx'
    df =  pd.read_excel(filename)

    return df
