# -*- coding: utf-8 -*-
import datetime
import uuid


class Blog:

    # constructor
    def __init__(self):
        self.__blog_entries = []

    # add a new blog entry
    def add_blog_entry(self, author, title):
        entry = {
            'id': str(uuid.uuid4()),
            'author': author,
            'date': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'title': title
        }
        self.__blog_entries.append(entry)

    # remove an existing blog entry (if exists)
    def remove_blog_entry(self, entry):
        try:
            self.__blog_entries.remove(entry)
        except ValueError:
            return

    # get all the blog entries
    def get_blog_entries(self):
        return self.__blog_entries

    # get a blog entry by id
    def get_blog_entry_by_id(self, entry_id):
        for entry in self.__blog_entries:
            if entry['id'] == entry_id:
                return entry
        return None
