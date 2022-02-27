import psycopg2
from psycopg2 import Error


try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="123",
                                  host="localhost",
                                  port="5433",
                                  database="password")

    # Create a cursor to perform database operations
    cursor = connection.cursor()

    # Executing a SQL query
    cursor.execute("SELECT * FROM mypasswords;")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


password = input("What is the master password?")


def view():
    pass


def add():
    pass


while True:
    mode = input(
        "Would you like to add a new password or view your existing ones? \nPress q to quit")
    if mode == "q":
        break
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Please choose a valid mode!")
        continue
