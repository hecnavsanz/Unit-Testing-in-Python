# -*- coding: utf-8 -*-
from utils import Utils


class CheckUtils:

    # test the get_emails function
    def get_emails_check(self):

        # author name and email test cases
        test_cases = [{"name": 'Ferren Adrea', "domain": "umm.io", "email": 'ferren.adrea@umm.io'},
                      {"name": 'Arzek', "domain": "yummy.org", "email": 'arzek@yummy.org'},
                      {"name": 'Dane Garcea Burrikin', "domain": "recip.es", "email": 'dane.garcea.burrikin@recip.es'}]

        # verify the __convert_to_email, __format_name and get_emails functions
        names = [test["name"] for test in test_cases]
        domains = [test["domain"] for test in test_cases]
        assert Utils.get_emails(names, domains) == [test["email"] for test in test_cases]

    # test the get_home_urls function
    def get_home_urls_check(self):

        # author name and email test cases
        test_cases = [{"name": 'Ferren Adrea', "domain": "umm.io", "home_url": 'http://blog.umm.io/ferren.adrea'},
                      {"name": 'Arzek', "domain": "yummy.org", "home_url": 'http://blog.yummy.org/arzek'},
                      {"name": 'Dane Garcea Burrikin', "domain": "recip.es", "home_url": 'http://blog.recip.es/dane.garcea.burrikin'}]

        # verify the __convert_to_home_url, __format_name and get_home_urls functions
        names = [test["name"] for test in test_cases]
        domains = [test["domain"] for test in test_cases]
        assert Utils.get_home_urls(names, domains) == [test["home_url"] for test in test_cases]
