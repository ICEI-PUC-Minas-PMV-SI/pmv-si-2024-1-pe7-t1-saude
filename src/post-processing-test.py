import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

avc = pd.read_csv('../healthcare-dataset-stroke-data-teste.csv')

#valores nulos
print(avc.bmi.isnull().sum())
print(avc.bmi.mean())
avc['bmi'].fillna(avc['bmi'].mean(),inplace = True)
print(avc.bmi.isnull().sum())
print(avc.bmi.mean())

#variáveis categóricas
columns_temp = ['gender', 'ever_married', 'work_type', 'smoking_status', 'Residence_type']
for col in columns_temp :
    print('column :', col)
    for index, unique in enumerate(avc[col].unique()) :
        print(unique, ':', index)
    print('_'*45)
avc = avc.replace(
    {'gender' : {'Male' : 0, 'Female' : 1, 'Other' : 2}}
)
avc =  avc.replace(
    {'ever_married' : {'Yes' : 0, 'No' : 1}}
)
avc =  avc.replace(
    {'work_type' : {'Private' : 0, 'Self-employed' : 1, 'Govt_job' : 2, 'children' : 3, 'Never_worked' : 4}}
)
avc =  avc.replace(
    {'smoking_status' : {'formerly smoked' : 0, 'never smoked' : 1, 'smokes' : 2, 'Unknown' : 3}}
)
avc =  avc.replace(
    {'Residence_type' : {'Urban' : 0, 'Rural' : 1}}
)
#print(avc.to_string())
print(avc.describe().to_string())

#normalização
mms = MinMaxScaler()
avc['age'] = mms.fit_transform(avc[['age']])
avc['bmi'] = mms.fit_transform(avc[['bmi']])
avc['avg_glucose_level'] = mms.fit_transform(avc[['avg_glucose_level']])
print(avc.describe().to_string())

#oversampling