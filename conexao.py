# importando módulos
import pyodbc
from pyodbc import Error


def conecta():
    """
        Esta função cria conexão com o banco de dados
    """

    try:
        server = 'sql-estudo.database.windows.net'
        driver = '{ODBC Driver 17 for SQL Server}'
        database = 'db-estudos'
        username = 'jaelson.matias@username.com.br'
        authentication = 'ActiveDirectoryInteractive'
        port = '1433'
        conn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';AUTHENTICATION='
        + authentication + ';PORT=' + port + ';DATABASE=' + database
        + ';UID=' + username)  # +';PWD='+password)

        return conn

    except Error:
        print('\033[1;34;40mErro de conexão!\033[m')



