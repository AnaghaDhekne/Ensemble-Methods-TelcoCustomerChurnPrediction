'''
This python code has all the utility functions used for Telco customer churn prediction
Created Date: 11/22/2022
Author: Anagha Dhekne, Shravan Sailada
Last Modified: 11/22/2022
'''
import Global_Defs

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score, f1_score, ConfusionMatrixDisplay, r2_score

'''
This function is used to get dataset from csv/excel file
Parameters: filename - string represent file path to dataset
'''
def loadDataset(filename):  
  return pd.read_csv(filename)

def getNumericColumns(df):
  return df.select_dtypes(include='number')

def getCategoricalColumns(df):
  return df.select_dtypes(include='object')

def getTrainingData(df, target):
  y = df[target]
  X = df.drop(columns=[target])
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
  scaler = StandardScaler()
  X_train[['Tenure Months','Monthly Charges','Total Charges']] = scaler.fit_transform(X_train[['Tenure Months','Monthly Charges','Total Charges']])

  smt = SMOTE(random_state=42)
  smt.fit_resample(X_train, y_train)
  return X_train,y_train

def getTestData(df, target):
  y = df[target]
  X = df.drop(columns=[target])
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
  return X_test, y_test
 
def buildPredictionModel(df,target):
  X_train, y_train = getTrainingData(df,target)
  rf_clf = RandomForestClassifier(n_estimators=500, max_samples=400, n_jobs=-1, random_state=42)
  rf_clf.fit(X_train, y_train)
  return rf_clf

def model_eval(model, df, target):
  X_test, y_test = getTestData(df, target)
  y_pred = model.predict(X_test)
  report = classification_report(y_test, y_pred,output_dict=True)
  reportDf = pd.DataFrame(report)
  reportDf.to_csv(Global_Defs.getEvalReportFilePath())
  cm=confusion_matrix(y_test, y_pred, labels=y_test.unique())
  disp = ConfusionMatrixDisplay(cm, display_labels=y_test.unique()).plot(cmap='cividis')
  plt.savefig(Global_Defs.getConfusionMatrixFilePath())
  m1 = roc_auc_score(y_test, y_pred)
  m2 = f1_score(y_test, y_pred)
  print('ROC_AUC_Score: {:.04f}'.format(m1))
  print('F1 Score: {:.04f}'.format(m2))

def model_save(model):
  joblib.dump(model, "./output/random_forest.joblib")
  
 

 






