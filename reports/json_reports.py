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

    def detailedPaymentTypeOrders(self):
        # Reading CSV file with the data
        df_payments = pd.read_csv('data_files/olist_order_payments_dataset.csv')

        # Filtering only the column 'payment_type'
        df_filtered = df_payments[['payment_type']]

        # Count the number of orders per payment type
        df_grouped = df_filtered.groupby('payment_type').size().reset_index(name='Orders per payment type')

        # Setting the column 'payment_type' as the dataframe index
        df_grouped.set_index('payment_type', inplace=True)

        # Convert the dataframe to a dictionary
        grouped_dict = df_grouped.to_dict('tight')

        self.addBarChartData("Payments types detailed", grouped_dict)
    
    def generateJSONReport(self) -> Dict:
        return super().generateJSONReport()

