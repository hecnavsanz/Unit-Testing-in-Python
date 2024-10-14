# -*- coding: utf-8 -*-
import random
import json
from blog import Blog

# create some blog entries
blog = Blog()
print('Adding blog recipes')
blog.add_blog_entry('Ferren Adrea', 'Potato omelette recipe')
blog.add_blog_entry('Arzek', 'Cod fish recipe')
blog.add_blog_entry('Dane Garcea', 'Garlic shrimp recipe')

# display all the blog recipes
print('List of blog recipes')
for entry in blog.get_blog_entries():
    print(json.dumps(entry, indent=4))

# display a random blog entry
random_blog_entry = random.choice(blog.get_blog_entries())
print('Show a random blog recipe')
print(json.dumps(blog.get_blog_entry_by_id(random_blog_entry['id']), indent=4))

# remove a random blog entry
random_blog_entry_id = random.choice(blog.get_blog_entries())['id']
print('Removing the blog recipe with id', random_blog_entry_id)
blog.remove_blog_entry(random_blog_entry_id)

# display all the blog entries
print('List of blog recipes')
for entry in blog.get_blog_entries():
    print(json.dumps(entry, indent=4))
