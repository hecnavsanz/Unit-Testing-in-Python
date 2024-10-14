# -*- coding: utf-8 -*-
from utils import Utils


class CheckUtils:

    # test the get_emails function
    def get_emails_check(self):

        # utils instance
        utils = Utils()

        # author name and email test cases
        test_cases = [{"name": 'Ferren Adrea', "domain": "umm.io", "email": 'ferren.adrea@umm.io'},
                      {"name": 'Arzek', "domain": "yummy.org", "email": 'arzek@yummy.org'},
                      {"name": 'Dane Garcea Burrikin', "domain": "recip.es", "email": 'dane.garcea.burrikin@recip.es'}]

        # verify the _convert_to_email, _format_name and get_emails functions
        names = [test["name"] for test in test_cases]
        domains = [test["domain"] for test in test_cases]
        assert utils.get_emails(names, domains) == [test["email"] for test in test_cases]

    def another_get_emails_check(self):

        # utils instance
        utils = Utils()

        # author name and email test cases
        test_cases = [{"name": 'Ferren Adrea', "domain": "umm.io", "email": 'ferren.adrea@umm.io'},
                      {"name": 'Arzek', "domain": "yummy.org", "email": 'arzek@yummy.org'},
                      {"name": 'Dane Garcea', "domain": "recip.es", "email": 'dane.garcea@recip.es'}]

        # verify the _convert_to_email, _format_name and get_emails functions
        names = [test["name"] for test in test_cases]
        domains = [test["domain"] for test in test_cases]
        assert utils.get_emails(names, domains) == [test["email"] for test in test_cases]
