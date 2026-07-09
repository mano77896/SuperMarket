import mysql.connector

def connect_db():
    try:
        con = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="msd7",
            database="supermarket"
        )
        return con

    except mysql.connector.Error as e:
        print("Database Error:", e)
        return None