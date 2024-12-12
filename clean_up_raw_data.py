import pandas as pd
import openpyxl
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('TkAgg')


def clean_up_raw_data(
        input_file_name='data/kefir_biomass.xlsx',
        output_file_name='data/kefir_biomass_reshaped.csv'
):
    """

    :param input_file_name: Excel raw data file
    :param output_file_name: CSV data output file
    """
    df_raw = openpyxl.load_workbook(input_file_name)
    df_raw_ws = df_raw.active
    data = df_raw_ws.values
    columns = next(data)[0:]
    df_raw = pd.DataFrame(data, columns=columns)
    df_raw = df_raw.rename(
        columns={
            "TRATAMIENTOS": "treatment",
            "TIEMPO DE FERMENTACIÒN (h)": "time",
            "Repetición 1": "rep_1",
            "Repetición 2": "rep_2",
            "Repetición 3": "rep_3"
        }
    )
    df = df_raw.melt(
        id_vars=['time', 'treatment'],
        value_vars=[
            'rep_1',
            'rep_2',
            'rep_3'
        ],
        var_name='repetition',
        value_name='biomass'
    )
    treatment_list = list(df['treatment'].unique())
    i = 0
    for treatment in treatment_list:
        # print(treatment)
        treatment_mask = df["treatment"].eq(treatment)
        df.loc[treatment_mask, 'treatment'] = 'T' + str(i)
        i=i+1
    df.to_csv(output_file_name, index=False)
    return df
