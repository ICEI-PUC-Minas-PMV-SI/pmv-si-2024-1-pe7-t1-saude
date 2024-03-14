import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

avc = pd.read_csv('../healthcare-dataset-stroke-data.csv')
#print(avc.to_string())
avc.info()
print(avc.isnull().sum())
print(avc.describe().to_string())
print ("\nValores únicos :  \n",avc.nunique())


fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
avc.plot(kind="hist", y="age", bins=82, color="b", ax=axes[0][0])
avc.plot(kind="hist", y="bmi", bins=87, color="r", ax=axes[0][1])
avc.plot(kind="hist", y="heart_disease", bins=5, color="g", ax=axes[1][0])
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
avc.plot(kind='scatter', x='age', y='avg_glucose_level', alpha=0.5, color='green', ax=axes[0], title="Age vs. avg_glucose_level")
avc.plot(kind='scatter', x='bmi', y='avg_glucose_level', alpha=0.5, color='red', ax=axes[1], title="bmi vs. avg_glucose_level")
plt.show()

labels = avc['stroke'].value_counts(sort=True).index
sizes = avc['stroke'].value_counts(sort=True)
colors = ["lightblue","red"]
explode = (0.05,0)
plt.figure(figsize=(7,7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90,)
plt.title('Porcentagem de pessoas com AVC no dataset')
plt.show()


label_encoder = LabelEncoder()
scaler = StandardScaler()
dados_processados = avc.apply(lambda x: label_encoder.fit_transform(x) if x.dtype == 'O' else x)
dados_normalizados = pd.DataFrame(scaler.fit_transform(dados_processados), columns=dados_processados.columns)
cov_matrix = abs(dados_normalizados.cov())
plt.figure(figsize=(10, 10))
sns.heatmap(cov_matrix, annot=True, cmap='copper', fmt='.2f', linewidths=.5)
plt.title('Mapa de calor')
plt.show()