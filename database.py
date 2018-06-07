# Import required libraries
import socket as system_information
import pypyodbc as sql_server


# Create a class that will be used to manage connections with the database
class Database:
    # Create a constructor that's able to take in the required information
    def __init__(self, database_name: str, username: str, password: str, server_name: str = system_information.gethostname(), driver: str = "SQL Server"):
        # Set the class variables
        self.database_name = database_name
        self.username = username
        self.password = password
        self.server_name = server_name
        self.driver = driver

    # Create a method that returns the connection string
    def get_connection_string(self) -> str:
        # Return the connection string
        return 'Driver={{0}}; Server={1}; Database={2}; uid={3}; pwd={4}'.format(self.driver, self.server_name, self.database_name, self.username, self.password)