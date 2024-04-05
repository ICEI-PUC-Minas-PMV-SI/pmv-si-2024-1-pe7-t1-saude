import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

avc = pd.read_csv('../healthcare-dataset-stroke-data.csv')
# print(avc.to_string())
avc.info()
print(avc.isnull().sum())
print("\nValores ever_married: \n", avc.ever_married.value_counts())
print("\nValores smoking_status: \n",avc.smoking_status.value_counts())
print("\nValores work_type: \n",avc.work_type.value_counts())
print("\nValores gender: \n",avc.gender.value_counts())
print("\nValores Residence_type: \n",avc.Residence_type.value_counts())
print(avc.age.isin([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]).sum())
print("\nValores únicos :  \n", avc.nunique())

# plt.rcParams['figure.dpi'] = 500

# grafico de valores interessantes
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

# grafico de correlação fumante X avc
fig = plt.figure(figsize=(20, 8), facecolor='white')
gs = fig.add_gridspec(1, 2)
ax = [None for _ in range(2)]
ax[0] = fig.add_subplot(gs[0, 0])
ax[1] = fig.add_subplot(gs[0, 1])

ax[0].text(-0.6, 2200, "Distribuição de pessoas por histórico de tabagismo", fontsize=15, fontweight='bold',
           fontfamily='monospace')
ax[0].text(-0.6, 2100, "Categorizando os 4 tipos descritos no dataset", fontsize=10, fontweight='light',
           fontfamily='monospace')

ax[1].text(-0.7, 2100, "Correlação de tabagismo com AVC", fontsize=15, fontweight='bold', fontfamily='monospace')
ax[1].text(-0.7, 2000, "Quantas pessoas em cada categoria tiveram AVC?", fontsize=10, fontweight='light',
           fontfamily='monospace')

palette1 = ["silver" for _ in range(4)]
palette1[1] = "grey"
palette2 = ["lightcoral", "palegreen"]

sns.countplot(data=avc, x='smoking_status', ax=ax[0], order=['formerly smoked', 'never smoked', 'smokes', 'Unknown'],
              palette=palette1, zorder=2)
sns.countplot(data=avc, x='smoking_status', ax=ax[1], hue='stroke',
              order=['formerly smoked', 'never smoked', 'smokes', 'Unknown'], zorder=2, palette=palette2)

for i in range(2):
    ax[i].grid(color='black', linestyle=':', axis='y', zorder=0, dashes=(5, 10))
    ax[i].set_ylabel('')
    ax[i].set_xlabel('')

    for direction in ['top', 'right', 'left']:
        ax[i].spines[direction].set_visible(False)

plt.tight_layout()
plt.show()

# grafico de emprego X avc
fig = plt.figure(figsize=(20, 8), facecolor='white')
gs = fig.add_gridspec(1, 2)
ax = [None for _ in range(2)]
ax[0] = fig.add_subplot(gs[0, 0])
ax[1] = fig.add_subplot(gs[0, 1])

ax[0].text(-0.6, 3900, "Distribuição de pessoas por vínculo empregatício", fontsize=15, fontweight='bold',
           fontfamily='monospace')
ax[0].text(-0.6, 3750, "Categorizando os 5 tipos descritos no dataset", fontsize=10, fontweight='light',
           fontfamily='monospace')

ax[1].text(-0.7, 3700, "Correlação de vínculo empregatício com AVC", fontsize=15, fontweight='bold',
           fontfamily='monospace')
ax[1].text(-0.7, 3550, "Quantas pessoas em cada estado empregatício tiveram AVC?", fontsize=10, fontweight='light',
           fontfamily='monospace')

palette1 = ["wheat" for _ in range(5)]
palette1[3] = "gold"
palette2 = ["lightcoral", "palegreen"]

sns.countplot(data=avc, x='work_type', ax=ax[0],
              order=['children', 'Govt_jov', 'Never_worked', 'Private', 'Self-employed'], palette=palette1, zorder=2)
sns.countplot(data=avc, x='work_type', ax=ax[1], hue='stroke',
              order=['children', 'Govt_jov', 'Never_worked', 'Private', 'Self-employed'], zorder=2, palette=palette2)

for i in range(2):
    ax[i].grid(color='black', linestyle=':', axis='y', zorder=0, dashes=(5, 10))
    ax[i].set_ylabel('')
    ax[i].set_xlabel('')

    for direction in ['top', 'right', 'left']:
        ax[i].spines[direction].set_visible(False)

plt.tight_layout()
plt.show()

# grafico correlação casado X avc
fig = plt.figure(figsize=(20, 8), facecolor='white')
gs = fig.add_gridspec(1, 2)
ax = [None for _ in range(2)]
ax[0] = fig.add_subplot(gs[0, 0])
ax[1] = fig.add_subplot(gs[0, 1])

ax[0].text(-0.6, 3900, "Distribuição de pessoas por histórico de estado civil", fontsize=15, fontweight='bold',
           fontfamily='monospace')
ax[0].text(-0.6, 3750, "Categorizando se as pessoas já se casaram ou não", fontsize=10, fontweight='light',
           fontfamily='monospace')

ax[1].text(-0.7, 3700, "Correlação de histórico de estado civil com AVC", fontsize=15, fontweight='bold',
           fontfamily='monospace')
ax[1].text(-0.7, 3550, "Quantas pessoas já casadas tiveram AVC?", fontsize=10, fontweight='light',
           fontfamily='monospace')

palette1 = ["salmon" for _ in range(2)]
palette1[1] = "firebrick"
palette2 = ["lightcoral", "palegreen"]

sns.countplot(data=avc, x='ever_married', ax=ax[0], order=['No', 'Yes'], palette=palette1, zorder=2)
sns.countplot(data=avc, x='ever_married', ax=ax[1], hue='stroke', order=['No', 'Yes'], zorder=2, palette=palette2)

for i in range(2):
    ax[i].grid(color='black', linestyle=':', axis='y', zorder=0, dashes=(5, 10))
    ax[i].set_ylabel('')
    ax[i].set_xlabel('')

    for direction in ['top', 'right', 'left']:
        ax[i].spines[direction].set_visible(False)

plt.tight_layout()
plt.show()

#grafico de correlação de genero X avc
fig = plt.figure(figsize=(20, 8), facecolor='white')
gs = fig.add_gridspec(1, 2)
ax = [None for _ in range(2)]
ax[0] = fig.add_subplot(gs[0, 0])
ax[1] = fig.add_subplot(gs[0, 1])

ax[0].text(-0.6, 3900, "Distribuição de pessoas por sexo", fontsize=15, fontweight='bold',
           fontfamily='monospace')
ax[0].text(-0.6, 3750, "Categorizando sexo das pessoas do dataset", fontsize=10, fontweight='light',
           fontfamily='monospace')

ax[1].text(-0.7, 3700, "Correlação de sexo com AVC", fontsize=15, fontweight='bold',
           fontfamily='monospace')
ax[1].text(-0.7, 3550, "Quantas pessoas de cada sexo tiveram AVC?", fontsize=10, fontweight='light',
           fontfamily='monospace')

palette1 = ["slateblue" for _ in range(2)]
palette1[1] = "darkslateblue"
palette2 = ["lightcoral", "palegreen"]

sns.countplot(data=avc, x='gender', ax=ax[0], order=['Male', 'Female'], palette=palette1, zorder=2)
sns.countplot(data=avc, x='gender', ax=ax[1], hue='stroke', order=['Male', 'Female'], zorder=2, palette=palette2)

for i in range(2):
    ax[i].grid(color='black', linestyle=':', axis='y', zorder=0, dashes=(5, 10))
    ax[i].set_ylabel('')
    ax[i].set_xlabel('')

    for direction in ['top', 'right', 'left']:
        ax[i].spines[direction].set_visible(False)

plt.tight_layout()
plt.show()

# grafico relação idade X avc
fig = plt.figure(figsize=(20, 8), facecolor='white')
ax = [None for i in range(2)]
gs = fig.add_gridspec(1, 1)
gs.update(wspace=0, hspace=0.8)

ax[0] = fig.add_subplot(gs[0, 0])
ax[0].text(-20, 0.04, 'Correlação entre idade e AVC', fontsize=21, fontweight='bold', fontfamily='monospace')
ax[0].text(-20, 0.035, 'A curva vermelha indica a incidência de AVC por idade', fontsize=16, fontweight='light',
           fontfamily='monospace')
sns.kdeplot(data=avc[avc.stroke == 1], x='age', ax=ax[0], shade=True, color='lightcoral', alpha=1)

ax[0].set_yticklabels('')
ax[0].set_ylabel('')
ax[0].tick_params(axis='y', length=0)
for direction in ['top', 'right', 'left']:
    ax[0].spines[direction].set_visible(False)

plt.tight_layout()
plt.show()


# grafico de distribuição por atributo
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 10))
avc.plot(kind="hist", y="age", bins=104, color="b", ax=axes[0][0])
avc.plot(kind="hist", y="bmi", bins=418, color="r", ax=axes[0][1])
avc.plot(kind="hist", y="heart_disease", bins=20, color="g", ax=axes[0][2])
avc.plot(kind="hist", y="avg_glucose_level", bins=107, color="purple", ax=axes[1][0])
avc.plot(kind="hist", y="hypertension", bins=20, color="gray", ax=axes[1][1])
avc.plot(kind="hist", y="stroke", bins=20, color="orange", ax=axes[1][2])
fig.tight_layout()
plt.show()

# grafico de correlação entre atributos
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 8))
avc.plot(kind='scatter', x='age', y='avg_glucose_level', alpha=0.6, color='green', ax=axes[0][0],
         title="Idade X Nível de glicose")
avc.plot(kind='scatter', x='bmi', y='avg_glucose_level', alpha=0.6, color='red', ax=axes[0][1],
         title="IMC X Nível de glicose")
avc.plot(kind='scatter', x='bmi', y='age', alpha=0.1, color='blue', ax=axes[1][0],
         title="IMC X Idade")
avc.plot(kind='scatter', x='bmi', y='stroke', alpha=0.6, color='orange', ax=axes[1][1],
         title="IMC X AVC")
fig.tight_layout()
plt.show()

# grafico de porcentagem de avc
labels = avc['stroke'].value_counts(sort=True).index
sizes = avc['stroke'].value_counts(sort=True)
colors = ["lightblue", "red"]
explode = (0.05, 0)
plt.figure(figsize=(7, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, )
plt.title('Porcentagem de pessoas com AVC no dataset')
plt.show()

# mapa de calor
label_encoder = LabelEncoder()
scaler = StandardScaler()
dados_processados = avc.apply(lambda x: label_encoder.fit_transform(x) if x.dtype == 'O' else x)
dados_normalizados = pd.DataFrame(scaler.fit_transform(dados_processados), columns=dados_processados.columns)
cov_matrix = abs(dados_normalizados.cov())
plt.figure(figsize=(10, 10))
sns.heatmap(cov_matrix, annot=True, cmap='copper', fmt='.2f', linewidths=.5)
plt.title('Mapa de calor')
plt.show()
