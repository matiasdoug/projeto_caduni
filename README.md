# Projeto Caduni

![cover](/cover1.jpg)

Projeto Caduni is a Python application that allows users to register passengers, bus drivers, bus cards, and buses. Additionally, it provides functionality to check the registered records.

## Dependencies

Before running Projeto Caduni, make sure you have the following dependencies installed:



**Python 3.x**


**pyodbc**


**pandas**


You can install the required dependencies using pip by running the following command within your virtual environment:


**pip install pyodbc pandas**

## Database Connectivity

Projeto Caduni utilizes the pyodbc connector to establish a connection with a SQL Server database. Before running the application, ensure that you have the appropriate database set up and configured with the necessary tables for passenger, bus driver, bus card, and bus records.

Modify the connection details in the code according to your SQL Server database credentials:

**import pyodbc**

**server = 'your_server_name'**


**database = 'your_database_name'**


**username = 'your_username'**


**password = 'your_password'**

## Modify the connection string as needed based on your SQL Server configuration

**connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'**
**conn = pyodbc.connect(connection_string)**

## Installation

To install Projeto Caduni on your system, follow these steps:

1 - Clone the repository:


**git clone https://github.com/your_username/projeto_caduni.git**

2 - Navigate to the project directory:


**cd projeto_caduni**

3- Create a virtual environment:


**python -m venv venv**

4- Activate the virtual environment:


**windows - venv\Scripts\activate**


**linux/macOS - source venv/bin/activate**

## Usage
Once you have installed the project and activated the virtual environment, you can run Projeto Caduni:


**python main.py**

## Contributing
If you wish to contribute to Projeto Caduni, feel free to fork the repository and submit pull requests with your improvements.




