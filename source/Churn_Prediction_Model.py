'''
This python code has the definition of main function for Telco Churn prediction
Created Date: 11/22/2022
Author: Anagha Dhekne, Shravan Sailada
Last Modified: 11/22/2022
'''

import Global_Defs
import Data_Preprocessing
import Dataset_Information
import Churn_Prediction_Utils

'''
This is the main function 
It controls flow and execution of operations being performed in the project
The followed steps are: load dataset, get basic data information build the model, save it and evaluate 
'''
def main():
    dataset = Global_Defs.getDataSet()
    dataset = Data_Preprocessing.preprocessData(dataset)
    Dataset_Information.getDataInformation(dataset,Global_Defs.getPathPreprocessing())
    rf_clf = Churn_Prediction_Utils.buildPredictionModel(dataset,"Churn Value")  
    Churn_Prediction_Utils.model_eval(rf_clf,dataset,"Churn Value") 
    Churn_Prediction_Utils.model_save(rf_clf)

if __name__ == "__main__":
    main()