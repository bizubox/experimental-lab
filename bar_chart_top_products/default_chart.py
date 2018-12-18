import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Read data
df = pd.read_csv('data/mock_produtos.csv')
# Group by product
df = df.groupby('Produto', as_index=False).agg({"Receita": "sum"})
# Sort value
df = df.sort_values(['Receita'],ascending=[False]).reset_index(drop=True)
# Set order value
df['Ordem'] = list(range(1,6))
df.Produto = df.apply(lambda row: str(row.Ordem) + ' ' + row.Produto, axis=1)
print(df.head())
#objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
#y_pos = np.arange(len(objects))
fig  = plt.figure()
plt.barh(df.Produto, df.Receita, align='center')

#plt.yticks(y_pos, objects)
plt.xlabel('Faturamento (R$)')
plt.title('Top 5 produtos')
fig.set_size_inches(8.7*1.91,1*8.7)
fig.savefig('default_chart.png', dpi=100)