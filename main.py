import mysql.connector

def get_connection():
    connection=mysql.connector.connect(
        host="localhost",
        database="test",
        port=3307,
        username="root",
        password="")

    return connection

def close_connection(connection):
    if connection:
        connection.close()

def main():
    print('Available Options: C=Create, R=Read, U=Update, D=Delete ')
    choice = input('Choose your option = ')

    if choice == 'C' or choice=='c':
        createObj=Create()
        createObj.func_CreateData()
    elif choice == 'R' or choice=='r':
        readObj =Read()
        readObj.func_ReadData()
    elif choice == 'U' or choice=='u':
        updateObj =Update()
        updateObj.func_UpdateData()
    elif choice == 'D' or choice=='d':
        deleteObj =Delete()
        deleteObj.func_DeleteData()
    else:
        print('Wrong choice, Thank u')

# Call the main function


class Create:
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




class Read:
    def func_ReadData(self):
        print("in")
           
        # Get the sql connection
        connection = get_connection()
        cursor = connection.cursor()

        # Execute the sql query
        cursor.execute('Select * from employee')

        # Print the data
        for i in cursor:
            print("data: ",i)
            #print('row = %r' % (i,))

class Update:
    def func_UpdateData(self):
        # Get the SQL connection
        connection = get_connection()

        id = input('Enter Employee Id = ')
    
        try:
            # Fetch the data which needs to be updated
            sql = "Select * From employee Where Id = %s" 
            cursor = connection.cursor()
            cursor.execute(sql, [id,])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\t\t Age')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            print('Enter New Data To Update Employee Record ')

            name = input('Enter New Name = ')
            age = input('Enter New Age = ')
            query = "Update employee Set Name = %s, Age =%s Where Id =%s" 
        
            # Execute the update query
            cursor.execute(query, [name, age, id,])
            connection.commit()

            #to show the updated data
            sql = "Select * From employee Where Id = %s" 
            cursor = connection.cursor()
            cursor.execute(sql, [id,])
            item = cursor.fetchone()

            print("Udpated data: ")
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\tAge')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            print('Data Updated Successfully')

        except:
            print('Something wrong, please check')

        finally:
           # Close the connection
            connection.close()

class Delete:
    def func_DeleteData(self):
        # Get the SQL connection
        connection = get_connection()

        id = input('Enter Employee Id = ')
    
        try:
            # Get record which needs to be deleted
            sql = "Select * From employee Where Id = %s" 
            cursor = connection.cursor()
            cursor.execute(sql, [id])
            item = cursor.fetchone()
            print('Data Fetched for Id = ', id)
            print('ID\t\t Name\t\tAge')
            print('-------------------------------------------')       
            print(' {}\t\t {} \t\t{} '.format(item[0], item[1], item[2]))
            print('-------------------------------------------')
            confirm = input('Are you sure to delete this record (Y/N)?')

            # Delete after confirmation
            if confirm == 'Y':
                deleteQuery = "Delete From employee Where Id = %s"
                cursor.execute(deleteQuery,[id,])
                connection.commit()
                print('Data deleted successfully!')
            else:
                print('Wrong Entry')
        except:
            print('Something wrong, please check')
        finally:
            connection.close()

main()



