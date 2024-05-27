import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix
import pickle
data = pd.read_csv('sample2.csv')
pd.options.display.max_columns = None
pd.options.display.max_rows = None
data.fillna(0, inplace=True)
test_t=data[:1].drop(['Risk'], axis=1)
X = data.drop(['Risk'], axis=1)
y = data['Risk']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = OneVsRestClassifier(SVC())
model.fit(X_train, y_train.apply(str) )
current_dir = os.path.dirname(os.path.realpath(__file__))
model_pkl_file = os.path.join(current_dir, "iris_classifier_model.pkl")

with open(model_pkl_file, 'wb') as file:  
    pickle.dump(model, file)