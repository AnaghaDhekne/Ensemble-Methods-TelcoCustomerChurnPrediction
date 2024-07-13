'''
This python code has the definition of main function for Telco Churn prediction
Created Date: 11/29/2022
Author: Anagha Dhekne, Shravan Sailada
Last Modified: 11/29/2022
'''

import pandas as pd

'''
This is the function called before training the model 
It converts the dataset in appropriate format, removes unnecessary data and null values etc.   
'''
def preprocessData(df):
    
    df.drop(columns=['CustomerID','Lat Long','Count','Country','State','City','Zip Code','Churn Label','Churn Reason'], inplace=True)
    
    df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
    df['Total Charges'] = df['Total Charges'].fillna(0)

    # Creating a dummy variable for some of the categorical variables and dropping the first one.
    encode_data1=pd.get_dummies(df[['Contract', 'Payment Method', 'Gender', 'Internet Service']])
    # Adding the results to the master dataframe
    df=pd.concat([df,encode_data1],axis=1)

    # Creating dummy variables for the variable 'MultipleLines'
    encoded_data2=pd.get_dummies(df['Multiple Lines'],prefix='Multiple Lines')
    #Adding the results to the master dataframe
    df = pd.concat([df,encoded_data2], axis=1)

    # Creating dummy variables for the variable 'OnlineSecurity'.
    encoded_data3 = pd.get_dummies(df['Online Security'], prefix='Online Security')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data3], axis=1)

    # Creating dummy variables for the variable 'OnlineBackup'.
    encoded_data4 = pd.get_dummies(df['Online Backup'], prefix='Online Backup')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data4], axis=1)

    # Creating dummy variables for the variable 'DeviceProtection'. 
    encoded_data5 = pd.get_dummies(df['Device Protection'], prefix='Device Protection')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data5], axis=1)

    # Creating dummy variables for the variable 'TechSupport'. 
    encoded_data6 = pd.get_dummies(df['Tech Support'], prefix='Tech Support')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data6], axis=1)

    # Creating dummy variables for the variable 'StreamingTV'.
    encoded_data7 = pd.get_dummies(df['Streaming TV'], prefix='Streaming TV')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data7], axis=1)

    # Creating dummy variables for the variable 'StreamingMovies'. 
    encoded_data8 = pd.get_dummies(df['Streaming Movies'], prefix='Streaming Movies')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data8], axis=1)

    encoded_data9 = pd.get_dummies(df['Partner'], prefix='Partner')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data9], axis=1)

    encoded_data10 = pd.get_dummies(df['Dependents'], prefix='Dependents')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data10], axis=1)

    encoded_data11 = pd.get_dummies(df['Senior Citizen'], prefix='Senior Citizen')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data11], axis=1)

    encoded_data12 = pd.get_dummies(df['Paperless Billing'], prefix='Paperless Billing')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data12], axis=1)

    encoded_data13 = pd.get_dummies(df['Phone Service'], prefix='Phone Service')
    # Adding the results to the master dataframe
    df = pd.concat([df,encoded_data13], axis=1)

    df = df.drop(['Multiple Lines','Internet Service', 'Online Security', 'Online Backup', 'Device Protection', 'Phone Service',
       'Tech Support', 'Streaming TV', 'Streaming Movies','Partner','Dependents','Senior Citizen','Contract','Payment Method','Gender','Paperless Billing'], axis=1)

    #The varaible was imported as a string we need to convert it to float
    df['Total Charges'] = df['Total Charges']._convert(numeric=True)

    return df