import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_raw =pd.read_csv('data/kefir_biomass.csv')
df_raw = df_raw.rename(
    columns={
        "TRATAMIENTOS": "treatment",
        "TIEMPO": "time",
        "Rep1": "rep_1",
        "Rep2": "rep_2",
        "Rep3": "rep_3"
    }
)

df_treatment_0 = df_raw[df_raw['treatment'] == 'Testigo']
df_treatment_1 = df_raw[df_raw['treatment'] == '20 W/cm2 15 seg']
df_treatment_2 = df_raw[df_raw['treatment'] == '20 W/cm2 1 min']
df_treatment_3 = df_raw[df_raw['treatment'] == '34 W/cm2 15']
df_treatment_4 = df_raw[df_raw['treatment'] == '34 W/cm2 1 min']


df_treatment_0['treatment'] = 'T0'
df_treatment_1['treatment'] = 'T1'
df_treatment_2['treatment'] = 'T2'
df_treatment_3['treatment'] = 'T3'
df_treatment_4['treatment'] = 'T4'

df_treatment_0_rep_1 = df_treatment_0[["time", "rep_1", "treatment"]]
df_treatment_0_rep_2 = df_treatment_0[["time", "rep_2", "treatment"]]
df_treatment_0_rep_3 = df_treatment_0[["time", "rep_3", "treatment"]]
df_treatment_0_ = df_treatment_0_rep_1
df_treatment_0_["rep_"] = 1
df_treatment_0_rep_2["rep_"] = 2
df_treatment_0_rep_3["rep_"] = 3

df_treatment_0_ = df_treatment_0_.rename(
    columns={"rep_1":"biomass"}
)
df_treatment_0_rep_2 = df_treatment_0_rep_2.rename(
    columns={"rep_2":"biomass"}
)
df_treatment_0_rep_3 = df_treatment_0_rep_3.rename(
    columns={"rep_3":"biomass"}
)

frames = [df_treatment_0_, df_treatment_0_rep_2, df_treatment_0_rep_3]
df_treatment_0 = pd.concat(frames)

sns.scatterplot(
    data=df_treatment_0,
    x='time',
    y='biomass',
    hue = 'rep_'
)
plt.show()
