# Automating Business Reports Visualization with Streamlit

## Introduction:
In today's data-driven world, generating business reports efficiently and effectively is crucial for decision-making and analysis. Manual report creation can be time-consuming and error-prone, leading to delays and inaccuracies. However, with the help of Streamlit, a powerful Python library for data visualization and application development, automating business reports becomes a streamlined and straightforward process. In this article, we will explore how to leverage Streamlit to automate the creation of business reports, saving time and improving data insights.

### 1. Understanding Streamlit:
Streamlit is an open-source Python library designed for rapid prototyping and building interactive data applications. It simplifies creating web-based data visualizations, allowing developers and data scientists to transform raw data into visually appealing and interactive reports quickly. Streamlit's simplicity lies in its ability to effortlessly convert Python scripts into interactive web apps.

### 2. Creating the Report Structure:
It is essential to establish a clear definition of the overall structure and layout to initiate the automation of the business report. The preferred format for exchanging data between the backend and visualization tool in this project was JSON. Furthermore, I established some specific patterns to construct the JSON. Presented below is a snippet of JSON that serves as an example, illustrating the organized structure of the data.

``` json

{
    "tableContentDescription0" : "Products Revenue",
    "tableData0" : 
        [
       { "Year": "2022", "Product": "Product 1","Total":10000.00},
       { "Year": "2021", "Product": "Product 1","Total":9000.00}
       ],
    "mapDescription1": "Sales per region in 2022",
    "mapData1": [
        { "lat": -23.5489, "lon": -46.6388},
        { "lat": -23.5587, "lon": -46.6411},
        { "lat": -23.5599, "lon": -46.6541},
        { "lat": -23.5689, "lon": -46.6599},
        { "lat": -23.5789, "lon": -46.6630}
        ]
} 

``` 

The class BaseReport automatically produces the JSON structure defined. The primary purpose of this class is to generate the JSON in the format described above. 

``` python
class BaseJSONReport():

    def __init__(self, title:str, subtitle:str):
        self.data_dict = {}
        self.keySuffix = 0

        self.addTitleData(title)
        self.addSubtitleData(subtitle)
   
    def addTitleData(self, description: str) -> None:
        self.data_dict["title" + str(self.keySuffix)] = description
        self.keySuffix += 1

    def addSubtitleData(self, description: str) -> None:
        self.data_dict["subtitle" + str(self.keySuffix)] = description
        self.keySuffix += 1

    def addMapData(self, description: str, data: Dict[str, Dict]) -> None:
        self.data_dict["mapDescription" + str(self.keySuffix)] = description
        self.data_dict["mapData" + str(self.keySuffix)] = data
        self.keySuffix += 1

    def addTableData(self, description: str, data: Dict[str, Dict]) -> None:
        self.data_dict["tableDescription" + str(self.keySuffix)] = description
        self.data_dict["tableData" + str(self.keySuffix)] = data
        self.keySuffix += 1
    
    def addBarChartData(self, description: str, data: Dict[str, Dict]) -> None:
        self.data_dict["barchartDescription" + str(self.keySuffix)] = description
        self.data_dict["barchartData" + str(self.keySuffix)] = data
        self.keySuffix += 1

    def generateJSONReport(self) -> Dict:
        json_object = json.dumps(self.data_dict)
        return json_object
```

Each method generates the component description and the JSON section with the data. For instance, the addTableData method generates the JSON section of the table description and the table data. To build this is used a Python dictionary type. Once the dictionary's key is unique, the 'keySuffix' variable adds a number to each key to distinguish among keys with similar components. 

Below is an example of how to compose a JSON data report inheriting the BaseReport class:

``` python
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
```

CustomerReport class has two report sections: a customer detailed information section, defined in the method 'customerDetailedInformation', and a customer location section, described in the  'customerLocation' method. The methods of the class BaseReport 'addTableData' and 'addMapData' are used to generate the JSON in the previously specified format. After implementing the report sections, run the 'generateJSONReport' method to create the whole report structure. 

The following code sets the values of the title and subtitle of the report in the superclass BaseReport:

``` python
def __init__(self, title:str, subtitle:str):
        super(CustomerReport, self).__init__(title, subtitle)
```

Once you implement the CustomerReport, it is time to instantiate the report and retrieve the JSON result for display in the visualization tool. The following code performs this task:

``` python
customerReportTitle = "Clients Report"
customerReportSubtitle = "Detailed information about the Olist clients"
cr = CustomerReport(customerReportTitle, customerReportSubtitle)
cr.customerDetailedInformation()
cr.customerLocation()
data = cr.generateJSONReport()
```

You can define the title and subtitle in the 'customerReportTitle' and 'customerReportSubtitle' variables and add detailed customer information and location sections to the report. It is essential to note that it is possible to compose the report with only the sections needed. If only the customer location section is necessary, then only the method 'customerLocation' should be called. It gives flexibility to the solution. Finally, the method 'generateJSONReport()' generates the whole JSON with the report data.

The figures below show the Client Report:

![alt text](https://github.com/diegomiranda02/automaticVizWithStreamlit/blob/main/images/client_table_count_and_percentage.png?raw=true)

![alt text](https://github.com/diegomiranda02/automaticVizWithStreamlit/blob/main/images/map_with_SP_clients.png?raw=true)


I implemented another example demonstrating exchanging data with indexes from the backend to the visualization tool. FinancialReport class has a 'detailedPaymentTypeOrders' section which generates data with the payment type as indexes. These indexes are sent in JSON as well as the values.  

``` python
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
```

The figures below show the Financial Report:

![alt text](https://github.com/diegomiranda02/automaticVizWithStreamlit/blob/main/images/financial_report.png?raw=true)



### 3. Setting up your local environment:

1. Install Docker: Visit the official Docker website (https://docs.docker.com/get-docker/) and follow the instructions to install Docker on your system.

2. Install Git: Install Git from the official website (https://git-scm.com/downloads) if you haven't already.

3. Clone the GitHub project:

- Open a terminal or command prompt
- Change to the directory where you want to clone the project.
- Run the following command to clone the project:

``` 
git clone https://github.com/diegomiranda02/automaticVizWithStreamlit.git
```
Once the project download is done, change to the project directory:

```
cd <project_directory>
```

4. Build the Docker image:
- Run the following command to build the Docker image:

```
docker build -t my_app .
```
This command builds the Docker image and tags it with the name my_app. The . at the end indicates that the build context is the current directory.

5. Run the Docker container:
- Once the image is built, you can run the Docker container using the following command:

```
docker run -p 8501:8501 my_app
```

This command runs the Docker container and forwards the port 8501 from the container to the host machine. Streamlit runs on port 8501 by default.
You can access your Streamlit application by opening a web browser and visiting http://localhost:8501.

That's it! You've created a Docker image and run a Streamlit application using Python 3.10.9 and the source code from a GitHub project.

### 4. Loading and Preprocessing Data:

Next, it is needed to load and preprocess the data that will populate the report. Streamlit supports various data formats, including CSV, Excel, and databases. This project used the Kaggle Dataset of the Brazilian E-Commerce Olist (link in the Dataset section) in CSV format, and the data underwent some preprocessing:

``` python
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
```

We only needed the 'customer_state' column for this task. I renamed the columns and calculated the number of clients per state and the percentage for each state. The last step is to convert the dataframe to a Python dictionary, orienting by the records to print in the exact JSON specification.

The map data is in the 'olist_geolocation_dataset_filtered_SP.csv' file, a more minor and filtered data than the original one. Only the Sao Paulo location is in the file. The only preprocessing step is to convert the 'lat' and 'lon' columns, which represent the latitude and the longitude, respectively, to a dictionary oriented by the records to meet the specification.

``` python
# Read the CSV file from Olist Kaggle Dataset 
df_geolocation = pd.read_csv('data_files/olist_geolocation_dataset_filtered_SP.csv')

# Convert the dataframe to a dictionary
grouped_dict = df_geolocation.to_dict(orient='records')
```
        

### 5. Visualizing Data:

With the JSON data in the pattern defined previously, it is possible to automate the visualization process. In this project, Streamlit was used to implement the frontend part, but it could be another tool or framework once the JSON standard is defined automatically. Below is the code to generate the visualization:

``` python
def generate_report(data_content):
    for key,value in data_content.items():
        if key.startswith("table") and isinstance(value, list):
            st.table(pd.DataFrame(value))

        elif key.startswith("title") and isinstance(value, str):
            st.header(value)
    
        elif key.startswith("subtitle") and isinstance(value, str):
            st.header(value)

        elif isinstance(value, str):
            st.write(value)    

        elif key.startswith("map") and isinstance(value, list):
            # Converting list to Dataframe
            df = pd.DataFrame(value)

            # Snippet of code based on the article 1 in References section
            max_bound = max(abs(max(df['lat'])- min(df['lat'])), abs(max(df['lon'])- min(df['lon']))) * 111
            zoom = 11.5 - np.log(max_bound)

            # Snippet of code based on the article 2 in References section
            fig = px.scatter_mapbox(df, lat="lat", lon="lon", zoom=zoom)

            fig.update_layout(mapbox_style="open-street-map")
            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
            st.plotly_chart(fig)
```

Each method compares if the key has some pattern and the value type. For instance, if the key starts with 'map' and the value is a list, it generates a map component. Another example is if the key starts with 'table' and the value is an instance of a list, then a datatable is generated. The 'data_content' variable is the data in JSON specification format. The method 'generate_report' receives the JSON data as a parameter, generating the report automatically.

### 6. Deploying and Sharing the Report:

Streamlit makes it effortless to deploy your automated business report. You can host your Streamlit application on cloud platforms like Heroku, AWS, or Google Cloud, allowing stakeholders to access the report remotely. Additionally, you can share the application's URL, or embed it within an existing website or intranet.

### References

1. https://towardsdatascience.com/3-easy-ways-to-include-interactive-maps-in-a-streamlit-app-b49f6a22a636

2. https://stackoverflow.com/questions/63787612/plotly-automatic-zooming-for-mapbox-maps

### Datasets

1. https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
