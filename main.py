import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import plotly.express as px
from clean_up_raw_data import clean_up_raw_data
mpl.use('TkAgg')
sns.set_theme(style="darkgrid")
df_ = clean_up_raw_data()

g = sns.lineplot(
    data=df_,
    x='time',
    y='biomass',
    hue = 'treatment',
    style = 'repetition',
    marker='o'
)
g = sns.lineplot(
    data=df_,
    x='time',
    y='biomass',
    hue = 'treatment'
)
sns.move_legend(g, "upper left", bbox_to_anchor=(.55, .45), frameon=False)
plt.show()