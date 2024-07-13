import Churn_Prediction_Utils

colors = ['#007bc1', '#ca3c3d', '#f0aa1f', '#408b35', '#da3227']
datasetFilePath = "./resources/Telco_Customer_Churn.csv"
dataInfoFilePath = "./output/Dataset_Information.txt"
demographicStatsFilePath = "./output/DemographicStats.html"
evalReportFilePath = "./output/Report.csv"
confusionMatrixFilePath = "./output/Confusionmatrix.jpg"
custAccountInfoFilePath = "./output/CustomerAccountInformation.html"
serviceUsageInfoFilePath = "./output/ServiceUsageInformation.html"
customerChurnInfoFilePath = "./output/CustomerChurnInformation.html"
uploadFolder = 'C:/Users/CE-OFFICE/Desktop/DS Project/DS Project/Code/resources/upload'
pathPreprocessing = "./output/Dataset_Info_Preprocessing.txt"
services = ['Phone Service', 'Multiple Lines', 'Internet Service', 'Online Security', 'Online Backup', 'Device Protection', 'Tech Support', 'Streaming TV', 'Streaming Movies']
dataset = Churn_Prediction_Utils.loadDataset(datasetFilePath)
datainformation = []
columnlist = ['Latitude', 'Longitude', 'Tenure Months', 'Monthly Charges',
       'Total Charges', 'Score', 'CLTV',
       'Contract_Month-to-month', 'Contract_One year', 'Contract_Two year',
       'Payment Method_Bank transfer (automatic)',
       'Payment Method_Credit card (automatic)',
       'Payment Method_Electronic check', 'Payment Method_Mailed check',
       'Gender_Female', 'Gender_Male', 'Internet Service_DSL',
       'Internet Service_Fiber optic', 'Internet Service_No',
       'Multiple Lines_No', 'Multiple Lines_No phone service',
       'Multiple Lines_Yes', 'Online Security_No',
       'Online Security_No internet service', 'Online Security_Yes',
       'Online Backup_No', 'Online Backup_No internet service',
       'Online Backup_Yes', 'Device Protection_No',
       'Device Protection_No internet service', 'Device Protection_Yes',
       'Tech Support_No', 'Tech Support_No internet service',
       'Tech Support_Yes', 'Streaming TV_No',
       'Streaming TV_No internet service', 'Streaming TV_Yes',
       'Streaming Movies_No', 'Streaming Movies_No internet service',
       'Streaming Movies_Yes', 'Partner_No', 'Partner_Yes', 'Dependents_No',
       'Dependents_Yes', 'Senior Citizen_No', 'Senior Citizen_Yes',
       'Paperless Billing_No', 'Paperless Billing_Yes', 'Phone Service_No',
       'Phone Service_Yes']

def getColors():
    return colors

def getServices():
    return services

def getDatasetFilePath():
    return datasetFilePath

def getPathPreprocessing():
    return pathPreprocessing

def getCustomerChurnInfoFilePath():
    return customerChurnInfoFilePath

def getConfusionMatrixFilePath():
    return confusionMatrixFilePath

def getEvalReportFilePath():
    return evalReportFilePath

def getDataInfoFilePath():
    return dataInfoFilePath

def getCustAccountInfoFilePath():
    return custAccountInfoFilePath

def getServiceUsageInfoFilePath():
    return serviceUsageInfoFilePath

def getDemographicStatsFilePath():
    return demographicStatsFilePath

def getDataSet():
    return dataset

def getDataInformation():
    return datainformation

def setDataInformation(param):
    datainformation = param