# import mysql.connector

# get_connection=mysql.connector.connect(
#     host="localhost",
#     username="root",
#     password="",
#     database="test",
#     port=3307)



# if get_connection:
#     print("Connection done !")
# else:
#     print("Connection failed !")

import mysql.connector

def get_connection():
    connection=mysql.connector.connect(
        host="localhost",
        database="employees",
        port=3307,
        username="root",
        password="")

    return connection

def close_connection(connection):
    if connection:
        connection.close()


def func_CreateData(self):
        

        # Get the sql connection
        connection = get_connection()
        cursor=connection.cursor()
        
        name = input('Enter Name = ')
        age = input('Enter Age = ')

        try:       
            
            query = "Insert Into employee (Name, Age) Values (%s,%s)" 
            cursor = connection.cursor()

            # Execute the sql query
            cursor.execute(query, [name, age])

            # Commit the datac

            connection.commit()
            print('Data Saved Successfully')

        except:
            print('Something wrong, please check')

        finally:
            # Close the connection
            connection.close()

func_CreateData(self)