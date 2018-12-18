import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Say, "the default sans-serif font is Rajdhani"
plt.rcParams['font.sans-serif'] = "Rajdhani"
# Then, "ALWAYS use sans-serif fonts"
plt.rcParams['font.family'] = "sans-serif"

# Read data
df = pd.read_csv('data/mock_produtos.csv')
# Group by product
df = df.groupby('Produto', as_index=False).agg({"Receita": "sum"})
# Sort value
df = df.sort_values(['Receita'],ascending=[False]).reset_index(drop=True)
# Set order value
df['Ordem'] = list(range(1,6))
df.Produto = df.apply(lambda row: str(row.Ordem) + ' ' + row.Produto, axis=1)

#Set new seaborn chart
sns.set(style="whitegrid", font="Rajdhani")
# Color pallet
flatui = ["#14dce5", "#00b5bd", "#00b5bd", "#00b5bd", "#00b5bd", "#00b5bd"]
sns.set_palette(flatui)
# Font size
plt.rcParams.update({'font.size': 20})
plt.rcParams.update({'ytick.labelsize': 20})
# Title
fig  = plt.figure()
fig.suptitle('Top 5 produtos (R$)', fontsize=35, color="#95a5a6")
# Horizontal Barchart
g = sns.barplot(y="Produto", x="Receita",data=df)
g.set_xlabel('')
g.set_ylabel('')
# Configure ticker color and size
g.tick_params(axis='y', colors="#95a5a6", which = 'major', pad = 10)

# add y value over the bar
for index, row in df.iterrows():
    if (index == 0):
        g.text(500, index, str(round(row.Receita,2)),
            va='center', color='#ffffff', fontweight='bold')
    else:
        g.text(500, index, str(round(row.Receita,2)),
            va='center', color='#ffffff')
            
sns.despine(left=True, bottom=True)
g.set_xticks([])

# Set the top 1 label to bold
y_ticks = g.yaxis.get_major_ticks()
y_ticks[0].label.set_color('#14dce5')
y_ticks[0].label.set_fontweight('bold')

fig.set_size_inches(8.7*1.91,1*8.7)
fig.savefig('output.png', dpi=100)

'''
References
https://matplotlib.org/gallery/showcase/bachelors_degrees_by_gender.html#sphx-glr-gallery-showcase-bachelors-degrees-by-gender-py
https://seaborn.pydata.org/examples/horizontal_barplot.html
https://stackoverflow.com/questions/32528154/bar-chart-in-seaborn
https://stackoverflow.com/questions/12444716/how-do-i-set-the-figure-title-and-axes-labels-font-size-in-matplotlib
'''

    
    
    