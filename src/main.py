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
print(avc.age.isin([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]).sum())
print("\nValores únicos :  \n", avc.nunique())

# plt.rcParams['figure.dpi'] = 500

fig = plt.figure(figsize=(2.7, 1.1), facecolor='#f6f5f5')
gs = fig.add_gridspec(1, 1)
gs.update(wspace=0, hspace=0)

background_color = "#f6f5f5"

ax0 = fig.add_subplot(gs[0, 0])
ax0.set_facecolor(background_color)
for s in ["top", "right", 'left', 'bottom']:
    ax0.spines[s].set_visible(False)
ax0.set_xticks([])
ax0.set_yticks([])
ax0.grid(which='major', axis='y', zorder=0, color='#EEEEEE')
ax0.text(-0.12, 1, 'Valores relevantes', color='black', fontsize=7, ha='left', weight='bold', va='bottom')
ax0.text(-0.12, 0.99, 'Uma olhada rápida em valores encontrados no dataset', color='#292929', fontsize=5, ha='left',
         va='top')
ax0.text(0.15, 0.3, avc.bmi.isnull().sum(), color='red', fontsize=20, ha='center', weight='bold', va='bottom')
ax0.text(0.15, 0.3, 'Valores nulos de IMC \nQual estratégia utilizar \npara lidar?', color='dimgray', fontsize=6,
         ha='center', va='top', weight='bold')
ax0.text(0.85, 0.3, "%.1f" % avc.bmi.mean(), color='red', fontsize=20, ha='center', weight='bold', va='bottom')
ax0.text(0.85, 0.3, 'IMC médio no Dataset \nA média mundial é \nem torno de 25%', color='dimgray', fontsize=6,
         ha='center', va='top', weight='bold')
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 10))
avc.plot(kind="hist", y="age", bins=104, color="b", ax=axes[0][0])
avc.plot(kind="hist", y="bmi", bins=418, color="r", ax=axes[0][1])
avc.plot(kind="hist", y="heart_disease", bins=5, color="g", ax=axes[0][2])
avc.plot(kind="hist", y="avg_glucose_level", bins=107, color="purple", ax=axes[1][0])
avc.plot(kind="hist", y="hypertension", bins=5, color="gray", ax=axes[1][1])
avc.plot(kind="hist", y="stroke", bins=5, color="orange", ax=axes[1][2])
fig.tight_layout()
plt.show()

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 8))
avc.plot(kind='scatter', x='age', y='avg_glucose_level', alpha=0.6, color='green', ax=axes[0][0],
         title="Idade X Nível de glicose")
avc.plot(kind='scatter', x='bmi', y='avg_glucose_level', alpha=0.6, color='red', ax=axes[0][1],
         title="IMC X Nível de glicose")
avc.plot(kind='scatter', x='age', y='avg_glucose_level', alpha=0.6, color='blue', ax=axes[1][0],
         title="Idade X Nível de glicose")
avc.plot(kind='scatter', x='age', y='stroke', alpha=0.6, color='orange', ax=axes[1][1],
         title="Idade X AVC")
fig.tight_layout()
plt.show()

labels = avc['stroke'].value_counts(sort=True).index
sizes = avc['stroke'].value_counts(sort=True)
colors = ["lightblue", "red"]
explode = (0.05, 0)
plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, )
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
