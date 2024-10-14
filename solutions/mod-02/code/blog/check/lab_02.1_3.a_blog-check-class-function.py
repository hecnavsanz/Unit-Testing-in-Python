# -*- coding: utf-8 -*-
from blog import Blog


class CheckBlog:

    # test the add blog entry
    def add_blog_entry_check(self):

        # create a blog instance
        blog = Blog()

        # recipes with author name and title
        blog_entries = [('Ferren Adrea', 'Potato omelette recipe'),
                        ('Arzek', 'Cod fish recipe'),
                        ('Dane Garcea', 'Garlic shrimp recipe')]

        # add three blog entries
        for entry in blog_entries:
            blog.add_blog_entry(entry[0], entry[1])

        # verify the number of blog entries is three
        assert len(blog.get_blog_entries()) == 3

    # test the get blog entry by id function
    def get_blog_entry_by_id_check(self):

        # create a blog instance
        blog = Blog()

        # recipes with author name and title
        blog_entries = [('Ferren Adrea', 'Potato omelette recipe'),
                        ('Arzek', 'Cod fish recipe'),
                        ('Dane Garcea', 'Garlic shrimp recipe')]

        # add three blog entries
        for entry in blog_entries:
            blog.add_blog_entry(entry[0], entry[1])

        # verify the invalid blog entry (doesn't exist)
        assert blog.get_blog_entry_by_id('abcdefgh-1234-0000-4321-hgfedcba') is None
        # verify the second blog entry exists
        assert blog.get_blog_entry_by_id(blog.get_blog_entries()[1]['id'])['id'] is not None

    # test the remove blog entry function
    def remove_blog_entry_check(self):

        # create a blog instance
        blog = Blog()

        # recipes with author name and title
        blog_entries = [('Ferren Adrea', 'Potato omelette recipe'),
                        ('Arzek', 'Cod fish recipe'),
                        ('Dane Garcea', 'Garlic shrimp recipe')]

        # add three blog entries
        for entry in blog_entries:
            blog.add_blog_entry(entry[0], entry[1])

        # remove a non-existing blog entry
        invalid_blog_entry = {
            'id': 'abcdefgh-1234-0000-4321-hgfedcba',
            'author': 'Dane Adrea',
            'date': '2027-08-15 04:46:37',
            'title': 'Garlic french fries'
        }
        blog.remove_blog_entry(invalid_blog_entry)

        # verify the invalid blog entry was not removed (doesn't exist)
        assert len(blog.get_blog_entries()) == 3

        # remove the second blog entry
        blog_entry = blog.get_blog_entries()[1]
        blog.remove_blog_entry(blog_entry)

        # verify the second blog entry was removed
        assert len(blog.get_blog_entries()) == 2
        assert blog_entry not in [entry for entry in blog.get_blog_entries()]
