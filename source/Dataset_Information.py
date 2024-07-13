'''
This python code is used to get basic information about the dataset - Telco customer churn 
Created Date: 11/22/2022
Author: Anagha Dhekne, Shravan Sailada
Last Modified: 11/22/2022
'''

import Churn_Prediction_Utils 
import File_Operations
import Global_Defs

import pandas as pd

'''
This function is used to get information about shape of dataset
Its column details such as name, type, unique values, number of missing entries 
It also provides data description including count, mean, standard deviation, minimum, maximum and percentile values
Parameters: df - dataframe consisting dataset
'''
def getDataInformation(df,path):
  pd.set_option('display.max_columns', None)
  information = Global_Defs.getDataInformation()

  File_Operations.deleteFile(path)
  file = File_Operations.openFile(path,"w")
  # get the shape of dataset
  information.append("The shape of dataset is: "+ str(df.shape))

  # get the columns of dataset
  information.append("\n\n\nThe columns of dataset are: \n"+ str(df.columns)) 

  # get the dataset information
  information.append("\n\n\nThe dataset details are: \n"+ str(df.info)) 

  # get the dataset description
  information.append("\n\n\nThe dataset description is: \n"+ str(df.describe().T))

  # get the unique values of the features from dataset 
  numeric_columns = Churn_Prediction_Utils.getNumericColumns(df)
  categorical_columns = Churn_Prediction_Utils.getCategoricalColumns(df)
  information.append("\n\n\nThe numerical columns are: \n"+ str(numeric_columns.columns.tolist()))
  information.append("\n\n\nThe categorical Columns are: \n"+ str(categorical_columns.columns.tolist()))
  information.append("\n\n\nThe unique values in categorical columns are: \n")
  information.append(str([f'{column}: {categorical_columns[column].unique()}' for column in categorical_columns]))

  # check if dataset has any null values present or not
  df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
  information.append("\n\n\nThe number of missing values in dataset are: \n"+ str(df.isnull().sum()))

  File_Operations.writeFile(file,information) 
  File_Operations.closeFile(file)
  Global_Defs.setDataInformation([])
