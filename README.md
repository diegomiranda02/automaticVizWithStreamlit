# Automating Business Reports Visualization with Streamlit

## Introduction:
In today's data-driven world, generating business reports efficiently and effectively is crucial for decision-making and analysis. Manual report creation can be time-consuming and error-prone, leading to delays and inaccuracies. However, with the help of Streamlit, a powerful Python library for data visualization and application development, automating business reports becomes a streamlined and straightforward process. In this article, we will explore how to leverage Streamlit to automate the creation of business reports, saving time and improving data insights.

### 1. Understanding Streamlit:
Streamlit is an open-source Python library designed for rapid prototyping and building interactive data applications. It simplifies the process of creating web-based data visualizations, allowing developers and data scientists to quickly transform raw data into visually appealing and interactive reports. Streamlit's simplicity lies in its ability to convert Python scripts into interactive web apps effortlessly.

### 2. Setting up your local environment:

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

### 3. Creating the Report Structure:
To begin automating your business report, start by defining the overall structure and layout. Streamlit provides various components, such as containers, columns, and widgets, to organize and present your data effectively. For instance, you can use the `st.sidebar` container for navigation and configuration options, while using `st.columns` to create multiple columns for displaying different aspects of your report.

### 4. Loading and Preprocessing Data:
Next, you need to load and preprocess the data that will populate your report. Streamlit supports various data formats, including CSV, Excel, and databases. Use the appropriate data loading functions to read the data into your Python script. Once loaded, perform any necessary preprocessing steps, such as data cleaning, filtering, and aggregation, to ensure the data is in the desired format for analysis.

### 5. Visualizing Data:
Streamlit offers a wide range of interactive visualization options to present your data effectively. You can leverage popular data visualization libraries like Matplotlib, Plotly, and Seaborn to create charts, graphs, and plots. Streamlit provides simple functions like `st.line_chart`, `st.bar_chart`, and `st.pyplot` to integrate these visualizations seamlessly into your report. Experiment with different visualization techniques to highlight key insights and trends in your data.

### 6. Adding Interactive Elements:
To enhance user engagement and interactivity, Streamlit enables you to incorporate widgets and controls. These interactive elements allow users to customize the report's parameters, such as date ranges, filter options, or metric selection. Streamlit provides widgets like sliders, dropdowns, checkboxes, and buttons through which users can interact with the report dynamically. Utilize these widgets to enable users to explore the data and extract personalized insights.

### 7. Generating Report Outputs:
Once your report is ready, Streamlit offers functionalities to generate various output formats. You can save the report as an interactive web application that users can access through a browser. Streamlit also allows you to export the report as a PDF, PNG, or HTML file, making it easier to share and distribute the insights with stakeholders.

### 8. Deploying and Sharing the Report:
Streamlit makes it effortless to deploy your automated business report. You can host your Streamlit application on cloud platforms like Heroku, AWS, or Google Cloud, allowing stakeholders to access the report remotely. Additionally, you can share the application's URL, or embed it within an existing website or intr

### References

1. https://towardsdatascience.com/3-easy-ways-to-include-interactive-maps-in-a-streamlit-app-b49f6a22a636

2. https://stackoverflow.com/questions/63787612/plotly-automatic-zooming-for-mapbox-maps

