from time import sleep

from splinter import Browser


browser = Browser('firefox')

browser.visit('http://localhost:15000/')
title_element = browser.find_by_id('title')

if title_element.is_empty():
    print("No title found")
else:
    print(f"Title: {title_element.text}")

browser.quit()
