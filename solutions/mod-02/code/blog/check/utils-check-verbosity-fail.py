# -*- coding: utf-8 -*-
from utils import Utils


class CheckUtils:

    # test the get_emails function
    def get_emails_one_check(self):

        # utils instance
        utils = Utils()

        # author name and email test case (the third test case has a typo in the email)
        blog_user ={
            "name": 'Ferren Adrea',
            "domain": "umm.io",
            "email": 'ferren.adrea@umm.io'}

        # verify the _convert_to_email, _format_name and get_emails functions
        names = [test["name"] for test in test_cases]
        domains = [test["domain"] for test in test_cases]
        assert utils.get_emails(names, domains) == [test["email"] for test in test_cases]

    def get_emails_another_check(self):

        # utils instance
        utils = Utils()

        # author name and email test cases
        test_cases = [{"name": 'Ferren Adrea', "domain": "umm.io", "email": 'ferren.adrea@umm.io'},
                      {"name": 'Arzek', "domain": "yummy.org", "email": 'arzek@yummy.org'},
                      {"name": 'Dane Garcea', "domain": "recip.es", "email": 'dane.garcea@recip.esss'}]

        # verify the _convert_to_email, _format_name and get_emails functions
        names = [test["name"] for test in test_cases]
        domains = [test["domain"] for test in test_cases]
        assert utils.get_emails(names, domains) == [test["email"] for test in test_cases]
