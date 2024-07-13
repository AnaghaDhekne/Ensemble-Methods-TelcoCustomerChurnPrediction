'''
This python code has the definition of main function for Telco Churn prediction
Created Date: 11/22/2022
Author: Anagha Dhekne, Shravan Sailada
Last Modified: 11/22/2022
'''

import Global_Defs
import Dataset_Information
import Dataset_Analysis
import Global_Defs

'''
This is the main function 
It controls flow and execution of operations being performed in the project
The followed steps are: load dataset, get basic data information
'''
def main():
    dataset = Global_Defs.getDataSet()
    Dataset_Information.getDataInformation(dataset,Global_Defs.getDataInfoFilePath())
    Dataset_Analysis.getDemographicStats(dataset)
    Dataset_Analysis.getCustomerAccountInformation(dataset)
    Dataset_Analysis.getServiceUsageInformation(dataset)
    Dataset_Analysis.getCustomerChurnInformation(dataset)
    

if __name__ == "__main__":
    main()