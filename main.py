import pandas as pd
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from clean_up_raw_data import clean_up_raw_data
mpl.use('TkAgg')

df_ = clean_up_raw_data()


sns.lineplot(
    data=df_,
    x='time',
    y='biomass',
    hue = 'treatment'
)
plt.show()