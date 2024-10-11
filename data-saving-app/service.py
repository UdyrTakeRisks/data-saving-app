import sqlite3
from fastapi import HTTPException

DATABASE_PATH = "storage/data.db"
SQL_QUERY = "INSERT INTO messages (name, message) VALUES (?, ?)"


async def store_in_db(name: str, message: str):
    try:
        # connect to the sqlite database and execute queries using cursor refer to: https://docs.python.org/3.12/library/sqlite3.html
        connection = sqlite3.connect(DATABASE_PATH)
        cursor = connection.cursor()
        cursor.execute(SQL_QUERY, (name, message))
        connection.commit()
        cursor.close()
        connection.close()

        if cursor.rowcount > 0:  # check affected rows
            return "Data is stored in database successfully"

        else:
            raise HTTPException(status_code=400, detail="Failed to insert data into database")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An Error Occurred while adding the data in database: {e}")
