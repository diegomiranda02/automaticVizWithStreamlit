from typing import Dict
from reports.base_report import BaseJSONReport

import pandas as pd

##################################################
#
# Class to generate the client information report
#
##################################################
class CustomerReport(BaseJSONReport):

    def __init__(self, title:str, subtitle:str):
        super(CustomerReport, self).__init__(title, subtitle)

    def customerDetailedInformation(self):

        # Read the CSV file from Olist Kaggle Dataset 
        df = pd.read_csv('data_files/olist_customers_dataset.csv')

        # Selecting only the custome_state column
        df_states = df[['customer_state']]

        # Renaming the column "customer_state" to "Customer State" 
        df_states.rename(columns={"customer_state": "Customer State"}, inplace=True)

        # Count the number of clients per state
        grouped = df_states.groupby('Customer State').size().reset_index(name='Count')

        # Calculating the percentage of clients per state
        grouped['Percentage'] = (grouped['Count']/grouped['Count'].sum()) * 100

        # Rounding the percentage to two decimals
        grouped['Percentage'] = grouped['Percentage'].round(2)

        # Sorting the percentage values in descending order
        grouped.sort_values('Percentage', ascending=False, inplace=True)

        # Convert the dataframe to a dictionary
        grouped_dict = grouped.to_dict(orient='records')
        
        self.addTableData("Count and percentage of clients per state", grouped_dict)

    def customerLocation(self):

        # Read the CSV file from Olist Kaggle Dataset 
        df_geolocation = pd.read_csv('data_files/olist_geolocation_dataset_filtered_SP.csv')

        # Convert the dataframe to a dictionary
        grouped_dict = df_geolocation.to_dict(orient='records')
        
        self.addMapData("Clients in the SP state", grouped_dict)
    
    def generateJSONReport(self) -> Dict:
        return super().generateJSONReport()
    
##################################################
#
# Class to generate the financial report
#
##################################################
class FinancialReport(BaseJSONReport):

    def __init__(self, title:str, subtitle:str):
        super(FinancialReport, self).__init__(title, subtitle)

    def detailedRevenue(self):
        df1 = pd.DataFrame({'Name': ['John', 'Alice'], 'Age': [25, 30]})
        df2 = pd.DataFrame({'City': ['New York', 'London'], 'Country': ['USA', 'UK']})

        df1_dict = df1.to_dict(orient='records')
        df2_dict = df2.to_dict(orient='records')

        self.addBarChartData("Payments", df1_dict)

    def detailedExpenses(self):

        mapdf1 = pd.DataFrame({'lat': [-23.5489, -23.5587, -23.5599, -23.5689, -23.5789], 'lon': [-46.6388, -46.6411, -46.6541, -46.6599, -46.6630]})
        mapdf1_dict = mapdf1.to_dict(orient='records')
        
        self.addMapData("Map Teste", mapdf1_dict)
    
    def generateJSONReport(self) -> Dict:
        return super().generateJSONReport()

