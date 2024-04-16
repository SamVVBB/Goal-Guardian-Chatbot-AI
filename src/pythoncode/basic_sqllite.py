import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a connection to the SQLite database specified by db_file"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection is established: Database is created in memory")
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create a table from the create_table_sql statement"""
    try:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                task TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            );
        ''')
        print("Table is created")
    except Error as e:
        print(e)

def add_task(conn, task):
    """Add a new task to the tasks table"""
    sql = ''' INSERT INTO tasks(task,completed)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def main():
    database = "pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)

    if conn is not None:
        # create tasks table
        create_table(conn)

        # add a new task
        task = ('Review Python Code', False)
        task_id = add_task(conn, task)
        print(f"Task added with id: {task_id}")

        # close connection
        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
