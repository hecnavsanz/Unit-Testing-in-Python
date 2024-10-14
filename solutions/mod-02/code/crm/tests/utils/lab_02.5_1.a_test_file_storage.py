# -*- coding: utf-8 -*-
# test the storage utils
import json
import os
from pathlib import Path
import pytest
from utils.file_storage import FileStorage


class TestFileStorage:

    # fixture to create some data
    @pytest.fixture(scope='class', autouse=True)
    def data(self):
        return [json.dumps({'id': 1, 'data': "something"}),
                json.dumps({'id': 2, 'data': "something else"}),
                json.dumps({'id': 3, 'data': "what else"})]

    # fixture to read database temporary directory
    @pytest.fixture(scope='class', autouse=True)
    def db_path(self):
        return Path(os.getenv('DBDIR_FS'))

    # fixture to read database file variable
    @pytest.fixture(scope='class', autouse=True)
    def db_file(self):
        return os.getenv('DBFILE_FS')

    # fixture to create a database
    @pytest.fixture(scope='class', autouse=True)
    def database(self, db_path, db_file):
        return FileStorage(db_path, db_file)

    # test database initialization
    def test_init(self, db_path, db_file, database):
        assert (database.dir, database.file) == (db_path, db_file)

    # test the write method to add data to a file
    def test_write(self, db_path, db_file, database, data):
        for d in data:
            database.write(d)

        with open(db_path / db_file, 'r') as file:
            lines = [line.rstrip('\n') for line in file.readlines()]
        for da, li in zip(data, lines):
            assert da == li

    # test the remove method to remove some data from a file
    def test_remove(self, db_path, db_file, database, data):
        database.remove(data[0])

        with open(db_path / db_file, 'r') as file:
            lines = [line.rstrip('\n') for line in file.readlines()]
        assert lines == data[1:]

    # test the modify method to modify some data in a file
    def test_modify(self, db_path, db_file, database, data):
        database.modify(data[2], data[0])

        with open(db_path / db_file, 'r') as file:
            lines = [line.rstrip('\n') for line in file.readlines()]
        assert lines == [data[1], data[0]]

    # test the read method to read some data from a file
    def test_read(self, db_path, db_file, database, data):
        with open(db_path / db_file, 'r') as file:
            lines = [line.rstrip('\n') for line in file.readlines()]
        assert database.read(data[0]) in lines

    # test the read_all method to read all data from a file
    def test_read_all(self, database, data):
        assert database.read_all() == [data[1], data[0]]

    # test the read_by_key method to search for a json object in a file by a key value
    def test_read_by_key(self, database, data):
        assert database.read_by_key("id", 1) == data[0]
        assert database.read_by_key("data", "something else") == data[1]
        assert database.read_by_key("id", 4) is None
        assert database.read_by_key("data", "nothing") is None

    # test the cleanup method to delete a file
    def test_cleanup(self, db_path, db_file, database):
        assert database.cleanup() is True
        assert not (db_path / db_file).exists()
