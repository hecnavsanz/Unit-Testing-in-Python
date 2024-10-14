# -*- coding: utf-8 -*-
from blog import Blog


class TestBlog:

    # test the blog
    def test_blog(self):

        # create a blog instance
        blog = Blog()

        # add three blog entries
        blog.add_blog_entry('Ferren Adrea', 'Potato omelette recipe')
        blog.add_blog_entry('Arzek', 'Cod fish recipe')
        blog.add_blog_entry('Dane Garcea', 'Garlic shrimp recipe')
        initial_blog_entries = blog.get_blog_entries().copy()
        # verify the number of blog entries is three
        assert len(initial_blog_entries) == 3

        # get an invalid blog entry
        invalid_blog_entry = blog.get_blog_entry_by_id('abcdefgh-1234-0000-4321-hgfedcba')
        # verify the invalid blog entry (doesn't exist)
        assert invalid_blog_entry is None

        # get the second blog entry by id
        second_blog_entry = blog.get_blog_entries()[1]
        second_blog_entry_id = blog.get_blog_entry_by_id(second_blog_entry['id'])['id']
        # verify the second blog entry exists
        assert second_blog_entry_id is not None

        # remove a non-existing blog entry
        invalid_blog_entry = {
            'id': 'abcdefgh-1234-0000-4321-hgfedcba',
            'author': 'Dane Adrea',
            'date': '2027-08-15 04:46:37',
            'title': 'Garlic french fries'
        }
        blog.remove_blog_entry(invalid_blog_entry)
        updated_blog_entries = blog.get_blog_entries().copy()
        # verify the invalid blog entry was not removed (doesn't exist)
        assert len(updated_blog_entries) == 3

        # remove the second blog entry
        blog.remove_blog_entry(second_blog_entry)
        updated_blog_entries = blog.get_blog_entries().copy()
        # verify the second blog entry was removed
        assert len(updated_blog_entries) == len(initial_blog_entries) - 1
        assert second_blog_entry['id'] not in [entry['id'] for entry in updated_blog_entries]
