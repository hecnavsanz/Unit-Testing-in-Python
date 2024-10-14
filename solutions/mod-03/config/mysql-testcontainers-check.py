# sample testcontainers to display mysql version
import sqlalchemy
from testcontainers.mysql import MySqlContainer


with MySqlContainer('mysql:8.0', 'labs', 'Pytest-TDD.Labs_4ALL', 'Pytest-TDD.Labs_4ALL', 'sampledb', 3306, 'tests/data') as mysql:

    engine = sqlalchemy.create_engine(mysql.get_connection_url())

    with engine.begin() as connection:

        version = connection.execute(sqlalchemy.text('select version()'))
        print('Version: ' + str(version.fetchone()))

        user = connection.execute(sqlalchemy.text('select user()'))
        print('User: ' + str(user.fetchone()))

        database = connection.execute(sqlalchemy.text('select database()'))
        print('Database: ' + str(database.fetchone()))

        tables = connection.execute(sqlalchemy.text('show tables from sampledb'))
        print('Tables: ' + str(tables.fetchone()))

        rows = connection.execute(sqlalchemy.text('select * from sampledb.sample_table'))
        print('Rows: ' + str(rows.fetchall()))
