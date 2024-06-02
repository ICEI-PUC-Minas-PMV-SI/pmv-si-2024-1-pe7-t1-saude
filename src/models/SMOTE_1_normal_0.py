import pandas as pd
from sklearn import metrics
import seaborn as sns
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, precision_score, recall_score, f1_score
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from datetime import datetime


avc = pd.read_csv('../../healthcare-dataset-stroke-data-teste.csv')
avc = avc.drop(['id'], axis = 1)

# valores nulos
print(avc.bmi.isnull().sum())
print(avc.bmi.mean())
avc['bmi'].fillna(avc['bmi'].mean(), inplace=True)
print(avc.bmi.isnull().sum())
print(avc.bmi.mean())

# variáveis categóricas
columns_temp = ['gender', 'ever_married', 'work_type', 'smoking_status', 'Residence_type']
for col in columns_temp:
    print('column :', col)
    for index, unique in enumerate(avc[col].unique()):
        print(unique, ':', index)
    print('_' * 45)
avc = avc.replace(
    {'gender': {'Male': 0, 'Female': 1, 'Other': 2}}
)
avc = avc.replace(
    {'ever_married': {'Yes': 0, 'No': 1}}
)
avc = avc.replace(
    {'work_type': {'Private': 0, 'Self-employed': 1, 'Govt_job': 2, 'children': 3, 'Never_worked': 4}}
)
avc = avc.replace(
    {'smoking_status': {'formerly smoked': 0, 'never smoked': 1, 'smokes': 2, 'Unknown': 3}}
)
avc = avc.replace(
    {'Residence_type': {'Urban': 0, 'Rural': 1}}
)
# print(avc.to_string())
print(avc.describe().to_string())

# oversampling
oversample = SMOTE(random_state=42)
avc_x = avc.drop(['stroke'], axis = 1)
avc_y = avc['stroke']
x_train_res, y_train_res = oversample.fit_resample(avc_x, avc_y.ravel())

print('After OverSampling, the shape of train_X: {}'.format(x_train_res.shape))
print('After OverSampling, the shape of train_y: {} \n'.format(y_train_res.shape))
print("After OverSampling, counts of label '1': {}".format(sum(y_train_res==1)))
print("After OverSampling, counts of label '0': {}".format(sum(y_train_res==0)))
x_train, x_test, y_train, y_test = train_test_split(x_train_res,y_train_res, test_size = 0.2, random_state = 42)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

#inicialização de vetor dos modelos a serem utilizados
models = []
models.append(['Logistic Regreesion', LogisticRegression(random_state=42, max_iter=200)])
models.append(['SVM', SVC(random_state=42)])
models.append(['KNeighbors', KNeighborsClassifier()])
models.append(['Decision Tree', DecisionTreeClassifier(random_state=42)])
models.append(['Random Forest', RandomForestClassifier(random_state=42)])
lst_1= []

#funcao para imprimir matriz de confusao
def plot_confusion_matrix(y_test, y_prediction, nome):
    cm = metrics.confusion_matrix(y_test, y_prediction)
    ax = plt.subplot()
    ax = sns.heatmap(cm, annot=True, fmt='', cmap="Greens")
    ax.set_xlabel('Prediced labels')
    ax.set_ylabel('True labels')
    ax.set_title(nome)
    ax.xaxis.set_ticklabels(['Dont Had Stroke', 'Had Stroke'])
    ax.yaxis.set_ticklabels(['Dont Had Stroke', 'Had Stroke'])
    plt.show()

#loop para treinamento dos modelos
for m in range(len(models)):
    t1 = datetime.now()
    lst_2= []
    model = models[m][1]
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    t2 = datetime.now()
    delta = t2 - t1
    delta_rf = round(delta.total_seconds(), 3)

    if ('Tree' in models[m][0] ):
        print ('A profundidade da árvore é: ',model.tree_.max_depth)
        profundidade_arvore = model.tree_.max_depth
        plt.figure(figsize=(50,12))
        tree.plot_tree(model, fontsize=5, max_depth=5, feature_names=x_train.columns.values)
        #plt.savefig('teste1', dpi=200)
        #plt.show()
        r = export_text(model, feature_names=x_train.columns.values)
        #print(r)
        #with open('decision_tree.txt', 'w') as f:
        #    f.write("Profudidade: "+ str(model.tree_.max_depth) + '\n')
        #    f.write(export_text(model, feature_names=x_train.columns.values))
    if ('Forest' in models[m][0]):
        fig, axes = plt.subplots(nrows = 1,ncols = 5,figsize = (50,10))
        #myfile = open('floresta.txt', 'w')
        for index in range(0, 100):
            if (index < 5):
                tree.plot_tree(model.estimators_[95+index], fontsize=4, max_depth=3,
                    feature_names = x_train.columns.values,
                    ax = axes[index])
                axes[index].set_title('Profundidade: ' + str(model.estimators_[95+index].tree_.max_depth), fontsize = 8)
                #plt.savefig('teste2', dpi=200)
            #myfile.write("Arvore: "+ str(index)+", Profudidade: "+ str(model.estimators_[index].tree_.max_depth) + '\n')
            #myfile.write(export_text(model.estimators_[index], feature_names=x_train.columns.values) + '\n')
        #myfile.close()
    if ('Neighbors' in models[m][0]):
        print('Parametros: ', model.get_params())

    cm = confusion_matrix(y_test, y_pred)  #Confusion Matrix
    plot_confusion_matrix(y_test, y_pred, models[m][0])
    accuracies = cross_val_score(estimator = model, X = x_train, y = y_train, cv = 10)
    roc = roc_auc_score(y_test, y_pred)  #ROC AUC Score
    precision = precision_score(y_test, y_pred)  #Precision Score
    recall = recall_score(y_test, y_pred)  #Recall Score
    f1 = f1_score(y_test, y_pred)  #F1 Score
    print(models[m][0],':')
    print(cm)
    print('Validation Accuracy Score: ',accuracy_score(y_test, y_pred))
    print('')
    print('Training Accuracy Score: ',accuracy_score(y_train,model.predict(x_train)))
    print('')
    print("K-Fold Validation Mean Accuracy: {:.2f} %".format(accuracies.mean()*100))
    print('')
    print("Standard Deviation: {:.2f} %".format(accuracies.std()*100))
    print('')
    print('ROC AUC Score: {:.2f}'.format(roc))
    print('')
    print('Precision: {:.2f}'.format(precision))
    print('')
    print('Recall: {:.2f}'.format(recall))
    print('')
    print('F1: {:.2f}'.format(f1))
    print(models[m][0], ' leva : ', delta_rf, 'segundos')
    print('')
    print('-----------------------------------')
    print('')
    lst_2.append(models[m][0])
    lst_2.append((accuracy_score(y_test, y_pred))*100)
    lst_2.append(accuracies.mean()*100)
    lst_2.append(accuracies.std()*100)
    lst_2.append(roc)
    lst_2.append(precision)
    lst_2.append(recall)
    lst_2.append(f1)
    lst_2.append(delta_rf)
    lst_1.append(lst_2)

#imprime as métricas de cada modelo
df = pd.DataFrame(lst_1, columns= ['Model', 'Accuracy', 'K-Fold Mean Accuracy', 'Std. Deviation', 'ROC AUC', 'Precision', 'Recall', 'F1', 'Execução(s)'])
df.sort_values(by= ['Recall', 'Precision'], inplace= True, ascending= False)
print (df.to_string())
print ('A profundidade da árvore é ', profundidade_arvore)