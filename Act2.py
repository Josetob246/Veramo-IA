import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#direccion del archivo
ruta = '/Users/super/Downloads/diabetes.csv'
df = pd.read_csv(ruta)
resumen = df.describe(include='all')
print(df.head(10)) 
print(resumen)
#fill null data with median
dfm= df.fillna(df.median())
print(dfm)
#normaliza data
df_normalized = (df - df.min()) / (df.max() - df.min())
print(df_normalized)
#histogram with glucose
df['Glucose'].hist(bins=5, edgecolor='black')
plt.title('Glucose before')
plt.xlabel('Glucose')
plt.ylabel('Time')
plt.show()
df_normalized['Glucose'].hist(bins=5, edgecolor='black')
plt.title('Glucose after')
plt.xlabel('Glucose')
plt.ylabel('Time')
plt.show()
#boxplot
third_column_name = df.columns[2]
df.boxplot(column=third_column_name)
plt.title("Blood Pressure")
plt.show()

#scatter plot
colores = ['red' if x > 5 else 'blue' for x in df[df.columns[5]]]
df.plot.scatter(x=df.columns[1], y=df.columns[5],color=colores)

plt.show()

#bar chart
data_outcome = df.iloc[:, 8].value_counts()
barras = data_outcome.head(2)
fig, ax = plt.subplots(figsize=(8, 5))
barras.plot(kind='bar', ax=ax, color=['blue', 'green'])
ax.set_title('Outcome', fontsize=14)
ax.set_xlabel('Categorías')
ax.set_ylabel('Frecuencia')
plt.xticks(rotation=0) 
plt.show()