import sqlalchemy
from config import db_user, db_pass, db_name, cloud_sql_connection_name


db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername="mysql+pymysql",
        username=db_user,
        password=db_pass,
        database=db_name,
        query={"unix_socket": "/cloudsql/{}".format(cloud_sql_connection_name)},
    ),
)


def create_table(table_name):
    with db.connect() as conn:
        conn.execute(
            f"CREATE TABLE IF NOT EXISTS {table_name} "
            "(title CHAR(30) NOT NULL, description CHAR(50), PRIMARY KEY (title) );"
        )


def insert_record(table_name, **properties):
    fields = tuple(key for key in properties.keys())
    values = tuple(value for value in properties.values())
    query = f"INSERT INTO {table_name} VALUES {values};"
    with db.connect() as conn:
        conn.execute(query)


def search_table(table_name, *columns):
    with db.connect() as conn:
        columns = ", ".join([col for col in columns])
        print("QUERY:", str(columns), f"SELECT {columns} FROM {table_name};")
        records = conn.execute(f"SELECT {columns} FROM {table_name};").fetchall()
    return records


def show_record(table_name, title):
    with db.connect() as conn:
        records = conn.execute(f"SELECT * FROM {table_name} WHERE title = '{title}';").fetchall()[0]
    return records


def search_record(table_name, title):
    with db.connect() as conn:
        records = conn.execute(f"SELECT * FROM {table_name} WHERE title LIKE '%%{title}%%';").fetchall()
    return records


def drop_table(table_name):
    with db.connect() as conn:
        conn.execute("DROP TABLE {table_name};")
