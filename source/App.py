# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
import os
import joblib
import pandas as pd

import Global_Defs
import Churn_Prediction_Utils
import Data_Preprocessing

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
UPLOAD_FOLDER = Global_Defs.uploadFolder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
bootstrap = Bootstrap(app)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/upload", methods=["POST", "GET"])
def upload():
    uploaded_files = request.files.getlist('file')
    file = request.files['file']
    if file.filename == '':
        flash('No Selected File', 'warning')
        return render_template('index.html')
    for file in uploaded_files:
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return redirect(url_for('predict'))
          

@app.route("/predict", methods=["POST", "GET"])
def predict():
    fileList = os.listdir(UPLOAD_FOLDER)
    filePath = ''
    for file in fileList:
        filePath = os.path.join(UPLOAD_FOLDER,file)
    df = Churn_Prediction_Utils.loadDataset(filePath)
    df = Data_Preprocessing.preprocessData(df)
    dataset = pd.DataFrame(columns=Global_Defs.columnlist)
    for col_name in df.columns:
        dataset[col_name] = df[col_name]
    dataset.fillna(0, inplace=True)
    loaded_rf = joblib.load("./output/random_forest.joblib")
    result = loaded_rf.predict(dataset)
    return render_template('success.html',result=result)

# main driver function
if __name__ == '__main__':
	app.run()
