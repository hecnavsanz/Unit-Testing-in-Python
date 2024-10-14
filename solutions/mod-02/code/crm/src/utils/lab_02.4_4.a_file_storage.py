# -*- coding: utf-8 -*-
# storage class to persist data
import os
from pathlib import Path
import json


class FileStorage:

    # constructor
    def __init__(self, loc: Path, file: str):
        self.dir = loc
        self.dir.mkdir(parents=True, exist_ok=True)
        self.file = file

    # write an object to a file
    def write(self, obj):
        with open(self.dir / self.file, 'a') as file:
            file.write(str(obj) + '\n')

    # remove an object from a file
    def remove(self, obj):
        with open(self.dir / self.file, 'r') as file:
            lines = file.readlines()

        with open(self.dir / self.file, 'w') as file:
            for line in lines:
                if line.strip() != str(obj):
                    file.write(line)

    # modify an existing object in a file
    def modify(self, old_obj, new_obj):
        with open(self.dir / self.file, 'r') as file:
            lines = file.readlines()

        with open(self.dir / self.file, 'w') as file:
            for line in lines:
                json_obj = json.loads(line.rstrip('\n'))
                if str(old_obj) == str(json_obj).replace('\'', '\"'):
                    file.write(str(new_obj) + '\n')
                else:
                    file.write(line)

    # search for an object in a file
    def read(self, obj):
        with open(self.dir / self.file, 'r') as file:
            lines = file.readlines()

        for line in lines:
            if str(obj) in line:
                return line.rstrip('\n')

        return None

    # read all the objects from a file
    def read_all(self):
        with open(self.dir / self.file, 'r') as file:
            lines = file.readlines()

        return [line.rstrip('\n') for line in lines]

    # search for an object in a file using a key and return the key value
    def read_by_key(self, key, value):
        with open(self.dir / self.file, 'r') as file:
            lines = file.readlines()
        for line in lines:
            json_obj = json.loads(line.rstrip('\n'))
            if key in json_obj and str(json_obj[key]) == str(value):
                return line.rstrip('\n')
        return None

    # delete the file
    def cleanup(self):
        os.remove(self.dir / self.file)
        return True
