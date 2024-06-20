import os
from flask import Flask, request, jsonify
import pandas as pd
from sklearn import metrics
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, precision_score, recall_score, f1_score
from datetime import datetime
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Permitir todas as origens

# Load and preprocess the dataset
avc = pd.read_csv('healthcare-dataset-stroke-data-teste.csv')
avc = avc.drop(['id'], axis=1)
avc['bmi'] = avc['bmi'].fillna(avc['bmi'].mean())
avc = avc.replace({
    'gender': {'Male': 0, 'Female': 1, 'Other': 2},
    'ever_married': {'Yes': 0, 'No': 1},
    'work_type': {'Private': 0, 'Self-employed': 1, 'Govt_job': 2, 'children': 3, 'Never_worked': 4},
    'smoking_status': {'formerly smoked': 0, 'never smoked': 1, 'smokes': 2, 'Unknown': 3},
    'Residence_type': {'Urban': 0, 'Rural': 1}
})

# Oversampling
oversample = SMOTE(random_state=42)
avc_x = avc.drop(['stroke'], axis=1)
avc_y = avc['stroke']
x_train_res, y_train_res = oversample.fit_resample(avc_x, avc_y.to_numpy())
x_train, x_test, y_train, y_test = train_test_split(x_train_res, y_train_res, test_size=0.2, random_state=42)

# Train models
models = [
    ['Logistic Regression', LogisticRegression(random_state=42, max_iter=200)],
    ['SVM', SVC(random_state=42, probability=True)],
    ['KNeighbors', KNeighborsClassifier()],
    ['Decision Tree', DecisionTreeClassifier(random_state=42)],
    ['Random Forest', RandomForestClassifier(random_state=42)]
]

# Train all models initially
for name, model in models:
    model.fit(x_train, y_train)

def evaluate_models(x_test, y_test):
    results = []
    for name, model in models:
        start_time = datetime.now()
        y_pred = model.predict(x_test)
        end_time = datetime.now()
        execution_time = (end_time - start_time).total_seconds()

        try:
            accuracy = accuracy_score(y_test, y_pred)
        except Exception as e:
            accuracy = str(e)
        try:
            precision = precision_score(y_test, y_pred)
        except Exception as e:
            precision = str(e)
        try:
            recall = recall_score(y_test, y_pred)
        except Exception as e:
            recall = str(e)
        try:
            f1 = f1_score(y_test, y_pred)
        except Exception as e:
            f1 = str(e)

        result = {
            'Model': name,
            'Accuracy': accuracy,
            'Precision': precision,
            'Recall': recall,
            'F1': f1,
            'Execution Time (s)': execution_time
        }

        # Only calculate ROC AUC if there are at least two classes in y_test
        try:
            if len(set(y_test)) > 1:
                roc = roc_auc_score(y_test, y_pred)
                result['ROC AUC'] = roc
            else:
                result['ROC AUC'] = 'undefined'
        except Exception as e:
            result['ROC AUC'] = str(e)

        results.append(result)
    
    # Order results by Recall in descending order
    results = sorted(results, key=lambda x: x['Recall'], reverse=True)
    return results

def get_recall(model, x_test, y_test):
    y_pred = model.predict(x_test)
    return recall_score(y_test, y_pred)

def calculate_majority_prediction(predictions):
    count = sum(predictions)
    majority = count > len(predictions) / 2
    return 'Sim' if majority else 'Não'

def calculate_probability(predictions, models, input_df):
    majority = [model for model, pred in zip(models, predictions) if pred == 1]
    if not majority:
        return 0.0
    best_model = max(majority, key=lambda model: get_recall(model[1], x_test, y_test))
    proba = best_model[1].predict_proba(input_df)[0][1]
    return proba

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    try:
        data = request.json
        input_df = pd.DataFrame([data])
        input_df = input_df.replace({
            'gender': {'Male': 0, 'Female': 1, 'Other': 2},
            'ever_married': {'Yes': 0, 'No': 1},
            'work_type': {'Private': 0, 'Self-employed': 1, 'Govt_job': 2, 'children': 3, 'Never_worked': 4},
            'smoking_status': {'formerly smoked': 0, 'never smoked': 1, 'smokes': 2, 'Unknown': 3},
            'Residence_type': {'Urban': 0, 'Rural': 1}
        }).infer_objects()

        results = []
        predictions = []
        for name, model in models:
            start_time = datetime.now()
            y_pred = model.predict(input_df)
            predictions.append(y_pred[0])
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()

            results.append({
                'Model': name,
                'Prediction': 'Sim' if y_pred[0] == 1 else 'Não',
                'Execution Time (s)': execution_time
            })

        majority_prediction = calculate_majority_prediction(predictions)
        probability = calculate_probability(predictions, models, input_df)
        evaluation_results = evaluate_models(x_test, y_test)

        return jsonify({
            'predictions': results,
            'evaluation': evaluation_results,
            'result': {
                'Prediction': majority_prediction,
                'Probability': probability
            }
        })
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
